# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QToolButton, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1008, 741)
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #191a29")
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setDocumentMode(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(30, 30, 271, 91))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(48)
        self.title.setFont(font1)
        self.title.setFrameShadow(QFrame.Shadow.Plain)
        self.title.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.title.setMargin(10)
        self.record_midi_Frame = QFrame(self.centralwidget)
        self.record_midi_Frame.setObjectName(u"record_midi_Frame")
        self.record_midi_Frame.setEnabled(True)
        self.record_midi_Frame.setGeometry(QRect(360, 160, 631, 511))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.record_midi_Frame.sizePolicy().hasHeightForWidth())
        self.record_midi_Frame.setSizePolicy(sizePolicy)
        self.record_midi_Frame.setMinimumSize(QSize(480, 362))
        self.record_midi_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.record_midi_Frame.setFrameShadow(QFrame.Shadow.Plain)
        self.waveframe = QFrame(self.record_midi_Frame)
        self.waveframe.setObjectName(u"waveframe")
        self.waveframe.setGeometry(QRect(10, 40, 600, 171))
        self.waveframe.setMinimumSize(QSize(600, 170))
        self.waveframe.setStyleSheet(u"background-color: rgb(18, 19, 30)")
        self.waveframe.setFrameShape(QFrame.Shape.NoFrame)
        self.waveframe.setFrameShadow(QFrame.Shadow.Raised)
        self.midiframe = QFrame(self.record_midi_Frame)
        self.midiframe.setObjectName(u"midiframe")
        self.midiframe.setGeometry(QRect(10, 320, 601, 170))
        self.midiframe.setMinimumSize(QSize(600, 170))
        self.midiframe.setStyleSheet(u"background-color: rgb(18, 19, 30)")
        self.midiframe.setFrameShape(QFrame.Shape.NoFrame)
        self.midiframe.setFrameShadow(QFrame.Shadow.Raised)
        self.recordButton = QToolButton(self.record_midi_Frame)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.recordButton)
        self.recordButton.setObjectName(u"recordButton")
        self.recordButton.setEnabled(True)
        self.recordButton.setGeometry(QRect(270, 180, 80, 80))
        self.recordButton.setMinimumSize(QSize(80, 80))
        self.recordButton.setStyleSheet(u"border-radius: 40px;\n"
"background-color: #45259b;")
        icon = QIcon()
        icon.addFile(u":/icons/ui/icons/mic.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.recordButton.setIcon(icon)
        self.recordButton.setIconSize(QSize(55, 55))
        self.recordButton.setCheckable(True)
        self.recordButton.setChecked(False)
        self.convertButton = QPushButton(self.record_midi_Frame)
        self.buttonGroup.addButton(self.convertButton)
        self.convertButton.setObjectName(u"convertButton")
        self.convertButton.setEnabled(True)
        self.convertButton.setGeometry(QRect(380, 190, 60, 60))
        self.convertButton.setMinimumSize(QSize(60, 60))
        font2 = QFont()
        font2.setPointSize(12)
        self.convertButton.setFont(font2)
        self.convertButton.setStyleSheet(u"border-radius: 30px;\n"
"background-color: #45259b;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/ui/icons/convert.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.convertButton.setIcon(icon1)
        self.convertButton.setIconSize(QSize(35, 35))
        self.convertButton.setCheckable(True)
        self.convertButton.setChecked(False)
        self.playButton = QPushButton(self.record_midi_Frame)
        self.buttonGroup.addButton(self.playButton)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setEnabled(True)
        self.playButton.setGeometry(QRect(180, 190, 60, 60))
        self.playButton.setMinimumSize(QSize(60, 60))
        self.playButton.setFont(font2)
        self.playButton.setStyleSheet(u"border-radius: 30px;\n"
"background-color: #45259b;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/ui/icons/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.playButton.setIcon(icon2)
        self.playButton.setIconSize(QSize(35, 35))
        self.playButton.setCheckable(True)
        self.playButton.setChecked(False)
        self.mid_frame_label = QLabel(self.record_midi_Frame)
        self.mid_frame_label.setObjectName(u"mid_frame_label")
        self.mid_frame_label.setGeometry(QRect(10, 280, 111, 21))
        font3 = QFont()
        font3.setFamilies([u"Ubuntu"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.mid_frame_label.setFont(font3)
        self.mid_frame_label.setStyleSheet(u"color: rgb(72, 76, 115)")
        self.record_frame_label = QLabel(self.record_midi_Frame)
        self.record_frame_label.setObjectName(u"record_frame_label")
        self.record_frame_label.setGeometry(QRect(10, 10, 151, 21))
        self.record_frame_label.setFont(font3)
        self.record_frame_label.setStyleSheet(u"color: rgb(72, 76, 115)")
        self.voice_settings = QGroupBox(self.centralwidget)
        self.voice_settings.setObjectName(u"voice_settings")
        self.voice_settings.setGeometry(QRect(20, 170, 318, 291))
        self.voice_settings.setMinimumSize(QSize(318, 250))
        self.voice_settings.setStyleSheet(u"background-color: #12131e;\n"
"border-radius: 10px")
        self.record_parameter_groupBox = QGroupBox(self.voice_settings)
        self.record_parameter_groupBox.setObjectName(u"record_parameter_groupBox")
        self.record_parameter_groupBox.setGeometry(QRect(30, 70, 251, 91))
        self.save_voice_label = QLabel(self.record_parameter_groupBox)
        self.save_voice_label.setObjectName(u"save_voice_label")
        self.save_voice_label.setGeometry(QRect(0, 30, 121, 41))
        font4 = QFont()
        font4.setFamilies([u"Ubuntu"])
        font4.setPointSize(15)
        self.save_voice_label.setFont(font4)
        self.save_voice_label.setStyleSheet(u"border-radius:5px;\n"
"background-color: #45259b")
        self.save_voice_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.save_voice_label.setMargin(10)
        self.save_voice_field = QLineEdit(self.record_parameter_groupBox)
        self.save_voice_field.setObjectName(u"save_voice_field")
        self.save_voice_field.setGeometry(QRect(110, 30, 141, 41))
        self.save_voice_field.setFont(font4)
        self.save_voice_field.setStyleSheet(u"border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.record_parameters_header = QLabel(self.record_parameter_groupBox)
        self.record_parameters_header.setObjectName(u"record_parameters_header")
        self.record_parameters_header.setGeometry(QRect(0, 0, 251, 21))
        self.record_parameters_header.setFont(font3)
        self.record_parameters_header.setStyleSheet(u"color: rgb(93, 98, 159)")
        self.audio_parameters_groupBox = QGroupBox(self.voice_settings)
        self.audio_parameters_groupBox.setObjectName(u"audio_parameters_groupBox")
        self.audio_parameters_groupBox.setGeometry(QRect(30, 170, 271, 121))
        self.gain_slider = QSlider(self.audio_parameters_groupBox)
        self.gain_slider.setObjectName(u"gain_slider")
        self.gain_slider.setGeometry(QRect(80, 40, 171, 31))
        self.gain_slider.setMinimumSize(QSize(0, 10))
        self.gain_slider.setStyleSheet(u"QSlider:horizontal {\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #2d2d3d;\n"
"    height: 10px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        /* Tick at 0% */\n"
"        stop:0.0 #4b4b5e, stop:0.01 #4b4b5e, stop:0.011 #1e1e24,\n"
"        /* Gap */\n"
"        stop:0.24 #1e1e24,\n"
"        /* Tick at 25% */\n"
"        stop:0.241 #4b4b5e, stop:0.25 #4b4b5e, stop:0.251 #1e1e24,\n"
"        /* Gap */\n"
"        stop:0.49 #1e1e24,\n"
"        /* Tick at 50% */\n"
"        stop:0.491 #4b4b5e, stop:0.50 #4b4b5e, stop:0.501 #1e1e24,\n"
"        /* Gap */\n"
"        stop:0.74 #1e1e24,\n"
"        /* Tick at 75% */\n"
"        stop:0.741 #4b4b5e, stop:0.75 #4b4b5e, stop:0.751 #1e1e24,\n"
"        /* Gap */\n"
"        stop:0.99 #1e1e24,\n"
"        /* Tick at 100% */\n"
"        stop:0.991 #4b4b5e, stop:1.0 #4b4b5e);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:"
                        "1, y2:0,\n"
"        /* Tick at 0% (Dark Purple) */\n"
"        stop:0.0 #4b4b5e, stop:0.01 #4b4b5e, stop:0.011 #45259b,\n"
"        /* Gap blending from dark purple to mid purple */\n"
"        stop:0.24 #4a28a3,\n"
"        /* Tick at 25% */\n"
"        stop:0.241 #4b4b5e, stop:0.25 #4b4b5e, stop:0.251 #4a28a3,\n"
"        /* Gap blending toward center */\n"
"        stop:0.49 #502fb3,\n"
"        /* Tick at 50% */\n"
"        stop:0.491 #4b4b5e, stop:0.50 #4b4b5e, stop:0.501 #502fb3,\n"
"        /* Gap blending toward vibrant purple */\n"
"        stop:0.74 #5532cc,\n"
"        /* Tick at 75% */\n"
"        stop:0.741 #4b4b5e, stop:0.75 #4b4b5e, stop:0.751 #5532cc,\n"
"        /* Gap leading to the end color */\n"
"        stop:0.99 #5b36e3,\n"
"        /* Tick at 100% */\n"
"        stop:0.991 #4b4b5e, stop:1.0 #4b4b5e);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #8b5cf6;\n"
"	border: 2px solid #8b5cf6;\n"
"    width: 14px;\n"
"    margin-top: -5px;     \n"
""
                        "    margin-bottom: -5px;\n"
"    border-radius: 8px;   \n"
"}\n"
"\n"
"QSlider::ticks:horizontal {\n"
"    background: none;\n"
"    color: #4b4b5e;\n"
"    height: 5px;\n"
"}")
        self.gain_slider.setMaximum(100)
        self.gain_slider.setSingleStep(10)
        self.gain_slider.setSliderPosition(50)
        self.gain_slider.setTracking(False)
        self.gain_slider.setOrientation(Qt.Orientation.Horizontal)
        self.gain_slider.setInvertedAppearance(False)
        self.gain_slider.setInvertedControls(True)
        self.gain_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.gain_slider.setTickInterval(5)
        self.gain_left = QProgressBar(self.audio_parameters_groupBox)
        self.gain_left.setObjectName(u"gain_left")
        self.gain_left.setGeometry(QRect(0, 0, 21, 71))
        self.gain_left.setMinimumSize(QSize(19, 17))
        self.gain_left.setStyleSheet(u"QProgressBar:vertical {\n"
"    border: 1px solid #2d2d3d;\n"
"    background: #11121a;\n"
"    width: 12px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QProgressBar::chunk:vertical {\n"
"    background: qlineargradient(x1:0, y1:1, x2:0, y2:0,\n"
"                                stop:0.0 #46c280,  /* Vibrant Green */\n"
"                                stop:0.7 #dbd374,  /* Warm Yellow/Orange */\n"
"                                stop:0.9 #c97c77,);  /* Danger Red */\n"
"    border-radius: 2px;\n"
"}")
        self.gain_left.setValue(100)
        self.gain_left.setTextVisible(False)
        self.gain_left.setOrientation(Qt.Orientation.Vertical)
        self.gain_left.setInvertedAppearance(False)
        self.gain_left.setTextDirection(QProgressBar.Direction.BottomToTop)
        self.gain_right = QProgressBar(self.audio_parameters_groupBox)
        self.gain_right.setObjectName(u"gain_right")
        self.gain_right.setGeometry(QRect(40, 0, 21, 71))
        self.gain_right.setMinimumSize(QSize(19, 17))
        self.gain_right.setStyleSheet(u"QProgressBar:vertical {\n"
"    border: 1px solid #2d2d3d;\n"
"    background: #11121a;\n"
"    width: 12px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QProgressBar::chunk:vertical {\n"
"    background: qlineargradient(x1:0, y1:1, x2:0, y2:0,\n"
"                                stop:0.0 #46c280,  /* Vibrant Green */\n"
"                                stop:0.7 #dbd374,  /* Warm Yellow/Orange */\n"
"                                stop:0.9 #c97c77,);  /* Danger Red */\n"
"    border-radius: 2px;\n"
"}")
        self.gain_right.setValue(100)
        self.gain_right.setTextVisible(False)
        self.gain_right.setOrientation(Qt.Orientation.Vertical)
        self.gain_right.setInvertedAppearance(False)
        self.gain_right.setTextDirection(QProgressBar.Direction.BottomToTop)
        self.input_gain_header = QLabel(self.audio_parameters_groupBox)
        self.input_gain_header.setObjectName(u"input_gain_header")
        self.input_gain_header.setGeometry(QRect(90, 10, 171, 21))
        self.input_gain_header.setFont(font3)
        self.input_gain_header.setStyleSheet(u"color: rgb(93, 98, 159)")
        self.zero_perc = QLabel(self.audio_parameters_groupBox)
        self.zero_perc.setObjectName(u"zero_perc")
        self.zero_perc.setGeometry(QRect(90, 70, 21, 16))
        font5 = QFont()
        font5.setFamilies([u"Ubuntu"])
        self.zero_perc.setFont(font5)
        self.zero_perc.setStyleSheet(u"color: rgb(83, 80, 120)")
        self.fifty_perc = QLabel(self.audio_parameters_groupBox)
        self.fifty_perc.setObjectName(u"fifty_perc")
        self.fifty_perc.setGeometry(QRect(150, 70, 31, 16))
        self.fifty_perc.setFont(font5)
        self.fifty_perc.setStyleSheet(u"color: rgb(83, 80, 120)")
        self.hundred_perc = QLabel(self.audio_parameters_groupBox)
        self.hundred_perc.setObjectName(u"hundred_perc")
        self.hundred_perc.setGeometry(QRect(210, 70, 41, 16))
        self.hundred_perc.setFont(font5)
        self.hundred_perc.setStyleSheet(u"color: rgb(83, 80, 120)")
        self.L = QLabel(self.audio_parameters_groupBox)
        self.L.setObjectName(u"L")
        self.L.setGeometry(QRect(0, 80, 21, 20))
        self.L.setFont(font5)
        self.L.setStyleSheet(u"color: rgb(83, 80, 120)")
        self.R = QLabel(self.audio_parameters_groupBox)
        self.R.setObjectName(u"R")
        self.R.setGeometry(QRect(41, 80, 20, 21))
        self.R.setFont(font5)
        self.R.setStyleSheet(u"color: rgb(83, 80, 120)")
        self.voice_input_header = QLabel(self.voice_settings)
        self.voice_input_header.setObjectName(u"voice_input_header")
        self.voice_input_header.setGeometry(QRect(30, 30, 261, 21))
        self.voice_input_header.setFont(font3)
        self.voice_input_header.setStyleSheet(u"color: rgb(141, 146, 201)")
        self.gitbutton = QPushButton(self.centralwidget)
        self.gitbutton.setObjectName(u"gitbutton")
        self.gitbutton.setGeometry(QRect(920, 60, 61, 61))
        self.gitbutton.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #45259b;\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/ui/icons/github.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.gitbutton.setIcon(icon3)
        self.gitbutton.setIconSize(QSize(32, 32))
        self.gitbutton.setFlat(False)
        self.settings_3 = QGroupBox(self.centralwidget)
        self.settings_3.setObjectName(u"settings_3")
        self.settings_3.setGeometry(QRect(20, 480, 318, 189))
        self.settings_3.setMinimumSize(QSize(318, 189))
        self.settings_3.setStyleSheet(u"background-color: #12131e;\n"
"border-radius: 10px")
        self.midi_parameter = QGroupBox(self.settings_3)
        self.midi_parameter.setObjectName(u"midi_parameter")
        self.midi_parameter.setGeometry(QRect(30, 70, 281, 91))
        self.midi_parameter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.save_midi_field = QLineEdit(self.midi_parameter)
        self.save_midi_field.setObjectName(u"save_midi_field")
        self.save_midi_field.setGeometry(QRect(110, 30, 141, 41))
        self.save_midi_field.setFont(font4)
        self.save_midi_field.setStyleSheet(u"border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.save_midi_field.setFrame(True)
        self.save_midi_field.setClearButtonEnabled(False)
        self.save_midi_label = QLabel(self.midi_parameter)
        self.save_midi_label.setObjectName(u"save_midi_label")
        self.save_midi_label.setGeometry(QRect(0, 30, 131, 41))
        self.save_midi_label.setFont(font4)
        self.save_midi_label.setStyleSheet(u"border-radius:5px;\n"
"background-color: #45259b")
        self.save_midi_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.save_midi_label.setMargin(10)
        self.save_midi_label.raise_()
        self.save_midi_field.raise_()
        self.midiOutput = QLabel(self.settings_3)
        self.midiOutput.setObjectName(u"midiOutput")
        self.midiOutput.setGeometry(QRect(30, 30, 261, 21))
        self.midiOutput.setFont(font3)
        self.midiOutput.setStyleSheet(u"color: rgb(141, 146, 201)")
        self.midi_header = QLabel(self.settings_3)
        self.midi_header.setObjectName(u"midi_header")
        self.midi_header.setGeometry(QRect(30, 70, 251, 21))
        self.midi_header.setFont(font3)
        self.midi_header.setStyleSheet(u"color: rgb(93, 98, 159);\n"
"")
        self.about = QLabel(self.centralwidget)
        self.about.setObjectName(u"about")
        self.about.setGeometry(QRect(530, 50, 385, 74))
        font6 = QFont()
        font6.setFamilies([u"Ubuntu"])
        font6.setPointSize(12)
        self.about.setFont(font6)
        self.about.setFrameShadow(QFrame.Shadow.Plain)
        self.about.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.about.setMargin(10)
        self.record_parameters_header_11 = QLabel(self.centralwidget)
        self.record_parameters_header_11.setObjectName(u"record_parameters_header_11")
        self.record_parameters_header_11.setGeometry(QRect(40, 110, 441, 21))
        font7 = QFont()
        font7.setFamilies([u"Ubuntu"])
        font7.setPointSize(19)
        font7.setBold(False)
        self.record_parameters_header_11.setFont(font7)
        self.record_parameters_header_11.setStyleSheet(u"color: rgb(255, 255, 255)")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"harmonize", None))
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>harmonize</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(statustip)
        self.title.setStatusTip(QCoreApplication.translate("MainWindow", u"Developed by Sreya Saju \u00a9 2024 ", None))
#endif // QT_CONFIG(statustip)
        self.title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">harmonize</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.record_midi_Frame.setStatusTip(QCoreApplication.translate("MainWindow", u"Developed by Sreya Saju ", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.recordButton.setToolTip(QCoreApplication.translate("MainWindow", u"Start/Stop Recording...", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.recordButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Start/Stop Recording!", None))
#endif // QT_CONFIG(statustip)
        self.recordButton.setText("")
#if QT_CONFIG(tooltip)
        self.convertButton.setToolTip(QCoreApplication.translate("MainWindow", u"Convert to MIDI", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.convertButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Convert to MIDI!", None))
#endif // QT_CONFIG(statustip)
        self.convertButton.setText("")
#if QT_CONFIG(tooltip)
        self.playButton.setToolTip(QCoreApplication.translate("MainWindow", u"Play/ Pause your Voice!", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.playButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Play/Pause your Voice!", None))
#endif // QT_CONFIG(statustip)
        self.playButton.setText("")
        self.mid_frame_label.setText(QCoreApplication.translate("MainWindow", u"MIDI RENDER", None))
        self.record_frame_label.setText(QCoreApplication.translate("MainWindow", u"VOICE WAVEFORM", None))
        self.save_voice_label.setText(QCoreApplication.translate("MainWindow", u"Save Voice As:", None))
#if QT_CONFIG(tooltip)
        self.save_voice_field.setToolTip(QCoreApplication.translate("MainWindow", u"Enter the filename to save your voice recording, don't forget the extension! e.g., voice.wav", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.save_voice_field.setStatusTip(QCoreApplication.translate("MainWindow", u"Enter filename to save recording, with \".wav\" extension", None))
#endif // QT_CONFIG(statustip)
        self.save_voice_field.setText("")
        self.save_voice_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"voice.wav", None))
        self.record_parameters_header.setText(QCoreApplication.translate("MainWindow", u"Record Parameters: ", None))
        self.input_gain_header.setText(QCoreApplication.translate("MainWindow", u"Input Gain: ", None))
        self.zero_perc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.fifty_perc.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.hundred_perc.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.L.setText(QCoreApplication.translate("MainWindow", u"  L", None))
        self.R.setText(QCoreApplication.translate("MainWindow", u" R", None))
        self.voice_input_header.setText(QCoreApplication.translate("MainWindow", u"VOICE INPUT ", None))
#if QT_CONFIG(statustip)
        self.gitbutton.setStatusTip(QCoreApplication.translate("MainWindow", u"Checkout the git repo! https://github.com/sreyasaju/harmonize", None))
#endif // QT_CONFIG(statustip)
        self.gitbutton.setText("")
#if QT_CONFIG(tooltip)
        self.save_midi_field.setToolTip(QCoreApplication.translate("MainWindow", u"Enter the filename to save the MIDI output, and don't forget the extension! e.g., output.midi", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.save_midi_field.setStatusTip(QCoreApplication.translate("MainWindow", u"Enter filename to save the midi file, with \".midi\" extension", None))
#endif // QT_CONFIG(statustip)
        self.save_midi_field.setText("")
        self.save_midi_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"output.midi", None))
        self.save_midi_label.setText(QCoreApplication.translate("MainWindow", u"Save MIDI As:", None))
        self.midiOutput.setText(QCoreApplication.translate("MainWindow", u"MIDI OUTPUT", None))
        self.midi_header.setText(QCoreApplication.translate("MainWindow", u"MIDI Parameters: ", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:18pt;\">Transform your voice to MIDI</span></p><p align=\"right\"><span style=\" font-size:18pt;\">Set the parameters and start recording!</span></p></body></html>", None))
        self.record_parameters_header_11.setText(QCoreApplication.translate("MainWindow", u"Copyright \u00a9 2024-2026, Sreya Saju, MIT license", None))
    # retranslateUi

