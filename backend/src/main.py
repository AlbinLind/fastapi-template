"""Main module for the backend."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.config import app_configs
from src.config.logging import setup_logging


def start_backend() -> FastAPI:
    """Starts the backend with settings and configs set."""
    setup_logging()

    start_app = FastAPI(**app_configs)

    start_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return start_app


app = start_backend()
