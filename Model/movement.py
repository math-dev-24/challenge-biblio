from Model.db import DbModel
from tinydb import Query
from datetime import datetime


class MovementBook(DbModel):
    def __init__(self, isbn: str, date_start: datetime, date_end: datetime):
        super().__init__()
        self._isbn: str = isbn
        self._date_start: datetime = date_start
        self._date_end: datetime = date_end

    def get_all_movements(self) -> list:
        return self.instance.table('movement').all()

    def get_all_movement_by_isbn(self, isbn: str) -> list:
        return self.instance.table('movement').search(Query().isbn == isbn)

    def book_is_available(self) -> bool:
        available: bool = True
        movement = Query()
        tmp_movements = self.instance.table('movement').search(movement.isbn == self._isbn)
        if tmp_movements:
            for movement in tmp_movements:

                date_start = datetime.strptime(movement['date_start'], '%Y-%m-%d')
                date_end = datetime.strptime(movement['date_end'], '%Y-%m-%d')
                current_date = datetime.now()

                if date_start <= current_date <= date_end:
                    available = False
                    break
        return available

    def register(self) -> None:
        self.instance.table('movement').insert({
            'isbn': self._isbn,
            'date_start': self._date_start.isoformat().split('T')[0],
            'date_end': self._date_end.isoformat().split('T')[0],
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
