# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\name.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_D2(object):
    def nameChange(self) :
        self.label_2.setText("")

    def setName(self,d,w, teams) :
        text = self.lineEdit.text()
        if text not in teams and text!="":
            self.lineEdit.setText("")
            w.setText(text)
            d.hide()
        else :
            self.label_2.setText('<html><head/><body><p><span style=" color:#ff0000;">name exists !!!</span></p></body></html>')

    def close(self, d) :
        d.hide()

    def setupUi(self, D2, teamName, teams):
        D2.setObjectName("D2")
        D2.resize(362, 94)
        self.label = QtWidgets.QLabel(D2)
        self.label.setGeometry(QtCore.QRect(30, 20, 81, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(D2)
        self.lineEdit.setGeometry(QtCore.QRect(150, 20, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(D2)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(210, 0, 81, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(D2)
        self.pushButton.setGeometry(QtCore.QRect(164, 50, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(D2)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 50, 81, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton.clicked.connect(lambda : self.setName(D2,teamName,teams))
        self.pushButton_2.clicked.connect(lambda : self.close(D2))
        self.lineEdit.textChanged.connect(self.nameChange)

        self.retranslateUi(D2)
        QtCore.QMetaObject.connectSlotsByName(D2)

    def retranslateUi(self, D2):
        _translate = QtCore.QCoreApplication.translate
        D2.setWindowTitle(_translate("D2", "Team Name"))
        self.label.setText(_translate("D2", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Enter Name</span></p></body></html>"))
        self.label_2.setText(_translate("D2", "<html><head/><body><p><span style=\" color:#ff0000;\"></span></p></body></html>"))
        self.pushButton.setText(_translate("D2", "OK"))
        self.pushButton_2.setText(_translate("D2", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    D2 = QtWidgets.QDialog()
    ui = Ui_D2()
    ui.setupUi(D2)
    D2.show()
    sys.exit(app.exec_())