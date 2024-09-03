from Model.db import DbModel
from Model.movement import MovementBook
import datetime
from tinydb import where


class Book(DbModel):
    def __init__(self, title: str, author: str, isbn: str, book_type: str):
        super().__init__()
        self._title: str = title
        self._author: str = author
        self._isbn: str = isbn
        self._book_type: str = book_type
        self._available: bool = True

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

    def register(self):
        self.instance.table('book').insert(self.get_json)

    def delete_book(self, isbn: str):
        self.instance.table('book').remove(where('isbn') == isbn)

    def get_all_books(self):
        list_books: list[Book] = []
        for book in self.instance.table('book').all():
            list_books.append(Book(book['title'], book['author'], book['isbn'], book['book_type']))
        return list_books

    def isbn_exist(self, isbn: str):
        tmp_book = self.instance.table('book').search(where('isbn') == isbn)
        return True if tmp_book else False

    def get_book(self, isbn: str):
        tmp_book = self.instance.table('book').search(where('isbn') == isbn)[0]
        return Book(tmp_book['title'], tmp_book['author'], tmp_book['isbn'], tmp_book['book_type'])

    @property
    def get_available_book(self):

        return ""

    def __str__(self):
        return f"{self.title} by {self.author} - {self.isbn} - status : {self.available}"


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
