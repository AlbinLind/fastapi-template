"""Database module."""
from typing import Generator, TypeVar

from loguru import logger
from sqlalchemy import Result, Insert, Select, Update, create_engine
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import Session, as_declarative, sessionmaker

from src.config import settings


@as_declarative()
class Base:
    """Base class for all the models."""

    id: int
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        """Converts the class name to lower case and makes it the table name."""
        return cls.__name__.lower()

    def dict(self) -> dict[str, any]:
        """Generates a dictionary with all the column names and their values.

        Returns:
        -------
            dict[str, any]: Dictionary with the keys and values
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Model = TypeVar("Model", bound=Base)


class Database:
    """Class for the database and convinent functions."""

    def __init__(self, database_url: str = settings.database_url) -> None:
        """Initializes the database."""
        self.database_url = database_url
        logger.debug("Connecting to database at {}", self.database_url)
        self.engine = create_engine(self.database_url)
        self.db = next(self._get_db())
        
    def _get_db(self) -> Generator[Session, None, None]:
        """Get a database session.

        Yields:
            Generator[Session, None, None]: Database session
        """
        db = sessionmaker(self.engine)()
        logger.info("Created a session, you should not see this after initialisation.")
        try:
            yield db
        finally:
            db.close()

    def fetch_one(self, query: Select | Insert | Update) -> Model | None:
        """Fetches one row from the database.

        Args:
            query (Select | Insert | Update): query to execute

        Returns:
            Model | None: object of the model or none if no row is found
        """   

        logger.debug("Executing query {} for one object", query)
        result: Result = self.db.execute(query).first()
        self.db.commit()
        
        return result[0]

    def fetch_all(self, query: Select | Insert | Update) -> list[Model] | None:
        """Fetches all the rows from the database.

        Args:
            query (Select | Insert | Update): query to execute

        Returns:
            list[Model] | None: list of objects of the model or none if no row is found
        """
        logger.debug("Executing query {} for all objects", query)
        result: Result = self.db.execute(query).all()
        self.db.commit()

        # The result is a sequenced tuple like object, but we only want the first part of the tuple
        return [res[0] for res in result]

    def execute(self, query: Insert | Update) -> None:
        """Executes the query, but does not fetch any rows.

        Args:
            query (Insert | Update): query to execute
        """
        logger.debug("Executing query {}", query)
        self.db.execute(query)
        self.db.commit()

    def add(self, model_list: Model | list[Model]) -> None:
        """Add one or more objects to the database.

        Args:
            model_list (Model | list[Model]): object or list of objects to add
        """
        # If we get a single model, convert it to a list
        if not isinstance(model_list, list):
            logger.debug("Converting single model to list")
            model_list = [model_list]

        logger.info("Adding {} objects to database", len(model_list))
        self.db.add_all(model_list)
        self.db.commit()


database = Database()
