from Model.db import DbModel
from tinydb import Query
import datetime


class MovementBook(DbModel):
    def __init__(self, isbn: str, date_start: datetime, date_end: datetime):
        super().__init__()
        self._isbn: str = isbn
        self._date_start: datetime = date_start
        self._date_end: datetime = date_end

    def get_all_movements(self) -> list:
        return self.instance.table('movement').all()

    def book_is_available(self) -> bool:
        available: bool = True
        movement = Query()
        tmp_book = self.instance.table('movement').search(movement.isbn == self._isbn)
        if tmp_book:
            for bk in tmp_book:
                if bk['date_start'] <= self._date_start <= bk['date_end']:
                    available = False
                    break
        return available

    def register(self) -> None:
        self.instance.table('movement').insert({
            'isbn': self._isbn,
            'date_start': self._date_start,
            'date_end': self._date_end
        })

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def date_start(self) -> datetime:
        return self._date_start

    @property
    def date_end(self) -> datetime:
        return self._date_end

    def __str__(self):
        return f"{self.isbn} - {self.date_start} - {self.date_end}"
