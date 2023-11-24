# Bike Rental Management System
* The Bike Rental Management System encapsulates an array of functionalities to efficiently oversee and administer the rental service for bikes. It's structured around a database schema that includes four primary tables: Models, Bikes, Customers, and Rental.
* By leveraging this database schema, the system can efficiently track available bikes, manage customer data, calculate costs, and streamline the entire rental process from booking to bike return, ensuring a smooth and effective bike rental service for both customers and administrators alike.
* we integrated a robust tech stack comprising HTML, CSS, JavaScript, Flask, and SQLite3. The core of the system is powered by a well-defined database schema, as illustrated in the provided SQL commands. The Models, Bikes, Customers, and Rental tables lay the foundation for structured data management. HTML structures the user interface, creating dynamic web pages for customers to interact with. CSS enhances the aesthetics and ensures a visually appealing and responsive design.
* JavaScript adds interactivity, facilitating real-time updates and validations. Flask, a Python web framework, handles the server-side logic, seamlessly integrating with SQLite3 for efficient data storage and retrieval. 
* This stack enables a comprehensive Bike Rental Management System, allowing users to effortlessly browse and rent bikes, while administrators can efficiently manage inventory, customer data, and rental transactions through a user-friendly and dynamically responsive web application. The utilization of SQLite3 ensures data integrity and accessibility, contributing to a seamless and efficient bike rental experience for both customers and administrators.

## Models Table: 
* This table details various bike models available for rental, storing information like Model_ID (unique identifier), Model_Name (the model's name), Manufacturer (the brand producing the model), and Year (the manufacturing year of the model).
<br>
![Sample Data](https://github.com/laharip10/Bike_Rentals/blob/main/media/models.png)

## Bikes Table:
* Acting as the inventory manager, the Bikes table keeps track of individual bikes. It contains Bike_ID (unique identifier), Bike_Name (name or identifier for the bike), Model_ID (referencing the specific bike model from the Models table), Bike_Status (indicating whether the bike is available,not available), and Daily_Rental_Rate (the cost per day for renting the bike).
<br>
![Sample Data](https://github.com/laharip10/Bike_Rentals/blob/main/media/Bikes.png)

## Customers Table:
* This table stores information about customers utilizing the rental service. It holds Customer_ID (unique identifier), Customer_Name (customer's name), Contact_Number (contact information), and Email (customer's email address).
<br>
![Sample Data](https://github.com/laharip10/Bike_Rentals/blob/main/media/Customers.png)

## Rental Table:
* This pivotal table records the rental transactions. It includes Rental_ID (unique identifier), Bike_ID (referencing the specific bike rented), Customer_ID (identifying the customer involved in the rental), Rent_Start_Date, Rent_End_Date (indicating the start and end dates of the rental), and Total_Cost (the overall cost incurred for the rental period).
<br>
![Sample Data](https://github.com/laharip10/Bike_Rentals/blob/main/media/rental.png)

# Functional Dependencies
Models Table Functional Dependencies:
* Model_ID -> Model_Name, Manufacturer, Year
Bikes Table Functional Dependencies:
* Bike_ID -> Bike_Name, Model_ID, Bike_Status, Daily_Rental_Rate
* Model_ID -> Bike_Name, Bike_Status, Daily_Rental_Rate (Derived from the foreign key relationship)
Customers Table Functional Dependencies:
* Customer_ID -> Customer_Name, Contact_Number, Email
Rental Table Functional Dependencies:
* Rental_ID -> Bike_ID, Customer_ID, Rent_Start_Date, Rent_End_Date, Total_Cost
* Bike_ID -> Customer_ID, Rent_Start_Date, Rent_End_Date, Total_Cost (Derived from the foreign key relationship)
* Customer_ID -> Bike_ID, Rent_Start_Date, Rent_End_Date Total_Cost (Derived from the foreign key relationship)


# 3NF 
Bike Rental System schema are in Third Normal Form (3NF), principles of 3NF:

Models Table:
The Models table has no transitive dependencies or partial dependencies. Each non-prime attribute is solely dependent on the primary key (Model_ID). Hence, it satisfies 3NF.

Bikes Table:
Bike_ID: Primary key, uniquely identifying each bike.
Bike_Name, Model_ID, Bike_Status, Daily_Rental_Rate: All attributes depend on the primary key (Bike_ID) and are not transitively dependent on each other. The Model_ID links to the Models table. Thus, this table satisfies 3NF.
Customers Table:
Customer_ID: Primary key, uniquely identifying each customer.
Customer_Name, Contact_Number, Email: All attributes depend solely on the primary key (Customer_ID). Therefore, this table satisfies 3NF.
Rental Table:
Rental_ID: Primary key, uniquely identifying each rental entry.
Bike_ID, Customer_ID, Rent_Start_Date, Rent_End_Date, Total_Cost: All attributes are dependent on the primary key (Rental_ID) and not transitively dependent on each other. The Bike_ID and Customer_ID fields maintain relationships with the Bikes and Customers tables, respectively. Thus, this table satisfies 3NF.

# Relational among tables
## 1) One-to-Many relationship between Models and Bikes tables:
Each model can have many bikes associated with it, but each bike is associated with only one model (in the given schema).
This is established by the foreign key constraint in the Bikes table that references the Models table (Model_ID in Bikes references Model_ID in Models).

## 2) Many-to-One relationship between Customers and Rental tables:
Many rentals can belong to one customer, but each rental is associated with only one customer (in the given schema).
This is established by the foreign key constraint in the Rental table that references the Customers table (Customer_ID in Rental references Customer_ID in Customers).

## 3) Many-to-One relationship between Bikes and Rental tables:
Many rentals can involve one bike, but each rental involves only one bike (in the given schema).
This is established by the foreign key constraint in the Rental table that references the Bikes table (Bike_ID in Rental references Bike_ID in Bikes).
