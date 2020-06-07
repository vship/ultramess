# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindows(object):
    def setupUi(self, MainWindows):
        MainWindows.setObjectName("MainWindows")
        MainWindows.resize(451, 650)
        MainWindows.setMinimumSize(QtCore.QSize(450, 650))
        self.pushButton = QtWidgets.QPushButton(MainWindows)
        self.pushButton.setGeometry(QtCore.QRect(330, 540, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(MainWindows)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(MainWindows)
        self.textBrowser.setGeometry(QtCore.QRect(20, 80, 411, 341))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit_2 = QtWidgets.QLineEdit(MainWindows)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 40, 171, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(MainWindows)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 40, 171, 31))
        self.lineEdit_3.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textEdit = QtWidgets.QTextEdit(MainWindows)
        self.textEdit.setGeometry(QtCore.QRect(20, 430, 411, 101))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(MainWindows)
        QtCore.QMetaObject.connectSlotsByName(MainWindows)

    def retranslateUi(self, MainWindows):
        _translate = QtCore.QCoreApplication.translate
        MainWindows.setWindowTitle(_translate("MainWindows", "UltraMess"))
        self.pushButton.setText(_translate("MainWindows", "Send"))
        self.label.setText(_translate("MainWindows", "UltraMess"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindows", "Введите username"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindows", "Введите password"))
        self.textEdit.setPlaceholderText(_translate("MainWindows", "Введите сообщение..."))
