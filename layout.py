# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1025, 667)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.segment = QtWidgets.QPushButton(self.centralwidget)
        self.segment.setGeometry(QtCore.QRect(390, 260, 231, 91))
        self.segment.setObjectName("segment")
        self.segment.clicked.connect(self.seg)

        self.train = QtWidgets.QPushButton(self.centralwidget)
        self.train.setGeometry(QtCore.QRect(390, 390, 231, 81))
        self.train.setObjectName("train")
        self.train.clicked.connect(self.train_model)


        self.heading = QtWidgets.QTextEdit(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(330, 130, 361, 81))
        self.heading.setObjectName("heading")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1025, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Create instance variable for window
        self.segment_window = None
        self.train_window = None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.segment.setText(_translate("MainWindow", "ACTIVE - CONTOUR SEGMENTATION"))
        self.train.setText(_translate("MainWindow", "TRAIN MODEL"))
        self.heading.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#ff0000;\">SELECT FROM THE </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#ff0000;\">OPTIONS</span></p></body></html>"))

    def seg(self):
        # Check if window is already open
        if self.segment_window is not None:
            self.segment_window.show()
            return

        # Create new window
        self.segment_window = QWidget()
        self.segment_window.setWindowTitle("Segmentation")
        self.segment_window.setGeometry(150, 150, 400, 300)
        self.segment_window.show()

    def train_model(self):
        # Check if window is already open
        if self.train_window is not None:
            self.train_window.show()
            return

        # Create new window
        self.train_window = QWidget()
        self.train_window.setWindowTitle("Training ML Models")
        self.train_window.setGeometry(150, 150, 400, 300)
        self.train_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



