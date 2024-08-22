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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(829, 609)
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #191a29")
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.settings = QWidget(self.centralwidget)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(20, 160, 311, 321))
        self.settings.setStyleSheet(u"background-color: #12131e;\n"
"border-radius: 5px")
        self.record_parameter_frame_2 = QFrame(self.settings)
        self.record_parameter_frame_2.setObjectName(u"record_parameter_frame_2")
        self.record_parameter_frame_2.setGeometry(QRect(20, 40, 271, 151))
        self.record_parameter_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.record_parameter_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.save_voice_label = QLabel(self.record_parameter_frame_2)
        self.save_voice_label.setObjectName(u"save_voice_label")
        self.save_voice_label.setGeometry(QRect(0, 90, 121, 41))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(15)
        self.save_voice_label.setFont(font1)
        self.save_voice_label.setStyleSheet(u"border-radius:5px;\n"
"background-color: #45259b")
        self.save_voice_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.save_voice_label.setMargin(10)
        self.duration_label = QLabel(self.record_parameter_frame_2)
        self.duration_label.setObjectName(u"duration_label")
        self.duration_label.setGeometry(QRect(0, 30, 171, 41))
        self.duration_label.setFont(font1)
        self.duration_label.setStyleSheet(u"border-radius:5px;\n"
"background-color: #45259b")
        self.duration_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.duration_label.setMargin(5)
        self.save_voice_label_2 = QLineEdit(self.record_parameter_frame_2)
        self.save_voice_label_2.setObjectName(u"save_voice_label_2")
        self.save_voice_label_2.setGeometry(QRect(110, 90, 141, 41))
        self.save_voice_label_2.setStyleSheet(u"border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.record_parameters_header = QLabel(self.record_parameter_frame_2)
        self.record_parameters_header.setObjectName(u"record_parameters_header")
        self.record_parameters_header.setGeometry(QRect(0, 0, 251, 21))
        font2 = QFont()
        font2.setFamilies([u"Ubuntu"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.record_parameters_header.setFont(font2)
        self.record_parameters_header.setStyleSheet(u"color: rgb(56, 59, 94)")
        self.duration_field = QLineEdit(self.record_parameter_frame_2)
        self.duration_field.setObjectName(u"duration_field")
        self.duration_field.setGeometry(QRect(160, 30, 91, 41))
        self.duration_field.setStyleSheet(u"border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.duration_field.setMaxLength(7200)
        self.frame_3 = QFrame(self.settings)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 200, 271, 81))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.midi_header = QLabel(self.frame_3)
        self.midi_header.setObjectName(u"midi_header")
        self.midi_header.setGeometry(QRect(0, 0, 251, 21))
        self.midi_header.setFont(font2)
        self.midi_header.setStyleSheet(u"color: rgb(56, 59, 94)")
        self.save_MIDI_label = QLabel(self.frame_3)
        self.save_MIDI_label.setObjectName(u"save_MIDI_label")
        self.save_MIDI_label.setGeometry(QRect(0, 30, 131, 41))
        self.save_MIDI_label.setFont(font1)
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
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(350, 30, 451, 151))
        self.frame.setStyleSheet(u"background-color: rgb(18, 19, 30)")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(450, 150, 61, 61))
        font3 = QFont()
        font3.setPointSize(12)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"border-radius: 30px;\n"
"background-color: #45259b;")
        icon = QIcon()
        icon.addFile(u"icons/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u"icons/pause.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(35, 35))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(630, 150, 61, 61))
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet(u"border-radius: 30px;\n"
"background-color: #45259b;")
        icon1 = QIcon()
        icon1.addFile(u"icons/convert.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(35, 35))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(False)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(350, 260, 451, 301))
        self.frame_2.setStyleSheet(u"background-color: rgb(18, 19, 30)")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.record_parameters_header_2 = QLabel(self.frame_2)
        self.record_parameters_header_2.setObjectName(u"record_parameters_header_2")
        self.record_parameters_header_2.setGeometry(QRect(10, 10, 41, 21))
        self.record_parameters_header_2.setFont(font2)
        self.record_parameters_header_2.setStyleSheet(u"color: rgb(56, 59, 94)")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(530, 140, 81, 81))
        self.pushButton.setStyleSheet(u"border-radius: 40px;\n"
"background-color: #45259b;")
        icon2 = QIcon()
        icon2.addFile(u"icons/mic.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u"icons/stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(55, 55))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
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
        self.save_voice_label.setText(QCoreApplication.translate("MainWindow", u"Save Voice As:", None))
        self.duration_label.setText(QCoreApplication.translate("MainWindow", u"Duration (in seconds):", None))
        self.save_voice_label_2.setText("")
        self.save_voice_label_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"voice.wav", None))
        self.record_parameters_header.setText(QCoreApplication.translate("MainWindow", u"Record Parameters: ", None))
        self.duration_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"60", None))
        self.midi_header.setText(QCoreApplication.translate("MainWindow", u"MIDI File: ", None))
        self.save_MIDI_label.setText(QCoreApplication.translate("MainWindow", u"Save MIDI As:", None))
        self.save_midi_label.setText("")
        self.save_midi_label.setPlaceholderText(QCoreApplication.translate("MainWindow", u"output.midi", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"Play your Voice!", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"Convert to MIDI", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_3.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton_3.setText("")
        self.record_parameters_header_2.setText(QCoreApplication.translate("MainWindow", u"MIDI", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Start Recording...", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton.setText("")
    # retranslateUi

