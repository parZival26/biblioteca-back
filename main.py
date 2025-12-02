from typing_extensions import Annotated
from fastapi import Depends, FastAPI
from sqlmodel import SQLModel
from contextlib import asynccontextmanager

from controllers.book_controller import router as book_router
from controllers.report_controller import router as report_router
from database import engine, get_session


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Include routers
app.include_router(book_router, dependencies=[Depends(get_session)])
app.include_router(report_router, dependencies=[Depends(get_session)])


@app.get("/")
async def root():
    return {"message": "Biblioteca API - use /docs for API documentation"}
