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

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to display bike models
@app.route('/model')
def display_bike_models():
    conn = sqlite3.connect('bike_rental.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Models')
    models = cursor.fetchall()
    conn.close()
    return render_template('model.html', models=models)

# Route to add a new bike model
@app.route('/add_model', methods=['GET', 'POST'])
def add_model():
    conn = sqlite3.connect('bike_rental.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        model_name = request.form['model_name']
        manufacturer = request.form['manufacturer']
        year = int(request.form['year'])
        
        current_year = datetime.now().year
        
        if year > current_year:
            conn.close()
            return "Year should not be greater than the current year"
        else:
            cursor.execute('''
                INSERT INTO Models (Model_Name, Manufacturer, Year)
                VALUES (?, ?, ?)
            ''', (model_name, manufacturer, year))
            
            conn.commit()
            conn.close()
            return redirect('/model')
    
    conn.close()
    return render_template('model_add.html')

# Route to edit a bike model
@app.route('/edit_model/<int:model_id>', methods=['GET', 'POST'])
def edit_model(model_id):
    conn = sqlite3.connect('bike_rental.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        model_name = request.form['model_name']
        manufacturer = request.form['manufacturer']
        year = request.form['year']
        
        cursor.execute('''
            UPDATE Models
            SET Model_Name=?, Manufacturer=?, Year=?
            WHERE Model_ID=?
        ''', (model_name, manufacturer, year, model_id))
        
        conn.commit()
        conn.close()  # Close connection after commit
        return redirect('/model')
    
    cursor.execute('SELECT * FROM Models WHERE Model_ID=?', (model_id,))
    bike_model = cursor.fetchone()
    conn.close()  # Close connection after fetching data
    return render_template('model_edit.html', model=bike_model)


@app.route('/delete_model/<int:model_id>')
def delete_model(model_id):
    try:
        conn = sqlite3.connect('bike_rental.db')
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM Models WHERE Model_ID = ?''', (model_id,))
        conn.commit()
    except sqlite3.Error as e:
        print("SQLite error:", e)
        # Handle the error appropriately (rollback transaction, log, etc.)
    finally:
        conn.close()
    return redirect('/model')

@app.route('/bike')
def display_bike_table():
    conn = sqlite3.connect('bike_rental.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Bikes')
    data = cursor.fetchall()
    conn.close()
    return render_template('bike.html', bikes=data)

def generate_unique_number(existing_numbers):
    while True:
        # Generate a 5-digit random number
        unique_number = random.randint(10000, 99999)
        # Ensure uniqueness by checking against existing numbers
        if unique_number not in existing_numbers:
            return unique_number

@app.route('/bike_add', methods=['GET', 'POST'])
def add_bike():
    conn = sqlite3.connect('bike_rental.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        bike_name = request.form['bike_name']
        model_id = request.form['model_id']
        bike_status = request.form['bike_status']
        daily_rental_rate = request.form['daily_rental_rate']

        # Fetch existing bike numbers from the database
        cursor.execute('SELECT Bike_ID FROM Bikes')
        existing_numbers = {int(row[0]) for row in cursor.fetchall()}

        # Generate a unique 5-digit number
        unique_number = generate_unique_number(existing_numbers)

        cursor.execute('''
            INSERT INTO Bikes (Bike_ID, Bike_Name, Model_ID, Bike_Status, Daily_Rental_Rate)
            VALUES (?, ?, ?, ?, ?)
        ''', (unique_number, bike_name, model_id, bike_status, daily_rental_rate))

        conn.commit()
        conn.close()
        return redirect('/bike')

    # Fetch Model IDs from the database
    cursor.execute('SELECT Model_ID, Model_Name FROM Models')
    model_ids = cursor.fetchall()
    conn.close()
    
    return render_template('bike_add.html', model_ids=model_ids)


@app.route('/bike_edit/<int:bike_id>', methods=['GET', 'POST'])
def edit_bike(bike_id):
    if request.method == 'POST':
        # Retrieve form data
        bike_name = request.form['bike_name']
        model_id= request.form['model_id']
        bike_status = request.form['bike_status']
        daily_rental_rate = request.form['daily_rental_rate']
        # Update the bike information in the database
        conn = sqlite3.connect('bike_rental.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Bikes
            SET Bike_Name=?, Model_ID=?, Bike_Status=?, Daily_Rental_Rate=?
            WHERE Bike_ID=?
        ''', (bike_name, model_id, bike_status, daily_rental_rate, bike_id))
        conn.commit()
        conn.close()
        return redirect('/bike')  # Redirect to bike table after editing
    # Fetch the bike data for the given ID
    conn = sqlite3.connect('bike_rental.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Bikes WHERE Bike_ID = ?', (bike_id,))
    bike_data = cursor.fetchone()
    conn.close()
    
    return render_template('bike_edit.html', bike_data=bike_data)

# Route for deleting a bike
@app.route('/bike_delete/<int:bike_id>')
def delete_bike(bike_id):
    try:
        conn = sqlite3.connect('bike_rental.db')
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM Bikes WHERE Bike_ID = ?''', (bike_id,))
        conn.commit()
    except sqlite3.Error as e:
        print("SQLite error:", e)
        # Consider rolling back the transaction or handling the error accordingly
    finally:
        conn.close()
    return redirect('/bike')
 

if __name__ == '__main__':
    app.run(debug=True)
    