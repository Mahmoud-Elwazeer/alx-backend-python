#!/usr/bin/python3

"""create a reusable context manager that takes a query as input and executes it,
    managing both connection and the query execution
"""

import sqlite3 

class ExecuteQuery:
    def __init__(self, db_name, query, parameter=None):
        self.db_name = db_name
        self.query = query
        self.parameter = parameter

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        if self.parameter:
            self.cursor.execute(self.query, self.parameter)
        else:
            self.cursor.execute(self.query)
        return self.cursor.fetchall()

    def  __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"An error occurred: {exc_value}")
        if self.connection:
            self.connection.close()


with ExecuteQuery('users.db', "SELECT * FROM users WHERE age > ?", (25, )) as out:
    for row in out:
        print(row)