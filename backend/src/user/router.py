from fastapi import APIRouter
from sqlalchemy import select, text

from src.database import database
from src.models import User
from src.user.schemas import UserBase, UserCreate

router = APIRouter()


@router.get("/")
def get_all_user(limit: int = 30, offset: int = 30) -> list[UserBase]:
    query = select(User)
    query_result = database.fetch_all(query)
    return query_result


@router.get("/{user_id}")
def get_user_by_id(user_id: int) -> UserBase:
    query = select(User).where(User.id == user_id)
    return database.fetch_one(query)


@router.post("/")
def add_user(user: UserCreate) -> dict[str, str]:
    user = User(**user.model_dump())
    database.add(user)
    return {"message": "User created"}
