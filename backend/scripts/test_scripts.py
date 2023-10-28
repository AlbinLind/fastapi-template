"""All scripts regarding testing the backend."""
import os

from src.config.constants import PROJECT_PATH


def run_tests() -> None:
    """Run all tests and generate a coverage report."""
    os.system(f"coverage run -m pytest {PROJECT_PATH}/tests")
    os.system("coverage html")


def github_coverage() -> None:
    """Run all tests and generate a coverage report for GitHub Actions."""
    os.system(f"coverage run -m pytest {PROJECT_PATH}/tests")
    os.system("coverage xml")
