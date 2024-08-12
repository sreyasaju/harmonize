

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
import QtQuick.Timeline 1.0
import QtQuick.Layouts

Rectangle {
    id: rectangle
    width: 1280
    height: 832
    opacity: 1
    color: "#151524"
    radius: 0
    border.color: "#00000000"

    Text {
        id: harmonize
        width: 379
        height: 94
        color: "#ffffff"
        text: qsTr("harmonize")
        font.pixelSize: 69
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.family: "Tahoma"
        anchors.verticalCenterOffset: -301
        anchors.horizontalCenterOffset: 16
        font.styleName: "Medium"
        anchors.centerIn: parent
    }

    Rectangle {
        id: rectangle1
        x: 83
        y: 188
        width: 491
        height: 522
        color: "#0f0f1d"
        radius: 26
        border.color: "#00000000"
    }

    Rectangle {
        id: saveMIDIPathLabel
        x: 118
        y: 580
        width: 218
        height: 78
        color: "#7c1ec3"
        radius: 17
        Rectangle {
            id: rectangle5
            x: 181
            y: 0
            width: 195
            height: 78
            color: "#00ffffff"
            radius: 16
            border.color: "#7c1ec3"
            border.width: 5
            TextInput {
                id: textInput2
                x: 40
                y: 8
                width: 147
                height: 62
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

        Text {
            id: text5
            x: 14
            y: 8
            width: 188
            height: 62
            color: "#fcdeff"
            text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:24pt; font-weight:700;\">Save MIDI As:</span></p>\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:24pt; font-weight:700; font-style:italic; color:#bdafcc;\">e.g. &quot;output.midi&quot;</span></p></body></html>"
            font.pixelSize: 35
            textFormat: Text.RichText
        }
    }

    Rectangle {
        id: recordDurationLabel
        x: 118
        y: 286
        width: 209
        height: 78
        color: "#7c1ec3"
        radius: 17

        Rectangle {
            id: rectangle3
            x: 181
            y: 0
            width: 194
            height: 78
            color: "#00ffffff"
            radius: 16
            border.color: "#7c1ec3"
            border.width: 5

            TextInput {
                id: textInput
                x: 32
                y: 8
                width: 154
                height: 62
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
            x: 12
            y: 8
            width: 186
            height: 62
            color: "#fcdeff"
            text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:24pt; font-weight:700;\">Record Duration</span></p>\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:24pt; font-weight:700;\">(in seconds):</span></p></body></html>"
            font.pixelSize: 35
            textFormat: Text.RichText
        }
    }

    Text {
        id: text3
        x: 118
        y: 223
        width: 235
        height: 36
        color: "#42426f"
        text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:24pt; font-weight:700; color:#513c8c;\">Record Parameters:</span></p></body></html>"
        font.pixelSize: 35
        textFormat: Text.RichText
    }

    Text {
        id: text4
        x: 121
        y: 525
        width: 235
        height: 36
        color: "#42426f"
        text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:24pt; font-weight:700; color:#513c8c;\">MIDI File:</span></p></body></html>"
        font.pixelSize: 35
        textFormat: Text.RichText
    }

    RoundButton {
        id: recordButton
        x: 885
        y: 519
        width: 85
        height: 85
        text: "+"
        icon.source: "images/mic.png"
        icon.height: 60
        icon.width: 60
        display: AbstractButton.IconOnly
        palette {
            button: "#642bab"
            buttonText: "white"
        }

        DesignEffect {
            layerBlurRadius: 0
        }

        Connections {
            target: recordButton
            onPressed: rectangle.state = "stop"
        }

        Connections {
            target: recordButton
            onReleased: rectangle.state = ""
        }
    }

    Rectangle {
        id: saveWaveLabel
        x: 118
        y: 402
        width: 209
        height: 78
        color: "#7c1ec3"
        radius: 17
        Rectangle {
            id: rectangle4
            x: 181
            y: 0
            width: 195
            height: 78
            color: "#00ffffff"
            radius: 16
            border.color: "#7c1ec3"
            border.width: 5
            TextInput {
                id: textInput1
                x: 32
                y: 8
                width: 155
                height: 62
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

        Text {
            id: text2
            x: 14
            y: 8
            width: 188
            height: 62
            color: "#fcdeff"
            text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:24pt; font-weight:700;\">Save Voice As:</span></p>\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:24pt; font-weight:700; font-style:italic; color:#bdafcc;\">e.g. &quot;file.wav&quot;</span></p></body></html>"
            font.pixelSize: 35
            textFormat: Text.RichText
        }
    }

    GroupItem {
    }




    states: [
        State {
            name: "stop"

            PropertyChanges {
                target: recordButton
                text: "+"
                icon.source: "../stop.png"
            }
        }
    ]
}
