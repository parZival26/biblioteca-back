from fastapi import APIRouter, HTTPException, status
from typing import Annotated
from sqlmodel import Session
from fastapi import Depends

from schemas.book_schema import BookCreate, BookUpdate, BookResponse
from repositories.book_repository import BookRepository
from services.book_service import BookService
from database import get_session


router = APIRouter(prefix="/books", tags=["books"])


def get_book_service(session: Session = Depends(get_session)) -> BookService:
    repository = BookRepository(session)
    return BookService(repository)


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(
    book: BookCreate, service: Annotated[BookService, Depends(get_book_service)]
):
    """Create a new book"""
    return service.create_book(book)


@router.get("/", response_model=list[BookResponse])
def list_books(
    service: Annotated[BookService, Depends(get_book_service)],
    skip: int = 0,
    limit: int = 100,
):
    """List all books with optional pagination"""
    return service.list_books(skip=skip, limit=limit)


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, service: Annotated[BookService, Depends(get_book_service)]):
    """Get a single book by ID"""
    book = service.get_book(book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return book


@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    book_data: BookUpdate,
    service: Annotated[BookService, Depends(get_book_service)],
):
    """Update a book by ID"""
    updated_book = service.update_book(book_id, book_data)
    if not updated_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return updated_book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(
    book_id: int, service: Annotated[BookService, Depends(get_book_service)]
):
    """Delete a book by ID"""
    success = service.delete_book(book_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return None
