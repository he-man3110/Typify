# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Typify.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 250))
        MainWindow.setMaximumSize(QtCore.QSize(500, 250))
        MainWindow.setFocusPolicy(QtCore.Qt.WheelFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("myicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.8)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0.489, y1:1, x2:0.483, y2:0, stop:0.0454545 rgba(0, 0, 0, 182), stop:0.443182 rgba(0, 0, 0, 212), stop:0.9375 rgba(0, 0, 0, 255));")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("\n"
"QPushButton#pushButton_record \n"
"{  \n"
"    color: black;  \n"
"    background-color: #bebebe;  \n"
"    border-width: 0px;  \n"
"    border-radius: 15px; \n"
"}\n"
"QPushButton#pushButton_record:hover {background-color: #06e306;}\n"
" \n"
"\n"
"QPushButton#pushButton_stop \n"
"{  \n"
"    color: black;  \n"
"    background-color: #bebebe;  \n"
"    border-width: 0px;  \n"
"    border-radius: 15px; \n"
"}\n"
"QPushButton#pushButton_stop:hover {background-color: #ff0f0f;}\n"
"\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.label_typify = QtWidgets.QLabel(self.centralwidget)
        self.label_typify.setGeometry(QtCore.QRect(170, 12, 151, 41))
        self.label_typify.setStyleSheet(" background-color: qlineargradient(spread:pad, x1:0.512, y1:1, x2:0.483, y2:0, stop:0.204545 rgba(109, 109, 109, 0), stop:0.960227 rgba(0, 0, 0, 0));")
        self.label_typify.setObjectName("label_typify")
        self.label_inform = QtWidgets.QLabel(self.centralwidget)
        self.label_inform.setGeometry(QtCore.QRect(20, 230, 461, 31))
        self.label_inform.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.512, y1:1, x2:0.483, y2:0, stop:0.204545 rgba(14, 14, 14, 0), stop:0.960227 rgba(221, 221, 221, 32));\n"
"border-radius : 15px;\n"
" ")
        self.label_inform.setObjectName("label_inform")
        self.pushButton_record = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_record.setGeometry(QtCore.QRect(50, 90, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_record.setFont(font)
        self.pushButton_record.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_record.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_record.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_record.setObjectName("pushButton_record")
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(50, 150, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.label_display = QtWidgets.QLabel(self.centralwidget)
        self.label_display.setGeometry(QtCore.QRect(280, 80, 100, 100))
        self.label_display.setMinimumSize(QtCore.QSize(100, 100))
        self.label_display.setMaximumSize(QtCore.QSize(100, 100))
        self.label_display.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_display.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_display.setText("")
        self.label_display.setPixmap(QtGui.QPixmap("Resources/auwave_black.png"))
        self.label_display.setObjectName("label_display")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Typify™"))
        self.label_typify.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#ffffff;\">TYP</span><span style=\" font-size:26pt; font-weight:600; color:#11f80d;\">IFY</span><span style=\" font-size:26pt; font-weight:600; color:#ffffff; vertical-align:super;\">™</span></p></body></html>"))
        self.label_inform.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#d0d0d0;\">Use ctrl + arrow down to convert in short Bursts.</span></p><p><span style=\" font-size:10pt; color:#d0d0d0;\"><br/></span></p></body></html>"))
        self.pushButton_record.setText(_translate("MainWindow", "ENABLE"))
        self.pushButton_stop.setText(_translate("MainWindow", "STOP"))
