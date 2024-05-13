# Courier Management System (C.M.S.)

## Introduction
C.M.S. is a comprehensive application designed to streamline courier management operations. It provides functionalities for placing orders, tracking deliveries, managing employees, generating reports, and more. This README file provides an overview of the project structure, functionalities, and instructions for setting up and running the application.

## Directory Structure


.
├── entity
│ ├── init.py
│ ├── courier.py
│ ├── courier_collection.py
│ ├── courierCompany.py
│ ├── courierServices.py
│ ├── employee.py
│ ├── location.py
│ ├── payment.py
│ ├── user.py
|
├── dao
│ ├── init.py
│ ├── courier_admin_collection_impl.py
│ ├── courier_admin_service.py
│ ├── courier_admin_service_impl.py
│ ├── courier_service_DB.py
│ ├── courier_user_service.py
│ ├── courier_user_service_impl.py
│ ├── courier_user_service_collection_impl.py
├── exceptions
│ ├── init.py
│ └── my_exceptions.py
├── util
│ ├── init.py
│ ├── db_connection.py
│ └── db_property_util.py
└── main
├── init.py
└── main_module.py


## Key Functionalities
- **Schema Design**: Define the database schema including tables for Customers, Couriers, Orders, Parcels, etc.
- **Service Provider Interface**: Implement interfaces for customer and admin functionalities.
- **Database Interaction**: Connect the application to an SQL database and perform CRUD operations.
- **Exception Handling**: Define and handle custom exceptions throughout the application.
- **Main Module**: Implement a menu-driven interface to interact with the functionalities.

## Getting Started
1. **Clone the Repository**: Clone the project repository to your local machine.
2. **Install Dependencies**: Ensure you have Python installed, and install the required dependencies using `pip install -r requirements.txt`.
3. **Set Up Database**: Execute the SQL scripts provided in the `sql` directory to set up the database schema.
4. **Update Database Connection Details**: Update the database connection details in the `db_property_util` file.
5. **Run the Application**: Execute the `main_module.py` file to start the application.

## Contributors
- Pratham Agarwal

## Scope
The project covers a wide range of topics including object-oriented programming principles, control flow statements, loops, arrays, collections, exception handling, database interaction, and unit testing.

