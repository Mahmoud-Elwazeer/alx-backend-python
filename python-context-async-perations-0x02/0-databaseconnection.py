#!/usr/bin/python3

"""class based context manager to handle opening and closing 
    database connections automatically
"""

import sqlite3 

class DatabaseConnection:
    """A class-based context manager to handle SQLite3 database connections."""
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        """Establish the database connection and return it."""
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def  __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"An error occurred: {exc_value}")
        self.connection.commit()
        self.connection.close()


with DatabaseConnection('users.db') as cursor:
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

