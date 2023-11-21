
# server = 'LAPPYTOPPY'
# database = 'Northwind' 
# # use_windows_authentication = False
# username = 'sa' 
# password = 'Hyperx80' 
# # Create the connection string based on the authentication method chosen
# connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

import pyodbc
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from type_of_login import Ui_MainWindow
# from login import Ui_MainWindow
# from registration import Ui_MainWindow
# from homepage import Ui_MainWindow
# from transfer_money import Ui_MainWindow

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog

class MyApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Additional setup for your application
        self.userButton.clicked.connect(self.handleUserClick)
        self.servicebutton.clicked.connect(self.handleUserClick)
        self.adminbutton.clicked.connect(self.handleUserClick)
        self.donationbutton.clicked.connect(self.handleUserClick)

    def handleUserClick(self):
        self.view_form_window = SecondUI()

# from login import Ui_MainWindow
class SecondUI(QtWidgets.QMainWindow):

    def __init__(self):
    
        super(SecondUI, self).__init__()
        uic.loadUi('Login.ui',self)
        self.show()
        
app = QApplication(sys.argv)
window = MyApplication()
window.show()
sys.exit(app.exec())

if __name__ == "__main__":
    main()

# from PyQt6 import QtWidgets, uic, QtGui, QtCore
# import sys

# class UI(QtWidgets.QMainWindow):
#     def _init_(self):
#         super(UI,self).__init__()
#         uic.loadUi('Login.ui',self)
#         self.show()
        

# app = QtWidgets.QApplication ( sys.argv )
# window = UI()
# window.show()
# sys.exit(app.exec())