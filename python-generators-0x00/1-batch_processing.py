#!/usr/bin/env python3

seed = __import__('seed')

def stream_users_in_batches(batch_size):
    """generator to fetch and process data in batches
    from the users database"""

    connection = seed.connect_to_prodev()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM user_data")
            while True:
                batch = cursor.fetchmany(batch_size)
                if not batch:
                # Break the loop when no more rows are available
                    break
                yield batch 
        finally:
            connection.close()


def batch_processing(batch_size):
    """processes each batch to filter users over the age of25`
    """
    for batch in stream_users_in_batches(batch_size):
        filtered_batch = (user for user in batch if float(user[3]) > 25)
