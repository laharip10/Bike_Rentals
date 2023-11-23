# main.py
from datetime import datetime
from flask import Flask, render_template, request, redirect,g,url_for, jsonify
import sqlite3
import uuid
import random
from flask import render_template
app = Flask(__name__)

# Database connection helper function
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('bike_rental.db')
    return db

with app.app_context():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Models(
            Model_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Model_Name TEXT NOT NULL,
            Manufacturer TEXT NOT NULL,
            Year INTEGER
        )''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Bikes (
            Bike_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Bike_Name TEXT NOT NULL,
            Model_ID INTEGER,
            Bike_Status TEXT DEFAULT 'Available',
            Daily_Rental_Rate DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (Model_ID) REFERENCES Models(Model_ID)

        )''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            Customer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Customer_Name TEXT NOT NULL,
            Contact_Number INTEGER,
            Email TEXT
        )''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Rental(
            Rental_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Bike_ID INTEGER,
            Customer_ID INTEGER,
            Rent_Start_Date DATE,
            Rent_End_Date DATE,
            Total_Cost DECIMAL(10, 2),
            FOREIGN KEY (Rental_ID) REFERENCES Rental(Rental_ID),
            FOREIGN KEY (Bike_ID) REFERENCES Bikes(Bike_ID),
            FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID)
        )''')

    conn.commit()
    cursor.close()
    conn.close()

#if table is empty insert values 
def insert_multiple_models(models):
    conn = sqlite3.connect('bike_rental.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM Models')
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany('''
            INSERT INTO Models (Model_Name, Manufacturer, Year)
            VALUES (?, ?, ?)
        ''', models)

        conn.commit()

    conn.close()

# Example list of models
models_to_insert = [('Ninja 300', 'Kawasaki', 2021),
    ('CBR1000RR', 'Honda', 2022),
    ('R1250GS', 'BMW', 2020),
    ('YZF-R1', 'Yamaha', 2023),
    ('Panigale V4', 'Ducati', 2021),
    ('Iron 883', 'Harley-Davidson', 2022),
    ('GSX-R1000', 'Suzuki', 2023),
    ('Street Triple RS', 'Triumph', 2020),
    ('MT-07', 'Yamaha', 2022),
    ('Diavel 1260', 'Ducati', 2021),
    ('Ninja 300', 'Kawasaki', 2021),
    ('Ninja 300', 'KTM', 2022),
    ('Ninja 300', 'Suzuki', 2023),
    ('CBR1000RR', 'Honda', 2022),
    ('CBR1000RR', 'Kawasaki', 2023),
    ('CBR1000RR', 'Suzuki', 2020),
    ('R1250GS', 'BMW', 2020),
    ('R1250GS', 'Ducati', 2021),
    ('R1250GS', 'Triumph', 2022)]

# Usage:
insert_multiple_models(models_to_insert)
#insert bike 
def insert_multiple_bikes(bikes):
    conn = sqlite3.connect('bike_rental.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM Bikes')
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany('''
            INSERT INTO Bikes (Bike_Name, Model_ID, Bike_Status, Daily_Rental_Rate)
            VALUES (?, ?, ?, ?)
        ''', bikes)

        conn.commit()

    conn.close()

# Example bike data for insertion
bikes_to_insert = [
    ('Boss Hoss Cycles', 14, 'Available', 45.00),
    ('Suzuki Hayabusa', 5, 'Available', 60.00),
    ('Harley-Davidson Sportster', 8, 'Available', 55.00),
    ('Kawasaki Z900', 2, 'Available', 50.00),
    ('Ducati Monster', 3, 'Available', 65.00),
    ('BMW S1000RR', 4, 'Available', 70.00),
    ('Yamaha MT-09', 6, 'Available', 55.00),
    ('Honda CBR650R', 7, 'Available', 50.00),
    ('Triumph Speed Triple', 9, 'Available', 58.00),
    ('KTM Duke 390', 10, 'Available', 45.00),
    ('Aprilia Tuono V4', 11, 'Available', 68.00),
    ('Moto Guzzi V7', 12, 'Available', 48.00),
    ('Indian Scout', 13, 'Available', 55.00),
    ('Victory Octane', 15, 'Available', 52.00),
    ('Benelli TNT 300', 16, 'Available', 40.00)
]

# Usage:
insert_multiple_bikes(bikes_to_insert)


if __name__ == '__main__':
    app.run(debug=True)
    