#!/usr/bin/python3
import mysql.connector

def stream_users_in_batches(batch_size):
    """Generator that fetches rows in batches and yields one user at a time."""
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",  # ← Replace with your actual password
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            for user in batch:
                yield user

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def batch_processing(batch_size):
    """Process and print users over the age of 25."""
    for user in stream_users_in_batches(batch_size):
        if user['age'] > 25:
            print(user)
