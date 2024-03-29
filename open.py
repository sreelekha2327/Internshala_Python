# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\open.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_D3(object):

    def open(self, d, w, teams) :
        text = self.comboBox.currentText()
        if text != "Select Team" and (text in teams) :
            w.setText(text)
            d.hide()

    def close(self, d) :
        d.hide()

    def setupUi(self, D3, teamName, teams):
        D3.setObjectName("D3")
        D3.resize(400, 85)
        self.label = QtWidgets.QLabel(D3)
        self.label.setGeometry(QtCore.QRect(50, 20, 81, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(D3)
        self.comboBox.setGeometry(QtCore.QRect(160, 20, 161, 21))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(D3)
        self.pushButton.setGeometry(QtCore.QRect(180, 50, 61, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(D3)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 50, 61, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.comboBox.clear()
        for item in teams :
            self.comboBox.addItem(item)
        self.comboBox.setEditable(True)
        self.comboBox.setCurrentText("Select Team")
        self.pushButton.clicked.connect(lambda : self.open(D3,teamName,teams))
        self.pushButton_2.clicked.connect(lambda : self.close(D3))

        self.retranslateUi(D3)
        QtCore.QMetaObject.connectSlotsByName(D3)

    def retranslateUi(self, D3):
        _translate = QtCore.QCoreApplication.translate
        D3.setWindowTitle(_translate("D3", "Open Team"))
        self.label.setText(_translate("D3", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Select Team</span></p></body></html>"))
        self.pushButton.setText(_translate("D3", "OK"))
        self.pushButton_2.setText(_translate("D3", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    D3 = QtWidgets.QDialog()
    ui = Ui_D3()
    ui.setupUi(D3)
    D3.show()
    sys.exit(app.exec_())
