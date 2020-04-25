# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Борис\програмирование\свои проекты\myday\redactordesign.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RedactorWindow(object):
    def setupUi(self, RedactorWindow):
        RedactorWindow.setObjectName("RedactorWindow")
        RedactorWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RedactorWindow.sizePolicy().hasHeightForWidth())
        RedactorWindow.setSizePolicy(sizePolicy)
        RedactorWindow.setMinimumSize(QtCore.QSize(800, 600))
        RedactorWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(RedactorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelText = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelText.setObjectName("labelText")
        self.horizontalLayout_2.addWidget(self.labelText)
        self.label = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.label.setMaxLength(100)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textRedactor = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textRedactor.setObjectName("textRedactor")
        self.verticalLayout_2.addWidget(self.textRedactor)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.tagsEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.tagsEdit.setMaxLength(200)
        self.tagsEdit.setObjectName("tagsEdit")
        self.horizontalLayout_3.addWidget(self.tagsEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.SaveButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout.addWidget(self.SaveButton)
        self.closeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        RedactorWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RedactorWindow)
        QtCore.QMetaObject.connectSlotsByName(RedactorWindow)

    def retranslateUi(self, RedactorWindow):
        _translate = QtCore.QCoreApplication.translate
        RedactorWindow.setWindowTitle(_translate("RedactorWindow", "MainWindow"))
        self.labelText.setText(_translate("RedactorWindow", "Заголовок:"))
        self.textRedactor.setPlaceholderText(_translate("RedactorWindow", "Текст"))
        self.label_2.setText(_translate("RedactorWindow", "Теги (через запятую):"))
        self.SaveButton.setText(_translate("RedactorWindow", "Сохранить"))
        self.closeButton.setText(_translate("RedactorWindow", "Закрыть"))