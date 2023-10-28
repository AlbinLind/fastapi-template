"""Run the backend application."""

import os


def run_backend() -> None:
    """Runs the backend."""
    os.system("uvicorn src.main:app --reload --host 0.0.0.0")
