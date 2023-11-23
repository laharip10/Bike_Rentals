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


if __name__ == '__main__':
    app.run(debug=True)
    