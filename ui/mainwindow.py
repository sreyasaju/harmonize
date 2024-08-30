# This Python file uses the following encoding: utf-8
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic.properties import QtWidgets

from ui_form import Ui_MainWindow
from record import record_audio
from midi import convert_to_midi
from playback import play_wav_file

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connect UI elements to functions
        self.ui.duration_field.textChanged.connect(self.validate_inputs)
        self.ui.save_voice_field.textChanged.connect(self.validate_inputs)
        self.ui.save_midi_field.textChanged.connect(self.validate_inputs)

        self.ui.recordButton.clicked.connect(self.record_audio_action)
        self.ui.playButton.clicked.connect(self.play_audio_action)
        self.ui.convertButton.clicked.connect(self.convert_to_midi_action)
        # Initialize state
        self.wave_output_file = None
        self.midi_output_file = None

    def validate_inputs(self):
        # Check if all fields are filled
        record_seconds = self.ui.duration_field.text().strip()
        voice_filename = self.ui.save_voice_field.text().strip()
        midi_filename = self.ui.save_midi_field.text().strip()

        # Enable buttons if all fields are filled and the record file exists
        self.ui.recordButton.setEnabled(bool(record_seconds) and bool(voice_filename))
        self.ui.convertButton.setEnabled(bool(voice_filename) and bool(midi_filename))
        self.ui.playButton.setEnabled(bool(voice_filename))

    def record_audio_action(self):
        try:
            record_seconds = int(self.ui.duration_field.text().strip())
            if not record_seconds:
                raise ValueError("Invalid duration")

            # Get the filename from the UI field
            filename = self.ui.save_voice_field.text().strip()

            if filename:
                # Append .wav extension if not present
                if not filename.lower().endswith('.wav'):
                    filename += '.wav'

                self.wave_output_file = filename
                record_audio(record_seconds, self.wave_output_file)
                self.statusBar.showMessage(f"Recording saved to {self.wave_output_file}")
                self.validate_inputs()  # Revalidate inputs after recording
            else:
                self.statusBar.showMessage("No filename provided. Recording cancelled.")
        except ValueError:
            self.show_error_message("Please enter a valid duration in seconds.")

    def play_audio_action(self):
        if self.wave_output_file:
            play_wav_file(self.wave_output_file)
            self.statusBar.showMessage(f"Playing {self.wave_output_file}")
        else:
            self.show_error_message("No recorded audio file available!")

    def convert_to_midi_action(self):
        if self.wave_output_file:
            self.midi_output_file, _ = QFileDialog.getSaveFileName(self, "Save File", "", "MIDI Files (*.midi)")
            if self.midi_output_file:
                convert_to_midi(self.wave_output_file, self.midi_output_file)
                self.save_midi_filename_edit.setText(self.midi_output_file)
                self.statusBar.showMessage(f"Converted MIDI saved to {self.midi_output_file}")
                self.validate_inputs()  # Revalidate inputs after conversion
            else:
                self.statusBar.showMessage("Conversion cancelled.")
        else:
            self.show_error_message("You need to record audio first!")

    def show_error_message(self, message):
        QMessageBox.critical(self, "Error", message)
        self.statusBar.showMessage(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
