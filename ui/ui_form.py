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
        MainWindow.resize(800, 600)
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
        self.settings.setGeometry(QRect(40, 110, 341, 331))
        self.settings.setStyleSheet(u"background-color: #12131e;\n"
"border-radius: 5px")
        self.save_voice_label = QLabel(self.settings)
        self.save_voice_label.setObjectName(u"save_voice_label")
        self.save_voice_label.setGeometry(QRect(30, 130, 181, 41))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(15)
        self.save_voice_label.setFont(font1)
        self.save_voice_label.setStyleSheet(u"border-radius:5px;\n"
"background-color: #45259b")
        self.save_voice_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.save_voice_label.setMargin(10)
        self.midi_header = QLabel(self.settings)
        self.midi_header.setObjectName(u"midi_header")
        self.midi_header.setGeometry(QRect(30, 210, 141, 21))
        font2 = QFont()
        font2.setFamilies([u"Ubuntu"])
        font2.setPointSize(16)
        self.midi_header.setFont(font2)
        self.save_MIDI_label = QLabel(self.settings)
        self.save_MIDI_label.setObjectName(u"save_MIDI_label")
        self.save_MIDI_label.setGeometry(QRect(30, 240, 181, 41))
        self.save_MIDI_label.setFont(font1)
        self.save_MIDI_label.setStyleSheet(u"border-radius:5px;\n"
"background-color: #45259b")
        self.save_MIDI_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.save_MIDI_label.setMargin(10)
        self.duration_label = QLabel(self.settings)
        self.duration_label.setObjectName(u"duration_label")
        self.duration_label.setGeometry(QRect(30, 70, 181, 41))
        self.duration_label.setFont(font1)
        self.duration_label.setStyleSheet(u"border-radius:5px;\n"
"background-color: #45259b")
        self.duration_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.duration_label.setMargin(10)
        self.record_parameters_header = QLabel(self.settings)
        self.record_parameters_header.setObjectName(u"record_parameters_header")
        self.record_parameters_header.setGeometry(QRect(30, 40, 141, 21))
        self.record_parameters_header.setFont(font2)
        self.duration_field = QLineEdit(self.settings)
        self.duration_field.setObjectName(u"duration_field")
        self.duration_field.setGeometry(QRect(200, 70, 101, 41))
        self.duration_field.setStyleSheet(u"border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.duration_field.setMaxLength(7200)
        self.save_voice_label_2 = QLineEdit(self.settings)
        self.save_voice_label_2.setObjectName(u"save_voice_label_2")
        self.save_voice_label_2.setGeometry(QRect(200, 130, 101, 41))
        self.save_voice_label_2.setStyleSheet(u"border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.save_midi_label = QLineEdit(self.settings)
        self.save_midi_label.setObjectName(u"save_midi_label")
        self.save_midi_label.setGeometry(QRect(200, 240, 101, 41))
        self.save_midi_label.setStyleSheet(u"border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(530, 380, 101, 101))
        self.pushButton.setStyleSheet(u"border-radius: 50px;\n"
"background-color: #45259b;")
        icon = QIcon()
        icon.addFile(u"icons/mic.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u"icons/stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(60, 60))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(430, 170, 301, 181))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
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
        self.midi_header.setText(QCoreApplication.translate("MainWindow", u"MIDI File: ", None))
        self.save_MIDI_label.setText(QCoreApplication.translate("MainWindow", u"Save MIDI As:", None))
        self.duration_label.setText(QCoreApplication.translate("MainWindow", u"Duration (in seconds):", None))
        self.record_parameters_header.setText(QCoreApplication.translate("MainWindow", u"Record Parameters: ", None))
        self.duration_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"60", None))
        self.save_voice_label_2.setText("")
        self.save_voice_label_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"voice.wav", None))
        self.save_midi_label.setText("")
        self.save_midi_label.setPlaceholderText(QCoreApplication.translate("MainWindow", u"output.midi", None))
#if QT_CONFIG(statustip)
        self.pushButton.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton.setText("")
    # retranslateUi

