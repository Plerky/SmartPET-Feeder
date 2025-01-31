# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\smart_pet\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sql
import sqlite3
import feed
from config import DB_PATH
from qt_material import apply_stylesheet

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 471, 31))        
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.feed = QtWidgets.QPushButton(self.centralwidget)
        self.feed.setGeometry(QtCore.QRect(40, 80, 171, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.feed.setFont(font)
        self.feed.setObjectName("feed")
        self.hours_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.hours_1.setGeometry(QtCore.QRect(290, 140, 111, 41))     
        self.hours_1.setObjectName("hours_1")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(430, 80, 171, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 140, 471, 31))     
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight) 
       
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.minutes_1 = QtWidgets.QSpinBox(self.centralwidget)       
        self.minutes_1.setGeometry(QtCore.QRect(590, 140, 111, 41))   
        self.minutes_1.setObjectName("minutes_1")
        self.weight = QtWidgets.QSpinBox(self.centralwidget)
        self.weight.setGeometry(QtCore.QRect(620, 90, 71, 31))        
        self.weight.setObjectName("weight")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(700, 100, 54, 12))      
        self.label_3.setObjectName("label_3")
        self.delete = QtWidgets.QPushButton(self.centralwidget)
        self.delete.setGeometry(QtCore.QRect(310, 310, 171, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.delete.setFont(font)
        self.delete.setObjectName("delete")
        self.hours_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.hours_2.setGeometry(QtCore.QRect(180, 360, 111, 41))     
        self.hours_2.setObjectName("hours_2")
        self.minutes_2 = QtWidgets.QSpinBox(self.centralwidget)       
        self.minutes_2.setGeometry(QtCore.QRect(480, 360, 111, 41))   
        self.minutes_2.setObjectName("minutes_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 370, 471, 31))     
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(26)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)        
        self.label_4.setAutoFillBackground(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.weight_2 = QtWidgets.QSpinBox(self.centralwidget)        
        self.weight_2.setGeometry(QtCore.QRect(70, 140, 71, 31))      
        self.weight_2.setObjectName("weight_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 150, 54, 12))      
        self.label_5.setObjectName("label_5")
        self.label.raise_()
        self.feed.raise_()
        self.add.raise_()
        self.label_2.raise_()
        self.weight.raise_()
        self.label_3.raise_()
        self.delete.raise_()
        self.label_4.raise_()
        self.hours_1.raise_()
        self.minutes_1.raise_()
        self.minutes_2.raise_()
        self.hours_2.raise_()
        self.weight_2.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.feed.clicked.connect(self.feedfunc)
        self.add.clicked.connect(self.add_plan)
        self.delete.clicked.connect(self.del_plan)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SmartPET Control Panel"))
        
        self.feed.setText(_translate("MainWindow", "Feed/g"))
        self.add.setText(_translate("MainWindow", "Add feeding plan"))
        self.label_2.setText(_translate("MainWindow", ":"))
        self.label_3.setText(_translate("MainWindow", "g"))
        self.delete.setText(_translate("MainWindow", "Delete feeding plan"))
        self.label_4.setText(_translate("MainWindow", ":"))
        self.label_5.setText(_translate("MainWindow", "g"))
    
    def feedfunc(self):
        weight = self.weight_2.value()
        feed.feed(weight)

    def add_plan(self):
        with sqlite3.Connection(DB_PATH) as conn:
            cursor = sqlite3.Cursor(conn)
            hours = self.hours_1.value()
            minutes = self.minutes_1.value()
            weight = self.weight.value()
            if ((hours < 24) and (minutes < 60)):
                print(hours, minutes)
                sql.add_plan(hours, minutes, weight, cursor)
                conn.commit()
                # conn.close()
                QtWidgets.QMessageBox.information(self, 'Complete', 'Completed')
            else:
                QtWidgets.QMessageBox.information(self, 'Error', 'Invalid input')

    def del_plan(self):
        with sqlite3.Connection(DB_PATH) as conn:
            cursor = sqlite3.Cursor(conn)
            hours = self.hours_2.value()
            minutes = self.minutes_2.value()
            if ((hours < 24) and (minutes < 60)):
                sql.del_plan(hours, minutes, cursor)
                conn.commit()
                # conn.close()
                QtWidgets.QMessageBox.information(self, 'Complete', 'Completed')
            else:
                QtWidgets.QMessageBox.information(self, 'Error', 'Invalid input')

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    apply_stylesheet(app, 'default_dark.xml')
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
