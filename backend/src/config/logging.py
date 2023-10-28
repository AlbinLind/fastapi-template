"""Module with utilitiy functions for the whole project."""
import logging
import sys
from itertools import chain
from types import FrameType
from typing import cast

from loguru import logger

from src.config import settings


class InterceptHandler(logging.Handler):  # pragma: no cover
    """Class to intercept the standrad logger and redirect it to loguru."""

    def emit(self, record: logging.LogRecord) -> None:
        """Emit the loguru logger instead of the standard logger."""
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # Find the caller from where the log was called
        frame, depth = logging.currentframe(), 2

        # Iterate until we find the first logging.Logger object
        while frame.f_code.co_filename == logging.__file__:
            frame = cast(FrameType, frame.f_back)
            depth += 1

        # Get the path of the file where the logging call has been made
        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )


def _setup_logger_intercept(
    modules: tuple[str] = ("uvicorn.error", "uvicorn.asgi", "uvicorn.access"),
) -> None:
    """Sets up the correct logger intercepts."""
    logging.basicConfig(handlers=[InterceptHandler()], level=settings.log_level)
    for logger_name in chain(("",), modules):
        mod_logger = logging.getLogger(logger_name)
        mod_logger.handlers = [InterceptHandler(level=settings.log_level)]
        mod_logger.propagate = False


def setup_logging() -> None:  # pragma: no cover
    """Sets up the logger with the correct configuration according to the settings."""
    # Intercept the standard logger
    _setup_logger_intercept()

    # Remove the standard logger
    logger.remove(None)

    # If we want to log in the terminal add a handler for it
    if settings.log_in_terminal:
        logger.add(
            sys.stderr,
            level=settings.log_terminal_level,
            format=settings.log_format,
        )

    # If there exists a log file in the configuration add it to the logger
    if settings.log_file is not None:
        logger.add(
            settings.log_file,
            rotation=settings.log_file_rotation,
            level=settings.log_file_level,
            format=settings.log_format,
        )

    logger.info("Logger configured, and intercepted.")
