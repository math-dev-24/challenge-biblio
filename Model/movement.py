from Model.db import DbModel
import datetime


class MovementBook(DbModel):
    def __init__(self, isbn: str, date_start: datetime, date_end: datetime):
        super().__init__()
        self._isbn: str = isbn
        self._date_start: datetime = date_start
        self._date_end: datetime = date_end

    def get_all_movements(self):
        return self.instance.table('movement').all()

    def bookIsAvailable(self, isbn: str):
        available: bool = True
        tmp_book = self.instance.table('movement').where('isbn=?', isbn).get_all()
        if tmp_book:
            for bk in tmp_book:
                if bk['date_start'] <= self._date_start <= bk['date_end']:
                    available = False
        return available

    def register(self):
        self.instance.table('movement').insert({
            'isbn': self._isbn,
            'date_start': self._date_start,
            'date_end': self._date_end
        })

    @property
    def isbn(self):
        return self._isbn

    @property
    def date_start(self):
        return self._date_start

    @property
    def date_end(self):
        return self._date_end

    def __str__(self):
        return f"{self.isbn} - {self.date_start} - {self.date_end}"