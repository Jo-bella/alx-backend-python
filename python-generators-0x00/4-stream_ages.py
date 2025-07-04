seed = __import__('seed')


def stream_user_ages():
    """
    Generator that yields ages of users one by one from the user_data table.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    row = cursor.fetchone()
    while row:
        yield row[0]
        row = cursor.fetchone()
    cursor.close()
    connection.close()


def calculate_average_age():
    """
    Uses the stream_user_ages generator to compute the average age without loading
    all ages into memory at once.
    """
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    if count == 0:
        print("Average age of users: 0")
    else:
        average = total_age / count
        print(f"Average age of users: {average}")


if __name__ == "__main__":
    calculate_average_age()
