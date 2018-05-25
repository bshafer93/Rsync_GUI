# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_SRC/FSLA_rsyncGUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 550)
        MainWindow.setMaximumSize(QtCore.QSize(600, 550))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridWidget.setGeometry(QtCore.QRect(10, 10, 581, 481))
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
       
        self.Destination_Machine_Label = QtWidgets.QLabel(self.gridWidget)
        self.Destination_Machine_Label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.Destination_Machine_Label.setScaledContents(False)
        self.Destination_Machine_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Destination_Machine_Label.setObjectName("Destination_Machine_Label")
        
        self.gridLayout.addWidget(self.Destination_Machine_Label, 0, 1, 1, 1)
        
        self.S_M_01 = QtWidgets.QComboBox(self.gridWidget)
        self.S_M_01.setObjectName("S_M_01")
        self.S_M_01.addItem("")
        self.S_M_01.addItem("")
        self.S_M_01.addItem("")
        self.S_M_01.addItem("")
        
        self.gridLayout.addWidget(self.S_M_01, 1, 0, 1, 1)
        
        self.Source_Path_Label = QtWidgets.QLabel(self.gridWidget)
        self.Source_Path_Label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.Source_Path_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Source_Path_Label.setObjectName("Source_Path_Label")
        
        self.gridLayout.addWidget(self.Source_Path_Label, 2, 0, 1, 1)
        
        self.D_P_Button01 = QtWidgets.QPushButton(self.gridWidget)
        self.D_P_Button01.setObjectName("D_P_Button01")
        
        self.gridLayout.addWidget(self.D_P_Button01, 4, 1, 1, 1)
        
        self.D_M_01 = QtWidgets.QComboBox(self.gridWidget)
        self.D_M_01.setObjectName("D_M_01")
        self.D_M_01.addItem("")
        self.D_M_01.addItem("")
        self.D_M_01.addItem("")
        self.D_M_01.addItem("")
        
        self.gridLayout.addWidget(self.D_M_01, 1, 1, 1, 1)
        
        self.Source_Machine_Label = QtWidgets.QLabel(self.gridWidget)
        self.Source_Machine_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Source_Machine_Label.setObjectName("Source_Machine_Label")
        
        self.gridLayout.addWidget(self.Source_Machine_Label, 0, 0, 1, 1)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.gridLayout.addWidget(self.pushButton_3, 5, 1, 1, 1)
        
        #line edit 1 D_P for destination path 

        self.D_P_LineEdit01 = QtWidgets.QLineEdit(self.gridWidget)
        self.D_P_LineEdit01.setObjectName("D_P_LineEdit01")
        
        self.gridLayout.addWidget(self.D_P_LineEdit01, 3, 1, 1, 1)
        
        self.S_P_Button01 = QtWidgets.QPushButton(self.gridWidget)
        self.S_P_Button01.setObjectName("S_P_Button01")
        
        self.gridLayout.addWidget(self.S_P_Button01, 4, 0, 1, 1)
        
        self.Destination_Path_Label = QtWidgets.QLabel(self.gridWidget)
        self.Destination_Path_Label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.Destination_Path_Label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.Destination_Path_Label.setObjectName("Destination_Path_Label")
        self.gridLayout.addWidget(self.Destination_Path_Label, 2, 1, 1, 1)
        
        #line edit 2 S_P for source path 

        self.S_P_LineEdit01 = QtWidgets.QLineEdit(self.gridWidget)
        self.S_P_LineEdit01.setObjectName("S_P_LineEdit01")
        
        self.gridLayout.addWidget(self.S_P_LineEdit01, 3, 0, 1, 1)
        self.UserName_LineEdit = QtWidgets.QLineEdit(self.gridWidget)
        self.UserName_LineEdit.setObjectName("UserName_LineEdit")
        self.gridLayout.addWidget(self.UserName_LineEdit, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        self.menuUseless = QtWidgets.QMenu(self.menubar)
        self.menuUseless.setObjectName("menuUseless")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuUseless.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FSLA_rsync"))
        self.Destination_Machine_Label.setText(_translate("MainWindow", "Destination Machine"))
        self.S_M_01.setItemText(0, _translate("MainWindow", "dm1.la.Employ.com"))
        self.S_M_01.setItemText(1, _translate("MainWindow", "dm1.nyc.Employ.com"))
        self.S_M_01.setItemText(2, _translate("MainWindow", "dm1.ldn.Employ.com"))
        self.S_M_01.setItemText(3, _translate("MainWindow", "dm1.chi.Employ.com"))
        
        self.Source_Path_Label.setText(_translate("MainWindow", "Source Path"))
        self.D_P_Button01.setText(_translate("MainWindow", "Open Folder"))
        self.D_M_01.setItemText(0, _translate("MainWindow", "dm1.la.Employ.com"))
        self.D_M_01.setItemText(1, _translate("MainWindow", "dm1.nyc.Employ.com"))
        self.D_M_01.setItemText(2, _translate("MainWindow", "dm1.ldn.Employ.com"))
        self.D_M_01.setItemText(3, _translate("MainWindow", "dm1.chi.Employ.com"))
        self.Source_Machine_Label.setText(_translate("MainWindow", "Source Machine"))
        self.pushButton_3.setText(_translate("MainWindow", "Rsync"))
        self.S_P_Button01.setText(_translate("MainWindow", "Find File"))
        self.Destination_Path_Label.setText(_translate("MainWindow", "Destination Path"))
        self.UserName_LineEdit.setPlaceholderText(_translate("MainWindow", "Enter your username"))
        self.menuUseless.setTitle(_translate("MainWindow", "Useless"))

