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
import QtQuick.Studio.Components 1.0

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
        anchors.verticalCenterOffset: -346
        anchors.horizontalCenterOffset: 1
        font.styleName: "Medium"
        anchors.centerIn: parent
    }

    Frame {
        id: recordFrame
        x: 110
        y: 214
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
            x: -12
            y: -20
            width: 1068
            height: 200
            color: "#080817"
        }
    }

    Rectangle {
        id: recordDurationLabel
        x: 110
        y: 426
        width: 263
        height: 87
        color: "#7c1ec3"
        radius: 17

        Rectangle {
            id: rectangle3
            x: 235
            y: 0
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
                font.pixelSize: 26
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


    Rectangle {
        id: savefilenameLabel
        x: 707
        y: 426
        width: 184
        height: 87
        color: "#7c1ec3"
        radius: 17
        Text {
            id: text2
            x: 16
            y: 8
            width: 137
            height: 71
            color: "#fcdeff"
            text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:28pt; font-weight:700;\">Save As</span></p>\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:28pt;\">(filename):</span></p>\n<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"
            font.pixelSize: 35
            textFormat: Text.RichText
        }


        Rectangle {
            id: rectangle4
            x: 153
            y: 0
            width: 310
            height: 87
            color: "#00ffffff"
            radius: 16
            border.color: "#7c1ec3"
            border.width: 5
        }


        TextInput {
            id: textInput1
            x: 195
            y: 0
            width: 268
            height: 87
            color: "#d2d2ff"
            font.pixelSize: 26
            verticalAlignment: Text.AlignVCenter
            topPadding: 4
            selectionColor: "#6666a0"
            selectedTextColor: "#1e1e36"
            rightPadding: 4
            padding: 4
            leftPadding: 4
            cursorVisible: true
            bottomPadding: 4
        }
    }

    RoundButton {
        id: roundButton
        x: 585
        y: 425
        width: 86
        height: 90
        text: "+"
        icon.source: "images/mic.png"
        icon.height: 69
        icon.width: 69
        display: AbstractButton.IconOnly
        palette {
            button: "#642bab"
            buttonText: "white"
        }

        DesignEffect {
            layerBlurRadius: 0
        }
    }

    Frame {
        id: recordFrame1
        x: 110
        y: 615
        width: 1062
        height: 185
        data: [
            DesignEffect {
                effects: [
                    DesignDropShadow {
                    }]
            }]
        Rectangle {
            id: rectangle2
            x: -12
            y: -21
            width: 1068
            height: 200
            color: "#080817"
        }
    }

    Text {
        id: text3
        x: 110
        y: 566
        color: "#4a4a7f"
        text: qsTr("MIDI Output")
        font.pixelSize: 25
        font.family: "Verdana"
    }

    Rectangle {
        id: savefilenameLabel1
        x: 403
        y: 827
        width: 184
        height: 87
        color: "#7c1ec3"
        radius: 17
        Text {
            id: text4
            x: 16
            y: 8
            width: 137
            height: 71
            color: "#fcdeff"
            text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:28pt; font-weight:700;\">Save As</span></p>\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:28pt;\">(filename):</span></p>\n<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"
            font.pixelSize: 35
            textFormat: Text.RichText
        }

        Rectangle {
            id: rectangle5
            x: 153
            y: 0
            width: 310
            height: 87
            color: "#00ffffff"
            radius: 16
            border.color: "#7c1ec3"
            border.width: 5
        }

        TextInput {
            id: textInput2
            x: 195
            y: 0
            width: 268
            height: 87
            color: "#d2d2ff"
            font.pixelSize: 26
            verticalAlignment: Text.AlignVCenter
            topPadding: 4
            selectionColor: "#6666a0"
            selectedTextColor: "#1e1e36"
            rightPadding: 4
            padding: 4
            leftPadding: 4
            cursorVisible: true
            bottomPadding: 4
        }
    }


}
