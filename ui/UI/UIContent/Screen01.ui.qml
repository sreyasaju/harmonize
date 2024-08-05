/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick 6.5
import QtQuick.Controls 6.5
import UI

Rectangle {
    width: Constants.width
    height: Constants.height
    color: "#151524"


    Text {
        width: 465
        height: 121
        color: "#ffffff"
        text: qsTr("harmonize")
        font.pixelSize: 100
        horizontalAlignment: Text.AlignRight
        verticalAlignment: Text.AlignVCenter
        font.family: "Tahoma"
        anchors.verticalCenterOffset: -340
        anchors.horizontalCenterOffset: 1
        font.styleName: "Medium"
        anchors.centerIn: parent
    }
}
