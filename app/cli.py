import click
from app.jobs.add import add_job
from models import JobPosting

@click.group()
def cli():
    pass

@cli.command()
@click.argument('company')
@click.argument('title')
@click.argument('date_applied')
@click.option('--source', default='N/A', help='Where did you apply for this job, LinkedIn, Indeed, etc. Can be link to job posting')
@click.option('--status', default='recently applied', help='Application status. Interview, Ghosted, etc')
@click.option('--notes', default='N/A', help='Additional notes')
def add(company, title, date_applied, source, status, notes):
    try:
        job = JobPosting(
            company=company,
            title=title,
            date_applied=date_applied,
            source=source,
            status=status,
            notes=notes
        )
    except Exception as e:
        click.secho(f"Error creating new job application instance: {e}", fg="red")
        return
    finally:
        add_job(job)
