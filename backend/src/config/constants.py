"""Constants used in the application."""
from enum import Enum
from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parents[2]


class Environment(Enum):
    """The different environments that the project can run in."""

    LOCAL = "local"
    PRODUCTION = "production"
    TESTING = "testing"

    @property
    def is_debug(self) -> bool: # pragma: no cover
        """Whether or not the environment is in debug mode."""
        return self in {Environment.LOCAL, Environment.TESTING}

    @property
    def is_testing(self) -> bool: # pragma: no cover
        """Whether or not the environment is in testing mode."""
        return self == Environment.TESTING

    @property
    def is_production(self) -> bool: # pragma: no cover
        """Whether or not the environment is in production mode."""
        return self == Environment.PRODUCTION
