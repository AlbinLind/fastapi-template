"""All scripts regarding formatting and linting the backend."""
import os

from src.config.constants import PROJECT_PATH


def lint() -> None:
    """Format the codebase, and lint it."""
    os.system(f"ruff format {PROJECT_PATH} --preview")
    os.system(f"ruff {PROJECT_PATH} --fix --preview")
