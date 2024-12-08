#!/usr/bin/python3

import time
import sqlite3 
import functools


query_cache = {}

def with_db_connection(func):
    """ your code goes here""" 
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

def cache_query(func):
    """Using decorators to cache Database Queries"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = args[0]
        if query in query_cache:
            print("Cache hit for query:", query)
            return query_cache[query]
        print("Cache miss for query:", query)
        result = func(*args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
