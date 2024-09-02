from Model.db import DbModel


class Book(DbModel):
    def __init__(self, title: str, author: str, isbn: str, book_type: str):
        super().__init__()
        self._title: str = title
        self._author: str = author
        self._isbn: str = isbn
        self._book_type: str = book_type

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
    def get_json(self) -> dict:
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'book_type': self.book_type
        }

    def register(self):
        self.instance.table('book').insert(self.get_json)

    def get_all_books(self):
        return self.instance.table('book').all()


class Paperback(Book):
    def __init__(self, title: str, author: str, isbn: str):
        super().__init__(title, author, isbn, "paper")

    def __str__(self):
        return f"Paperback: {self.title} by {self.author}"


class NumericBook(Book):
    def __init__(self, title: str, author: str, isbn: str):
        super().__init__(title, author, isbn, "numeric")

    def __str__(self):
        return f"Numeric: {self.title} by {self.author}"
