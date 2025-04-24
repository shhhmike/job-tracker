import click
from app.jobs import add_job, list_jobs, update_job_status, generate_digest

@click.group()
def cli():
    pass

@cli.command()
@click.option('--company', prompt='Company')
@click.option('--role', prompt='Role')
@click.option('--source', prompt='Source')
@click.option('--date-applied', prompt='Date applied (YYYY-MM-DD)')
def add(company, role, source, date_applied):
    add_job(company, role, source, date_applied)

@cli.command()
def list():
    list_jobs()

@cli.command()
@click.option('--company', prompt='Company')
@click.option('--status', prompt='Status')
def update(company, status):
    update_job_status(company, status)

@cli.command()
def digest():
    generate_digest()

if __name__ == '__main__':
    cli()
