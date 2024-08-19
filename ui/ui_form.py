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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 130, 341, 331))
        self.widget.setStyleSheet(u"background-color: #12131e;\n"
"border-radius: 5px")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 130, 181, 41))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(15)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"border-radius:5px;\n"
"background-color: #45259b")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setMargin(10)
        self.textEdit_2 = QTextEdit(self.widget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(200, 130, 111, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setFont(font1)
        self.textEdit_2.viewport().setProperty("cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.textEdit_2.setStyleSheet(u"border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"")
        self.textEdit_2.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.textEdit_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 210, 141, 21))
        font2 = QFont()
        font2.setFamilies([u"Ubuntu"])
        font2.setPointSize(16)
        self.label_5.setFont(font2)
        self.textEdit_3 = QTextEdit(self.widget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(200, 240, 111, 41))
        sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy)
        self.textEdit_3.setFont(font1)
        self.textEdit_3.viewport().setProperty("cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.textEdit_3.setStyleSheet(u"border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"")
        self.textEdit_3.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.textEdit_3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.textEdit_3.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.textEdit_3.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 240, 181, 41))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"border-radius:5px;\n"
"background-color: #45259b")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setMargin(10)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 181, 41))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"border-radius:5px;\n"
"background-color: #45259b")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setMargin(10)
        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(200, 70, 111, 41))
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setFont(font1)
        self.textEdit.viewport().setProperty("cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.textEdit.setStyleSheet(u"border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"")
        self.textEdit.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 141, 21))
        self.label.setFont(font2)
        self.label_3.raise_()
        self.textEdit_2.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.textEdit_3.raise_()
        self.label_2.raise_()
        self.textEdit.raise_()
        self.label.raise_()
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(550, 340, 101, 101))
        self.pushButton.setStyleSheet(u"border-radius: 50px;\n"
"background-color: #45259b;")
        icon = QIcon()
        icon.addFile(u"icons/mic.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u"icons/stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(60, 60))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.textEdit_2)
        self.label_4.setBuddy(self.textEdit_3)
        self.label_2.setBuddy(self.textEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)
        self.pushButton.windowIconChanged.connect(self.pushButton.click)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>harmonize</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Save Voice As:", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"voice.wav", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"MIDI File: ", None))
        self.textEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"output.midi", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Save Voice As:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Duration (in seconds):", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"60", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Record Parameters: ", None))
        self.pushButton.setText("")
    # retranslateUi

