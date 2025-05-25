#!/usr/bin/python3
import mysql.connector

def stream_users_in_batches(batch_size):
    """Generator that yields batches of users from the database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',  # Change to your MySQL password
            database='ALX_prodev'
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield from batch  # Yield one by one (not as list)

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def batch_processing(batch_size):
    """Processes users in batches and yields users older than 25."""
    for user in stream_users_in_batches(batch_size):
        if user['age'] > 25:
            print(user)
