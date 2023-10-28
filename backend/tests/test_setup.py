"""Tests the database connection and queries."""

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


def test_db_connection(db: Session):
    """Tests the database connection."""
    assert db.query("*") is not None


def test_client(client: TestClient):
    """Tests the client."""
    assert client is not None
