# Database Schema for Bike Rental System

## Models Table
```sql
CREATE TABLE IF NOT EXISTS Models(
    Model_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Model_Name TEXT NOT NULL,
    Manufacturer TEXT NOT NULL,
    Year INTEGER
);

## Bikes
CREATE TABLE IF NOT EXISTS Bikes (
    Bike_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Bike_Name TEXT NOT NULL,
    Model_ID INTEGER,
    Bike_Status TEXT DEFAULT 'Available',
    Daily_Rental_Rate DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (Model_ID) REFERENCES Models(Model_ID)
);

## Customers table

CREATE TABLE IF NOT EXISTS Customers (
    Customer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Customer_Name TEXT NOT NULL,
    Contact_Number INTEGER,
    Email TEXT
);

## Rental Table
CREATE TABLE IF NOT EXISTS Rental(
    Rental_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Bike_ID INTEGER,
    Customer_ID INTEGER,
    Rent_Start_Date DATE,
    Rent_End_Date DATE,
    Total_Cost DECIMAL(10, 2),
    FOREIGN KEY (Bike_ID) REFERENCES Bikes(Bike_ID),
    FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID)
);
