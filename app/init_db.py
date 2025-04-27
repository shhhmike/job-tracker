import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
from dotenv import load_dotenv
from utils import init_db_client

# Load environment variables
load_dotenv()

pg_user_name = os.getenv("POSTGRES_USER")
pg_password = os.getenv("POSTGRES_PASSWORD")
db_name = "jobtracker"

def init():
    try:
        # Step 1: Connect to the 'postgres' database to create a new database
        con, cur = init_db_client('postgres')

        # Step 2: Create the database (if it doesn't exist)
        try:
            cur.execute(sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier(db_name))
            )
            print(f"Database {db_name} created successfully!")
        except psycopg2.errors.DuplicateDatabase as e:
            print(f"Error: Database '{db_name}' already exists.")
            print(f"Details: {e}")

        # Step 3: Now, connect to the newly created 'jobtracker' database
        con.close()  # Close connection to 'postgres'

        # Reconnect to 'jobtracker' DB
        con, cur = init_db_client(name=db_name)

        # Step 4: Create a table for the user
        try:
            table_name = f"job_applications_{pg_user_name}"
            create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id SERIAL PRIMARY KEY,
                    company_name VARCHAR(255) NOT NULL,
                    job_title VARCHAR(255) NOT NULL,
                    application_date DATE,
                    status VARCHAR(50),
                    notes TEXT
                );
            """
            cur.execute(create_table_query)
            print(f"Table '{table_name}' is ready for user {pg_user_name}!")
        except Exception as e:
            print(f"Error creating table for user {pg_user_name}: {e}")

        finally:
            if cur:
                cur.close()
            if con:
                con.close()
    except Exception as e:
        print("Error while connecting to PostgreSQL:", e)

if __name__ == '__main__':
    init()
