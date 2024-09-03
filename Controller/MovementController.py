from Model.book import Book
from Core.printer import Message


class MovementController:
    def __init__(self):
        self.book: Book = Book("Titre", "Auteur", "ISBN", "paper")

    def get_all_movements(self):
        print("\n")
        Message.title("Liste des déplacements")
        list_movements: list = self.book.get_all_movements()
        for i, movement in enumerate(list_movements):
            Message.msg(f"{i + 1} | {movement.book.title} by {movement.book.author} - {movement.book.book_type}")
        print("\n")

    def create_movement(self):
        print("\n")
        Message.title("Ajouter un déplacement")
        while True:
            Message.question("Entrez le numéros ISBN du livre :")
            isbn: str = Message.input()
            if isbn:

                break
            else:
                Message.warning("Le numéros ISBN est obligatoire")
        while True:
            Message.question("Date de début de l'emprunt :")
            date_start: str = Message.input()
            if date_start:
                break
            else:
                Message.warning("La date de début est obligatoire")
        while True:
            Message.question("Date de fin de l'emprunt :")
            date_end: str = Message.input()
            if date_end:
                break
            else:
                Message.warning("La date de fin est obligatoire")
