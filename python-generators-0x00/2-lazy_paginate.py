#!/usr/bin/env python3
"""Objective: Simulte fetching paginated data 
from the users database using a generator to lazily load each page
"""
seed = __import__('seed')

def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_paginate(page_size):
    offset = 0
    while True:
        users = paginate_users(page_size, offset)
        if not users:
            # If no more users are available, stop the iteration
            break

        yield users
        offset += page_size
