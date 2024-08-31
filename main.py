import os
import webbrowser

from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6 import QtGui

from ui.ui_form import Ui_MainWindow
from record import RecordAudio
from midi import convert_to_midi
from playback import playAudio

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.save_voice_field.textChanged.connect(self.validate_inputs)
        self.save_midi_field.textChanged.connect(self.validate_inputs)
        self.recordButton.clicked.connect(self.record_audio_action)
        self.playButton.clicked.connect(self.play_audio_action)
        self.convertButton.clicked.connect(self.convert_to_midi_action)
        self.gitbutton.clicked.connect(self.git_url_action)
        self.title = self.statusBar()

        self.wave_output_file = None
        self.midi_output_file = None
        self.recorder = RecordAudio(self.waveframe)
        self.recording = False
        self.audio_player = None

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
                self.show_error_message("No filename! Recording cancelled.")
                return

            if not filename.endswith('.wav'):
                filename += '.wav'

            self.wave_output_file = filename

            if self.recording:
                self.recorder.stop_recording()
                icon = QtGui.QIcon("ui/icons/mic.svg")
                self.recordButton.setIcon(icon)
                self.update_status_bar(f"Recording stopped! Saved to {self.wave_output_file}")
                self.recording = False
                self.validate_inputs()

            else:
                self.recorder.start_recording(self.wave_output_file)
                icon = QtGui.QIcon("ui/icons/stop.svg")
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

    def play_audio_action(self):
        if self.wave_output_file:
            if self.audio_player is None:
                self.audio_player = playAudio(self.wave_output_file)

            if self.audio_player:
                if self.audio_player.is_playing:
                    self.audio_player.pause()
                    self.playButton.setIcon(QtGui.QIcon("ui/icons/play.svg"))
                    self.update_status_bar("Playback paused")
                else:
                    self.audio_player.play()
                    self.playButton.setIcon(QtGui.QIcon("ui/icons/pause.svg"))
                    self.update_status_bar(f"Playing {self.wave_output_file}")
            else:
                self.show_error_message("Error initializing audio player.")
        else:
            self.show_error_message("No recorded audio file!")
        self.validate_inputs()

    def convert_to_midi_action(self):
        try:
            if self.wave_output_file:
                midi_filename = self.save_midi_field.text().strip()
                if not midi_filename.endswith('.midi'):
                    midi_filename += '.midi'

                self.midi_output_file =  midi_filename
                convert_to_midi(self.wave_output_file, self.midi_output_file)
                msg = QMessageBox(self)
                msg.setWindowTitle("MIDI Conversion Success!")
                msg.setText(f"Converted MIDI saved to {self.midi_output_file}. Listen to it in your favorite audio editor!")
                msg.setIconPixmap(QtGui.QPixmap("ui/icons/convert.svg"))
                msg.exec()
                self.update_status_bar(f"Converted MIDI saved to {self.midi_output_file}")

                self.update_status_bar(f"Converted MIDI saved to {self.midi_output_file}")

            else:
                self.show_error_message("You need to record audio first!")
        except Exception as e:
            self.show_error_message(f"Error during MIDI conversion: {str(e)}")

    def git_url_action(self):
        url = "https://github.com/sreyasaju/harmonize"
        webbrowser.open(url)

    def update_status_bar(self, message):
        self.title.showMessage(message, 10000)

    def show_error_message(self, message):
        QMessageBox.critical(self, "Error", message)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()