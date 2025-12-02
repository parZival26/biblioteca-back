from datetime import datetime
from sqlmodel import Field, SQLModel

from models.book import Room


class Report(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    bookId: int = Field(foreign_key="book.id")
    roomFound: Room = Field(default=Room.sala1)
    bookShelfFound: int = Field(default=1, ge=1, le=40)
    date: datetime = Field(default_factory=datetime.utcnow)
