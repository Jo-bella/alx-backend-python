#!/usr/bin/python3
import mysql.connector

def stream_users():
    """Generator that yields rows from the user_data table one by one as dictionaries."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',  # Replace with your actual MySQL password
            database='ALX_prodev'
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
