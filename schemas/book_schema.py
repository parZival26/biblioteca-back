from pydantic import BaseModel, ConfigDict
from models.book import Room


class BookBase(BaseModel):
    title: str
    author: str
    year: int | None = None
    room: Room = Room.sala1
    bookShelf: int = 1


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookResponse(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
