"""All models for the project are defined here."""
from sqlalchemy.orm import mapped_column, Mapped

from src.database import Base

class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()