from book import Book
from user import User
from db import DbModel
import datetime


class MovementBook(DbModel):
    def __init__(self, book: Book, user: User, date_start: datetime, date_end: datetime):
        super().__init__()
        self._book: Book = book
        self._user: User = user
        self._date_start: datetime = date_start
        self._date_end: datetime = date_end


