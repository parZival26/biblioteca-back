from typing import Annotated
from sqlmodel import Session, create_engine
from fastapi import Depends

postgresUrl = "postgresql://biblioteca_user:biblioteca_pass@localhost:5432/biblioteca"

engine = create_engine(
    postgresUrl,
)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
