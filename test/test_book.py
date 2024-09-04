from Model.book import Book
from tinydb import TinyDB
from tinydb.storages import MemoryStorage
import pytest


@pytest.fixture
def setup():
    Book.instance = TinyDB(storage=MemoryStorage)


@pytest.fixture
def book(setup):
    book = Book(title="Le livre de Bob", author="John Doe", isbn="1234443", book_type="paper")
    book.register()
    return book


def test_book_properties(book):
    assert book.title == "Le livre de Bob"
    assert book.author == "John Doe"
    assert book.isbn == "1234443"
    assert book.book_type == "paper"


def test_book_delete(book):
    is_delete: bool = book.delete_book(book.isbn)
    assert is_delete is True


def test_isbn_exist(book):
    is_exist: bool = book.isbn_exist(book.isbn)
    assert is_exist is True


def test_get_book(book):
    book_get = book.get_book(book.isbn)
    assert book_get['title'] == "Le livre de Bob"
