#!/usr/bin/python3

import sqlite3
import functools
from datetime import datetime

def log_message(message):
    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Print the log message with the timestamp
    print(f"{timestamp} - Executing query: {message}")

def log_queries(func):
    """Logging database Queries"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query', args[0] if args else None)
        log_message(query)
        func(*args, **kwargs)

    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")

print(users)