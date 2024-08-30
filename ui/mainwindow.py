# This Python file uses the following encoding: utf-8
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow
from record import record_audio
from midi import convert_to_midi
from playback import play_wav_file

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect UI elements to functions
        self.ui.recordButton.clicked.connect(self.record_voice)
        self.ui.playButton.clicked.connect(self.play_recorded_voice)
        self.ui.convertButton.clicked.connect(self.convert_audio_to_midi)

    def record_voice(self):
        record_seconds = int(self.ui.recordDurationInput.text())  # Assuming there is a QLineEdit for input
        self.wave_output_file = self.ui.outputFileNameInput.text()  # Assuming there is a QLineEdit for filename
        record_audio(record_seconds, self.wave_output_file)
        QtWidgets.QMessageBox.information(self, "Recording", "Recording saved successfully!")

    def play_recorded_voice(self):
        if self.wave_output_file is None:
            QtWidgets.QMessageBox.warning(self, "Error", "No recorded audio file available!")
            return
        play_wav_file(self.wave_output_file)

    def convert_audio_to_midi(self):
        if self.wave_output_file is None:
            QtWidgets.QMessageBox.warning(self, "Error", "You need to record audio first!")
            return
        midi_output = self.ui.midiOutputFileNameInput.text()  # Assuming there is a QLineEdit for MIDI filename
        convert_to_midi(self.wave_output_file, midi_output)
        QtWidgets.QMessageBox.information(self, "Conversion", "Audio converted to MIDI successfully!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
