import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv
import click
from utils import init_db_client

# Load environment variables
load_dotenv()

pg_user_name = os.getenv("POSTGRES_USER")
pg_password = os.getenv("POSTGRES_PASSWORD")
db_name = "jobtracker"

def init():
    try:
        # Connect to the 'postgres' database to create a new database
        con, cur = init_db_client('postgres')

        # Create the database (if it doesn't exist)
        try:
            cur.execute(sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier(db_name))
            )
            click.echo(f"Database '{db_name}' created successfully!")
        except psycopg2.errors.DuplicateDatabase:
            click.echo(f"Database '{db_name}' already exists.")

        # Close connection to 'postgres'
        con.close()  

        # Reconnect to 'jobtracker' DB
        con, cur = init_db_client(name=db_name)

        # Create a table for the user
        try:
            table_name = f"job_applications_{pg_user_name}"
            create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id SERIAL PRIMARY KEY,
                    company_name VARCHAR(255) NOT NULL,
                    job_title VARCHAR(255) NOT NULL,
                    application_date DATE NOT NULL,
                    source VARCHAR(50),
                    status VARCHAR(50),
                    notes TEXT
                );
            """
            cur.execute(create_table_query)
            click.echo(f"Table '{table_name}' is ready for user {pg_user_name}!")
        except Exception as e:
            click.echo(f"Error creating table for user {pg_user_name}: {e}")

        finally:
            if cur:
                cur.close()
            if con:
                con.close()
    except Exception as e:
        click.echo(f"Error while connecting to PostgreSQL: {e}")

if __name__ == '__main__':
    init()
