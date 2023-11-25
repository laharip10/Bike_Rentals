# crud operations on Rental table
* SELECT * FROM Rental;
* INSERT INTO Rental (Bike_ID, Customer_ID, Rent_Start_Date, Rent_End_Date, Total_Cost) VALUES (8, 1, '2023-11-21', '2023-11-23', 120);
* UPDATE Rental SET Rent_Start_Date = '2023-11-20', Rent_End_Date = '2023-12-1'
                WHERE Rental_ID = 6578;
* DELETE FROM Rental WHERE Rental_ID = 891;

# crud operations on Bike table
* SELECT * FROM Bikes;
* INSERT INTO Bikes (Bike_ID, Bike_Name, Model_ID, Bike_Status, Daily_Rental_Rate)
            VALUES ('Ducati Monster', 3, 'Available', 65.00);
* UPDATE Bikes
            SET Bike_Name='Rieju', Model_ID=11, Daily_Rental_Rate=56
            WHERE Bike_ID=81;
* DELETE FROM Bikes WHERE Bike_ID = 11;

# crud operations on Customer table
* Select * From Customers;
* INSERT INTO Customers (Customer_Name, Contact_Number, Email) VALUES ('xiam', 48764785644, 'xiam34@gamil.com');
* UPDATE Customers
            SET Contact_Number=3567897801
            WHERE Customer_ID=8;
* DELETE FROM Customers WHERE Customer_ID = 9;

# crud operations on model table
* Select * from Models;
* INSERT INTO Models (Model_Name, Manufacturer, Year) VALUES ('Ninja 300', 'Kawasaki', 2021);
* UPDATE Models
            SET Year=2020
            WHERE Model_ID=6;
* Delete FROM Models WHERE Model_ID= 6;