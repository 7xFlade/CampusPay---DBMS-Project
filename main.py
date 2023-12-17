import sys
import pyodbc
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QDateEdit,
)

from PyQt6.QtCore import Qt, QDate
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt
from datetime import date
import time

server = 'LAPPYTOPPY'
database = 'CampusPay' 
# use_windows_authentication = False
username = 'sa' 
password = 'Hyperx80' 
# Create the connection string based on the authentication method chosen
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# drivers = [item for item in pyodbc.drivers()]
# driver = drivers[-1]

# connection_string = f"DRIVER={driver};SERVER=localhost;DATABASE={database}; UID={username};PWD={password}; PORT=1433; TrustServerCertificate=yes;Connection Timeout=30;"

import sys
import pyodbc
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QDateEdit
from PyQt6.uic import loadUi


class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.user_type = None
        self.current_ui = None  # Keep track of the current UI instance
        self.user = None
        self.balance = None
        self.homepage = None
        self.ticket = None

        self.central_layout = QVBoxLayout(self.central_widget)

        self.load_ui("type_of_login.ui")  # Load the initial UI
        self.show()
        self.table = None

    def load_ui(self, ui_file):
        if self.current_ui:
            existing_layout = self.central_widget.layout()
            if existing_layout:
                while existing_layout.count():
                    item = existing_layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.setParent(None)

        self.current_ui = loadUi(ui_file)

        # Connect button clicks to handle switching UIs
        if ui_file == "type_of_login.ui":
            self.current_ui.userButton.clicked.connect(
                lambda: self.switch_ui("Login.ui", "user")
            )
            self.current_ui.servicebutton.clicked.connect(
                lambda: self.switch_ui("Login.ui", "service")
            )
            self.current_ui.adminbutton.clicked.connect(
                lambda: self.switch_ui("Login.ui", "admin")
            )
            self.current_ui.donationbutton.clicked.connect(
                lambda: self.switch_ui("Login.ui", "dd")
            )
            self.current_ui.eventbutton.clicked.connect(
                lambda: self.switch_ui("Login.ui", "event")
            )
            self.current_ui.employerbutton.clicked.connect(
                lambda: self.switch_ui("Login.ui", "employer")
            )

        # If we are loading the Login.ui, connect the login button
        elif ui_file == "Login.ui":
            self.current_ui.userTypeLabel.setText("Logging in as: " + self.user_type)
            if hasattr(self.current_ui, "loginButton"):
                self.current_ui.loginButton.clicked.connect(self.verify_credentials)
            if hasattr(self.current_ui, "registerButton"):
                self.current_ui.registerButton.clicked.connect(
                    lambda: self.load_ui("registration.ui")
                )
            self.current_ui.backButton.clicked.connect(
                lambda: self.load_ui("type_of_login.ui")
            )

        # If we are loading the registration.ui, connect the registration button
        elif ui_file == "registration.ui":
            self.current_ui.accType.currentIndexChanged.connect(self.changeRegState)
            if hasattr(self.current_ui, "registerNow"):
                self.current_ui.registerNow.clicked.connect(self.handleRegistration)
            self.current_ui.backButton.clicked.connect(lambda: self.load_ui("Login.ui"))

        elif ui_file == "events_homepage.ui":
            self.loadHomeDetails()
            self.current_ui.transferbutton.clicked.connect(
                lambda: self.load_ui("transfer_money.ui")
            )
            self.current_ui.loadbutton.clicked.connect(
                lambda: self.load_ui("load_money.ui")
            )
            self.current_ui.transactionButton.clicked.connect(
                lambda: self.load_ui("transaction_history_v2.ui")
            )
            self.current_ui.ticketButton.clicked.connect(
                lambda: self.load_ui("Ticketinfo.ui")
            )
            self.current_ui.backButton.clicked.connect(lambda: self.load_ui("Login.ui"))

        elif ui_file == "homepage.ui":
            self.loadHomeDetails()
            self.current_ui.transferbutton.clicked.connect(
                lambda: self.load_ui("transfer_money.ui")
            )
            self.current_ui.loadbutton.clicked.connect(
                lambda: self.load_ui("load_money.ui")
            )
            self.current_ui.transactionButton.clicked.connect(
                lambda: self.load_ui("transaction_history_v2.ui")
            )
            self.current_ui.backButton.clicked.connect(lambda: self.load_ui("Login.ui"))
            self.current_ui.ticketButton.clicked.connect(
                lambda: self.load_ui("buy_ticket.ui")
            )

        elif ui_file == "transfer_money.ui":
            self.current_ui.backButton.clicked.connect(
                lambda: self.load_ui(self.homepage)
            )
            self.current_ui.balText.setText(str(self.balance))
            self.current_ui.sendButton.clicked.connect(self.sendMoney)
            self.current_ui.recipientType.currentIndexChanged.connect(
                self.changeTransferState
            )

        elif ui_file == "admin.ui":
            self.loadAdminPage()
            self.current_ui.logoutButton.clicked.connect(
                lambda: self.load_ui("Login.ui")
            )

        elif ui_file == "load_money.ui":
            self.loadMoneyUi()
            self.current_ui.verifyButton.clicked.connect(self.verifyCoupon)
            self.current_ui.loadButton.clicked.connect(self.load_money_with_coupon)
            self.current_ui.backButton.clicked.connect(
                lambda: self.load_ui(self.homepage)
            )

        elif ui_file == "transaction_history_v2.ui":
            self.loadHistory()

            self.current_ui.backButton.clicked.connect(
                lambda: self.load_ui(self.homepage)
            )

        elif ui_file == "Ticketinfo.ui":
            self.loadTicket()
            self.current_ui.backButton.clicked.connect(
                lambda: self.load_ui(self.homepage)
            )
        elif ui_file == "buy_ticket.ui":
            self.populate_event_combobox()
            # Connect ComboBox signal to the function to update event details
            self.current_ui.events.currentIndexChanged.connect(
                self.update_event_details
            )
            self.current_ui.buyButton.clicked.connect(self.process_buy_transaction)
            self.current_ui.backButton.clicked.connect(
                lambda: self.load_ui(self.homepage)
            )
        self.setFixedSize(self.current_ui.size())
        self.central_layout.addWidget(self.current_ui)

    def switch_ui(self, ui_file, user_type=None):
        self.homepage = "homepage.ui"
        if user_type != None:
            self.user_type = user_type
            match user_type:
                case "user":
                    self.table = "UserAcc"
                case "service":
                    self.table = "ServiceProvider"
                case "admin":
                    self.table = "Admin"
                case "dd":
                    self.table = "DonationDrive"
                case "event":
                    self.homepage = "events_homepage.ui"
                    self.table = "Events"
                case "employer":
                    self.table = "StudentEmployer"

        self.load_ui(ui_file)

    def verify_credentials(self):
        # Function for verifying user credentials from the database
        this_username = self.current_ui.username.text()
        this_password = self.current_ui.password.text()

        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()
                query = f"SELECT * FROM {self.table} WHERE ID = ? AND password = ?"
                cursor.execute(query, (this_username, this_password))
                user = cursor.fetchone()

                if user:
                    # Add logic to switch to the next UI or perform other actions on successful login
                    self.user = this_username
                    if self.table == "Admin":
                        self.load_ui("admin.ui")
                    elif self.table == "Events":
                        self.load_ui("events_homepage.ui")
                    else:
                        self.load_ui("homepage.ui")

                else:
                    self.current_ui.incorrectPassword.setText(
                        "Incorrect Username or password, try again!"
                    )
                    self.current_ui.username.clear()
                    self.current_ui.password.clear()

        except pyodbc.Error as e:
            print(f"Error during login: {e}")

    def handleRegistration(self):
        # Function for handling user registration with database interaction
        new_username = self.current_ui.username.text()
        new_password = self.current_ui.password.text()
        detail2 = self.current_ui.detail2.text()
        f_name = self.current_ui.firstName.text()
        m_name = self.current_ui.midName.text()
        l_name = self.current_ui.lastName.text()
        new_email = self.current_ui.email.text()
        usertype = self.current_ui.accType.currentText()
        date_q = self.current_ui.birthDate.date()
        detail = self.current_ui.detail.text()
        date_python = date(date_q.year(), date_q.month(), date_q.day())

        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()
                # Perform database queries to insert the new user into the database
                match usertype:
                    case "User":
                        query = f"INSERT INTO UserAcc (ID, email, password, D_O_B, fName, mName, lName) VALUES (?, ?, ?, ?, ?, ?, ?)"
                        cursor.execute(
                            query,
                            (
                                new_username,
                                new_email,
                                new_password,
                                date_python,
                                f_name,
                                m_name,
                                l_name,
                            ),
                        )
                    case "Service Provider":
                        query = f"INSERT INTO ServiceProvider (ID, email, password, Name, service) VALUES ( ?, ?, ?, ?, ?)"
                        cursor.execute(
                            query,
                            (
                                new_username,
                                new_email,
                                new_password,
                                f_name + m_name + l_name,
                                detail,
                            ),
                        )
                    case "Donation Drive":
                        query = f"INSERT INTO DonationDrive (ID, email, password, name, purpose) VALUES ( ?, ?, ?, ?, ?)"
                        cursor.execute(
                            query,
                            (
                                new_username,
                                new_email,
                                new_password,
                                f_name + m_name + l_name,
                                detail,
                            ),
                        )
                    case "Event":
                        try:
                            tickets = int(detail) % 9000
                            cost = float(detail2)
                        except:
                            self.current_ui.errorLabel.setText(
                                "Invalid number for Tickets Cap or Cost"
                            )
                            return
                        query = f"INSERT INTO Events (ID, password, eventName, ticketsCap, [date]) VALUES ( ?, ?, ?, ?, ?)"
                        cursor.execute(
                            query,
                            (
                                new_username,
                                new_password,
                                f_name + m_name + l_name,
                                tickets,
                                date_python,
                            ),
                        )
                        for i in range(tickets):
                            query = f"INSERT INTO EventTickets (eventID, ticketID, cost) VALUES ( ?, ?, ?)"
                            cursor.execute(
                                query, (new_username, "TCK" + str(10001 + i), cost)
                            )
                    case "Student Employer":
                        query = f"INSERT INTO StudentEmployer (ID, name, IBAN) VALUES ( ?, ?, ?)"
                        cursor.execute(
                            query,
                            (
                                new_username,
                                f_name + " " + m_name + " " + l_name,
                                detail,
                            ),
                        )

                connection.commit()

                print("Registration successful")
                self.current_ui.successLabel.setText("Registeration Successful")
                self.current_ui.errorLabel.setText("")

        except pyodbc.Error as e:
            self.current_ui.errorLabel.setText("Username is not unique")
            self.current_ui.successLabel.setText("")
            print(f"Registration failed: {e}")

    def changeRegState(self):
        newUserType = self.current_ui.accType.currentText()
        self.current_ui.detailLabel2.setText("University ID")
        match newUserType:
            case "Service Provider":
                self.current_ui.birthDate.setDisabled(True)
                self.current_ui.detail.setEnabled(True)
                self.current_ui.detailLabel.setText("Service")
            case "User":
                self.current_ui.dateLabel.setText("Birth Date")
                self.current_ui.birthDate.setEnabled(True)
                self.current_ui.detail.setDisabled(True)
            case "Donation Drive":
                self.current_ui.birthDate.setDisabled(True)
                self.current_ui.detail.setEnabled(True)
                self.current_ui.detailLabel.setText("Purpose")
            case "Event":
                self.current_ui.birthDate.setEnabled(True)
                self.current_ui.detail.setEnabled(True)
                self.current_ui.detailLabel.setText("Tickets Cap")
                self.current_ui.dateLabel.setText("Event Date")
                self.current_ui.detailLabel2.setText("Cost of Tickets")
            case "Student Employer":
                self.current_ui.birthDate.setDisabled(True)
                self.current_ui.detail.setEnabled(True)
                self.current_ui.detailLabel.setText("IBAN")

    def loadHomeDetails(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()
                match self.table:
                    case "UserAcc":
                        query = f"SELECT CONCAT(fName, ' ', mName, ' ', lName) as name, balance FROM {self.table} WHERE ID = ?"
                    case "ServiceProvider":
                        query = f"SELECT name, balance FROM {self.table} WHERE ID = ?"
                    case "DonationDrive":
                        query = f"SELECT name, balance FROM {self.table} WHERE ID = ?"
                    case "Events":
                        query = f"SELECT eventName as name, balance FROM {self.table} WHERE ID = ?"
                    case "StudentEmployer":
                        query = f"SELECT name, balance FROM {self.table} WHERE ID = ?"

                cursor.execute(query, (self.user))
                result = cursor.fetchone()

                if result.balance is None:
                    text = "Balance is: 0 PKR"
                    self.balance = 0
                else:
                    text = "Balance is: " + str(result.balance) + " PKR"
                    self.balance = result.balance

        except pyodbc.Error as e:
            print(f"Homepage Load failed: {e}")
        self.current_ui.holderName.setText(result.name)
        self.current_ui.balance.setText(text)

    def getTrTables(self, recType):
        if recType == "Bank":
            trTable = "IBFTOutTransaction"
        elif recType == "Mobile Topup":
            trTable = "mobileTopup"
        else:
            trTable = "IntraTransaction"
        toTable = ""
        match recType:
            case "User":
                toTable = "UserAcc"
            case "ServiceProvider":
                toTable = "ServiceProvider"
            case "Event":
                toTable = "Events"
            case "DonationDrive":
                toTable = "DonationDrive"
        return trTable, toTable

    def checkUser(self, cursor, transactionTable, toTable, destinationAccount):
        if transactionTable == "IntraTransaction":
            cursor.execute(
                f"SELECT balance FROM {toTable} WHERE ID = ?",
                destinationAccount,
            )
            result = cursor.fetchone()
            if result:
                return True
            else:
                return False
        else:
            return True

    def sendMoney(self):
        sourceAccount = self.user
        recType = self.current_ui.recipientType.currentText()
        try:
            transferAmount = float(self.current_ui.amountText.text())
        except:
            self.current_ui.userError.setText("Invalid Amount")
            return None
        destinationAccount = self.current_ui.recipient.text()
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()
                fromTable = self.table
                transactionTable, toTable = self.getTrTables(recType)
                userExists = self.checkUser(
                    cursor, transactionTable, toTable, destinationAccount
                )
                if userExists:
                    # Retrieve the balance from the source account
                    cursor.execute(
                        f"SELECT balance FROM {fromTable} WHERE ID = ?", sourceAccount
                    )
                    sourceBalance = cursor.fetchone().balance
                    print(destinationAccount)
                    print(toTable)
                    # Check if there's enough balance for the transfer
                    if sourceBalance >= transferAmount:
                        # Update the balance of the source account
                        cursor.execute(
                            f"UPDATE {fromTable} SET balance = balance - ? WHERE ID = ?",
                            transferAmount,
                            sourceAccount,
                        )

                        # Update the balance of the destination account
                        if toTable != "":
                            cursor.execute(
                                f"UPDATE {toTable} SET balance = balance + ? WHERE ID = ?",
                                transferAmount,
                                destinationAccount,
                            )
                        t = time.localtime()
                        current_time = time.strftime("%H:%M:%S", t)
                        match transactionTable:
                            case "IntraTransaction":
                                cursor.execute(
                                    f"INSERT INTO {transactionTable} ([from], [to], amount, purpose, date, time, promotionID) VALUES (?, ?, ?, ?, ?, ?, ?) ",
                                    sourceAccount,
                                    destinationAccount,
                                    transferAmount,
                                    self.current_ui.purposeText.text(),
                                    date.today(),
                                    current_time,
                                    self.current_ui.promoText.text(),
                                )
                            case "IBFTOutTransaction":
                                cursor.execute(
                                    f"INSERT INTO {transactionTable} ([from], toIBAN, amount, purpose, date, time, tax) VALUES (?, ?, ?, ?, ?, ?, ?) ",
                                    sourceAccount,
                                    destinationAccount,
                                    transferAmount,
                                    self.current_ui.purposeText.text(),
                                    date.today(),
                                    current_time,
                                    23.53,
                                )
                            case "mobileTopup":
                                cursor.execute(
                                    f"INSERT INTO {transactionTable} ([from], toPhNum, amount, date, time) VALUES ( ?, ?, ?, ?, ?) ",
                                    sourceAccount,
                                    destinationAccount,
                                    transferAmount,
                                    date.today(),
                                    current_time,
                                )
                        # Commit the transaction
                        connection.commit()
                        print("Transfer successful!")
                        self.current_ui.successLabel.setText("Transaction Successful")
                        self.current_ui.userError.setText("")
                    else:
                        self.current_ui.successLabel.setText(
                            "Insufficient balance for the transfer."
                        )
                        self.current_ui.userError.setText("")
                else:
                    self.current_ui.userError.setText("User Not Found!")
                    self.current_ui.successLabel.setText("")

        except pyodbc.Error as e:
            print(f"Error during transfer: {e}")

    def changeTransferState(self):
        recType = self.current_ui.recipientType.currentText()
        if recType == "ServiceProvider":
            self.current_ui.promoText.clear()
            self.current_ui.promoText.setEnabled(True)
        else:
            self.current_ui.promoText.clear()
            self.current_ui.promoText.setDisabled(True)
        match recType:
            case "ServiceProvider":
                self.current_ui.recipientLabel.setText("Recipient Service Provider ID")
            case "User":
                self.current_ui.recipientLabel.setText("Recipient User ID")
            case "Mobile Topup":
                self.current_ui.recipientLabel.setText("Phone Number")
            case "Event":
                self.current_ui.recipientLabel.setText("Recipient Event ID")
            case "DonationDrive":
                self.current_ui.recipientLabel.setText("Recipient Donation Drive ID")
            case "Bank":
                self.current_ui.recipientLabel.setText("Recipient IBAN")

    def populate_intra_transaction_table(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()

                # Fetch data from the IntraTransaction table sorted by date
                cursor.execute(
                    "SELECT transactionID, [from], [to], amount, purpose, promotionID, date, time FROM IntraTransaction ORDER BY date DESC, time DESC"
                )
                intra_transaction_data = cursor.fetchall()
                self.current_ui.trTable.setRowCount(len(intra_transaction_data))
                # Populate the table widget
                for row, data in enumerate(intra_transaction_data):
                    for col, value in enumerate(data):
                        item = QTableWidgetItem(str(value))
                        self.current_ui.trTable.setItem(row, col, item)

        except pyodbc.Error as e:
            print(f"Error fetching IntraTransaction data: {e}")

    def populate_user_acc_table(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()

                # Fetch data from the UserAcc table sorted by ID
                cursor.execute(
                    "SELECT ID, fName, mName, lName, email, balance FROM UserAcc ORDER BY ID"
                )
                user_acc_data = cursor.fetchall()
                self.current_ui.usersTable.setRowCount(len(user_acc_data))
                # Populate the table widget
                for row, data in enumerate(user_acc_data):
                    id_item = QTableWidgetItem(str(data.ID))
                    name_item = QTableWidgetItem(
                        f"{data.fName} {data.mName} {data.lName}"
                    )

                    email_item = QTableWidgetItem(str(data.email))
                    balance_item = QTableWidgetItem(str(data.balance))
                    self.current_ui.usersTable.setItem(row, 0, id_item)
                    self.current_ui.usersTable.setItem(row, 1, name_item)
                    self.current_ui.usersTable.setItem(row, 2, email_item)
                    self.current_ui.usersTable.setItem(row, 3, balance_item)

        except pyodbc.Error as e:
            print(f"Error fetching UserAcc data: {e}")

    def populate_service_provider_table(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()

                # Fetch data from the ServiceProvider table sorted by ID
                cursor.execute(
                    "SELECT ID, Name, service, balance FROM ServiceProvider ORDER BY ID"
                )
                service_provider_data = cursor.fetchall()
                self.current_ui.spTable.setRowCount(len(service_provider_data))
                # Populate the table widget
                for row, data in enumerate(service_provider_data):
                    id_item = QTableWidgetItem(str(data.ID))
                    name_item = QTableWidgetItem(str(data.Name))
                    service_item = QTableWidgetItem(str(data.service))
                    balance_item = QTableWidgetItem(str(data.balance))
                    self.current_ui.spTable.setItem(row, 0, id_item)
                    self.current_ui.spTable.setItem(row, 1, name_item)
                    self.current_ui.spTable.setItem(row, 2, service_item)
                    self.current_ui.spTable.setItem(row, 3, balance_item)

        except pyodbc.Error as e:
            print(f"Error fetching ServiceProvider data: {e}")

    def populate_events_table(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()

                # Fetch data from the Events table sorted by Date
                cursor.execute(
                    "SELECT ID, eventName, date, balance FROM Events ORDER BY date DESC"
                )
                events_data = cursor.fetchall()
                self.current_ui.eventsTable.setRowCount(len(events_data))
                # Populate the table widget
                for row, data in enumerate(events_data):
                    id_item = QTableWidgetItem(str(data.ID))
                    name_item = QTableWidgetItem(str(data.eventName))
                    date_item = QTableWidgetItem(str(data.date))
                    balance_item = QTableWidgetItem(str(data.balance))

                    self.current_ui.eventsTable.setItem(row, 0, id_item)
                    self.current_ui.eventsTable.setItem(row, 1, name_item)
                    self.current_ui.eventsTable.setItem(row, 2, date_item)
                    self.current_ui.eventsTable.setItem(row, 3, balance_item)

        except pyodbc.Error as e:
            print(f"Error fetching Events data: {e}")

    def populate_donation_drive_table(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()

                # Fetch data from the DonationDrive table sorted by ID in descending order
                cursor.execute(
                    "SELECT ID, name, purpose, balance FROM DonationDrive ORDER BY ID DESC"
                )
                donation_drive_data = cursor.fetchall()
                self.current_ui.ddTable.setRowCount(len(donation_drive_data))
                # Populate the table widget
                for row, data in enumerate(donation_drive_data):
                    id_item = QTableWidgetItem(str(data.ID))
                    name_item = QTableWidgetItem(str(data.name))
                    purpose_item = QTableWidgetItem(str(data.purpose))
                    balance_item = QTableWidgetItem(str(data.balance))

                    self.current_ui.ddTable.setItem(row, 0, id_item)
                    self.current_ui.ddTable.setItem(row, 1, name_item)
                    self.current_ui.ddTable.setItem(row, 2, purpose_item)
                    self.current_ui.ddTable.setItem(row, 3, balance_item)

        except pyodbc.Error as e:
            print(f"Error fetching DonationDrive data: {e}")

    def populate_student_employer_table(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()

                # Fetch data from the StudentEmployer table
                cursor.execute("SELECT ID, name, balance FROM StudentEmployer")
                student_employer_data = cursor.fetchall()
                self.current_ui.employerTable.setRowCount(len(student_employer_data))
                # Populate the table widget
                for row, data in enumerate(student_employer_data):
                    id_item = QTableWidgetItem(str(data.ID))
                    name_item = QTableWidgetItem(str(data.name))
                    balance_item = QTableWidgetItem(str(data.balance))

                    self.current_ui.employerTable.setItem(row, 0, id_item)
                    self.current_ui.employerTable.setItem(row, 1, name_item)
                    self.current_ui.employerTable.setItem(row, 2, balance_item)

        except pyodbc.Error as e:
            print(f"Error fetching StudentEmployer data: {e}")

    def populate_coupons_table(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()

                # Fetch data from the Coupons table
                cursor.execute("SELECT CouponID, amount, isUsed, usedBy FROM Coupons")
                coupons_data = cursor.fetchall()
                self.current_ui.couponTable.setRowCount(len(coupons_data))
                # Populate the table widget
                for row, data in enumerate(coupons_data):
                    id_item = QTableWidgetItem(str(data.CouponID))
                    amount_item = QTableWidgetItem(str(data.amount))
                    is_used_item = QTableWidgetItem(str(data.isUsed))

                    # Display a hyphen if "Used By" is null
                    used_by_value = str(data.usedBy) if data.usedBy is not None else "-"
                    used_by_item = QTableWidgetItem(used_by_value)

                    self.current_ui.couponTable.setItem(row, 0, id_item)
                    self.current_ui.couponTable.setItem(row, 1, is_used_item)
                    self.current_ui.couponTable.setItem(row, 2, used_by_item)
                    self.current_ui.couponTable.setItem(row, 3, amount_item)

        except pyodbc.Error as e:
            print(f"Error fetching Coupons data: {e}")

    def populate_mobile_topup_table(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()

                # Fetch data from the mobileTopup table sorted by Date and Time in descending order
                cursor.execute(
                    "SELECT [from] as source, toPhNum, amount, date, time FROM mobileTopup ORDER BY date DESC, time DESC"
                )
                mobile_topup_data = cursor.fetchall()
                self.current_ui.topUpTable.setRowCount(len(mobile_topup_data))
                # Populate the table widget
                for row, data in enumerate(mobile_topup_data):
                    from_item = QTableWidgetItem(str(data.source))
                    to_phone_number_item = QTableWidgetItem(str(data.toPhNum))
                    amount_item = QTableWidgetItem(str(data.amount))
                    date_item = QTableWidgetItem(str(data.date))
                    time_item = QTableWidgetItem(str(data.time))

                    self.current_ui.topUpTable.setItem(row, 0, from_item)
                    self.current_ui.topUpTable.setItem(row, 1, to_phone_number_item)
                    self.current_ui.topUpTable.setItem(row, 2, amount_item)
                    self.current_ui.topUpTable.setItem(row, 3, date_item)
                    self.current_ui.topUpTable.setItem(row, 4, time_item)

        except pyodbc.Error as e:
            print(f"Error fetching mobileTopup data: {e}")

    def populate_promotions_table(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()

                # Fetch data from the Promotions table sorted by End Date in descending order
                cursor.execute(
                    "SELECT promotionID, description, [discount%] as amount, serviceProvider, start_date, end_date, isactive, category FROM Promotions ORDER BY end_date DESC"
                )
                promotions_data = cursor.fetchall()
                self.current_ui.promoTable.setRowCount(len(promotions_data))
                # Populate the table widget
                for row, data in enumerate(promotions_data):
                    id_item = QTableWidgetItem(str(data.promotionID))
                    description_item = QTableWidgetItem(str(data.description))
                    amount_item = QTableWidgetItem(str(data.amount))
                    service_provider_item = QTableWidgetItem(str(data.serviceProvider))
                    start_date_item = QTableWidgetItem(str(data.start_date))
                    end_date_item = QTableWidgetItem(str(data.end_date))
                    is_active_item = QTableWidgetItem(str(data.isactive))
                    category_item = QTableWidgetItem(str(data.category))

                    self.current_ui.promoTable.setItem(row, 0, id_item)
                    self.current_ui.promoTable.setItem(row, 1, description_item)
                    self.current_ui.promoTable.setItem(row, 2, amount_item)
                    self.current_ui.promoTable.setItem(row, 3, service_provider_item)
                    self.current_ui.promoTable.setItem(row, 4, start_date_item)
                    self.current_ui.promoTable.setItem(row, 5, end_date_item)
                    self.current_ui.promoTable.setItem(row, 6, is_active_item)
                    self.current_ui.promoTable.setItem(row, 7, category_item)

        except pyodbc.Error as e:
            print(f"Error fetching Promotions data: {e}")

    def populate_ibft_out_transactions_table(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()

                # Fetch data from the IBFTOutTransaction table sorted by Date and Time in descending order
                cursor.execute(
                    "SELECT transactionID, [from] as source, toIBAN, amount, purpose, tax, date, time FROM IBFTOutTransaction ORDER BY date DESC, time DESC"
                )
                ibft_out_transactions_data = cursor.fetchall()
                self.current_ui.bankTable.setRowCount(len(ibft_out_transactions_data))
                # Populate the table widget
                for row, data in enumerate(ibft_out_transactions_data):
                    id_item = QTableWidgetItem(str(data.transactionID))
                    from_item = QTableWidgetItem(str(data.source))
                    to_item = QTableWidgetItem(str(data.toIBAN))
                    amount_item = QTableWidgetItem(str(data.amount))
                    purpose_item = QTableWidgetItem(str(data.purpose))
                    tax_item = QTableWidgetItem(str(data.tax))
                    date_item = QTableWidgetItem(str(data.date))
                    time_item = QTableWidgetItem(str(data.time))

                    self.current_ui.bankTable.setItem(row, 0, id_item)
                    self.current_ui.bankTable.setItem(row, 1, from_item)
                    self.current_ui.bankTable.setItem(row, 2, to_item)
                    self.current_ui.bankTable.setItem(row, 3, amount_item)
                    self.current_ui.bankTable.setItem(row, 4, purpose_item)
                    self.current_ui.bankTable.setItem(row, 5, tax_item)
                    self.current_ui.bankTable.setItem(row, 6, date_item)
                    self.current_ui.bankTable.setItem(row, 7, time_item)

        except pyodbc.Error as e:
            print(f"Error fetching IBFTOutTransaction data: {e}")

    def populate_event_tickets_table(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()

                # Fetch data from the EventTickets table
                cursor.execute(
                    "SELECT eventID, ticketID, boughtBy, cost FROM EventTickets"
                )
                event_tickets_data = cursor.fetchall()
                self.current_ui.ticketsTable.setRowCount(len(event_tickets_data))
                # Populate the table widget
                for row, data in enumerate(event_tickets_data):
                    event_id_item = QTableWidgetItem(str(data.eventID))
                    ticket_id_item = QTableWidgetItem(str(data.ticketID))

                    # Display a hyphen if "Bought By" is null
                    bought_by_value = (
                        str(data.boughtBy) if data.boughtBy is not None else "-"
                    )
                    bought_by_item = QTableWidgetItem(bought_by_value)

                    cost_item = QTableWidgetItem(str(data.cost))

                    self.current_ui.ticketsTable.setItem(row, 0, event_id_item)
                    self.current_ui.ticketsTable.setItem(row, 1, ticket_id_item)
                    self.current_ui.ticketsTable.setItem(row, 2, bought_by_item)
                    self.current_ui.ticketsTable.setItem(row, 3, cost_item)

        except pyodbc.Error as e:
            print(f"Error fetching EventTickets data: {e}")

    def loadAdminPage(self):
        self.populate_coupons_table()
        self.populate_donation_drive_table()
        self.populate_event_tickets_table()
        self.populate_events_table()
        self.populate_ibft_out_transactions_table()
        self.populate_intra_transaction_table()
        self.populate_mobile_topup_table()
        self.populate_promotions_table()
        self.populate_service_provider_table()
        self.populate_user_acc_table()
        self.populate_student_employer_table()

    def loadMoneyUi(self):
        self.current_ui.userText.setText(self.user)
        self.current_ui.accText.setText(self.user_type)
        self.current_ui.balText.setText(str(self.balance))

    def verifyCoupon(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()
                coupon_id = self.current_ui.coupon.text()
                # Check if the coupon exists and is not used
                cursor.execute(
                    "SELECT CouponID, amount FROM Coupons WHERE CouponID = ? AND isUsed = 'false'",
                    coupon_id,
                )
                row = cursor.fetchone()

                if row:
                    # The coupon is valid and can be applied
                    self.current_ui.amountText.setText(str(row.amount))
                    self.current_ui.nextBalText.setText(str(row.amount + self.balance))
                    self.current_ui.verifiedLabel.setText("Coupon Verified")
                    self.current_ui.errorLabel.setText("")
                    # You can add further actions here, such as updating the coupon status or applying the discount.
                else:
                    self.current_ui.errorLabel.setText(
                        "Invalid coupon or the coupon has already been used."
                    )
                    self.current_ui.verifiedLabel.setText("")
                    # The coupon is either invalid or has already been used
                    # You can handle this case as needed, such as displaying an error message.

        except pyodbc.Error as e:
            print(f"Coupon verification error: {e}")

    def load_money_with_coupon(self):
        # Replace these values with the actual user ID, amount, and coupon ID entered by the user
        current_user_id = self.user
        coupon_to_use = self.current_ui.coupon.text()

        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()
                self.verifyCoupon()

                cursor.execute(
                    "SELECT CouponID, amount FROM Coupons WHERE CouponID = ? AND isUsed = 'false'",
                    coupon_to_use,
                )
                row = cursor.fetchone()
                if row:
                    if self.balance != 0:
                        query = f"UPDATE {self.table} SET balance = balance + ? WHERE ID = ?"
                    else:
                        query = f"UPDATE {self.table} SET balance = ? WHERE ID = ?"
                    print(query)
                    cursor.execute(
                        query,
                        row.amount,
                        current_user_id,
                    )

                    # Mark the coupon as used and associate it with the current user
                    cursor.execute(
                        "UPDATE Coupons SET isUsed = 'true', usedBy = ? WHERE CouponID = ?",
                        current_user_id,
                        coupon_to_use,
                    )

                    # Commit the transaction
                    connection.commit()
                    print(row.amount)
                    self.balance += row.amount
                    self.current_ui.verifiedLabel.setText("Coupon used successfully")
                else:
                    # The coupon is either invalid or has already been used
                    self.current_ui.errorLabel.setText(
                        "Invalid coupon or the coupon has already been used."
                    )
                    # You can handle this case as needed, such as displaying an error message.

        except pyodbc.Error as e:
            print(f"Loading Money error: {e}")

    def loadHistory(self):
        self.loadOutgoing()
        self.loadIncoming()
        self.loadBank()
        self.loadCoupons()
        self.loadTopUp()
        self.loadUserTicket()

    def loadOutgoing(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()
                query = """
                    SELECT transactionID, [to], amount, purpose, promotionID, date, time
                    FROM IntraTransaction
                    WHERE [from] = ? 
                    ORDER BY date DESC, time DESC
                """
                cursor.execute(query, self.user)
                data = cursor.fetchall()
                # self.current_ui.outTable.setRowCount(len(data))
                for row_index, row_data in enumerate(data):
                    self.current_ui.outTable.insertRow(row_index)
                    for col_index, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.current_ui.outTable.setItem(row_index, col_index, item)
        except pyodbc.Error as e:
            print(f"Loading Outgoing transaction error: {e}")

    def loadIncoming(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()
                query = """
                    SELECT transactionID, [from], amount, purpose, date, time
                    FROM IntraTransaction
                    WHERE [to] = ? 
                    ORDER BY date DESC, time DESC
                """
                cursor.execute(query, self.user)
                data = cursor.fetchall()
                # self.current_ui.inTable.setRowCount(len(data))
                for row_index, row_data in enumerate(data):
                    self.current_ui.inTable.insertRow(row_index)
                    for col_index, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.current_ui.inTable.setItem(row_index, col_index, item)
        except pyodbc.Error as e:
            print(f"Loading Incoming Transaction Error: {e}")

    def loadBank(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()
                query = """
                    SELECT transactionID, [toIBAN], amount, purpose, tax, date, time
                    FROM IBFTOutTransaction
                    WHERE [from] = ? 
                    ORDER BY date DESC, time DESC
                """
                cursor.execute(query, self.user)
                data = cursor.fetchall()
                # self.current_ui.bankTable.setRowCount(len(data))
                for row_index, row_data in enumerate(data):
                    self.current_ui.bankTable.insertRow(row_index)
                    for col_index, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.current_ui.bankTable.setItem(row_index, col_index, item)
        except pyodbc.Error as e:
            print(f"Loading Bank transaction error: {e}")

    def loadCoupons(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()
                query = """
                    SELECT CouponID, amount
                    FROM Coupons
                    WHERE [usedBy] = ? 
                    ORDER BY couponID
                """
                cursor.execute(query, self.user)
                data = cursor.fetchall()
                # self.current_ui.outTable.setRowCount(len(data))
                for row_index, row_data in enumerate(data):
                    self.current_ui.couponTable.insertRow(row_index)
                    for col_index, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.current_ui.couponTable.setItem(row_index, col_index, item)
        except pyodbc.Error as e:
            print(f"Loading Coupon transaction error: {e}")

    def loadTopUp(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()
                query = """
                    SELECT transactionID, toPhNum, amount, date, time
                    FROM mobileTopup
                    WHERE [from] = ? 
                    ORDER BY date DESC, time DESC
                """
                cursor.execute(query, self.user)
                data = cursor.fetchall()
                # self.current_ui.topUpTable.setRowCount(len(data))
                for row_index, row_data in enumerate(data):
                    self.current_ui.topUpTable.insertRow(row_index)
                    for col_index, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.current_ui.topUpTable.setItem(row_index, col_index, item)
        except pyodbc.Error as e:
            print(f"Loading Outgoing transaction error: {e}")

    def loadUserTicket(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()
                query = """
                        SELECT eventID, ticketID, cost
                        FROM EventTickets
                        WHERE boughtBy = ?
                    """
                cursor.execute(query, self.user)
                event_tickets = cursor.fetchall()

                # Populate the table with event ticket data
                self.current_ui.ticketTable.setRowCount(0)
                for row_index, row_data in enumerate(event_tickets):
                    self.current_ui.ticketTable.insertRow(row_index)
                    for col_index, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.current_ui.ticketTable.setItem(row_index, col_index, item)

        except pyodbc.Error as e:
            print(f"Database error: {e}")

    def loadTicket(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()
                query = """
                        SELECT ticketID, cost, boughtBy
                        FROM EventTickets
                        WHERE eventID = ?
                    """
                cursor.execute(query, self.user)
                event_tickets = cursor.fetchall()

                # Populate the table with event ticket data
                self.current_ui.ticketTable.setRowCount(0)
                for row_index, row_data in enumerate(event_tickets):
                    self.current_ui.ticketTable.insertRow(row_index)
                    for col_index, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.current_ui.ticketTable.setItem(row_index, col_index, item)

        except pyodbc.Error as e:
            print(f"Database error: {e}")

    def fetch_events(self):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()
                # Fetch events scheduled for today or later
                query = """
                    SELECT ID, eventName, date
                    FROM Events
                    WHERE date >= ?
                    ORDER BY date
                """
                cursor.execute(query, QDate.currentDate().toString("yyyy-MM-dd"))
                return cursor.fetchall()
        except pyodbc.Error as e:
            print(f"Database error: {e}")
            return []

    def populate_event_combobox(self):
        # Fetch events from the database
        allevents = self.fetch_events()

        # Populate the ComboBox with event names
        self.current_ui.events.clear()
        for event_id, event_name, event_date in allevents:
            self.current_ui.events.addItem(
                f"{event_name} - {event_date}", userData=event_id
            )

        # Trigger the update_event_details function for the first item in the ComboBox
        if self.current_ui.events.count() > 0:
            self.update_event_details(0)

    def update_event_details(self, index):
        # Get the selected event ID from the ComboBox userData
        selected_event_id = self.current_ui.events.itemData(index)

        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()
                # Fetch details of the selected event
                query = """
                    SELECT eventName, date
                    FROM Events
                    WHERE ID = ?
                """
                cursor.execute(query, selected_event_id)
                event_details = cursor.fetchone()

                if event_details:
                    self.ticket = self.fetch_ticket(selected_event_id)
                    if self.ticket:
                        # Display event details in the labels
                        event_name, event_date = event_details
                        self.current_ui.eventName.setText(str(event_name))
                        self.current_ui.eventDate.setText(str(event_date))
                        self.current_ui.price.setText(f"PKR: {str(self.ticket.cost)}")
                    else:
                        self.current_ui.price.setText("Tickets are Sold Out")

        except pyodbc.Error as e:
            print(f"Database error: {e}")

    def fetch_ticket(self, event_id):
        try:
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()
                query_tickets = """
                    SELECT ticketID, cost
                    FROM EventTickets
                    WHERE eventID = ? AND boughtBy IS NULL
                """
                cursor.execute(query_tickets, event_id)
                ticket = cursor.fetchone()
                return ticket

        except pyodbc.Error as e:
            print(f"Database error: {e}")

    def process_buy_transaction(self):
        # Get the selected event ID from the ComboBox userData
        selected_event_id = self.current_ui.events.currentData()
        if self.ticket:
            # Get the ticket cost from the QLabel text
            ticket_cost = self.ticket.cost
            # Check if the user has sufficient balance
            if self.balance < ticket_cost:
                self.current_ui.errorLabel.setText(
                    "Insufficient Balance! You do not have sufficient balance."
                )
                return

            try:
                with pyodbc.connect(connection_string) as connection:
                    cursor = connection.cursor()

                    query_deduct_balance = f"""
                        UPDATE {self.table}
                        SET balance = balance - ?
                        WHERE ID = ?
                    """
                    cursor.execute(query_deduct_balance, ticket_cost, self.user)

                    # Update the balance in the Events table
                    query_update_balance = """
                        UPDATE Events
                        SET balance = balance + ?
                        WHERE ID = ?
                    """
                    cursor.execute(query_update_balance, ticket_cost, selected_event_id)

                    # Record the transaction in the IntraTransaction table
                    t = time.localtime()
                    current_time = time.strftime("%H:%M:%S", t)
                    query_record_transaction = """
                        INSERT INTO IntraTransaction ([from], [to], amount, purpose, date, time)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """
                    cursor.execute(
                        query_record_transaction,
                        self.user,
                        selected_event_id,
                        ticket_cost,
                        "Ticket Purchase",
                        date.today(),
                        current_time,
                    )

                    query_update_ticket = """
                            UPDATE EventTickets
                            SET boughtBy = ?
                            WHERE ticketID = ? AND eventID = ?;"""
                    cursor.execute(
                        query_update_ticket,
                        self.user,
                        self.ticket.ticketID,
                        selected_event_id,
                    )
                    # Commit the transaction
                    connection.commit()

                    # Display success message
                    self.current_ui.successLabel.setText(
                        "Transaction Successful! Ticket purchase successful."
                    )

            except pyodbc.Error as e:
                print(f"Database error: {e}")
        else:
            self.current_ui.errorLabel.setText("No tickets Available")


def main():
    app = QApplication(sys.argv)
    window = MyApplication()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
