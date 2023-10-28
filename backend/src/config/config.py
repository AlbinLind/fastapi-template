"""Settings for the application, plus other configuration variables."""
from pathlib import Path
from typing import Any

import toml
from pydantic_settings import BaseSettings

from src.config.constants import PROJECT_PATH, Environment


class Settings(BaseSettings):
    """Settings for the backend."""

    pyproject_toml: dict[str, Any] = toml.load(PROJECT_PATH / "pyproject.toml")

    # Project metadata
    project_name: str = pyproject_toml["tool"]["poetry"]["name"]
    project_version: str = pyproject_toml["tool"]["poetry"]["version"]

    # Application settings
    environment: Environment = Environment.LOCAL

    # Database settings
    database_url: str = "sqlite:///./database.db"

    # General logging settings
    log_level: str = "DEBUG"
    log_format: str = (
        "<green>{time:DD-MM-YYYY > HH:mm:ss}</green>"
        " | <level>{level: <8}</level>"
        " | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
        " - <level>{message}</level>"
    )

    # Log file settings
    log_file: Path | None = Path("./logs/log.log")
    log_file_rotation: str = "5mb"
    log_file_level: str = log_level

    # Log terminal settings
    log_in_terminal: bool = True
    log_terminal_level: str = log_level


settings = Settings()

app_configs = {"title": settings.project_name, "version": settings.project_version}

if not settings.environment.is_debug:
    app_configs["openapi_url"] = None
