import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

pg_user_name = os.getenv("POSTGRES_USER")
pg_password = os.getenv("POSTGRES_PASSWORD")
db_name = "jobtracker"

def init_db_client(name=db_name, pg_user=pg_user_name, host='localhost', pg_pass=pg_password):
    """
    This is a helper function that initializes the connection to a postgres DB. 
    By default it will connect to the jobtracker database if no argument for first 
    parameter is provided.
    
    Returns a cursor so that we can execute Postgres commands.
    """
    con = None
    cur = None
    try:
        con = psycopg2.connect(dbname=name, user=pg_user, host=host, password=pg_pass)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()
        print(f'Successfully connected to database: {name}')
    except Exception as e:
        print("Error while connecting to PostgreSQL:", e)
    return con, cur
