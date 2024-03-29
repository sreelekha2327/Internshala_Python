# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from name import Ui_D2
from open import Ui_D3
from scores import Ui_MW2
from error import Ui_D1
import sqlite3
import re

Players = {}
notSelectedPlayers = {}
teams = []
match = ["Match_1"]
class Ui_MW1(object):

    def error(self, text) :
        self.window = QtWidgets.QDialog()
        self.ui=Ui_D1()
        self.ui.setupUi(self.window, text)
        self.window.show()

    def Slice(self,text) :
        out = re.search(">[0-9]+<", text)
        a=out.start()+1
        b=out.end()-1
        return text[a:b]

    def colorText(self, text) :
        return "<html><head/><body><p><span style='font-size:11pt; color:#00aaff;'>"+text+"</span></p></body></html>"

    def removeListA(self, item) :
        if int(self.Slice(self.pAvailable.text()))-Players[item.text()]["value"] >= 0 :
            if int(self.Slice(self.wk.text()))==1 and Players[item.text()]["ctg"]=="WK":
                self.error("Only one WK allowed in team")
            else :
                self.listA.takeItem(self.listA.row(item))
                self.listB.addItem(item.text())
                del notSelectedPlayers[item.text()]
                self.pAvailable.setText(self.colorText(str(int(self.Slice(self.pAvailable.text())) - Players[item.text()]["value"])))
                self.pUsed.setText(self.colorText(str(int(self.Slice(self.pUsed.text())) + Players[item.text()]["value"])))
                if Players[item.text()]["ctg"]=="BAT" :
                    self.bat.setText(self.colorText(str(int(self.Slice(self.bat.text()))+1)))
                elif Players[item.text()]["ctg"]=="BWL" :
                    self.bow.setText(self.colorText(str(int(self.Slice(self.bow.text()))+1)))
                elif Players[item.text()]["ctg"]=="AR" :
                    self.ar.setText(self.colorText(str(int(self.Slice(self.ar.text()))+1)))
                elif Players[item.text()]["ctg"]=="WK" :
                    self.wk.setText(self.colorText(str(int(self.Slice(self.wk.text()))+1)))
        else :
            self.error("Points not available for usage")

    def removeListB(self, item) :
        self.listB.takeItem(self.listB.row(item))
        notSelectedPlayers[item.text()]=Players[item.text()]["ctg"]
        
        self.pAvailable.setText(self.colorText(str(int(self.Slice(self.pAvailable.text())) + Players[item.text()]["value"])))
        self.pUsed.setText(self.colorText(str(int(self.Slice(self.pUsed.text())) - Players[item.text()]["value"])))
        
        if (self.rbBat.isChecked() == True) and ("BAT"==Players[item.text()]["ctg"]):
            self.listA.addItem(item.text())
        elif self.rbBowl.isChecked() == True and ("BWL"==Players[item.text()]["ctg"]):
            self.listA.addItem(item.text())
        elif self.rbAr.isChecked() == True and ("AR"==Players[item.text()]["ctg"]):
            self.listA.addItem(item.text())
        elif self.rbWk.isChecked() == True and ("WK"==Players[item.text()]["ctg"]):
            self.listA.addItem(item.text())

        if Players[item.text()]["ctg"]=="BAT" :
            self.bat.setText(self.colorText(str(int(self.Slice(self.bat.text()))-1)))
        elif Players[item.text()]["ctg"]=="BWL" :
            self.bow.setText(self.colorText(str(int(self.Slice(self.bow.text()))-1)))
        elif Players[item.text()]["ctg"]=="AR" :
            self.ar.setText(self.colorText(str(int(self.Slice(self.ar.text()))-1)))
        elif Players[item.text()]["ctg"]=="WK" :
            self.wk.setText(self.colorText(str(int(self.Slice(self.wk.text()))-1)))

    def openName(self) :
        teams.clear()
        Player = sqlite3.connect("cricket.db")
        myCursor = Player.cursor()
        sql_1 = "SELECT DISTINCT teamName FROM tblTeams;"
        myCursor.execute(sql_1)
        result = myCursor.fetchall()
        for record in result:
            teams.append(record[0])
        Player.close()
        self.window = QtWidgets.QDialog()
        self.ui=Ui_D2()
        self.ui.setupUi(self.window, self.teamName, teams)
        self.window.show()

    def openTeam(self) :
        teams.clear()
        Player = sqlite3.connect("cricket.db")
        myCursor = Player.cursor()
        sql_1 = "SELECT DISTINCT teamName FROM tblTeams;"
        myCursor.execute(sql_1)
        result = myCursor.fetchall()
        for record in result:
            teams.append(record[0])
        Player.close()
        self.window = QtWidgets.QDialog()
        self.ui=Ui_D3()
        self.ui.setupUi(self.window, self.teamName, teams)
        self.window.show()

    def teamCount(self) :
        bat = int(self.Slice(self.bat.text()))
        bowl = int(self.Slice(self.bow.text()))
        ar = int(self.Slice(self.ar.text()))
        wk = int(self.Slice(self.wk.text()))
        total = bat+bowl+ar+wk
        totalBowl = bowl+ar
        if total == 11 and totalBowl >=5 and wk == 1:
            return True
        else :
            return False


    def saveTeam(self) :
        if self.teamCount() :
            Player = sqlite3.connect("cricket.db")
            myCursor = Player.cursor()
            sq = "DELETE FROM tblTeams WHERE teamName='{}';".format(self.teamName.text())
            myCursor.execute(sq)
            for item in Players.keys() :
                if item not in notSelectedPlayers.keys() :
                    sql_1 = "SELECT ID FROM tblPlayers WHERE playerName='{}';".format(item)
                    myCursor.execute(sql_1)
                    result = myCursor.fetchone()
                    sql = "INSERT INTO tblTeams (teamName, playerID, value) VALUES (?,?,?);"
                    myCursor.execute(sql, (self.teamName.text(), result[0], Players[item]["value"]))
            Player.commit()
            Player.close()
        else :
            self.error("Team Incomplete (Team rules violated) !!!")

    def evaluateTeam(self) :
        teams.clear()
        Player = sqlite3.connect("cricket.db")
        myCursor = Player.cursor()
        sql_1 = "SELECT DISTINCT teamName FROM tblTeams;"
        myCursor.execute(sql_1)
        result = myCursor.fetchall()
        for record in result:
            teams.append(record[0])
        Player.close()
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_MW2()
        self.ui.setupUi(self.window, teams, match)
        self.window.show()

    def teamNameChanged(self) :
        if self.teamName.text() != "Displayed Here" :
            self.bat.setText(self.colorText("0"))
            self.bow.setText(self.colorText("0"))
            self.ar.setText(self.colorText("0"))
            self.wk.setText(self.colorText("0"))
            self.pAvailable.setText(self.colorText("1000"))
            self.pUsed.setText(self.colorText("0"))  
            self.rbBat.setEnabled(True)
            self.rbBowl.setEnabled(True)
            self.rbAr.setEnabled(True)
            self.rbWk.setEnabled(True)
            self.listB.clear()
            self.listPlayers()
          
    def listPlayers(self) :
        Player = sqlite3.connect("cricket.db")
        myCursor = Player.cursor()
        sql_1 = "SELECT playerName, value, ctg FROM tblPlayers JOIN tblStats ON tblPlayers.ID = tblStats.playerID;"
        myCursor.execute(sql_1)
        result = myCursor.fetchall()
        for record in result:
            Players[record[0]]={"value":record[1], "ctg":record[2]}
            notSelectedPlayers[record[0]]=record[2]
        teamName = self.teamName.text()
        if teamName not in teams :
            Player.close()
        else :
            self.listB.clear()
            sql_2 = "SELECT playerName FROM tblPlayers JOIN tblTeams ON tblPlayers.ID=tblTeams.playerID WHERE teamName='"+teamName+"';"
            myCursor.execute(sql_2)
            result = myCursor.fetchall()
            for record in result:
                self.listB.addItem(record[0])
                self.pAvailable.setText(self.colorText(str(int(self.Slice(self.pAvailable.text())) - Players[record[0]]["value"])))
                self.pUsed.setText(self.colorText(str(int(self.Slice(self.pUsed.text())) + Players[record[0]]["value"])))
                if notSelectedPlayers[record[0]] == "BAT" :
                        self.bat.setText(self.colorText(str(int(self.Slice(self.bat.text()))+1)))
                elif notSelectedPlayers[record[0]]=="BWL" :
                    self.bow.setText(self.colorText(str(int(self.Slice(self.bow.text()))+1)))
                elif notSelectedPlayers[record[0]]=="AR" :
                    self.ar.setText(self.colorText(str(int(self.Slice(self.ar.text()))+1)))
                elif notSelectedPlayers[record[0]]=="WK" :
                    self.wk.setText(self.colorText(str(int(self.Slice(self.wk.text()))+1)))
                del notSelectedPlayers[record[0]]
            Player.close()

    def batPlayers(self):
        self.listA.clear()
        for name, ctg in notSelectedPlayers.items() :
            if ctg == "BAT" :
                self.listA.addItem(name)
 
    def bowlPlayers(self):
        self.listA.clear()
        for name, ctg in notSelectedPlayers.items() :
            if ctg == "BWL" :
                self.listA.addItem(name)     
    
    def arPlayers(self):
        self.listA.clear()
        for name, ctg in notSelectedPlayers.items() :
            if ctg == "AR" :
                self.listA.addItem(name) 

    def wkPlayers(self):
        self.listA.clear()
        for name, ctg in notSelectedPlayers.items() :
            if ctg == "WK" :
                self.listA.addItem(name) 
    

    def setupUi(self, MW1):
        MW1.setObjectName("MW1")
        MW1.resize(709, 550)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MW1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MW1.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MW1)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 40, 651, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 0, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(160, 40, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(310, 40, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(470, 40, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.bat = QtWidgets.QLabel(self.centralwidget)
        self.bat.setGeometry(QtCore.QRect(140, 80, 31, 16))
        self.bat.setObjectName("bat")
        self.bow = QtWidgets.QLabel(self.centralwidget)
        self.bow.setGeometry(QtCore.QRect(290, 80, 31, 16))
        self.bow.setObjectName("bow")
        self.ar = QtWidgets.QLabel(self.centralwidget)
        self.ar.setGeometry(QtCore.QRect(450, 80, 31, 16))
        self.ar.setObjectName("ar")
        self.wk = QtWidgets.QLabel(self.centralwidget)
        self.wk.setGeometry(QtCore.QRect(640, 80, 31, 16))
        self.wk.setObjectName("wk")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(50, 170, 271, 301))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.rbBat = QtWidgets.QRadioButton(self.frame_2)
        self.rbBat.setEnabled(False)
        self.rbBat.setGeometry(QtCore.QRect(20, 10, 51, 17))
        self.rbBat.setObjectName("rbBat")
        self.rbBowl = QtWidgets.QRadioButton(self.frame_2)
        self.rbBowl.setEnabled(False)
        self.rbBowl.setGeometry(QtCore.QRect(80, 10, 61, 17))
        self.rbBowl.setObjectName("rbBowl")
        self.rbAr = QtWidgets.QRadioButton(self.frame_2)
        self.rbAr.setEnabled(False)
        self.rbAr.setGeometry(QtCore.QRect(150, 10, 51, 17))
        self.rbAr.setObjectName("rbAr")
        self.rbWk = QtWidgets.QRadioButton(self.frame_2)
        self.rbWk.setEnabled(False)
        self.rbWk.setGeometry(QtCore.QRect(210, 10, 51, 17))
        self.rbWk.setObjectName("rbWk")
        self.listA = QtWidgets.QListWidget(self.frame_2)
        self.listA.setGeometry(QtCore.QRect(5, 30, 261, 261))
        self.listA.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listA.setObjectName("listA")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(390, 169, 271, 301))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.listB = QtWidgets.QListWidget(self.frame_3)
        self.listB.setGeometry(QtCore.QRect(5, 30, 261, 261))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.listB.setPalette(palette)
        self.listB.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listB.setObjectName("listB")
        self.teamName = QtWidgets.QLineEdit(self.frame_3)
        self.teamName.setGeometry(QtCore.QRect(110, 10, 113, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.teamName.setPalette(palette)
        self.teamName.setReadOnly(True)
        self.teamName.setObjectName("teamName")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(330, 310, 47, 13))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(50, 140, 111, 16))
        self.label_11.setObjectName("label_11")
        self.pAvailable = QtWidgets.QLabel(self.centralwidget)
        self.pAvailable.setGeometry(QtCore.QRect(170, 140, 51, 16))
        self.pAvailable.setObjectName("pAvailable")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(390, 140, 81, 16))
        self.label_13.setObjectName("label_13")
        self.pUsed = QtWidgets.QLabel(self.centralwidget)
        self.pUsed.setGeometry(QtCore.QRect(480, 140, 51, 16))
        self.pUsed.setObjectName("pUsed")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(410, 180, 81, 16))
        self.label_15.setObjectName("label_15")
        MW1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MW1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 22))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MW1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MW1)
        self.statusbar.setObjectName("statusbar")
        MW1.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MW1)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MW1)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MW1)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team_2 = QtWidgets.QAction(MW1)
        self.actionSAVE_Team_2.setObjectName("actionSAVE_Team_2")
        self.actionEvaluate_Team = QtWidgets.QAction(MW1)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team_2)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.actionNEW_Team.triggered.connect(self.openName)
        self.actionSAVE_Team_2.triggered.connect(self.saveTeam)
        self.actionOPEN_Team.triggered.connect(self.openTeam)
        self.actionEvaluate_Team.triggered.connect(self.evaluateTeam)
        self.teamName.textChanged.connect(self.teamNameChanged)

        self.rbBat.toggled.connect(lambda: self.batPlayers())
        self.rbBowl.toggled.connect(lambda: self.bowlPlayers())
        self.rbAr.toggled.connect(lambda: self.arPlayers())
        self.rbWk.toggled.connect(lambda: self.wkPlayers())

        self.listA.itemDoubleClicked.connect(self.removeListA)
        self.listB.itemDoubleClicked.connect(self.removeListB)
        self.listA.setSortingEnabled(True)
        self.listB.setSortingEnabled(True)

        self.retranslateUi(MW1)
        QtCore.QMetaObject.connectSlotsByName(MW1)

    def retranslateUi(self, MW1):
        _translate = QtCore.QCoreApplication.translate
        MW1.setWindowTitle(_translate("MW1", "Fantasy Cricket"))
        self.label.setText(_translate("MW1", "Your Selections"))
        self.label_2.setText(_translate("MW1", "Batsmen (BAT)"))
        self.label_3.setText(_translate("MW1", "Bowlers (BOW)"))
        self.label_4.setText(_translate("MW1", "Allrounders (AR)"))
        self.label_5.setText(_translate("MW1", "Wicket-Keeper (WK)"))
        self.bat.setText(_translate("MW1", "<html><head/><body><p><span style=\" font-size:11pt; color:#00aaff;\"># #</span></p></body></html>"))
        self.bow.setText(_translate("MW1", "<html><head/><body><p><span style=\" font-size:11pt; color:#00aaff;\"># #</span></p></body></html>"))
        self.ar.setText(_translate("MW1", "<html><head/><body><p><span style=\" font-size:11pt; color:#00aaff;\"># #</span></p></body></html>"))
        self.wk.setText(_translate("MW1", "<html><head/><body><p><span style=\" font-size:11pt; color:#00aaff;\"># #</span></p></body></html>"))
        self.rbBat.setText(_translate("MW1", "BAT"))
        self.rbBowl.setText(_translate("MW1", "BOW"))
        self.rbAr.setText(_translate("MW1", "AR"))
        self.rbWk.setText(_translate("MW1", "WK"))
        self.teamName.setText(_translate("MW1", "Displayed Here"))
        self.label_10.setText(_translate("MW1", "<html><head/><body><p><span style=\" font-size:12pt;\">&gt;&gt;</span></p></body></html>"))
        self.label_11.setText(_translate("MW1", "Points Available"))
        self.pAvailable.setText(_translate("MW1", "<html><head/><body><p><span style=\" font-size:11pt; color:#00aaff;\"># # # #</span></p></body></html>"))
        self.label_13.setText(_translate("MW1", "Points Used"))
        self.pUsed.setText(_translate("MW1", "<html><head/><body><p><span style=\" font-size:11pt; color:#00aaff;\"># # # #</span></p></body></html>"))
        self.label_15.setText(_translate("MW1", "<html><head/><body><p><span style=\" font-style:normal;\">Team Name</span></p></body></html>"))
        self.menuManage_Teams.setTitle(_translate("MW1", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MW1", "NEW Team"))
        self.actionSAVE_Team.setText(_translate("MW1", "SAVE Team"))
        self.actionOPEN_Team.setText(_translate("MW1", "OPEN Team"))
        self.actionSAVE_Team_2.setText(_translate("MW1", "SAVE Team"))
        self.actionEvaluate_Team.setText(_translate("MW1", "Evaluate Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MW1 = QtWidgets.QMainWindow()
    ui = Ui_MW1()
    ui.setupUi(MW1)
    MW1.show()
    sys.exit(app.exec_())
