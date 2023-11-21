# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1201, 874)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    border-image: url(bg_v2.png);\n"
"}\n"
"QLabel {\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"}\n"
"QLabel#heading {\n"
"  color: #0f1925;\n"
"  font-size: 18px;\n"
"  margin-bottom: 10px;\n"
"}\n"
"\n"
"QLabel#subheading {\n"
"  color: #0f1925;\n"
"  font-size: 12px;\n"
"  font-weight: normal;\n"
"  margin-bottom: 10px;\n"
"}\n"
"QLineEdit {\n"
"  background: transparent;\n"
"  color: rgb(86, 86, 86);\n"
"  border-bottom: 1px solid rgb(86, 86, 86);\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: #00557f;\n"
"  color: #0f1925;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid #00557f;\n"
"  padding: 5px 15px;\n"
"  margin-top: 10px;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  background-color: #8360aa;\n"
"  border: 3px solid #8360aa;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(80, 50, 1041, 711))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(450, 20, 171, 31))
        self.label_3.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"\n"
"color: rgb(86, 86, 86);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(160, 430, 731, 21))
        self.lineEdit.setStyleSheet("background:transparent;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 530, 731, 20))
        self.lineEdit_2.setStyleSheet("background:transparent;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(170, 380, 121, 30))
        self.label_4.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setGeometry(QtCore.QRect(170, 480, 151, 31))
        self.label_5.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 600, 511, 51))
        self.pushButton_2.setStyleSheet("QPushButton:hover,\n"
"QPushButton:focus {\n"
"    \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: #8360aa;\n"
"  border: 3px solid #8360aa;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setGeometry(QtCore.QRect(190, 110, 71, 30))
        self.label_6.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(460, 80, 131, 21))
        self.lineEdit_3.setStyleSheet("background:transparent;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(690, 80, 131, 21))
        self.lineEdit_4.setStyleSheet("background:transparent;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 80, 131, 21))
        self.lineEdit_5.setStyleSheet("background:transparent;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        self.label_7.setGeometry(QtCore.QRect(480, 110, 81, 31))
        self.label_7.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(parent=self.frame)
        self.label_9.setGeometry(QtCore.QRect(710, 110, 71, 30))
        self.label_9.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(parent=self.frame)
        self.label_8.setGeometry(QtCore.QRect(170, 150, 71, 30))
        self.label_8.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_8.setObjectName("label_8")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(170, 190, 201, 22))
        self.dateEdit.setWrapping(False)
        self.dateEdit.setObjectName("dateEdit")
        self.label_10 = QtWidgets.QLabel(parent=self.frame)
        self.label_10.setGeometry(QtCore.QRect(670, 150, 101, 30))
        self.label_10.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_10.setObjectName("label_10")
        self.comboBox = QtWidgets.QComboBox(parent=self.frame)
        self.comboBox.setGeometry(QtCore.QRect(670, 190, 201, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(6, "")
        self.label_11 = QtWidgets.QLabel(parent=self.frame)
        self.label_11.setGeometry(QtCore.QRect(170, 300, 81, 30))
        self.label_11.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_11.setObjectName("label_11")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 340, 731, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_13 = QtWidgets.QLabel(parent=self.frame)
        self.label_13.setGeometry(QtCore.QRect(170, 230, 71, 21))
        self.label_13.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_13.setObjectName("label_13")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(170, 260, 201, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(670, 260, 201, 22))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_14 = QtWidgets.QLabel(parent=self.frame)
        self.label_14.setGeometry(QtCore.QRect(670, 230, 71, 21))
        self.label_14.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1201, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "🔒Login Page"))
        self.label_3.setText(_translate("MainWindow", "Registration"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", " Enter your email"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "🔒 •••••••••••••"))
        self.label_4.setText(_translate("MainWindow", "Email"))
        self.label_5.setText(_translate("MainWindow", "Password"))
        self.pushButton_2.setText(_translate("MainWindow", "REGISTER"))
        self.label_6.setText(_translate("MainWindow", "First Name"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", " Enter your name"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", " Enter your name"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Enter your name"))
        self.label_7.setText(_translate("MainWindow", "Middle Name"))
        self.label_9.setText(_translate("MainWindow", "Last Name"))
        self.label_8.setText(_translate("MainWindow", "Birth Date"))
        self.label_10.setText(_translate("MainWindow", "Type of account"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Choose"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Admin"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Vendor"))
        self.comboBox.setItemText(3, _translate("MainWindow", "User"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Recipient"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Others"))
        self.label_11.setText(_translate("MainWindow", "Organisation"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Enter your affiliated organisation"))
        self.label_13.setText(_translate("MainWindow", "CNIC"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "example: 42301-3776165-1"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "example: 08229"))
        self.label_14.setText(_translate("MainWindow", "University ID"))

# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow
# from registration import Ui_MainWindow

# class MyApplication(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         # Additional setup for your application

# def main():
#     app = QApplication(sys.argv)
#     window = MyApplication()
#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()