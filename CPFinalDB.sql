CREATE DATABASE CampusPay;

-- Create UserAcc table
CREATE TABLE UserAcc (
    ID VARCHAR(10) PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    balance DECIMAL(10, 2) DEFAULT 0,
    D_O_B DATE,
    address VARCHAR(255),
    fName VARCHAR(255),
    mName VARCHAR(255),
    lName VARCHAR(255),
    QR VARCHAR(255),
    url VARCHAR(255),
    IBAN VARCHAR(26)
);

-- Create Admin table
CREATE TABLE Admin (
    ID VARCHAR(10) PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    fName VARCHAR(255),
    mName VARCHAR(255),
    lName VARCHAR(255),
    address VARCHAR(255),
    dob DATE
);

-- Create ServiceProvider table
CREATE TABLE ServiceProvider (
    ID VARCHAR(10) PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    Name VARCHAR(255),
    address VARCHAR(255),
    service VARCHAR(255),
    balance DECIMAL(10, 2) DEFAULT 0,
    QR VARCHAR(255),
    link VARCHAR(255)
);

-- Create IntraTransaction table
CREATE TABLE IntraTransaction (
    transactionID INT IDENTITY(1,1) PRIMARY KEY,
    transactionID_VARCHAR AS 'IT' + RIGHT('00000' + CAST(transactionID AS VARCHAR(5)), 5),
    [from] VARCHAR(10),
    [to] VARCHAR(10),
    receipt VARCHAR(255),
    amount DECIMAL(10, 2),
    purpose VARCHAR(255),
    promotionID VARCHAR(10) NULL,
    date DATE,
    time TIME
);

-- Create IBFTOutTransaction table
CREATE TABLE IBFTOutTransaction (
    transactionID INT IDENTITY(1,1) PRIMARY KEY,
    transactionID_VARCHAR AS 'IO' + RIGHT('00000' + CAST(transactionID AS VARCHAR(5)), 5),
    [from] VARCHAR(10),
    toIBAN VARCHAR(26),
    purpose VARCHAR(255),
    amount DECIMAL(10, 2),
    tax DECIMAL(5, 2),
    date DATE,
    time TIME
);

-- Create DonationDrive table
CREATE TABLE DonationDrive (
    ID VARCHAR(10) PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    name VARCHAR(255),
    purpose VARCHAR(255),
    balance DECIMAL(10, 2) DEFAULT 0
);

-- Create Coupons table
CREATE TABLE Coupons (
    CouponID VARCHAR(10) PRIMARY KEY,
    amount DECIMAL(10, 2),
    isUsed BIT,
    usedBy VARCHAR(10)
);

-- Create mobileTopup table
CREATE TABLE mobileTopup (
    transactionID   INT IDENTITY(1,1) PRIMARY KEY,
    transactionID_VARCHAR AS 'MT' + RIGHT('00000' + CAST(transactionID AS VARCHAR(5)), 5),
    [from] VARCHAR(10),
    toPhNum VARCHAR(10),
    amount DECIMAL(10, 2) ,
    date DATE,
    time TIME
);

-- Create StudentEmployer table
CREATE TABLE StudentEmployer (
    ID VARCHAR(10) PRIMARY KEY,
    name VARCHAR(255),
    IBAN VARCHAR(26),
    balance DECIMAL(10, 2) DEFAULT 0
);

-- Create Events table
CREATE TABLE Events (
    ID VARCHAR(10) PRIMARY KEY,
    eventName VARCHAR(255),
    ticketsCap INT,
    date DATE,
    password VARCHAR(255),
    registrationURL VARCHAR(255),
    balance DECIMAL(10, 2) DEFAULT 0
);

-- Create Promotions table
CREATE TABLE Promotions (
    promotionID INT IDENTITY (1,1) PRIMARY KEY,
    description VARCHAR(255),
    startTime TIME,
    endTime TIME,
    [discount%] DECIMAL(5, 2),
    category VARCHAR(255),
    isactive BIT,
    serviceProvider VARCHAR(10),
    start_date DATE,
    end_date DATE
);

-- Create EventTickets table
CREATE TABLE EventTickets(
    eventID VARCHAR(10),
    ticketID VARCHAR(10),
    cost DECIMAL(10, 2),
    boughtBy VARCHAR(10),
    CONSTRAINT PK_EventTicket PRIMARY KEY (eventID, ticketID)
);


INSERT INTO UserAcc (ID, email, password, balance, D_O_B, address, fName, mName, lName, QR, url, IBAN)
VALUES
  ('JA6891', 'john.adam@habib.edu.pk', 'thuiaheas67.', 7500.00, '1990-01-15', '123 Main St', 'John', 'Doe', 'Adams', 'user1_qr_image.jpg', 'https://user1website.com', 'US12345678901234567890123'),
  ('MJ2358', 'mary.jane@habib.edu.pk', '3r5fh2ghas!', 12000.00, '1985-05-20', '456 Oak St', 'Mary', NULL, 'Jane', 'user2_qr_image.jpg', 'https://user2website.com', 'US98765432109876543210987'),
  ('SJ9087', 'susan.jones@habib.edu.pk', 's7d8gha1s0!', 5000.00, '1992-08-10', '789 Elm St', 'Susan', 'Marie', 'Jones', 'user3_qr_image.jpg', 'https://user3website.com', 'US65432109876543210987654'),
  ('EM5672', 'eric.miller@habib.edu.pk', '2h38sklf!', 8000.00, '1988-03-25', '101 Pine St', 'Eric', NULL, 'Miller', 'user4_qr_image.jpg', 'https://user4website.com', 'US34567890123456789012345'),
  ('MJ1209', 'michelle.johnson@habib.edu.pk', 'ksd8f2ja5l!', 16000.00, '1995-11-05', '202 Cedar St', 'Michelle', 'Ann', 'Johnson', 'user5_qr_image.jpg', 'https://user5website.com', 'US56789012345678901234567'),
  ('SO7895', 'sophie.owen@habib.edu.pk', 'fgh23klj42!', 2000.00, '1980-07-18', '303 Maple St', 'Sophie', NULL, 'Owen', 'user6_qr_image.jpg', 'https://user6website.com', 'US09876543210987654321098'),
  ('DD3210', 'daniel.doe@habib.edu.pk', '6fg73lksd2!', 18000.00, '1993-04-12', '404 Birch St', 'Daniel', 'Robert', 'Doe', 'user7_qr_image.jpg', 'https://user7website.com', 'US87654321098765432109876'),
  ('OS2345', 'olivia.smith@habib.edu.pk', '72jk3lfs92!', 8500.00, '1986-09-30', '505 Walnut St', 'Olivia', NULL, 'Smith', 'user8_qr_image.jpg', 'https://user8website.com', 'US23456789012345678901234'),
  ('EJ6789', 'ethan.james@habib.edu.pk', '0dfgj39ksa!', 11000.00, '1998-02-22', '606 Pine St', 'Ethan', 'James', 'Evans', 'user9_qr_image.jpg', 'https://user9website.com', 'US67890123456789012345678'),
  ('AT0123', 'ava.taylor@habib.edu.pk', '1ja02l3njk!', 20000.00, '1983-06-08', '707 Oak St', 'Ava', NULL, 'Taylor', 'user10_qr_image.jpg', 'https://user10website.com', 'US01234567890123456789012');


-- Admin table with random alphanumeric passwords
INSERT INTO Admin (ID, email, password, fName, mName, lName, address, dob)
VALUES
  ('AJ1001', 'alice.joffrey@habib.edu.pk', 'Hx7rpZuGqE', 'Alice', NULL, 'Joffrey', '123 Admin St', '1975-08-15'),
  ('BH1002', 'bob.harrison@habib.edu.pk', 'y6sKv9nF4a', 'Bob', NULL, 'Harrison', '456 Admin St', '1980-03-22'),
  ('CS1003', 'carol.smith@habib.edu.pk', 'Z3pU8jX2wQ', 'Carol', NULL, 'Smith', '789 Admin St', '1985-11-10'),
  ('DW1004', 'david.white@habib.edu.pk', 'G9sR2vQ3pL', 'David', NULL, 'White', '101 Admin St', '1990-06-25'),
  ('EM1005', 'emma.martin@habib.edu.pk', 'A5mH8nK4oU', 'Emma', NULL, 'Martin', '202 Admin St', '1995-01-08');

INSERT INTO Events (ID, [password], eventName, ticketsCap, date, registrationURL, balance)
VALUES
  ('PHE1001','PHE1001','PHEC', 500, '2023-01-15', 'https://phec.com/register', 5000.00),
  ('MUF1002','MUF1002','Music Festival', 1000, '2023-02-20', 'https://musicfest.com/register', 8000.50),
  ('CNV1003','CNV1003', 'Carnival', 300, '2023-03-25', 'https://hucarnival.com/register', 3500.75),
  ('AEX1004','AEX1004','Art Exhibition', 200, '2023-04-10', 'https://artexpo.com/register', 2500.25),
  ('SPT1005','SPT1005', 'Sports Tournament', 800, '2023-05-05', 'https://sportstourney.com/register', 6000.00),
  ('CTD1006','CTD1006','Cultural Day', 400, '2023-06-10', 'https://culturalfair.com/register', 4500.75),
  ('CON1007','CON1007', 'HUCON', 600, '2023-07-15', 'https://HUCON.com/register', 5500.50),
  ('SCF1008','SCF1008', 'Science Fair', 250, '2023-08-20', 'https://sciencefair.com/register', 3000.25),
  ('EHU1009','EHU1009','Eat Habib', 700, '2023-09-25', 'https://eathabib.com/register', 7000.00),
  ('CTG1010','CTG1010','Charity Gala', 150, '2023-10-30', 'https://charitygala.com/register', 4000.75);

-- ServiceProvider table with random alphanumeric passwords
INSERT INTO ServiceProvider (ID, email, password, Name, address, service, balance, QR, link)
VALUES
  ('TC1001', 'tapal.cafeteria@habib.edu.pk', 'Hx7rpZuGqE', 'Tapal Cafeteria', 'Main Cafeteria, Habib University', 'Cafeteria Services', 5000.00, 'tapal_cafeteria_qr_image.jpg', 'https://tapalcafeteria.com'),
  ('C2G1002', 'cafe2go@habib.edu.pk', 'y6sKv9nF4a', 'Cafe2Go', 'Student Center, Habib University', 'Cafe Services', 8000.50, 'cafe2go_qr_image.jpg', 'https://cafe2go.com'),
  ('HUD1003', 'habib.dukaan@habib.edu.pk', 'Z3pU8jX2wQ', 'Habib Dukaan', 'Habib Mall, Habib University', 'General Store', 3500.75, 'habib_dukaan_qr_image.jpg', 'https://habibdukaan.com'),
  ('GJB1004', 'gritto.juicebar@habib.edu.pk', 'G9sR2vQ3pL', 'Gritto Juice Bar', 'Student Center, Habib University', 'Juice Bar', 2500.25, 'gritto_juicebar_qr_image.jpg', 'https://grittojuicebar.com'),
  ('DHB1005', 'dhaba@habib.edu.pk', 'A5mH8nK4oU', 'Dhaba', 'Habib Mall, Habib University', 'Dhaba Services', 6000.00, 'dhaba_qr_image.jpg', 'https://dhaba.com'),
  ('RHB1006', 'raheem.bhai@habib.edu.pk', 'V8eS3tN7pM', 'Raheem Bhai', 'Main Cafeteria, Habib University', 'Fast Food', 4500.75, 'raheem_bhai_qr_image.jpg', 'https://raheembhai.com'),
  ('SWR1007', 'shawarma@habib.edu.pk', 'C1oU4gA9jH', 'Shawarma', 'Student Center, Habib University', 'Shawarma Services', 5500.50, 'shawarma_qr_image.jpg', 'https://shawarma.com'),
  ('HOB1008', 'hobnob@habib.edu.pk', 'N5mH1oB8nU', 'Hobnob', 'Habib Mall, Habib University', 'Bakery', 3000.25, 'hobnob_qr_image.jpg', 'https://hobnob.com');



INSERT INTO Promotions ([description], startTime, endTime, [discount%], category, isactive, serviceProvider, [start_date], end_date)
VALUES
  ('Tech Expo Promo', '09:00:00', '14:00:00', 10.25, 'Mobile Accessories', 'true', 'S0004', '2023-03-01', '2023-03-15'),
  ('Spring Sale', '12:00:00', '18:00:00', 30.00, 'Flowers', 'true', 'S0007', '2023-04-01', '2023-04-15'),
  ('Back to University', '08:30:00', '13:30:00', 25.75, 'Fries', 'true', 'S0008', '2023-05-01', '2023-05-10'),
  ('Summer Discount', '11:00:00', '16:00:00', 15.50, 'Swimming Gear', 'true', 'S0005', '2023-06-01', '2023-06-15'),
  ('Independence Day Sale', '10:00:00', '15:00:00', 18.75, 'Flags', 'true', 'S0006', '2023-07-01', '2023-07-10'),
  ('Labor Day Special', '09:30:00', '14:30:00', 22.00, 'Dukaan Specials', 'true', 'S0009', '2023-08-01', '2023-08-15'),
  ('Fall Savings', '12:00:00', '17:00:00', 12.25, 'HU Merch', 'true', 'S0010', '2023-09-01', '2023-09-10'),
  ('Golden Savings off Golden Hour', '14:30:00', '15:30:00', 50, 'Fresh Juices', 'true', 'S0002', '2023-10-01', '2023-10-15');


INSERT INTO mobileTopup ([from], toPhNum, amount, date, time)
VALUES
  ('JA6891', '1234567890', 500.00, '2023-01-15', '11:15:00'),
  ('AT0123', '9876543210', 999, '2023-02-20', '14:30:00'),
  ('SJ9087', '2345678901', 1200, '2023-03-25', '09:45:00'),
  ('MJ2358', '3456789012', 650, '2023-04-10', '16:00:00'),
  ('SO7895', '4567890123', 2000, '2023-05-05', '12:30:00'),
  ('MJ1209', '5678901234', 40, '2023-06-10', '17:45:00'),
  ('SJ9087', '6789012345', 720, '2023-07-15', '10:00:00'),
  ('EM5672', '7890123456', 1600, '2023-08-20', '14:15:00'),
  ('MJ2358', '8901234567', 2500, '2023-09-25', '11:30:00'),
  ('EM5672', '9012345678', 5000, '2023-10-30', '13:45:00');

-- DonationDrive table with random alphanumeric passwords
INSERT INTO DonationDrive (ID, email, password, name, purpose, balance)
VALUES
  ('LDL1001', 'labourers.donation@habib.edu.pk', 'X5cJ9zH1bN', 'Labourers Donation Drive', 'Support underprivileged labourers and helpers', 12000.00),
  ('SFS1002', 'students.fees@habib.edu.pk', 'V3gH9pZ7dQ', 'Students Fees Support', 'Aid students in financial need for education fees', 8000.50),
  ('BRD1003', 'bikes.relief@habib.edu.pk', 'K8mS2nA4oE', 'Bikes Relief Drive', 'Provide mode of transport (bikes) for laborers', 15000.75),
  ('CFA1004', 'current.affairs@habib.edu.pk', 'M4gH9oN5bX', 'Current Affairs Relief', 'Support current affairs relief efforts (e.g., flood relief, Palestine)', 5000.25),
  ('HFL1005', 'helping.families@habib.edu.pk', 'N2pL6bR7wE', 'Helping Families Drive', 'Assist families in need with financial and essential support', 10000.50),
  ('CHE1006', 'children.education@habib.edu.pk', 'G9jR4kN8pZ', 'Children Education Support', 'Support education for underprivileged children', 7000.00),
  ('HMR1007', 'home.repair@habib.edu.pk', 'D6iH8xN3qM', 'Home Repair Drive', 'Help repair and improve living conditions for families', 8500.75),
  ('MOT1008', 'medical.aid@habib.edu.pk', 'A1sD4fG2hJ', 'Medical Aid Drive', 'Provide financial aid for medical treatments and expenses', 12000.25);

-- StudentEmployer table with random alphanumeric IBANs and balances
INSERT INTO StudentEmployer (ID, name, IBAN, balance)
VALUES
  ('STE1001', 'Teaching Assistant Department', 'PKR12345678901234567890123', 5000.00),
  ('STE1002', 'Marketing Department', 'PKR23456789012345678901234', 6500.50),
  ('STE1003', 'Library Assistant', 'PKR34567890123456789012345', 4800.75),
  ('STE1004', 'Freshman Orientation Leaders', 'PKR45678901234567890123456', 7200.25),
  ('STE1005', 'Clubs and Society Management', 'PKR56789012345678901234567', 5500.50);

-- IntraTransaction involving users and service providers
INSERT INTO IntraTransaction ([from], [to], receipt, amount, purpose, promotionID, date, time)
VALUES
  ('JA6891', 'TC1001', '', 1200.75, 'Payment for food purchased', NULL, '2023-04-15', '12:00:00'),
  ('MJ2358', 'DHB1005', '', 500.00, 'Dhaba Services', NULL, '2023-04-16', '14:30:00'),
  ('SJ9087', 'C2G1002', '', 1000.50, 'Cafe2Go Purchase', NULL, '2023-04-17', '10:45:00'),
  ('EM5672', 'GJB1004', '', 250.25, 'Juice Bar Refreshment', NULL, '2023-04-18', '16:20:00'),
  ('MJ1209', 'SWR1007', '', 750.00, 'Shawarma Meal', NULL, '2023-04-19', '13:15:00');

-- IntraTransaction involving users and donation drives
INSERT INTO IntraTransaction ([from], [to], receipt, amount, purpose, promotionID, date, time)
VALUES
  ('SO7895', 'BRD1003', '', 2000.00, 'Donation for Bikes Relief Drive', NULL, '2023-04-20', '11:00:00'),
  ('DD3210', 'SFS1002', '', 1500.75, 'Support for Students Fees Drive', NULL, '2023-04-21', '15:45:00'),
  ('OS2345', 'MOT1008', '', 1200.25, 'Medical Aid Support', NULL, '2023-04-22', '09:30:00'),
  ('EJ6789', 'LDL1001', '', 1000.50, 'Support for Labourers Donation Drive', NULL, '2023-04-23', '12:30:00'),
  ('AT0123', 'CHE1006', '', 1800.00, 'Children Education Fund', NULL, '2023-04-24', '14:00:00');

-- IntraTransaction for employment wages
INSERT INTO IntraTransaction ([from], [to], receipt, amount, purpose, promotionID, date, time)
VALUES
  ('STE1001', 'JA6891', '', 500.00, 'Teaching Assistant Salary', NULL, '2023-04-25', '16:30:00'),
  ('STE1002', 'MJ2358', '', 650.50, 'Marketing Department Wages', NULL, '2023-04-26', '11:45:00'),
  ('STE1003', 'SJ9087', '', 480.75, 'Library Assistant Salary', NULL, '2023-04-27', '14:15:00'),
  ('STE1004', 'EM5672', '', 720.25, 'Orientation Leaders Payment', NULL, '2023-04-28', '10:00:00'),
  ('STE1005', 'MJ1209', '', 550.50, 'Clubs and Society Management Wages', NULL, '2023-04-29', '12:45:00');

-- IntraTransaction for stationery purchase
INSERT INTO IntraTransaction ([from], [to], receipt, amount, purpose, promotionID, date, time)
VALUES
  ('JA6891', 'HUD1003', 'DUK-STNRY-20230425', 350.00, 'Stationery Purchase', NULL, '2023-04-25', '14:00:00');


INSERT INTO IBFTOutTransaction ([from], toIBAN, purpose, amount, tax, date, time)
VALUES
  ('SO7895', 'PKR98765432109876543210987', 'Rent Payment', 1200.00, 3.00, '2023-05-14', '14:30:00');


INSERT INTO IBFTOutTransaction ([from], toIBAN, purpose, amount, tax, date, time)
VALUES
  ('C2G1002', 'PKR87654321098765432109876', 'Supplier Payment', 500.75, 1.50, '2023-05-16', '12:45:00');


INSERT INTO IBFTOutTransaction ([from], toIBAN, purpose, amount, tax, date, time)
VALUES
  ('LDL1001', 'PKR76543210987654321098765', 'Labourers Donation Transfer', 1500.50, 2.00, '2023-05-18', '10:00:00');

INSERT INTO IBFTOutTransaction ([from], toIBAN, purpose, amount, tax, date, time)
VALUES
  ('STE1001', 'PKR65432109876543210987654', 'Teaching Assistant Salary', 800.25, 1.00, '2023-05-20', '15:30:00');

INSERT INTO IBFTOutTransaction ([from], toIBAN, purpose, amount, tax, date, time)
VALUES
  ('HUCON', 'PKR54321098765432109876543', 'Event Ticket Sales', 3000.00, 5.00, '2023-05-22', '13:00:00');

INSERT INTO IBFTOutTransaction ([from], toIBAN, purpose, amount, tax, date, time)
VALUES
  ('GJB1004', 'PKR43210987654321098765432', 'Juice Bar Supplies Payment', 700.50, 2.50, '2023-05-24', '11:45:00');

INSERT INTO IBFTOutTransaction ([from], toIBAN, purpose, amount, tax, date, time)
VALUES
  ('CHE1006', 'PKR32109876543210987654321', 'Children Education Fund Transfer', 900.75, 1.75, '2023-05-26', '09:15:00');

INSERT INTO IBFTOutTransaction ([from], toIBAN, purpose, amount, tax, date, time)
VALUES
  ('STE1005', 'PKR21098765432109876543210', 'Clubs and Society Management Salary', 600.25, 1.25, '2023-05-28', '16:45:00');

INSERT INTO Coupons (CouponID, amount, isUsed, usedBy)
VALUES
  ('CPNABC123', 1000, 'true', 'MOT1008'),
  ('CPNDEF456', 2000, 'false', NULL),
  ('CPNXYZ789', 1500, 'false', NULL),
  ('CPN123ABC', 3000, 'true', 'JA6891'),
  ('CPN456DEF', 5000, 'false', NULL),
  ('CPN789XYZ', 5500, 'false', NULL),
  ('CPNABC456', 12000, 'false', NULL),
  ('CPNDEF789', 11000, 'false', NULL),
  ('CPNXYZ123', 2500, 'true', 'MJ1209'),
  ('CPN123XYZ', 22500, 'false', NULL);

-- EventTickets table with updated ticket prices and some boughtBy values
INSERT INTO EventTickets (eventID, ticketID, cost, boughtBy)
VALUES
  ('PHE1001', 'TCK10001', 800.00, 'JA6891'),
  ('PHE1001', 'TCK10002', 950.00, NULL),
  ('PHE1001', 'TCK10003', 700.00, 'SJ9087'),
  ('PHE1001', 'TCK10004', 1200.00, 'EM5672'),
  ('PHE1001', 'TCK10005', 1100.00, 'MJ1209'),

  ('MUF1002', 'TCK20001', 1200.00, 'SO7895'),
  ('MUF1002', 'TCK20002', 800.00, 'DD3210'),
  ('MUF1002', 'TCK20003', 1000.00, 'OS2345'),
  ('MUF1002', 'TCK20004', 1300.00, NULL),
  ('MUF1002', 'TCK20005', 1400.00, 'AT0123'),

  ('CNV1003', 'TCK30001', 900.00, 'JA6891'),
  ('CNV1003', 'TCK30002', 1100.00, 'MJ2358'),
  ('CNV1003', 'TCK30003', 800.00, NULL),
  ('CNV1003', 'TCK30004', 1300.00, 'EM5672'),
  ('CNV1003', 'TCK30005', 1200.00, NULL),

  ('AEX1004', 'TCK40001', 600.00, 'SO7895'),
  ('AEX1004', 'TCK40002', 400.00, NULL),
  ('AEX1004', 'TCK40003', 500.00, 'OS2345'),
  ('AEX1004', 'TCK40004', 700.00, 'EJ6789'),
  ('AEX1004', 'TCK40005', 800.00, 'AT0123'),

  ('SPT1005', 'TCK50001', 1100.00, 'JA6891'),
  ('SPT1005', 'TCK50002', 900.00, 'MJ2358'),
  ('SPT1005', 'TCK50003', 1000.00, 'SJ9087'),
  ('SPT1005', 'TCK50004', 1200.00, 'EM5672'),
  ('SPT1005', 'TCK50005', 1300.00, 'MJ1209'),

  ('CTD1006', 'TCK60001', 600.00, 'SO7895'),
  ('CTD1006', 'TCK60002', 800.00, 'DD3210'),
  ('CTD1006', 'TCK60003', 700.00, 'OS2345'),
  ('CTD1006', 'TCK60004', 900.00, NULL),
  ('CTD1006', 'TCK60005', 1000.00, 'AT0123'),

  ('CON1007', 'TCK70001', 800.00, NULL),
  ('CON1007', 'TCK70002', 600.00, 'MJ2358'),
  ('CON1007', 'TCK70003', 700.00, 'SJ9087'),
  ('CON1007', 'TCK70004', 900.00, 'EM5672'),
  ('CON1007', 'TCK70005', 1000.00, 'MJ1209'),

  ('SCF1008', 'TCK80001', 600.00, 'SO7895'),
  ('SCF1008', 'TCK80002', 800.00, 'DD3210'),
  ('SCF1008', 'TCK80003', 700.00, 'OS2345'),
  ('SCF1008', 'TCK80004', 900.00, 'EJ6789'),
  ('SCF1008', 'TCK80005', 1000.00, 'AT0123'),

  ('EHU1009', 'TCK90001', 900.00, 'JA6891'),
  ('EHU1009', 'TCK90002', 700.00, NULL),
  ('EHU1009', 'TCK90003', 800.00, 'SJ9087'),
  ('EHU1009', 'TCK90004', 1000.00, 'EM5672'),
  ('EHU1009', 'TCK90005', 1100.00, 'MJ1209'),

  ('CTG1010', 'TCK10001', 1200.00, 'JA6891'),
  ('CTG1010', 'TCK10002', 1000.00, 'MJ2358'),
  ('CTG1010', 'TCK10003', 1100.00, 'SJ9087'),
  ('CTG1010', 'TCK10004', 1300.00, NULL),
  ('CTG1010', 'TCK10005', 1400.00, 'MJ1209');



SELECT * FROM IBFTOutTransaction;
SELECT * FROM Events;
-- Update rows in table '[TableName]' in schema '[dbo]'
UPDATE [UserAcc]
SET
  [balance] = 5500
WHERE ID = 'h270'
GO
SELECT * FROM UserAcc
SELECT * FROM IntraTransaction
UPDATE Coupons
SET isUsed = 'false', usedBy = NULL
WHERE CouponID = 'CPN789XYZ' or CouponID = 'CPN456DEF'
SELECT * FROM Coupons

/*
DROP TABLE IF EXISTS EventTickets;
DROP TABLE IF EXISTS Promotions;
DROP TABLE IF EXISTS Events;
DROP TABLE IF EXISTS StudentEmployer;
DROP TABLE IF EXISTS mobileTopup;
DROP TABLE IF EXISTS Coupons;
DROP TABLE IF EXISTS DonationDrive;
DROP TABLE IF EXISTS IBFTOutTransaction;
DROP TABLE IF EXISTS IntraTransaction;
DROP TABLE IF EXISTS ServiceProvider;
DROP TABLE IF EXISTS Admin;
DROP TABLE IF EXISTS UserAcc;
*/


SELECT * FROM UserAcc;

