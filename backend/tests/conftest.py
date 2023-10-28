"""Configuration for pytest.
Import source files only in the functions to avoid undefined behaviour, such as extra db creation.
"""
import os
from pathlib import Path

os.environ["PROJECT_ENVIRONEMNT"] = "testing"
os.environ["LOG_FILE"] = str(Path(__file__).parent / "logs" / "test.log")
os.environ["DATABASE_URL"] = ""

from typing import Generator

import pytest
from fastapi.testclient import TestClient
from loguru import logger


@pytest.fixture(autouse=True, scope="session")
def _setup_db(tmp_path_factory: pytest.TempPathFactory):
    from src.config import settings

    """Sets up the database for testing, and running latest migrations."""
    settings.database_url = f"sqlite:///{tmp_path_factory.mktemp('data')}/test.db"

    os.system("alembic upgrade head")


@pytest.fixture(autouse=True, scope="session")
def _setup_logging():
    """Sets up the logging for testing."""
    from src.config import logging, settings

    logger.remove(None)
    settings.log_level = "DEBUG"
    logging.setup_logging()


@pytest.fixture()
def db():
    """Return a database session."""
    from src.database import database

    return next(database.get_db())


@pytest.fixture(scope="module")
def client() -> Generator:
    """Get A FastAPI client."""
    from src.main import app

    with TestClient(app) as c:
        yield c
