# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MapUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# Я устал
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1014, 555)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.typesmap = QtWidgets.QComboBox(self.centralwidget)
        self.typesmap.setGeometry(QtCore.QRect(740, 30, 241, 31))
        self.typesmap.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.typesmap.setObjectName("typesmap")
        self.map = QtWidgets.QLabel(self.centralwidget)
        self.map.setGeometry(QtCore.QRect(70, 80, 650, 450))
        self.map.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.map.setObjectName("map")
        self.searchline = QtWidgets.QLineEdit(self.centralwidget)
        self.searchline.setGeometry(QtCore.QRect(70, 30, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchline.setFont(font)
        self.searchline.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.searchline.setObjectName("searchline")
        self.searchbutton = QtWidgets.QPushButton(self.centralwidget)
        self.searchbutton.setGeometry(QtCore.QRect(550, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchbutton.setFont(font)
        self.searchbutton.setObjectName("searchbutton")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(640, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.postcode = QtWidgets.QRadioButton(self.centralwidget)
        self.postcode.setGeometry(QtCore.QRect(790, 120, 101, 17))
        self.postcode.setObjectName("postcode")
        self.info = QtWidgets.QTextBrowser(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(740, 150, 256, 301))
        self.info.setObjectName("info")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1014, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.map.setText(_translate("MainWindow", "КАРТИНКА"))
        self.searchbutton.setText(_translate("MainWindow", "Поиск"))
        self.clear.setText(_translate("MainWindow", "Сброс"))
        self.postcode.setText(_translate("MainWindow", "Почтовый код"))
