#!/usr/bin/env python3

seed = __import__('seed')

def stream_user_ages():
    """generator that yields user ages one by one."""
    connection = seed.connect_to_prodev()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT age FROM user_data")
            for row in cursor:
                yield row[0]
        finally:
            connection.close()

# Function to calculate the average age using the stream_user_ages generator
def calculate_average_age():
    total_age = 0
    count = 0
    
    # Iterate over the generator to calculate the total age and count
    for age in stream_user_ages():
        total_age += age
        count += 1
    
    if count == 0:
        return 0  # Prevent division by zero if no users are found
    return total_age / count  # Calculate and return the average age



