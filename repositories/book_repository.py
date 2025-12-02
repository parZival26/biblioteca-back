from sqlmodel import Session, select
from models.book import Book


class BookRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, book: Book) -> Book:
        self.session.add(book)
        self.session.commit()
        self.session.refresh(book)
        return book

    def get_by_id(self, book_id: int) -> Book | None:
        return self.session.get(Book, book_id)

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Book]:
        statement = select(Book).offset(skip).limit(limit)
        return list(self.session.exec(statement).all())

    def update(self, book_id: int, book_data: Book) -> Book | None:
        db_book = self.session.get(Book, book_id)
        if not db_book:
            return None

        db_book.title = book_data.title
        db_book.author = book_data.author
        db_book.year = book_data.year
        db_book.room = book_data.room
        db_book.bookShelf = book_data.bookShelf

        self.session.add(db_book)
        self.session.commit()
        self.session.refresh(db_book)
        return db_book

    def delete(self, book_id: int) -> bool:
        db_book = self.session.get(Book, book_id)
        if not db_book:
            return False

        self.session.delete(db_book)
        self.session.commit()
        return True
