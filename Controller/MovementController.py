from Model.book import Book
from Model.movement import MovementBook
from Model.user import User
from datetime import datetime
from math import ceil


class MovementController:
    def __init__(self):
        """
        Constructor -> initialisation des models
        """
        self.book: Book = Book("Titre", "Auteur", "ISBN", "paper")
        self.movement: MovementBook = MovementBook("ISBN", 1, "date", "date")
        self.user: User = User("<NAME>", "<NAME>", "<NAME>", "<NAME>")

    def get_all_movements(self):
        """
        Retourne toutes les movements
        :return: liste de tous les movements
        """
        return self.movement.get_all_movements()

    @staticmethod
    def create_movement(user_id: int, isbn: str, date_start: str, date_end: str):
        """
        Crée un nouveau mouvement
        :param user_id: id de l'utilisateur
        :param isbn: isbn du livre
        :param date_start: date de début du mouvement
        :param date_end: date de fin du mouvement
        :return: str ->  message de réussite ou erreur
        """
        list_movements = MovementController().get_movements_by_isbn(isbn)
        date_start = datetime.strptime(date_start, '%Y-%m-%d')
        date_end = datetime.strptime(date_end, '%Y-%m-%d')

        for movement in list_movements:
            tmp_date_start = datetime.strptime(movement['date_start'], '%Y-%m-%d')
            tmp_date_end = datetime.strptime(movement['date_end'], '%Y-%m-%d')
            if tmp_date_start <= date_start <= tmp_date_end or tmp_date_start <= date_end <= tmp_date_end or (
                    tmp_date_start <= date_start and tmp_date_end >= date_end):
                return "Non disponible"

        tmp_movement = MovementBook(isbn, user_id, date_start, date_end)
        tmp_movement.register()
        return "ok"

    def get_movements_by_isbn(self, isbn: str):
        """
        Retourne tous les mouvements d'un livre
        :param isbn: isbn du livre
        :return: liste de tous les mouvements
        """
        tmp_movement = self.movement.get_all_movement_by_isbn(isbn)
        if tmp_movement:
            for movement in tmp_movement:
                user_id: int = int(movement['user_id'])
                user = self.user.get_user_by_id(user_id)[0]
                movement['user'] = user
        return tmp_movement

    def get_movements_by_user_id(self, user_id: str):
        """
        Retourne tous les mouvements d'un utilisateur
        :param user_id: id de l'utilisateur
        :return: liste de tous les mouvements
        """
        tmp_movements = self.movement.get_all_movements_by_user_id(user_id)
        for movement in tmp_movements:
            user_id: int = int(movement['user_id'])
            user = self.user.get_user_by_id(user_id)[0]
            movement['user'] = user
            isbn = movement['isbn']
            movement['book'] = self.book.get_book(isbn)
        return tmp_movements

    def get_movements_in_today(self):
        """
        Retourne tous les mouvements de la journée
        :return: liste de tous les mouvements
        """
        today = datetime.today()
        return self.movement.get_all_movements_in_today(today)

    def get_all_movements_page(self, page: int, per_page: int):
        """
        Retourne tous les mouvements -> gestion des pages impossible avec tinyDb
        :param page: page courante
        :param per_page: nombre de mouvements par page
        :return: liste de tous les mouvements
        """
        list_movements = self.get_all_movements()
        available_movements = self.get_movements_in_today()
        for movement in list_movements:
            if movement not in available_movements:
                movement['available'] = False
            else:
                movement['available'] = True
            movement['book'] = self.book.get_book(movement['isbn'])
            movement['user'] = self.user.get_user_by_id(int(movement['user_id']))[0]

        data = {
            "page": page,
            "per_page": per_page,
            "nb_movements": len(list_movements),
            "nb_pages": ceil(len(list_movements) / per_page),
            "list_movements": list_movements[per_page * (page - 1): per_page * page]
        }

        return data

    def delete_movements(self, movement_id: str, isbn: str):
        """
        Supprime un mouvement
        :param movement_id: id du mouvement
        :param isbn: isbn du livre
        :return: str -> message de réussite ou erreur
        """
        return self.movement.delete_movements(movement_id, isbn)

    def get_movement_by_isbn_and_user_id(self, isbn: str, user_id: str):
        """
        Retourne un mouvement par son isbn et son id
        :param isbn: isbn du livre
        :param user_id: id de l'utilisateur
        :return: Movement -> le mouvement
        """
        movement = self.movement.get_movement_by_isbn_and_user_id(isbn, user_id)
        data = {
            "movement": movement,
            "book": self.book.get_book(movement['isbn']),
            "user": self.user.get_user_by_id(int(movement['user_id']))[0],
        }
        return data

    def update_movement(self, isbn: str, date_end: str) -> bool:
        """
        Mettre à jour un mouvement
        :param isbn:
        :param date_end:
        :return:
        """
        return self.movement.update_movement(isbn, date_end)