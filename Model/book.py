from Model.db import DbModel
from Model.movement import MovementBook
import datetime
from tinydb import where


class Book(DbModel):
    def __init__(self, title: str, author: str, isbn: str, book_type: str):
        super().__init__()
        self.book_table = self.instance.table('book')
        self._title: str = title
        self._author: str = author
        self._isbn: str = isbn
        self._book_type: str = book_type
        self._available: bool = True

    def register(self) -> int:
        return self.book_table.insert(self.get_json)

    def delete_book(self, isbn: str) -> bool:
        deleted_book: list = self.book_table.remove(where('isbn') == isbn)
        return len(deleted_book) > 0

    def get_all_books(self) -> list:
        return self.book_table.all()

    def isbn_exist(self, isbn: str) -> bool:
        tmp_book = self.book_table.search(where('isbn') == isbn)
        return len(tmp_book) > 0

    def get_book(self, isbn: str) -> dict | None:
        tmp_book = self.book_table.search(where('isbn') == isbn)
        if tmp_book:
            return tmp_book[0]
        return tmp_book

    def update_book(self, isbn: str, title: str, author: str, book_type: str) -> bool:
        updated_book: list = self.book_table.update({'title': title, 'author': author, 'book_type': book_type}, where('isbn') == isbn)
        return len(updated_book) > 0

    def get_available_book(self) -> list:
        results = []
        for book in self.get_all_books():
            date_start = datetime.datetime.strptime("2021-01-01", '%Y-%m-%d')
            date_end = datetime.datetime.strptime("2021-01-01", '%Y-%m-%d')
            is_available: bool = MovementBook(book['isbn'], 1, date_start, date_end).book_is_available()
            if is_available:
                results.append(book)
        return results

    def get_not_available_book(self) -> list:
        results = []
        for book in self.get_all_books():
            date_start = datetime.datetime.strptime("2021-01-01", '%Y-%m-%d')
            date_end = datetime.datetime.strptime("2021-01-01", '%Y-%m-%d')
            is_available: bool = MovementBook(book['isbn'], 1, date_start, date_end).book_is_available()
            if not is_available:
                results.append(book)
        return results

    def __str__(self):
        return f"{self.title} by {self.author} - {self.isbn} - status : {self.available}"

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def book_type(self):
        return self._book_type

    @property
    def available(self):
        return self._available

    @property
    def get_json(self) -> dict:
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'book_type': self.book_type
        }


class PaperBook(Book):
    def __init__(self, title: str, author: str, isbn: str):
        super().__init__(title, author, isbn, "paper")

    def __str__(self):
        return f"Paperback: {self.title} by {self.author}"


class NumericBook(Book):
    def __init__(self, title: str, author: str, isbn: str):
        super().__init__(title, author, isbn, "numeric")

    def __str__(self):
        return f"Numeric: {self.title} by {self.author}"
