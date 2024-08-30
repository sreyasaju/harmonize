# This Python file uses the following encoding: utf-8
import sys
import os
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QStatusBar
from PyQt6 import QtGui

from ui_form import Ui_MainWindow
from record import AudioRecorder
from midi import convert_to_midi
from playback import play_wav_file

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.duration_field.textChanged.connect(self.validate_inputs)
        self.save_voice_field.textChanged.connect(self.validate_inputs)
        self.save_midi_field.textChanged.connect(self.validate_inputs)

        self.recordButton.clicked.connect(self.record_audio_action)
        self.playButton.clicked.connect(self.play_audio_action)
        self.convertButton.clicked.connect(self.convert_to_midi_action)

        self.wave_output_file = None
        self.midi_output_file = None
        self.recorder = AudioRecorder()
        self.recording = False

        # disable all the buttons
        self.recordButton.setEnabled(False)
        self.playButton.setEnabled(False)
        self.convertButton.setEnabled(False)

    def validate_inputs(self):
        record_seconds = self.duration_field.text().strip() if self.duration_field.text() else ''
        voice_filename = self.save_voice_field.text().strip() if self.save_voice_field.text() else ''
        midi_filename = self.save_midi_field.text().strip() if self.save_midi_field.text() else ''

        self.recordButton.setEnabled(bool(record_seconds) and bool(voice_filename))
        wave_file_exists = bool(self.wave_output_file) and os.path.exists(self.wave_output_file or "")
        self.playButton.setEnabled(wave_file_exists)
        all_filled = bool(record_seconds and voice_filename and midi_filename) and wave_file_exists
        self.convertButton.setEnabled(all_filled)

    def record_audio_action(self):
        try:
            record_seconds = int(self.duration_field.text().strip())
            filename = self.save_voice_field.text().strip()

            if not filename:
                self.title.setStatusTip("No filename! Recording cancelled.")
                return

            if not filename.lower().endswith('.wav'):
                filename += '.wav'

            self.wave_output_file = filename

            if self.recording:
                # stop recording
                self.recorder.stop_recording()
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/mic.svg"), QtGui.QIcon.Mode.Normal)
                self.title.setStatusTip("Recording stopped.")
                self.recording = False
            else:
                # start recording
                self.recorder.start_recording(self.wave_output_file)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/stop.svg"), QtGui.QIcon.Mode.Normal)
                self.title.setStatusTip(f"Recording started for {record_seconds} seconds.")
                self.recording = True

        except ValueError:
            self.show_error_message("Please enter a valid duration in seconds.")
        except KeyboardInterrupt:
            self.recording = False
            self.title.setStatusTip("Recording stopped by interrupt.")
        except Exception as e:
            self.show_error_message(f"An error occurred: {str(e)}")

    def play_audio_action(self):
        if self.wave_output_file:
            play_wav_file(self.wave_output_file)
            self.title.setStatusTip(f"Playing {self.wave_output_file}")
        else:
            self.show_error_message("No recorded audio file available!")

    def convert_to_midi_action(self):
        if self.wave_output_file:
            midi_filename = self.save_midi_field.text().strip()
            if not midi_filename.lower().endswith('.midi'):
                midi_filename += '.midi'

            self.midi_output_file = midi_filename
            convert_to_midi(self.wave_output_file, self.midi_output_file)
            self.title.setStatusTip(f"Converted MIDI saved to {self.midi_output_file}")
        else:
            self.show_error_message("You need to record audio first!")

    def show_error_message(self, message):
        QMessageBox.critical(self, "Error", message)
        self.title.setStatusTip(message)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
