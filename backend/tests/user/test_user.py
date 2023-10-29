"""Tests for the user."""

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.models import User
from src.user.schemas import UserCreate
from tests.utils import generate_random_string


def test_add_client(client: TestClient, db: Session):
    """Tests adding a client via the api."""
    user = UserCreate(name=generate_random_string())
    req = client.post("/users/", json=user.model_dump())
    assert req.status_code == 200


def test_getting_client(client: TestClient, db: Session):
    """Tests getting a client via the api."""
    user = UserCreate(name=generate_random_string())
    req = client.post("/users/", json=user.model_dump())
    assert req.status_code == 200

    _id = db.query(User).where(User.name == user.name).first().id

    req = client.get(f"/users/{_id}")
    assert req.status_code == 200
    assert req.json()["name"] == user.name


def test_getting_multiple_clients(client: TestClient, db: Session):
    """Tests getting multiple clients via the api."""
    user1 = UserCreate(name=generate_random_string())
    user2 = UserCreate(name=generate_random_string())
    req = client.post("/users/", json=user1.model_dump())
    assert req.status_code == 200
    req = client.post("/users/", json=user2.model_dump())
    assert req.status_code == 200
    req = client.get("/users/", params={"limit": 2})
    assert req.status_code == 200
    assert len(req.json()) == 2
