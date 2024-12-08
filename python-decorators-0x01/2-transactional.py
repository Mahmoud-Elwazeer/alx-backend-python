#!/usr/bin/python3

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

def transactional(func):
    """manages database transactions by automatically
    committing or rolling back changes"""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit() 
            return result
        except Exception as e:
            conn.rollback()
            print(f"Transaction failed: {e}")
            raise
    return wrapper



@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 

#### Update user's email with automatic transaction handling 
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')