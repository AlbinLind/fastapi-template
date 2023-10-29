"""Configuration for pytest.
Import source files only in the functions to avoid undefined behaviour, such as extra db creation.
"""
import os
from pathlib import Path

from sqlalchemy import create_engine

os.environ["PROJECT_ENVIRONEMNT"] = "testing"
os.environ["LOG_FILE"] = str(Path(__file__).parent / "logs" / "test.log")

from typing import Generator

import pytest
from fastapi.testclient import TestClient
from loguru import logger

from alembic import command
from alembic.config import Config


@pytest.fixture(autouse=True, scope="session")
def _setup_db(tmp_path_factory: pytest.TempPathFactory):
    from src.config import constants, settings

    """Sets up the database for testing, and running latest migrations."""
    settings.database_url = f"sqlite:///{tmp_path_factory.mktemp('data')}/test.db"

    # Run alemibic migrations
    alembic_cfg = Config(constants.PROJECT_PATH / "alembic.ini")
    alembic_cfg.set_main_option("script_location", str(constants.PROJECT_PATH / "alembic"))
    command.upgrade(alembic_cfg, "head")

    from src.database import database

    database.engine = create_engine(settings.database_url)
    database.db = next(database._get_db())


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

    return next(database._get_db())


@pytest.fixture(scope="module")
def client() -> Generator:
    """Get A FastAPI client."""
    from src.main import app

    with TestClient(app) as c:
        yield c
