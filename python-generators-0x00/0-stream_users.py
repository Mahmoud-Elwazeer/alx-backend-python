#!/usr/bin/env python3

seed = __import__('seed')

def stream_users():
    """uses a generator to fetch rows 
    one by one from the user_data table"""

    connection = seed.connect_to_prodev()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM user_data")
            for row in cursor:
                yield row
        finally:
            connection.close()
