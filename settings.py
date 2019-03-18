# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(440, 173)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 130, 411, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 421, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.playerTwoName_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.playerTwoName_label.setObjectName("playerTwoName_label")
        self.gridLayout.addWidget(self.playerTwoName_label, 1, 0, 1, 1)
        self.numberOfPlayers_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.numberOfPlayers_label.setObjectName("numberOfPlayers_label")
        self.gridLayout.addWidget(self.numberOfPlayers_label, 3, 0, 1, 1)
        self.playerOneName_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.playerOneName_label.setObjectName("playerOneName_label")
        self.gridLayout.addWidget(self.playerOneName_label, 0, 0, 1, 1)
        self.playerTwoName_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.playerTwoName_lineEdit.setObjectName("playerTwoName_lineEdit")
        self.gridLayout.addWidget(self.playerTwoName_lineEdit, 1, 1, 1, 1)
        self.playerOneName_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.playerOneName_lineEdit.setObjectName("playerOneName_lineEdit")
        self.gridLayout.addWidget(self.playerOneName_lineEdit, 0, 1, 1, 1)
        self.numberOfPlayers_spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.numberOfPlayers_spinBox.setMinimum(2)
        self.numberOfPlayers_spinBox.setMaximum(4)
        self.numberOfPlayers_spinBox.setObjectName("numberOfPlayers_spinBox")
        self.gridLayout.addWidget(self.numberOfPlayers_spinBox, 3, 1, 1, 1)
        self.apply_pushButton = QtWidgets.QPushButton(Dialog)
        self.apply_pushButton.setGeometry(QtCore.QRect(10, 130, 75, 23))
        self.apply_pushButton.setObjectName("apply_pushButton")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.playerTwoName_label.setText(_translate("Dialog", "Players Two Name:"))
        self.numberOfPlayers_label.setText(_translate("Dialog", "Number of Players:"))
        self.playerOneName_label.setText(_translate("Dialog", "Player One Name:"))
        self.apply_pushButton.setText(_translate("Dialog", "Apply"))

