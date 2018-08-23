# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Sun Feb 14 22:10:53 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(433, 334)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(240, 240, 240);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.logo = QtGui.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(90, 20, 261, 51))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/res/images/logo.png")))
        self.logo.setObjectName(_fromUtf8("logo"))
        self.username = QtGui.QTextEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(170, 200, 161, 31))
        self.username.setStyleSheet(_fromUtf8("border: 1px solid #9F9F9F;\n"
                                              "border-radius: 4px;\n"
                                              "background: #FFFFFF;\n"
                                              "color: #3D3D3D;"))
        self.username.setObjectName(_fromUtf8("username"))
        self.apoyo = QtGui.QLabel(self.centralwidget)
        self.apoyo.setGeometry(QtCore.QRect(0, 80, 441, 111))
        self.apoyo.setText(_fromUtf8(""))
        self.apoyo.setPixmap(QtGui.QPixmap(_fromUtf8(":/res/images/grafica_login.png")))
        self.apoyo.setScaledContents(True)
        self.apoyo.setObjectName(_fromUtf8("apoyo"))
        self.password = QtGui.QTextEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(170, 240, 161, 31))
        self.password.setStyleSheet(_fromUtf8("border: 1px solid #9F9F9F;\n"
                                              "border-radius: 4px;\n"
                                              "background: #FFFFFF;\n"
                                              "color: #3D3D3D;"))
        self.password.setObjectName(_fromUtf8("password"))
        self.enter = QtGui.QPushButton(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(170, 280, 81, 31))
        self.enter.setStyleSheet(_fromUtf8("font-weight: normal;\n"
                                           "font-size: 1em;\n"
                                           "color: #ffffff;\n"
                                           "padding: .4em 1em;\n"
                                           "border-radius: 4px;\n"
                                           "border: 1px solid #0069aa;\n"
                                           "line-height: normal;\n"
                                           "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #4094d0, stop:1 #073a93);"))
        self.enter.setObjectName(_fromUtf8("enter"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 204, 65, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 243, 65, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Gskin", None))
        self.enter.setText(_translate("MainWindow", "Enter", None))
        self.label.setText(_translate("MainWindow", "Username", None))
        self.label_2.setText(_translate("MainWindow", "Password", None))


import resources_rc
