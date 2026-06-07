import os
os.environ["NUMBA_DISABLE_JIT"] = "1"
import webbrowser

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide6.QtCore import QThread, Signal as QtSignal

from PySide6 import QtGui

from ui.ui_form import Ui_MainWindow
from record import RecordAudio
from midi import convert_to_midi
from midi_playback import MidiPlayback
from playback import playAudio
import sys

import res_rc

class ConvertWorker(QThread):
    finished = QtSignal(list)
    error = QtSignal(str)

    def __init__(self, wave_file, midi_output):
        super().__init__()
        self.wave_file = wave_file
        self.midi_output = midi_output

    def run(self):
        try:
            notes = convert_to_midi(self.wave_file, self.midi_output)
            self.finished.emit(notes)
        except Exception as e:
            self.error.emit(str(e)) 

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.save_voice_field.textChanged.connect(self.validate_inputs)
        self.save_midi_field.textChanged.connect(self.validate_inputs)
        self.recordButton.clicked.connect(self.record_audio_action)
        self.playButton.clicked.connect(self.play_audio_action)
        self.playmidiButton.clicked.connect(self.play_midi_action)
        self.convertButton.clicked.connect(self.convert_to_midi_action)
        self.gitbutton.clicked.connect(self.git_url_action)
        self.title = self.statusBar()

        self.wave_output_file = None
        self.midi_output_file = None
        self.recorder = RecordAudio(self.waveframe)

        self.midi_player = MidiPlayback(self.midiframe)

        # connect audio peak updates to UI gain meters
        self.recorder.update_signal.connect(self.on_audio_update)

        # connect gain slider to recorder and make it update while dragging
        self.gain_slider.setTracking(True)
        self.gain_slider.valueChanged.connect(self.on_gain_changed)
        self.on_gain_changed(self.gain_slider.value())

        self.recording = False
        self.audio_player = None
        self.midi_is_playing = False

        self.recordButton.setEnabled(False)
        self.playButton.setEnabled(False)
        self.convertButton.setEnabled(False)
        self.playmidiButton.setEnabled(False)

    def get_output_dir(self):
        """Get the base output directory.
        for packaged apps: ~/Harmonize/
        for development: current working directory
        """
        if getattr(sys, 'frozen', False):
            # in case of packaged app, use user's home directory to avoid permission issues
            base_dir = os.path.expanduser("~/Harmonize")
        else:
            # for dev, use cwd :)
            base_dir = os.getcwd()
        
        return base_dir
    
    def get_recordings_dir(self):
        """Get the recordings directory, creating it if needed."""
        recordings_dir = os.path.join(self.get_output_dir(), "recordings")
        os.makedirs(recordings_dir, exist_ok=True)
        return recordings_dir
    
    def get_midi_dir(self):
        """Get the MIDI directory, creating it if needed."""
        midi_dir = os.path.join(self.get_output_dir(), "midi")
        os.makedirs(midi_dir, exist_ok=True)
        return midi_dir

    def validate_inputs(self):
        voice_filename = self.save_voice_field.text().strip() if self.save_voice_field.text() else ''
        midi_filename = self.save_midi_field.text().strip() if self.save_midi_field.text() else ''
        wave_file_exists = bool(self.wave_output_file) and os.path.exists(self.wave_output_file or "")
        all_filled = bool(voice_filename and midi_filename)
        self.playButton.setEnabled(wave_file_exists and not self.recording)

        midi_displayed = getattr(self.midi_player, 'midi_displayed', False)
        self.playmidiButton.setEnabled(midi_displayed)
        
        self.recordButton.setEnabled(all_filled)
        # Original: self.convertButton.setEnabled(wave_file_exists)
        # TEST: Enable convert button optionally for testing
        midi_filename_filled = bool(self.save_midi_field.text().strip())
        self.convertButton.setEnabled(midi_filename_filled and not self.recording)

    def record_audio_action(self):
        try:
            filename = self.save_voice_field.text().strip()

            if not filename:
                self.show_error_message("No filename! Recording cancelled.")
                return

            if not filename.endswith('.wav'):
                filename += '.wav'

            recordings_dir = self.get_recordings_dir()
            self.wave_output_file = os.path.join(recordings_dir, filename)

            if self.recording:
                self.recorder.stop_recording()
                icon = QtGui.QIcon(":/icons/ui/icons/mic.svg")
                self.recordButton.setIcon(icon)
                self.update_status_bar(f"Recording stopped! Saved to {self.wave_output_file}")
                self.recording = False
                self.validate_inputs()

            else:
                self.recorder.start_recording(self.wave_output_file)
                icon = QtGui.QIcon(":/icons/ui/icons/stop.svg")
                self.recordButton.setIcon(icon)
                self.update_status_bar(f"Recording started! Saving to {self.wave_output_file}")
                self.recording = True

        except ValueError:
            self.show_error_message("Please enter valid duration in seconds.")
        except KeyboardInterrupt:
            self.recording = False
            self.update_status_bar("Recording stopped.")
        except Exception as e:
            self.show_error_message(f"An error occurred: {str(e)}")

        self.validate_inputs()

    def on_gain_changed(self, value):
        # convert slider value to actual gain multiplier
        gain_multiplier = float(value) / 50.0
        self.recorder.update_gain(gain_multiplier)

    def play_audio_action(self):
        if self.wave_output_file:
            if self.audio_player is None:
                self.audio_player = playAudio(self.wave_output_file)

            if self.audio_player:
                if self.audio_player.is_playing:
                    self.audio_player.pause()
                    self.playButton.setIcon(QtGui.QIcon(":/icons/ui/icons/play.svg"))
                    self.update_status_bar("Playback paused")
                else:
                    self.audio_player.play()
                    self.playButton.setIcon(QtGui.QIcon(":/icons/ui/icons/pause.svg"))
                    self.update_status_bar(f"Playing {self.wave_output_file}")
            else:
                self.show_error_message("Error initializing audio player.")
        else:
            self.show_error_message("No recorded audio file!")
        self.validate_inputs()

    def convert_to_midi_action(self):
        try:
            # TEST: Bypass recording requirement - use test_sample.wav
            # Original logic:
            # if self.wave_output_file:
            midi_filename = self.save_midi_field.text().strip()
            if not midi_filename.endswith('.midi'):
                midi_filename += '.midi'

            midi_dir = self.get_midi_dir()
            self.midi_output_file = os.path.join(midi_dir, midi_filename)

            self.midi_player.reset_playhead()
            self.midi_player.show_loader()
            self.convertButton.setEnabled(False)

            self._worker = ConvertWorker(self.wave_output_file, self.midi_output_file)
            self._worker.finished.connect(self._on_conversion_done)
            self._worker.error.connect(self._on_conversion_error)
            self._worker.start()

        except Exception as e:
            self.show_error_message(f"Error duing MIDI conversion: {str(e)}")

    def _on_conversion_done(self, notes):
            self._rendered_wav = None        # force re-render for new MIDI
            self.midi_audio_player = None    # reset player 
            self.midi_player.set_notes(notes)
            self.midi_player.reset_playhead()
            self.midi_is_playing = False

            self.validate_inputs()

            msg = QMessageBox(self)
            msg.setWindowTitle("MIDI Conversion Success!")
            msg.setText(f"Converted MIDI saved to {self.midi_output_file}. Listen to it in your favorite audio editor!")
            msg.setIconPixmap(QtGui.QPixmap(":/icons/ui/icons/convert.svg"))
            msg.exec()
            self.update_status_bar(f"Converted MIDI saved to {self.midi_output_file}")

    def _on_conversion_error(self, error_msg):
        self.midi_player.stop_loader()      # clean up loader on error too
        self.show_error_message(f"Error during MIDI conversion: {error_msg}")
        self.validate_inputs()
        
    def play_midi_action(self):
        if self.midi_output_file and os.path.exists(self.midi_output_file):
            if self.midi_is_playing:
                self.midi_is_playing = False
                self.playmidiButton.setIcon(QtGui.QIcon(":/icons/ui/icons/play.svg"))
                self.playmidiButton.setText("PLAY MIDI")
                self.midi_player.stop_playhead() 
                self.update_status_bar("MIDI Playback paused")
            else:
                self.midi_is_playing = True
                self.playmidiButton.setIcon(QtGui.QIcon(":/icons/ui/icons/pause.svg"))
                self.playmidiButton.setText("PAUSE MIDI")
                self.midi_player.start_playhead() 

                # render of first play resuse on resume

                if not hasattr(self, '_rendered_wav') or self._rendered_wav is None:
                    try:
                        from midi_playback import render_midi_to_wav
                        self._rendered_wav = render_midi_to_wav(self.midi_output_file)
                    except Exception as e:
                        self.show_error_message(f"Failed to render MIDI audio: {e}")
                        self.midi_is_playing = False
                        return
                
                if self.midi_audio_player is None:
                    self.midi_audio_player = playAudio(self._rendered_wav)
                self.midi_audio_player.play()
                self.update_status_bar(f"MIDI Playback playing {self.midi_output_file}")
        else:
            self.show_error_message("No MIDI file to play!") 
        self.validate_inputs()


    def git_url_action(self):
        url = "https://github.com/sreyasaju/harmonize"
        webbrowser.open(url)

    def update_status_bar(self, message):
        self.title.showMessage(message, 10000)

    def on_audio_update(self, peak_min, peak_max):
        try:
            # normalize to 0-100
            left_val = min(100, int(abs(peak_min) / 32767 * 100)) # make +ve -> div by 32767 -> make % -> remove decimals -> cap at 100
            right_val = min(100, int(abs(peak_max) / 32767 * 100))

            level = max(left_val, right_val)
            if level < 60:
                color = "#46c280"  
            elif level < 80:
                color = "#dbd374"  
            else:
                color = "#c97c77" 

            style = (
                "QProgressBar:vertical { border: 1px solid #2d2d3d; background: #11121a;"
                " width: 12px; border-radius: 3px; }"
                f"QProgressBar::chunk:vertical {{ background: {color}; border-radius: 2px; }}"
            )

            self.gain_left.setValue(left_val)
            self.gain_right.setValue(right_val)
            self.gain_left.setStyleSheet(style)
            self.gain_right.setStyleSheet(style)
        except Exception:
            # avoid crashing the UI thread on unexpected errors
            pass

    def show_error_message(self, message):
        QMessageBox.critical(self, "Error", message)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()