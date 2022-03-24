import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog
import requests
import json
import time
import sqlite3



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(454, 567)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(340, 10, 100, 23))
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 11, 320, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 40, 100, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 70, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 85, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(18, 210, 80, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 130, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 88, 13))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 70, 340, 16))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 210, 341, 16))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 100, 340, 16))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 240, 341, 16))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 40, 220, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 280, 70, 13))
        self.label_6.setObjectName("label_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 300, 421, 221))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 40, 111, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 130, 341, 71))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 454, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.lineEdit.paste)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OCR Docs"))
        self.pushButton.setText(_translate("MainWindow", "select a file"))
        self.pushButton_2.setText(_translate("MainWindow", "Recognition"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Группа:</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Work Name:</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Educational cipher:</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Theme:</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Name student:</p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Adding information to the database"))
        self.label_6.setText(_translate("MainWindow", "Results"))
        self.pushButton_4.setText(_translate("MainWindow", "Recognition text"))

class Demo(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Demo, self).__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_2.clicked.connect(self.recognise_file)
        self.pushButton_4.clicked.connect(self.Work)
        self.pushButton_4.clicked.connect(self.Theme_Name)
        self.pushButton_4.clicked.connect(self.Group_Name)
        self.pushButton_4.clicked.connect(self.FIO_Students_Name)
        self.pushButton_4.clicked.connect(self.cipher_Name)
        self.pushButton_3.clicked.connect(self.Data_database)


    def on_click(self):
        self.data = QFileDialog.getOpenFileName(self, 'Open file', './', "Image (*.png *.jpg *jpeg)")
        self.lineEdit.setText(self.data[0])
        if isinstance(self.data, tuple):
            self.textBrowser.setText("File Download!")
        else:
            self.textBrowser.setText("File not loaded!")

    def recognise_file(self):
        if isinstance(self.data, tuple):
            self.data = self.data[0]  # Qt4/5 API difference
        if self.data == '':
          return
        self.data_r = {'file': open(self.data, 'rb')}
        url = 'https://app.nanonets.com/api/v2/OCR/Model/00000-e0000-00-000-400000/LabelFile/'
        response = requests.post(url, auth=requests.auth.HTTPBasicAuth('00000000', ''), files=self.data_r)
        with open("data_file.json", "w") as f:
            f.write(response.text)
        with open('data_file.json', 'r') as d:
            self.data_file = json.load(d)
            
        if self.data_file['message']=='Success':
            self.textBrowser.append("Image successfully recognized!")
            
        else:
            self.textBrowser.append("Image not recognized")


            


    def Work(self):
        
        work = self.data_file['result'][0]['prediction'][0]
        if work['label']=='cipher':
            print()
        elif work['label']=='Theme':
            print()
        elif work['label']=='Group':
            print()
        elif work['label']=='FIO_Students':
            print()
        elif work['label']=='Work_name':
            print()
            self.lineEdit_4.setText(work['ocr_text'])
            

       
            
    def Theme_Name(self):
        
        theme = self.data_file['result'][0]['prediction'][1]
        if theme['label']=='Work_name':
            print()
        elif theme['label']=='cipher':
            print()
        elif theme['label']=='Group':
            print()
        elif theme['label']=='FIO_Students':
            print()
        elif theme['label']=='Theme':
            print()
            self.textEdit.setText(theme['ocr_text'])


    def Group_Name(self):
        
        group = self.data_file['result'][0]['prediction'][2]
        if group['label']=='Work_name':
            print()
        elif group['label']=='Theme':
            print()
        elif group['label']=='cipher':
            print()
        elif group['label']=='FIO_Students':
            print()
        elif group['label']=='Group':
            print()
            self.lineEdit_2.setText(group['ocr_text'])


    def FIO_Students_Name(self):
        
        fio = self.data_file['result'][0]['prediction'][3]
        if fio['label']=='Work_name':
            print()
        elif fio['label']=='Theme':
            print()
        elif fio['label']=='Group':
            print()
        elif fio['label']=='cipher':
            print()
        elif fio['label']=='FIO_Students':
            print()
            self.lineEdit_5.setText(fio['ocr_text'])
          

    def cipher_Name(self):
        
        ciph = self.data_file['result'][0]['prediction'][4]
        if ciph['label']=='Work_name':
            print()
        elif ciph['label']=='Theme':
            print()
        elif ciph['label']=='Group':
            print()
        elif ciph['label']=='FIO_Students':
            print()
        elif ciph['label']=='cipher':
            print()
            self.lineEdit_3.setText(ciph['ocr_text'])
            self.textBrowser.append("Text  successfully recognition!")


    def Data_database(self):
            try:
                sqlite_connection = sqlite3.connect('sqlite_python.db')
                cursor = sqlite_connection.cursor()
                self.textBrowser.append("Connected in SQLite")

                sqlite_insert_with_param = """INSERT INTO Students (FIO_Students_Name, cipher_Name, Work, Theme_Name, Group_Name) VALUES (?, ?, ?, ?, ?);"""

                data_tuple = (self.lineEdit_5.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.textEdit.toPlainText(), self.lineEdit_2.text(),)
                cursor.execute(sqlite_insert_with_param, data_tuple)
                sqlite_connection.commit()
                self.textBrowser.append("Python variables successfully inserted into Students table")

                cursor.close()

            except sqlite3.Error:
                self.textBrowser.append("Error while working with SQLite")
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    self.textBrowser.append("SQLite connection closed")





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = Demo()
    #    ui = Ui_Form()
#    ui.setupUi(Form)
    Form.show()  # Show main form
    sys.exit(app.exec_())  # Waiting for the program to exit in a loop