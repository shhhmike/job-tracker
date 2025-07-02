import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
from dotenv import load_dotenv
import click

load_dotenv()

pg_user_name = os.getenv("POSTGRES_USER")
pg_password = os.getenv("POSTGRES_PASSWORD")
db_name = "jobtracker"


def init_db_client(name=db_name, pg_user=pg_user_name, host='localhost', pg_pass=pg_password):
    """
    Initializes and returns a connection + cursor to a PostgreSQL database.
    """
    try:
        con = psycopg2.connect(
            dbname=name,
            user=pg_user,
            password=pg_pass,
            host=host
        )
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()
    except Exception as e:
        click.secho(f"Failed to connect to database '{name}': {e}", fg="red")
        return None, None 
    else:
        click.secho(f"Successfully connected to database: {name}", fg="green")
        return con, cur

