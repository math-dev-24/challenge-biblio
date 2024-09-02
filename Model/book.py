class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self._title: str = title
        self._author: str = author
        self._isbn: str = isbn

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn


class Paperback(Book):
    def __init__(self, title: str, author: str, isbn: str):
        super().__init__(title, author, isbn)

    def __str__(self):
        return f"Paperback: {self.title} by {self.author}"


class NumericBook(Book):
    def __init__(self, title: str, author: str, isbn: str):
        super().__init__(title, author, isbn)

    def __str__(self):
        return f"Numeric: {self.title} by {self.author}"
