import mysql.connector

def stream_users_in_batches(batch_size):
    """Fetches all users in batches and returns them as a flat list (not a generator)."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",  # Replace with actual password
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    users = []
    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        users.extend(batch)

    cursor.close()
    connection.close()
    return users  # This is a return, not a generator

def batch_processing(batch_size):
    """Processes and returns all users over age 25."""
    filtered = []
    for user in stream_users_in_batches(batch_size):
        if user['age'] > 25:
            filtered.append(user)
    return filtered
