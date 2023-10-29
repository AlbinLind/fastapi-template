"""All models for the project are defined here."""
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class User(Base):
    """Database model for User."""

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
