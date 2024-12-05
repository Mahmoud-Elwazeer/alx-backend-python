#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error
import uuid
import csv

# Database connection details
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'collation': 'utf8mb4_unicode_ci',
    'charset': 'utf8mb4'
}

db_alx_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'collation': 'utf8mb4_unicode_ci',
    'charset': 'utf8mb4',
    'database': 'ALX_prodev'
}


def connect_db():
    """connects to the mysql database server"""
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print(f"Error: {e}")


def create_database(connection):
    """creates the database ALX_prodev if it does not exist"""
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()


def connect_to_prodev():
    """connects the the ALX_prodev database in MYSQL"""
    try:
        connection = mysql.connector.connect(**db_alx_config)
        return connection
    except Error as e:
        print(f"Error: {e}")


def create_table(connection):
    """creates a table user_data if it does not exists with the required fields"""
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_data (
            user_id UUID PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age   DECIMAL(10, 2) NOT NULL,
            INDEX (user_id)
        )""")
    cursor.close()


def insert_data(connection, data):
    """inserts data in the database if it does not exist"""
    cursor = connection.cursor()
    try:
        with open(data, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                user_id = str(uuid.uuid4())  # Generate a UUID
                name = row['name']
                email = row['email']
                age = row['age']
                
                cursor.execute("SELECT COUNT(*) FROM user_data WHERE email = %s", (email,))
                if cursor.fetchone()[0] == 0:  # No existing record found
                    user_id = str(uuid.uuid4())  # Generate a UUID
                    cursor.execute("""
                        INSERT INTO user_data (user_id, name, email, age)
                        VALUES (%s, %s, %s, %s)
                    """, (user_id, name, email, age))
        
        connection.commit()  # Commit the transaction
        print("Data inserted successfully.")
        
    except Error as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print(f"Error: The file '{data}' was not found.")
    finally:
        cursor.close()
