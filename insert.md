# Insert Operations for Bike Rental System Tables

## Models Table
```sql
INSERT INTO Models (Model_Name, Manufacturer, Year)
VALUES ('Ninja 300', 'Kawasaki', 2021),
    
INSERT INTO Models (Model_Name, Manufacturer, Year)
VALUES ('CBR1000RR', 'Honda', 2022);

INSERT INTO Models (Model_Name, Manufacturer, Year)
VALUES ('R1250GS', 'BMW', 2020);

INSERT INTO Models (Model_Name, Manufacturer, Year)
VALUES ('YZF-R1', 'Yamaha', 2023);

INSERT INTO Models (Model_Name, Manufacturer, Year)
VALUES ('Panigale V4', 'Ducati', 2021);


## customer
INSERT INTO Customers (Customer_Name, Contact_Number, Email)
VALUES ('honey', 3167305763, 'honey@gmail.com');

INSERT INTO Customers (Customer_Name, Contact_Number, Email)
VALUES ('konidela', 8784908456, 'konidela@gmail.com');

INSERT INTO Customers (Customer_Name, Contact_Number, Email)
VALUES ('daggupati', 2345637890, 'daggupati@gmail.com');

INSERT INTO Customers (Customer_Name, Contact_Number, Email)
VALUES ('kiran', 2938388905, 'kiran@gmail.com');

INSERT INTO Customers (Customer_Name, Contact_Number, Email)
VALUES ('william', 48764785644, 'illiam34@gamil.com');

#Bike Table
INSERT INTO Bikes (Bike_Name, Model_ID, Daily_Rental_Rate)
VALUES ('Boss Hoss Cycles', 14, 'Available', 45.00);
    

INSERT INTO Bikes (Bike_Name, Model_ID, Daily_Rental_Rate)
VALUES ('Suzuki Hayabusa', 5, 'Available', 60.00);
    
INSERT INTO Bikes (Bike_Name, Model_ID, Daily_Rental_Rate)
VALUES ('Harley-Davidson Sportster', 8, 'Available', 55.00);
    
INSERT INTO Bikes (Bike_Name, Model_ID, Daily_Rental_Rate)
VALUES ('Kawasaki Z900', 2, 'Available', 50.00);
    

INSERT INTO Bikes (Bike_Name, Model_ID, Daily_Rental_Rate)
VALUES ('Ducati Monster', 3, 'Available', 65.00);


## Rental table
INSERT INTO Rental (Bike_ID, Customer_ID, Rent_Start_Date, Rent_End_Date, Total_Cost)
VALUES (8, 6, '2023-11-24', '2023-01-20', 1620);

INSERT INTO Rental (Bike_ID, Customer_ID, Rent_Start_Date, Rent_End_Date, Total_Cost)
VALUES (18, 5, '2023-11-19', '2023-11-22', 144);

INSERT INTO Rental (Bike_ID, Customer_ID, Rent_Start_Date, Rent_End_Date, Total_Cost)
VALUES (26247, 2, '2023-03-05', '2023-03-10', 246);

INSERT INTO Rental (Bike_ID, Customer_ID, Rent_Start_Date, Rent_End_Date, Total_Cost)
VALUES (9, 1, '2023-1-22', '2023-11-30', 55);

INSERT INTO Rental (Bike_ID, Customer_ID, Rent_Start_Date, Rent_End_Date, Total_Cost)
VALUES (16, 4, '2023-1-22', '2023-05-30', 360);