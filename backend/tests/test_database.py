"""Tests the database methods."""

from sqlalchemy import text

from src.database import database


def test_database_fetch_one():
    """Tests the database fetch one method."""
    query = text("SELECT 1")
    result = database.fetch_one(query)
    assert result == 1


def test_database_fetch_all():
    """Tests the database fetch all method."""
    query = text("SELECT 1")
    result = database.fetch_all(query)
    assert result == [1]

    # Test a more complex query
    query = text("SELECT 1 UNION SELECT 2")
    result = database.fetch_all(query)
    assert result == [1, 2]


def test_database_execute():
    """Tests the database execute method."""
    query = text("SELECT 1")
    result = database.execute(query)
    assert result is None
