CREATE DATABASE CampusPay;
go

-- Create Admin Table
CREATE TABLE Admin (
    admin_id NCHAR(4) PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    fName VARCHAR(255),
    mName VARCHAR(255),
    IName VARCHAR(255),
    address VARCHAR(255),
    dob DATE
);

-- Insert into Admin Table
INSERT INTO Admin (admin_id, email, password, fName, mName, IName, address, dob)
VALUES
    ('A001', 'admin@example.com', 'adminpassword', 'Admin', NULL, 'User', '123 Admin St', '1980-10-20'),
    ('A002', 'admin2@example.com', 'adminpassword2', 'Super', NULL, 'Admin', '456 Admin Blvd', '1975-08-12'),
    ('A003', 'admin3@example.com', 'adminpassword3', 'System', NULL, 'Admin', '789 Admin Ave', '1988-03-25'),
    ('A004', 'admin4@example.com', 'adminpassword4', 'Network', NULL, 'Admin', '101 Admin Lane', '1972-06-30'),
    ('A005', 'admin5@example.com', 'adminpassword5', 'Database', NULL, 'Admin', '202 Admin Road', '1990-12-15'),
    ('A006', 'admin6@example.com', 'adminpassword6', 'Security', NULL, 'Admin', '303 Admin Circle', '1984-04-05');

-- Create ServiceProvider Table
CREATE TABLE ServiceProvider (
    srID NCHAR(5) PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    Name VARCHAR(255),
    address VARCHAR(255),
    service VARCHAR(255),
    balance FLOAT,
    QR VARCHAR(255),
    link VARCHAR(255)
);

-- Insert into ServiceProvider Table
INSERT INTO ServiceProvider (srID, email, password, Name, address, service, balance, QR, link)
VALUES
    ('S0001', 'service1@example.com', 'servicepassword', 'Service Provider 1', '123 Service St', 'Service A', 500.00, 'image3.jpg', 'http://serviceprovider1.com'),
    ('S0002', 'service2@example.com', 'servicepassword2', 'Service Provider 2', '456 Service St', 'Service B', 800.00, 'image4.jpg', 'http://serviceprovider2.com'),
    ('S0003', 'service3@example.com', 'servicepassword3', 'Service Provider 3', '789 Service Blvd', 'Service C', 1200.00, 'image5.jpg', 'http://serviceprovider3.com'),
    ('S0004', 'service4@example.com', 'servicepassword4', 'Service Provider 4', '101 Service Ave', 'Service D', 1500.00, 'image6.jpg', 'http://serviceprovider4.com'),
    ('S0005', 'service5@example.com', 'servicepassword5', 'Service Provider 5', '202 Service Lane', 'Service E', 2000.00, 'image7.jpg', 'http://serviceprovider5.com'),
    ('S0006', 'service6@example.com', 'servicepassword6', 'Service Provider 6', '303 Service Road', 'Service F', 1800.00, 'image8.jpg', 'http://serviceprovider6.com');

-- Create UtUTransaction Table
CREATE TABLE UtUTransaction (
    transactionID VARCHAR(255) PRIMARY KEY,
    fromUser VARCHAR(255),
    toUser VARCHAR(255),
    receipt VARCHAR(255),
    amount FLOAT,
    purpose VARCHAR(255)
);

-- Insert into UtUTransaction Table
INSERT INTO UtUTransaction (transactionID, fromUser, toUser, receipt, amount, purpose)
VALUES
    ('trans1', 'user1', 'user2', 'receipt1.jpg', 50.00, 'Payment for services'),
    ('trans2', 'user2', 'user1', 'receipt2.jpg', 30.00, 'Repayment'),
    ('trans3', 'user3', 'user1', 'receipt3.jpg', 70.00, 'Shared expenses'),
    ('trans4', 'user4', 'user2', 'receipt4.jpg', 25.00, 'Gift'),
    ('trans5', 'user5', 'user3', 'receipt5.jpg', 60.00, 'Loan repayment'),
    ('trans6', 'user6', 'user4', 'receipt6.jpg', '40.00', 'Dinner payment');

-- Create Donation Table
CREATE TABLE Donation (
    donationID NCHAR(10) PRIMARY KEY,
    fromUser VARCHAR(255),
    toDD NCHAR(7),
    receipt VARCHAR(255),
    amount FLOAT,
    purpose VARCHAR(255)
);

-- Insert into Donation Table
INSERT INTO Donation (donationID, fromUser, toDD, receipt, amount, purpose)
VALUES
    ('D000000001', 'user1', 'DD0001', 'donation_receipt1.jpg', 30.00, 'Charity'),
    ('D000000002', 'user2', 'DD0001', 'donation_receipt2.jpg', 20.00, 'Support'),
    ('D000000003', 'user3', 'DD0002', 'donation_receipt3.jpg', 40.00, 'Disaster relief'),
    ('D000000004', 'user4', 'DD0002', 'donation_receipt4.jpg', 25.00, 'Education'),
    ('D000000005', 'user5', 'DD0003', 'donation_receipt5.jpg', 60.00, 'Healthcare'),
    ('D000000006', 'user6', 'DD0003', 'donation_receipt6.jpg', 35.00, 'Animal welfare');

-- Create IBFTInTransaction Table
CREATE TABLE IBFTInTransaction (
    transactionID VARCHAR(255) PRIMARY KEY,
    fromIBAN NCHAR(24),
    toUser VARCHAR(255),
    purpose VARCHAR(255),
    amount FLOAT
);

-- Insert into IBFTInTransaction Table
INSERT INTO IBFTInTransaction (transactionID, fromIBAN, toUser, purpose, amount)
VALUES
    ('IBFTInTrans1', 'IBAN9876543210987654321098', 'user1', 'IBFT payment', 75.00),
    ('IBFTInTrans2', 'IBAN8765432109876543210987', 'user2', 'IBFT transfer', 120.00),
    ('IBFTInTrans3', 'IBAN7654321098765432109876', 'user3', 'IBFT settlement', 50.00),
    ('IBFTInTrans4', 'IBAN6543210987654321098765', 'user4', 'IBFT contribution', 80.00),
    ('IBFTInTrans5', 'IBAN5432109876543210987654', 'user5', 'IBFT repayment', 30.00),
    ('IBFTInTrans6', 'IBAN4321098765432109876543', 'user6', 'IBFT transfer', 100.00);
    
 CREATE TABLE mobileTopup (
    transactionID VARCHAR(255) PRIMARY KEY,
    fromUser VARCHAR(255),
    toPhNum NCHAR(11),
    amount FLOAT
);

-- Insert into mobileTopup Table
INSERT INTO mobileTopup (transactionID, fromUser, toPhNum, amount)
VALUES
    ('topup1', 'user1', '12345678901', 20.00),
    ('topup2', 'user2', '98765432109', 15.00),
    ('topup3', 'user3', '87654321098', 30.00),
    ('topup4', 'user4', '23456789012', 25.00),
    ('topup5', 'user5', '34567890123', 50.00),
    ('topup6', 'user6', '45678901234', 40.00);

-- Create SP_withdraw_transaction Table
CREATE TABLE SP_withdraw_transaction (
    transactionID VARCHAR(255) PRIMARY KEY,
    fromSP NCHAR(5),
    toIBAN NCHAR(24),
    receipt VARCHAR(255),
    amount FLOAT,
    purpose VARCHAR(255)
);

-- Insert into SP_withdraw_transaction Table
INSERT INTO SP_withdraw_transaction (transactionID, fromSP, toIBAN, receipt, amount, purpose)
VALUES
    ('withdraw1', 'S0001', 'IBAN9876543210987654321098', 'withdraw_receipt1.jpg', 50.00, 'Service payment'),
    ('withdraw2', 'S0002', 'IBAN8765432109876543210987', 'withdraw_receipt2.jpg', 30.00, 'Service fee'),
    ('withdraw3', 'S0003', 'IBAN7654321098765432109876', 'withdraw_receipt3.jpg', 70.00, 'Product purchase'),
    ('withdraw4', 'S0004', 'IBAN6543210987654321098765', 'withdraw_receipt4.jpg', 25.00, 'Consultation fee'),
    ('withdraw5', 'S0005', 'IBAN5432109876543210987654', 'withdraw_receipt5.jpg', 60.00, 'Service charge'),
    ('withdraw6', 'S0006', 'IBAN4321098765432109876543', 'withdraw_receipt6.jpg', '40.00', 'Transaction fee');

	-----------------------
	-- Create UserAcc Table
CREATE TABLE UserAcc (
    UserID VARCHAR(255) PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    balance FLOAT,
    D_O_B DATE,
    address VARCHAR(255),
    fName VARCHAR(255),
    mName VARCHAR(255),
    IName VARCHAR(255),
    QR VARCHAR(255),
    url VARCHAR(255),
    IBAN NCHAR(26) -- Increased the length to accommodate the provided example
);

-- Insert into UserAcc Table
INSERT INTO UserAcc (UserID, email, password, balance, D_O_B, address, fName, mName, IName, QR, url, IBAN)
VALUES
    ('user1', 'user1@example.com', 'password1', 1000.00, '1990-01-01', '123 Main St', 'John', 'Doe', 'JohnDoe', 'image1.jpg', 'http://example.com', 'IBAN12345678901234567890'),
    ('user2', 'user2@example.com', 'password2', 1500.00, '1985-04-15', '456 Oak St', 'Jane', NULL, 'Smith', 'image2.jpg', 'http://example.com/user2', 'IBAN23456789012345678901'),
    ('user3', 'user3@example.com', 'password3', 2000.00, '1992-07-22', '789 Pine St', 'Michael', 'A', 'Johnson', 'image3.jpg', 'http://example.com/user3', 'IBAN34567890123456789012'),
    ('user4', 'user4@example.com', 'password4', 800.00, '1988-11-10', '101 Cedar St', 'Emily', 'B', 'Clark', 'image4.jpg', 'http://example.com/user4', 'IBAN45678901234567890123'),
    ('user5', 'user5@example.com', 'password5', 1200.00, '1995-03-03', '202 Maple St', 'Daniel', NULL, 'Adams', 'image5.jpg', 'http://example.com/user5', 'IBAN56789012345678901234'),
    ('user6', 'user6@example.com', 'password6', 1600.00, '1987-08-18', '303 Elm St', 'Olivia', 'C', 'Turner', 'image6.jpg', 'http://example.com/user6', 'IBAN67890123456789012345');

-- Create IBFTOutTransaction Table
CREATE TABLE IBFTOutTransaction (
    transactionID VARCHAR(255) PRIMARY KEY,
    fromUser VARCHAR(255),
    toIBAN VARCHAR(26), -- Increased the length to accommodate the provided example
    purpose VARCHAR(255),
    amount FLOAT,
    tax FLOAT
);

-- Insert into IBFTOutTransaction Table
INSERT INTO IBFTOutTransaction (transactionID, fromUser, toIBAN, purpose, amount, tax)
VALUES
    ('IBFTTrans1', 'user1', 'IBAN98765432109876543210', 'IBFT payment', 75.00, 5.00),
    ('IBFTTrans2', 'user2', 'IBAN87654321098765432109', 'IBFT transfer', 120.00, 8.00),
    ('IBFTTrans3', 'user3', 'IBAN76543210987654321098', 'IBFT settlement', 50.00, 3.00),
    ('IBFTTrans4', 'user4', 'IBAN65432109876543210987', 'IBFT contribution', 80.00, 6.00),
    ('IBFTTrans5', 'user5', 'IBAN54321098765432109876', 'IBFT repayment', 30.00, 2.00),
    ('IBFTTrans6', 'user6', 'IBAN43210987654321098765', 'IBFT transfer', 100.00, 7.00);

-- Create DonationDrive Table
CREATE TABLE DonationDrive (
    ddID INTEGER PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    name VARCHAR(255),
    purpose VARCHAR(255)
);

-- Insert into DonationDrive Table
INSERT INTO DonationDrive (ddID, email, password, name, purpose)
VALUES
    (1, 'drive1@example.com', 'drivepassword', 'Charity Drive 1', 'Supporting a cause'),
    (2, 'drive2@example.com', 'drivepassword2', 'Helping Hands Campaign', 'Community assistance'),
    (3, 'drive3@example.com', 'drivepassword3', 'Hope for Tomorrow', 'Education and healthcare support'),
    (4, 'drive4@example.com', 'drivepassword4', 'Green Earth Initiative', 'Environmental conservation'),
    (5, 'drive5@example.com', 'drivepassword5', 'Caring Hearts Project', 'Aid for the needy'),
    (6, 'drive6@example.com', 'drivepassword6', 'Sustainable Futures', 'Promoting sustainability');