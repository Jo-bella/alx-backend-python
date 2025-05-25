#!/usr/bin/python3
import mysql.connector
import csv
import uuid
from mysql.connector import errorcode


def connect_db():
    """Connects to the MySQL server (not to a specific DB)"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # Replace with your actual MySQL password
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_database(connection):
    """Creates the ALX_prodev database if it does not exist"""
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    finally:
        cursor.close()


def connect_to_prodev():
    """Connects to the ALX_prodev database"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',  # Replace with your actual MySQL password
            database='ALX_prodev'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_table(connection):
    """Creates the user_data table if it does not exist"""
    cursor = connection.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL,
                INDEX(user_id)
            );
        """)
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
    finally:
        cursor.close()


def insert_data(connection, csv_file):
    """Inserts data from a CSV file into the user_data table"""
    cursor = connection.cursor()
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Check if user already exists
                cursor.execute("SELECT user_id FROM user_data WHERE user_id = %s", (row['user_id'],))
                if not cursor.fetchone():
                    cursor.execute("""
                        INSERT INTO user_data (user_id, name, email, age)
                        VALUES (%s, %s, %s, %s)
                    """, (row['user_id'], row['name'], row['email'], row['age']))
        connection.commit()
    except FileNotFoundError:
        print(f"File {csv_file} not found.")
    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")
    finally:
        cursor.close()
