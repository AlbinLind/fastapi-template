from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    # By setting from_attribute to true we can use this with the model of the
    # database object to validate it with pydantic
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class UserCreate(UserBase):
    # We do not want to pass an id when creating a database object.
    id: None = Field(default=None, exclude=True)
