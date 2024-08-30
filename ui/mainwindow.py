# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow
from record import record_audio
from midi import convert_to_midi
from playback import play_wav_file

class harmonize(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.wave_output_file = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = harmonize()
    widget.show()
    sys.exit(app.exec())
