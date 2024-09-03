from Model.book import Book
from Model.movement import MovementBook
from datetime import datetime


class MovementController:
    def __init__(self):
        self.book: Book = Book("Titre", "Auteur", "ISBN", "paper")
        self.movement: MovementBook = MovementBook("ISBN", 1,"date", "date")

    def get_all_movements(self):
        return self.movement.get_all_movements()

    @staticmethod
    def create_movement(user_id: int, isbn: str, date_start: str, date_end: str):
        list_movements = MovementController().get_movement_by_isbn(isbn)
        date_start = datetime.strptime(date_start, '%Y-%m-%d')
        date_end = datetime.strptime(date_end, '%Y-%m-%d')

        for movement in list_movements:
            tmp_date_start = datetime.strptime(movement['date_start'], '%Y-%m-%d')
            tmp_date_end = datetime.strptime(movement['date_end'], '%Y-%m-%d')
            if tmp_date_start <= date_start <= tmp_date_end or tmp_date_start <= date_end <= tmp_date_end or (tmp_date_start <= date_start and tmp_date_end >= date_end):
                return "Non disponible"

        tmp_movement = MovementBook(isbn, user_id, date_start, date_end)
        tmp_movement.register()
        return "ok"

    def get_movement_by_isbn(self, isbn: str):
        return self.movement.get_all_movement_by_isbn(isbn)

    def get_movement_by_user_id(self, user_id: int):
        return self.movement.get_all_movement_by_user_id(user_id)

