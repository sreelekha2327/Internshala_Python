# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\error.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_D1(object):
    def colorText(self, text) :
            return "<html><head/><body><p><span style=' font-size:9pt; font-weight:600; color:#ff5500;'>"+text+"</span></p></body></html>"
        
    def close(self, w):
        w.hide()

    def setupUi(self, D1, textError):
        
        D1.setObjectName("D1")
        D1.resize(421, 131)
        self.error = QtWidgets.QLabel(D1)
        self.error.setGeometry(QtCore.QRect(40, 10, 331, 21))
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setObjectName("error")
        self.textBrowser = QtWidgets.QTextBrowser(D1)
        self.textBrowser.setGeometry(QtCore.QRect(40, 40, 331, 61))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(D1)
        self.pushButton.setGeometry(QtCore.QRect(260, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")

        
        
        self.pushButton.clicked.connect(lambda : self.close(D1))

        self.retranslateUi(D1)
        self.error.setText(self.colorText(textError))
        QtCore.QMetaObject.connectSlotsByName(D1)

    def retranslateUi(self, D1):
        _translate = QtCore.QCoreApplication.translate
        D1.setWindowTitle(_translate("D1", "Error"))
        self.error.setText(_translate("D1", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ff5500;\">Error</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("D1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">Rules :</span><span style=\" font-style:italic;\"> </span><span style=\" font-style:italic; color:#ff0000;\">Total players - 11</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#ff0000;\">             Wicket Keeper - 1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#ff0000;\">             Bowlers+Allrounders - min 5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p></body></html>"))
        self.pushButton.setText(_translate("D1", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    D1 = QtWidgets.QDialog()
    ui = Ui_D1()
    ui.setupUi(D1)
    D1.show()
    sys.exit(app.exec_())