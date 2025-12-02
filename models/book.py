from typing import Annotated
from enum import Enum

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Room(str, Enum):
    sala1 = "sala1"
    sala3 = "sala3"
    sala4 = "sala4"


class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    author: str = Field(index=True)
    year: int | None = Field(default=None)

    room: Room = Field(default=Room.sala1)
    bookShelf: int = Field(default=1, ge=1, le=40)


# Code below omitted 👇
