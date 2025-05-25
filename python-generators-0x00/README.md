# Python MySQL Seeding

This script sets up a MySQL database and streams user data from a CSV file into a table.

## Files
- **seed.py** – Contains methods to:
  - Connect to MySQL
  - Create a database (`ALX_prodev`)
  - Create a `user_data` table
  - Insert user data from a `user_data.csv` file

## Function Prototypes

- `connect_db()` – Connects to MySQL server
- `create_database(connection)` – Creates the `ALX_prodev` database
- `connect_to_prodev()` – Connects to `ALX_prodev`
- `create_table(connection)` – Creates the `user_data` table
- `insert_data(connection, csv_file)` – Inserts data from CSV into table

## Running the Script

Ensure MySQL server is running and update `seed.py` with your MySQL password.

Then run:

```bash
./0-main.py
