#!/usr/bin/python3

import time
import sqlite3 
import functools

def with_db_connection(func):
    """ Database Connections with a Decorator """ 
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            # Pass the connection as the first argument to the wrapped function
            result = func(conn, *args, **kwargs)
        finally:
            # Ensure the connection is always closed
            conn.close()
        return result
    return wrapper

def retry_on_failure(retries, delay):
    """decorator that retries database operations
    if they fail due to transient errors"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    print(f"Attempt {attempt}...")
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    last_exception = e
                    print(f"Error: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)