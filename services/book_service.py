from repositories.book_repository import BookRepository
from models.book import Book
from schemas.book_schema import BookCreate, BookUpdate


class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def create_book(self, book_data: BookCreate) -> Book:
        book = Book(**book_data.model_dump())
        return self.repository.create(book)

    def get_book(self, book_id: int) -> Book | None:
        return self.repository.get_by_id(book_id)

    def list_books(self, skip: int = 0, limit: int = 100) -> list[Book]:
        return self.repository.get_all(skip, limit)

    def update_book(self, book_id: int, book_data: BookUpdate) -> Book | None:
        book = Book(**book_data.model_dump())
        return self.repository.update(book_id, book)

    def delete_book(self, book_id: int) -> bool:
        return self.repository.delete(book_id)
