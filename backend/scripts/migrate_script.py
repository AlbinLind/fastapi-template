"""A script that will handle migrations of the database."""
import os


def migrate() -> None:
    """Create a migration with alembic. Asks the user for a migration message."""
    msg = input("Changes since last migration (enter for setting up db): ")
    if '"' in msg:
        raise ValueError("Message cannot contain double quotes.")
    if len(msg) > 0:
        os.system(f'alembic revision --autogenerate -m "{msg}"')
    os.system("alembic upgrade head")
