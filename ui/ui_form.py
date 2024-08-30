# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 571)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #191a29")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        MainWindow.setDocumentMode(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(48)
        self.title.setFont(font)
        self.title.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setObjectName("widget")
        self.about = QtWidgets.QLabel(parent=self.widget)
        self.about.setGeometry(QtCore.QRect(90, 10, 381, 91))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(48)
        self.about.setFont(font)
        self.about.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.about.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.about.setObjectName("about")
        self.gitbutton = QtWidgets.QPushButton(parent=self.widget)
        self.gitbutton.setGeometry(QtCore.QRect(420, 100, 41, 41))
        self.gitbutton.setStyleSheet("border-radius: 5px;\n"
"background-color: #45259b;")
        self.gitbutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/github.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.gitbutton.setIcon(icon)
        self.gitbutton.setIconSize(QtCore.QSize(25, 25))
        self.gitbutton.setFlat(False)
        self.gitbutton.setObjectName("gitbutton")
        self.gridLayout.addWidget(self.widget, 0, 1, 2, 1)
        self.settings = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.settings.setMinimumSize(QtCore.QSize(315, 362))
        self.settings.setStyleSheet("background-color: #12131e;\n"
"border-radius: 10px")
        self.settings.setObjectName("settings")
        self.record_parameter_groupBox_2 = QtWidgets.QGroupBox(parent=self.settings)
        self.record_parameter_groupBox_2.setGeometry(QtCore.QRect(30, 40, 251, 151))
        self.record_parameter_groupBox_2.setObjectName("record_parameter_groupBox_2")
        self.save_voice_label = QtWidgets.QLabel(parent=self.record_parameter_groupBox_2)
        self.save_voice_label.setGeometry(QtCore.QRect(0, 90, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        self.save_voice_label.setFont(font)
        self.save_voice_label.setStyleSheet("border-radius:5px;\n"
"background-color: #45259b")
        self.save_voice_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.save_voice_label.setObjectName("save_voice_label")
        self.duration_label = QtWidgets.QLabel(parent=self.record_parameter_groupBox_2)
        self.duration_label.setGeometry(QtCore.QRect(0, 30, 171, 41))
        self.duration_label.setMinimumSize(QtCore.QSize(90, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        self.duration_label.setFont(font)
        self.duration_label.setStyleSheet("border-radius:5px;\n"
"background-color: #45259b")
        self.duration_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.duration_label.setObjectName("duration_label")
        self.save_voice_label_2 = QtWidgets.QLineEdit(parent=self.record_parameter_groupBox_2)
        self.save_voice_label_2.setGeometry(QtCore.QRect(110, 90, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        self.save_voice_label_2.setFont(font)
        self.save_voice_label_2.setStyleSheet("border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.save_voice_label_2.setText("")
        self.save_voice_label_2.setObjectName("save_voice_label_2")
        self.record_parameters_header = QtWidgets.QLabel(parent=self.record_parameter_groupBox_2)
        self.record_parameters_header.setGeometry(QtCore.QRect(0, 0, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(16)
        font.setBold(True)
        self.record_parameters_header.setFont(font)
        self.record_parameters_header.setStyleSheet("color: rgb(56, 59, 94)")
        self.record_parameters_header.setObjectName("record_parameters_header")
        self.duration_field_2 = QtWidgets.QLineEdit(parent=self.record_parameter_groupBox_2)
        self.duration_field_2.setGeometry(QtCore.QRect(160, 30, 91, 41))
        self.duration_field_2.setMinimumSize(QtCore.QSize(90, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        self.duration_field_2.setFont(font)
        self.duration_field_2.setStyleSheet("border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.duration_field_2.setMaxLength(7200)
        self.duration_field_2.setObjectName("duration_field_2")
        self.midi_parameters_groupBox = QtWidgets.QGroupBox(parent=self.settings)
        self.midi_parameters_groupBox.setGeometry(QtCore.QRect(30, 220, 271, 81))
        self.midi_parameters_groupBox.setObjectName("midi_parameters_groupBox")
        self.midi_header = QtWidgets.QLabel(parent=self.midi_parameters_groupBox)
        self.midi_header.setGeometry(QtCore.QRect(0, 0, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(16)
        font.setBold(True)
        self.midi_header.setFont(font)
        self.midi_header.setStyleSheet("color: rgb(56, 59, 94)")
        self.midi_header.setObjectName("midi_header")
        self.save_MIDI_label = QtWidgets.QLabel(parent=self.midi_parameters_groupBox)
        self.save_MIDI_label.setGeometry(QtCore.QRect(0, 30, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        self.save_MIDI_label.setFont(font)
        self.save_MIDI_label.setStyleSheet("border-radius:5px;\n"
"background-color: #45259b")
        self.save_MIDI_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.save_MIDI_label.setObjectName("save_MIDI_label")
        self.save_midi_label = QtWidgets.QLineEdit(parent=self.midi_parameters_groupBox)
        self.save_midi_label.setGeometry(QtCore.QRect(110, 30, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        self.save_midi_label.setFont(font)
        self.save_midi_label.setStyleSheet("border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.save_midi_label.setText("")
        self.save_midi_label.setFrame(True)
        self.save_midi_label.setClearButtonEnabled(False)
        self.save_midi_label.setObjectName("save_midi_label")
        self.midi_parameters_groupBox.raise_()
        self.record_parameter_groupBox_2.raise_()
        self.gridLayout.addWidget(self.settings, 3, 0, 2, 1)
        self.recordFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.recordFrame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recordFrame.sizePolicy().hasHeightForWidth())
        self.recordFrame.setSizePolicy(sizePolicy)
        self.recordFrame.setMinimumSize(QtCore.QSize(480, 362))
        self.recordFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.recordFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.recordFrame.setObjectName("recordFrame")
        self.waveframe = QtWidgets.QFrame(parent=self.recordFrame)
        self.waveframe.setGeometry(QtCore.QRect(0, 60, 480, 211))
        self.waveframe.setMinimumSize(QtCore.QSize(480, 210))
        self.waveframe.setStyleSheet("background-color: rgb(18, 19, 30)")
        self.waveframe.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.waveframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.waveframe.setObjectName("waveframe")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.recordFrame)
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setGeometry(QtCore.QRect(310, 230, 60, 60))
        self.pushButton_6.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border-radius: 30px;\n"
"background-color: #45259b;")
        self.pushButton_6.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/convert.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.pushButton_6)
        self.convertButton = QtWidgets.QPushButton(parent=self.recordFrame)
        self.convertButton.setEnabled(True)
        self.convertButton.setGeometry(QtCore.QRect(200, 220, 80, 80))
        self.convertButton.setMinimumSize(QtCore.QSize(80, 80))
        self.convertButton.setStyleSheet("border-radius: 40px;\n"
"background-color: #45259b;")
        self.convertButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/mic.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap("icons/stop.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.convertButton.setIcon(icon2)
        self.convertButton.setIconSize(QtCore.QSize(55, 55))
        self.convertButton.setCheckable(True)
        self.convertButton.setChecked(False)
        self.convertButton.setObjectName("convertButton")
        self.buttonGroup.addButton(self.convertButton)
        self.playButton = QtWidgets.QPushButton(parent=self.recordFrame)
        self.playButton.setEnabled(False)
        self.playButton.setGeometry(QtCore.QRect(110, 230, 60, 60))
        self.playButton.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("border-radius: 30px;\n"
"background-color: #45259b;")
        self.playButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/play.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon3.addPixmap(QtGui.QPixmap("icons/pause.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.playButton.setIcon(icon3)
        self.playButton.setIconSize(QtCore.QSize(35, 35))
        self.playButton.setCheckable(True)
        self.playButton.setChecked(False)
        self.playButton.setObjectName("playButton")
        self.buttonGroup.addButton(self.playButton)
        self.gridLayout.addWidget(self.recordFrame, 3, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "harmonize"))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>harmonize</p></body></html>"))
        self.title.setStatusTip(_translate("MainWindow", "Developed by Sreya Saju © 2024 "))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">harmonize</span></p><p><span style=\" font-size:18pt;\">Copyright © 2024 Sreya Saju</span></p><p><span style=\" font-size:18pt;\">Licensed under MIT license</span></p></body></html>"))
        self.about.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:18pt;\">Transform your voice to MIDI</span></p><p align=\"right\"><span style=\" font-size:18pt;\">Set the parameters and start recording!</span></p></body></html>"))
        self.gitbutton.setStatusTip(_translate("MainWindow", "Checkout the git repo! https://github.com/sreyasaju/harmonize"))
        self.save_voice_label.setText(_translate("MainWindow", "Save Voice As:"))
        self.duration_label.setText(_translate("MainWindow", "Duration (in seconds):"))
        self.save_voice_label_2.setToolTip(_translate("MainWindow", "Enter the filename to save your voice recording, don\'t forget the extension! e.g., voice.wav"))
        self.save_voice_label_2.setStatusTip(_translate("MainWindow", "Enter filename to save recording, with \".wav\" extension"))
        self.save_voice_label_2.setPlaceholderText(_translate("MainWindow", "voice.wav"))
        self.record_parameters_header.setText(_translate("MainWindow", "Record Parameters: "))
        self.duration_field_2.setToolTip(_translate("MainWindow", "Enter recording duration in seconds, e.g., 60"))
        self.duration_field_2.setStatusTip(_translate("MainWindow", "Enter the duration in seconds."))
        self.duration_field_2.setPlaceholderText(_translate("MainWindow", "60"))
        self.midi_header.setText(_translate("MainWindow", "MIDI File: "))
        self.save_MIDI_label.setText(_translate("MainWindow", "Save MIDI As:"))
        self.save_midi_label.setToolTip(_translate("MainWindow", "Enter the filename to save the MIDI output, and don\'t forget the extension! e.g., output.midi"))
        self.save_midi_label.setStatusTip(_translate("MainWindow", "Enter filename to save the midi file, with \".midi\" extension"))
        self.save_midi_label.setPlaceholderText(_translate("MainWindow", "output.midi"))
        self.recordFrame.setStatusTip(_translate("MainWindow", "Developed by Sreya Saju "))
        self.pushButton_6.setToolTip(_translate("MainWindow", "Convert to MIDI"))
        self.pushButton_6.setStatusTip(_translate("MainWindow", "Convert to MIDI!"))
        self.convertButton.setToolTip(_translate("MainWindow", "Start/Stop Recording..."))
        self.convertButton.setStatusTip(_translate("MainWindow", "Start/Stop Recording!"))
        self.playButton.setToolTip(_translate("MainWindow", "Play/ Pause your Voice!"))
        self.playButton.setStatusTip(_translate("MainWindow", "Play/Pause your Voice!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
