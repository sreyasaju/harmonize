# This Python file uses the following encoding: utf-8
import sys
import os
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QStatusBar
from PyQt6 import QtGui

from ui_form import Ui_MainWindow
from record import RecordAudio
from midi import convert_to_midi
from playback import playAudio

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.save_voice_field.textChanged.connect(self.validate_inputs)
        self.save_midi_field.textChanged.connect(self.validate_inputs)
        self.audio_widget = RecordAudio(self.waveframe)
        self.recordButton.clicked.connect(self.record_audio_action)
        self.playButton.clicked.connect(self.play_audio_action)
        self.convertButton.clicked.connect(self.convert_to_midi_action)
        self.title = self.statusBar()

        self.wave_output_file = None
        self.midi_output_file = None
        self.recorder = RecordAudio(self.waveframe)
        self.recording = False
        self.audio_player = None

        # disable all the buttons
        self.recordButton.setEnabled(False)
        self.playButton.setEnabled(False)
        self.convertButton.setEnabled(False)

    def validate_inputs(self):
        voice_filename = self.save_voice_field.text().strip() if self.save_voice_field.text() else ''
        midi_filename = self.save_midi_field.text().strip() if self.save_midi_field.text() else ''

        wave_file_exists = bool(self.wave_output_file) and os.path.exists(self.wave_output_file or "")
        all_filled = bool(voice_filename and midi_filename)
        self.playButton.setEnabled(wave_file_exists)
        self.recordButton.setEnabled(all_filled)
        self.convertButton.setEnabled(wave_file_exists)

    def record_audio_action(self):
        try:
            filename = self.save_voice_field.text().strip()

            if not filename:
                self.title.setStatusTip("No filename! Recording cancelled.")
                return

            if not filename.lower().endswith('.wav'):
                filename += '.wav'

            self.wave_output_file = filename

            if self.recording:
                # Stop recording
                self.recorder.stop_recording()
                icon = QtGui.QIcon("icons/mic.svg")
                self.recordButton.setIcon(icon)
                self.title.setStatusTip("Recording stopped.")
                self.recording = False
            else:
                # Start recording
                self.recorder.start_recording(self.wave_output_file)
                icon = QtGui.QIcon("icons/stop.svg")
                self.recordButton.setIcon(icon)
                self.recording = True

        except ValueError:
            self.show_error_message("Please enter a valid duration in seconds.")
        except KeyboardInterrupt:
            self.recording = False
            self.title.setStatusTip("Recording stopped by interrupt.")
        except Exception as e:
            self.show_error_message(f"An error occurred: {str(e)}")

        self.validate_inputs()


    def play_audio_action(self):
        if self.wave_output_file:
            if self.audio_player is None:
                self.audio_player = playAudio(self.wave_output_file)

            if self.audio_player:
                if self.audio_player.is_playing:
                    self.audio_player.pause()
                    self.playButton.setIcon(QtGui.QIcon("icons/play.svg"))
                    self.title.setStatusTip("Playback paused")
                else:
                    self.audio_player.play()
                    self.playButton.setIcon(QtGui.QIcon("icons/pause.svg"))
                    self.title.setStatusTip(f"Playing {self.wave_output_file}")
            else:
                self.show_error_message("Error initializing audio player.")
        else:
            self.show_error_message("No recorded audio file available!")
        self.validate_inputs()

    def convert_to_midi_action(self):
        try:
            if self.wave_output_file:
                midi_filename = self.save_midi_field.text().strip()
                if not midi_filename.lower().endswith('.midi'):
                    midi_filename += '.midi'

                self.midi_output_file = midi_filename
                convert_to_midi(self.wave_output_file, self.midi_output_file)
                self.title.setStatusTip(f"Converted MIDI saved to {self.midi_output_file}")
            else:
                self.show_error_message("You need to record audio first!")
        except Exception as e:
            self.show_error_message(f"Error during MIDI conversion: {str(e)}")

    def show_error_message(self, message):
        QMessageBox.critical(self, "Error", message)
        self.title.setStatusTip(message)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
