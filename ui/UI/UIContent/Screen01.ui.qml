/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick 6.5
import QtQuick.Controls 6.5
import UI
import QtQuick.Studio.DesignEffects

Rectangle {
    id: rectangle
    width: Constants.width
    height: Constants.height
    color: "#151524"


    Text {
        id: harmonize
        width: 465
        height: 121
        color: "#ffffff"
        text: qsTr("harmonize")
        font.pixelSize: 85
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.family: "Tahoma"
        anchors.verticalCenterOffset: -333
        anchors.horizontalCenterOffset: 9
        font.styleName: "Medium"
        anchors.centerIn: parent
    }

    Frame {
        id: recordFrame
        x: 109
        y: 222
        width: 1062
        height: 185
        data: [
            DesignEffect {
                effects: [
                    DesignDropShadow {
                    }
                ]
            }
        ]

        Rectangle {
            id: rectangle1
            x: -37
            y: -20
            width: 1108
            height: 200
            color: "#080817"
        }
    }

    RoundButton {
        id: recordButton
        x: 978
        y: 443
        width: 75
        height: 75
        text: "+"
    }

    Button {
        id: button1
        x: 593
        y: 443
        width: 342
        height: 73
        text: qsTr("Button")
    }

    Rectangle {
        id: rectangle3
        x: 344
        y: 443
        width: 202
        height: 87
        color: "#00ffffff"
        radius: 16
        border.color: "#7c1ec3"
        border.width: 5

        TextInput {
            id: textInput
            x: 32
            y: 1
            width: 170
            height: 86
            color: "#d2d2ff"
            font.pixelSize: 44
            verticalAlignment: Text.AlignVCenter
            padding: 4
            rightPadding: 4
            leftPadding: 4
            bottomPadding: 4
            topPadding: 4
            cursorVisible: true
            selectedTextColor: "#1e1e36"
            selectionColor: "#6666a0"
        }
    }

    Rectangle {
        id: rectangle2
        x: 109
        y: 443
        width: 263
        height: 87
        color: "#7c1ec3"
        radius: 17

        Text {
            id: text1
            x: 17
            y: 9
            width: 215
            height: 70
            color: "#fcdeff"
            text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:28pt; font-weight:700;\">Record Duration</span></p>\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:28pt; font-weight:700;\">(in seconds):</span></p></body></html>"
            font.pixelSize: 35
            textFormat: Text.RichText
        }
    }


}
