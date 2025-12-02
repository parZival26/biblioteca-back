from pydantic import BaseModel, ConfigDict
from datetime import datetime
from models.book import Room


class ReportBase(BaseModel):
    bookId: int
    roomFound: Room = Room.sala1
    bookShelfFound: int = 1


class ReportCreate(ReportBase):
    pass


class ReportResponse(ReportBase):
    id: int
    date: datetime

    model_config = ConfigDict(from_attributes=True)
