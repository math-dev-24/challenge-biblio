from Model.book import Book
from Model.movement import MovementBook


class MovementController:
    def __init__(self):
        self.book: Book = Book("Titre", "Auteur", "ISBN", "paper")
        self.movement: MovementBook = MovementBook("ISBN", "date", "date")

    def get_all_movements(self):
        return self.movement.get_all_movements()