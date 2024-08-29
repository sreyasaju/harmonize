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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(835, 610)
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #191a29")
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setDocumentMode(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(480, 220))
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Plain)
        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 40, 480, 211))
        self.frame.setMinimumSize(QSize(480, 150))
        self.frame.setStyleSheet(u"background-color: rgb(18, 19, 30)")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_6 = QPushButton(self.frame_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(310, 230, 60, 60))
        self.pushButton_6.setMinimumSize(QSize(60, 60))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(u"border-radius: 30px;\n"
"background-color: #45259b;")
        icon = QIcon()
        icon.addFile(u"icons/convert.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QSize(35, 35))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(False)
        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QRect(200, 220, 80, 80))
        self.pushButton_5.setMinimumSize(QSize(80, 80))
        self.pushButton_5.setStyleSheet(u"border-radius: 40px;\n"
"background-color: #45259b;")
        icon1 = QIcon()
        icon1.addFile(u"icons/mic.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u"icons/stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QSize(55, 55))
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setChecked(False)
        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(110, 230, 60, 60))
        self.pushButton_4.setMinimumSize(QSize(60, 60))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"border-radius: 30px;\n"
"background-color: #45259b;")
        icon2 = QIcon()
        icon2.addFile(u"icons/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u"icons/pause.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(35, 35))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setChecked(False)

        self.gridLayout.addWidget(self.frame_5, 3, 1, 2, 1)

        self.settings = QWidget(self.centralwidget)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(290, 320))
        self.settings.setStyleSheet(u"background-color: #12131e;\n"
"border-radius: 10px")
        self.record_parameter_frame_2 = QFrame(self.settings)
        self.record_parameter_frame_2.setObjectName(u"record_parameter_frame_2")
        self.record_parameter_frame_2.setGeometry(QRect(30, 40, 251, 151))
        self.record_parameter_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.record_parameter_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.save_voice_label = QLabel(self.record_parameter_frame_2)
        self.save_voice_label.setObjectName(u"save_voice_label")
        self.save_voice_label.setGeometry(QRect(0, 90, 121, 41))
        font2 = QFont()
        font2.setFamilies([u"Ubuntu"])
        font2.setPointSize(15)
        self.save_voice_label.setFont(font2)
        self.save_voice_label.setStyleSheet(u"border-radius:5px;\n"
"background-color: #45259b")
        self.save_voice_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.save_voice_label.setMargin(10)
        self.duration_label = QLabel(self.record_parameter_frame_2)
        self.duration_label.setObjectName(u"duration_label")
        self.duration_label.setGeometry(QRect(0, 30, 171, 41))
        self.duration_label.setMinimumSize(QSize(90, 41))
        self.duration_label.setFont(font2)
        self.duration_label.setStyleSheet(u"border-radius:5px;\n"
"background-color: #45259b")
        self.duration_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.duration_label.setMargin(5)
        self.save_voice_label_2 = QLineEdit(self.record_parameter_frame_2)
        self.save_voice_label_2.setObjectName(u"save_voice_label_2")
        self.save_voice_label_2.setGeometry(QRect(110, 90, 141, 41))
        self.save_voice_label_2.setFont(font2)
        self.save_voice_label_2.setStyleSheet(u"border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.record_parameters_header = QLabel(self.record_parameter_frame_2)
        self.record_parameters_header.setObjectName(u"record_parameters_header")
        self.record_parameters_header.setGeometry(QRect(0, 0, 251, 21))
        font3 = QFont()
        font3.setFamilies([u"Ubuntu"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.record_parameters_header.setFont(font3)
        self.record_parameters_header.setStyleSheet(u"color: rgb(56, 59, 94)")
        self.duration_field_2 = QLineEdit(self.record_parameter_frame_2)
        self.duration_field_2.setObjectName(u"duration_field_2")
        self.duration_field_2.setGeometry(QRect(160, 30, 91, 41))
        self.duration_field_2.setMinimumSize(QSize(90, 41))
        self.duration_field_2.setFont(font2)
        self.duration_field_2.setStyleSheet(u"border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.duration_field_2.setMaxLength(7200)
        self.frame_3 = QFrame(self.settings)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 220, 271, 81))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.midi_header = QLabel(self.frame_3)
        self.midi_header.setObjectName(u"midi_header")
        self.midi_header.setGeometry(QRect(0, 0, 251, 21))
        self.midi_header.setFont(font3)
        self.midi_header.setStyleSheet(u"color: rgb(56, 59, 94)")
        self.save_MIDI_label = QLabel(self.frame_3)
        self.save_MIDI_label.setObjectName(u"save_MIDI_label")
        self.save_MIDI_label.setGeometry(QRect(0, 30, 131, 41))
        self.save_MIDI_label.setFont(font2)
        self.save_MIDI_label.setStyleSheet(u"border-radius:5px;\n"
"background-color: #45259b")
        self.save_MIDI_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.save_MIDI_label.setMargin(10)
        self.save_midi_label = QLineEdit(self.frame_3)
        self.save_midi_label.setObjectName(u"save_midi_label")
        self.save_midi_label.setGeometry(QRect(110, 30, 141, 41))
        self.save_midi_label.setStyleSheet(u"border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.frame_3.raise_()
        self.record_parameter_frame_2.raise_()

        self.gridLayout.addWidget(self.settings, 3, 0, 2, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"Ubuntu"])
        font4.setPointSize(48)
        self.label.setFont(font4)
        self.label.setFrameShadow(QFrame.Shadow.Plain)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label.setMargin(10)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(10)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"harmonize", None))
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>harmonize</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.pushButton_6.setToolTip(QCoreApplication.translate("MainWindow", u"Convert to MIDI", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_6.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton_6.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_5.setToolTip(QCoreApplication.translate("MainWindow", u"Start Recording...", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_5.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton_5.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_4.setToolTip(QCoreApplication.translate("MainWindow", u"Play your Voice!", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_4.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton_4.setText("")
        self.save_voice_label.setText(QCoreApplication.translate("MainWindow", u"Save Voice As:", None))
        self.duration_label.setText(QCoreApplication.translate("MainWindow", u"Duration (in seconds):", None))
        self.save_voice_label_2.setText("")
        self.save_voice_label_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"voice.wav", None))
        self.record_parameters_header.setText(QCoreApplication.translate("MainWindow", u"Record Parameters: ", None))
        self.duration_field_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"60", None))
        self.midi_header.setText(QCoreApplication.translate("MainWindow", u"MIDI File: ", None))
        self.save_MIDI_label.setText(QCoreApplication.translate("MainWindow", u"Save MIDI As:", None))
        self.save_midi_label.setText("")
        self.save_midi_label.setPlaceholderText(QCoreApplication.translate("MainWindow", u"output.midi", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>harmonize</p><p><span style=\" font-size:18pt;\">Copyright \u00a9 2024 Sreya Saju</span></p><p><span style=\" font-size:18pt;\">Licensed under MIT license</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Convert your voice to MIDI</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

