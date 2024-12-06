#!/usr/bin/python3

import sqlite3
import csv

# Function to set up the database (create users table and insert sample data)
def setup_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create the users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            age REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert data into the database from a CSV file
def insert_data(data):
    """Inserts data into the database if it does not exist"""
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    try:
        with open(data, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                name = row['name']
                email = row['email']
                age = float(row['age'])  # Convert age to a float
                
                # Check if the email already exists in the database
                cursor.execute("SELECT COUNT(*) FROM users WHERE email = ?", (email,))
                if cursor.fetchone()[0] == 0:  # No existing record found
                    # Insert the new user
                    cursor.execute("""
                        INSERT INTO users (name, email, age)
                        VALUES (?, ?, ?)
                    """, ( name, email, age))
        
        connection.commit()  # Commit the transaction
        print("Data inserted successfully.")
        
    except FileNotFoundError:
        print(f"Error: The file '{data}' was not found.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

# Main script execution
setup_database()
insert_data("user_data.csv")
