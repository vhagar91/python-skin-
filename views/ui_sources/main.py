# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/qcode/Projects/Qt/design/main.ui'
#
# Created: Mon Feb 22 15:51:39 2016
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
        MainWindow.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.inventoryTabView = QtGui.QTabWidget(self.centralwidget)
        self.inventoryTabView.setGeometry(QtCore.QRect(0, 50, 788, 551))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inventoryTabView.sizePolicy().hasHeightForWidth())
        self.inventoryTabView.setSizePolicy(sizePolicy)
        self.inventoryTabView.setStyleSheet(_fromUtf8("QTabWidget::pane { /* The tab widget frame */\n"
"    border: 1px solid #C2C7CB;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"}\n"
"QTabBar::tab {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E1E1E1, stop: 0.4 #DDDDDD, stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"border: 2px solid #C4C4C3;\n"
"border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"min-width: 8ex;\n"
"padding: 3px 4px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fafafa, stop: 0.4 #f4f4f4, stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"QTabBar::tab:selected {\n"
"border-color: #9B9B9B;\n"
"border-bottom-color: #0162B1; /* same as pane color */\n"
"}\n"
"QTabBar::tab:!selected {\n"
"margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}"))
        self.inventoryTabView.setObjectName(_fromUtf8("inventoryTabView"))
        self.hardwareTab = QtGui.QWidget()
        self.hardwareTab.setObjectName(_fromUtf8("hardwareTab"))
        self.inventoryTabView.addTab(self.hardwareTab, _fromUtf8(""))
        self.softwareTab = QtGui.QWidget()
        self.softwareTab.setObjectName(_fromUtf8("softwareTab"))
        self.inventoryTabView.addTab(self.softwareTab, _fromUtf8(""))
        self.configTab = QtGui.QWidget()
        self.configTab.setObjectName(_fromUtf8("configTab"))
        self.enter = QtGui.QPushButton(self.configTab)
        self.enter.setGeometry(QtCore.QRect(160, 200, 91, 31))
        self.enter.setStyleSheet(_fromUtf8("font-weight: normal;\n"
"font-size: 1em;\n"
"color: #ffffff;\n"
"padding: .4em 1em;\n"
"border-radius: 4px;\n"
"border: 1px solid #0069aa;\n"
"line-height: normal;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #4094d0, stop:1 #073a93);"))
        self.enter.setObjectName(_fromUtf8("enter"))
        self.server_host = QtGui.QTextEdit(self.configTab)
        self.server_host.setGeometry(QtCore.QRect(160, 80, 161, 31))
        self.server_host.setStyleSheet(_fromUtf8("border: 1px solid #9F9F9F;\n"
"border-radius: 4px;\n"
"background: #FFFFFF;\n"
"color: #3D3D3D;"))
        self.server_host.setObjectName(_fromUtf8("server_host"))
        self.label = QtGui.QLabel(self.configTab)
        self.label.setGeometry(QtCore.QRect(70, 44, 91, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.id_collector = QtGui.QTextEdit(self.configTab)
        self.id_collector.setGeometry(QtCore.QRect(160, 40, 161, 31))
        self.id_collector.setStyleSheet(_fromUtf8("border: 1px solid #9F9F9F;\n"
"border-radius: 4px;\n"
"background: #FFFFFF;\n"
"color: #3D3D3D;"))
        self.id_collector.setObjectName(_fromUtf8("id_collector"))
        self.label_2 = QtGui.QLabel(self.configTab)
        self.label_2.setGeometry(QtCore.QRect(70, 83, 91, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.configTab)
        self.label_3.setGeometry(QtCore.QRect(70, 123, 91, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.httpscheckBox = QtGui.QCheckBox(self.configTab)
        self.httpscheckBox.setGeometry(QtCore.QRect(160, 160, 21, 26))
        self.httpscheckBox.setText(_fromUtf8(""))
        self.httpscheckBox.setObjectName(_fromUtf8("httpscheckBox"))
        self.label_4 = QtGui.QLabel(self.configTab)
        self.label_4.setGeometry(QtCore.QRect(70, 160, 91, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.server_port = QtGui.QSpinBox(self.configTab)
        self.server_port.setGeometry(QtCore.QRect(160, 120, 91, 33))
        self.server_port.setMinimum(1)
        self.server_port.setMaximum(65536)
        self.server_port.setObjectName(_fromUtf8("server_port"))
        self.inventoryTabView.addTab(self.configTab, _fromUtf8(""))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 305, 53))
        self.frame.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255,255,255,81), stop:0.495 #ffffff, stop:1 #dedede);\n"
"border-bottom: 1px solid #0069aa;"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.logo = QtGui.QLabel(self.frame)
        self.logo.setGeometry(QtCore.QRect(0, 0, 331, 52))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/res/images/logo.png")))
        self.logo.setObjectName(_fromUtf8("logo"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(303, 0, 490, 53))
        self.frame_2.setStyleSheet(_fromUtf8("background-color: rgba(255,255,255,255);\n"
"border-bottom: 2px solid #0069aa;"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.grafica = QtGui.QLabel(self.frame_2)
        self.grafica.setGeometry(QtCore.QRect(0, 0, 251, 51))
        self.grafica.setText(_fromUtf8(""))
        self.grafica.setPixmap(QtGui.QPixmap(_fromUtf8(":/res/images/grafica.jpg")))
        self.grafica.setObjectName(_fromUtf8("grafica"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.inventoryTabView.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Gclient", None))
        self.inventoryTabView.setTabText(self.inventoryTabView.indexOf(self.hardwareTab), _translate("MainWindow", "Hardware", None))
        self.inventoryTabView.setTabText(self.inventoryTabView.indexOf(self.softwareTab), _translate("MainWindow", "Software", None))
        self.enter.setText(_translate("MainWindow", "Aceptar", None))
        self.label.setText(_translate("MainWindow", "Id collector", None))
        self.label_2.setText(_translate("MainWindow", "Server host", None))
        self.label_3.setText(_translate("MainWindow", "Server port", None))
        self.label_4.setText(_translate("MainWindow", "HTTPS", None))
        self.inventoryTabView.setTabText(self.inventoryTabView.indexOf(self.configTab), _translate("MainWindow", "Configuration", None))

import resources_rc
