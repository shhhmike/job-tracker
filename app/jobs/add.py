from utils import init_db_client
from dotenv import load_dotenv
from models import JobPosting
import click
import os

load_dotenv()
pg_user_name = os.getenv("POSTGRES_USER")

def add_job(new_posting: JobPosting):
    con, cur = init_db_client()

    click.echo(f"[DB]: Adding job: {new_posting.company}, {new_posting.title}, {new_posting.date_applied}")

    add_job_query = f"""
        INSERT INTO job_applications_{pg_user_name} 
        (company_name, job_title, application_date, source, status, notes)
        VALUES (%s, %s, %s, %s, %s, %s);
    """

    try:
        cur.execute(add_job_query, (
            new_posting.company,
            new_posting.title,
            new_posting.date_applied,
            new_posting.location,
            new_posting.status,
            new_posting.notes,
        ))
    except Exception as e:
        con.rollback()
        click.secho(f"Error executing the command to postgres database with Exception: {e}", fg="red")       
    finally:
        click.secho("Successfully added new entry into users Postgresql database", fg="green")       
        if cur:
            cur.close()
        if con:
            con.close()