# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Борис\програмирование\свои проекты\myday\tagstable.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(348, 489)
        MainWindow.setMinimumSize(QtCore.QSize(200, 400))
        MainWindow.setMaximumSize(QtCore.QSize(900, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(260, 460, 71, 23))
        self.closeButton.setObjectName("closeButton")
        self.listOfTags = QtWidgets.QListWidget(self.centralwidget)
        self.listOfTags.setGeometry(QtCore.QRect(10, 30, 331, 391))
        self.listOfTags.setFrameShape(QtWidgets.QFrame.Box)
        self.listOfTags.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.listOfTags.setDragEnabled(False)
        self.listOfTags.setDragDropOverwriteMode(False)
        self.listOfTags.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listOfTags.setAlternatingRowColors(False)
        self.listOfTags.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listOfTags.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listOfTags.setTextElideMode(QtCore.Qt.ElideLeft)
        self.listOfTags.setMovement(QtWidgets.QListView.Static)
        self.listOfTags.setProperty("isWrapping", True)
        self.listOfTags.setViewMode(QtWidgets.QListView.IconMode)
        self.listOfTags.setSelectionRectVisible(True)
        self.listOfTags.setObjectName("listOfTags")
        self.primeButton = QtWidgets.QPushButton(self.centralwidget)
        self.primeButton.setEnabled(False)
        self.primeButton.setGeometry(QtCore.QRect(40, 460, 211, 23))
        self.primeButton.setObjectName("primeButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 430, 321, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Теги"))
        self.closeButton.setText(_translate("MainWindow", "Закрыть"))
        self.primeButton.setText(_translate("MainWindow", "Выделить запись с этим тегом"))
        self.label.setText(_translate("MainWindow", "Список тегов:"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Примечание</span>: возможно выделение нескольких тегов</p></body></html>"))

