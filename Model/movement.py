from Model.db import DbModel
from tinydb import Query, where
from datetime import datetime


class MovementBook(DbModel):
    def __init__(self, isbn: str, user_id: int, date_start: datetime, date_end: datetime):
        super().__init__()
        self.user_id: int = user_id
        self._isbn: str = isbn
        self.movement_table = self.instance.table('movement')
        self._date_start: datetime = date_start
        self._date_end: datetime = date_end

    def get_all_movements(self) -> list:
        return self.movement_table.all()

    def get_all_movement_by_isbn(self, isbn: str) -> list:
        return self.movement_table.search(Query().isbn == isbn)

    def book_is_available(self) -> bool:
        available: bool = True
        movement = Query()
        tmp_movements = self.movement_table.search(movement.isbn == self._isbn)
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
        self.movement_table.insert({
            "user_id": self.user_id,
            'isbn': self._isbn,
            'date_start': self._date_start.isoformat().split('T')[0],
            'date_end': self._date_end.isoformat().split('T')[0],
        })

    def get_all_movements_by_user_id(self, user_id: str) -> list:
        return self.movement_table.search(Query().user_id == user_id)

    def get_all_movements_in_today(self, today: datetime) -> list:
        return self.movement_table.search(Query().date_start <= today.isoformat().split('T')[0] <= Query().date_end)

    def delete_movement_by_isbn(self, isbn: str) -> bool:
        deleted_movement: list = self.movement_table.remove(where('isbn') == isbn)
        return len(deleted_movement) > 0

    def delete_movement_by_user_id(self, user_id: int) -> bool:
        deleted_movement: list = self.movement_table.remove(where('user_id') == user_id)
        return len(deleted_movement) > 0
