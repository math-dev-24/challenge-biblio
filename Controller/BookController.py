from Model.book import Book
from Model.movement import MovementBook
from math import ceil


class BookController:
    def __init__(self):
        """
        Constructor -> init des Model
        """
        self.book: Book = Book("Titre", "Auteur", "ISBN", "paper")
        self.movement: MovementBook = MovementBook("ISBN", 1, "date", "date")

    def get_all_books(self) -> list:
        """
        Retourne tous les livres
        :return: liste de livres
        """
        return self.book.get_all_books()

    def get_all_books_page(self, page: int, per_page: int):
        """
        Retourne tous les livres avec les informations de pagination, je ne peux pas requêter une quantité avec tinyDb
        :param page: page courante
        :param per_page: nombre de livres par page
        :return: liste de livres avec les informations de pagination
        """
        list_books = self.get_all_books()
        available_books = self.get_available_books()
        for book in list_books:
            if book not in available_books:
                book['available'] = False
            else:
                book['available'] = True

        data = {
            "page": page,
            "per_page": per_page,
            "nb_books": len(list_books),
            "nb_pages": ceil(len(list_books) / per_page),
            "list_books": list_books[per_page * (page - 1): per_page * page]
        }

        return data

    def get_available_books(self) -> list:
        """
        Retourne les livres disponibles
        :return: liste de livres disponibles
        """
        return self.book.get_available_book()

    @staticmethod
    def create_book(title: str, author: str, isbn: str, book_type: str) -> bool:
        """
        Créer un livre
        :param title:
        :param author:
        :param isbn:
        :param book_type:
        :return: bool
        """
        tmp_book: Book = Book(title, author, isbn, book_type)
        is_registered: bool = tmp_book.register() > 0
        return is_registered

    def delete_book(self, isbn: str) -> bool:
        """
        Supprimer un livre
        :param isbn:
        :return: bool
        """
        is_deleted: bool = self.book.delete_book(isbn)
        is_deleted_mov: bool = False
        if is_deleted:
            is_deleted_mov = self.movement.delete_movement_by_isbn(isbn)
        return is_deleted_mov and is_deleted

    def get_book(self, isbn: str) -> dict:
        """
        Retourne un livre
        :param isbn: ISBN du livre
        :return: livre
        """
        tmp_book = self.book.get_book(isbn)
        if not tmp_book:
            return None
        available_books = self.get_available_books()
        if tmp_book not in available_books:
            tmp_book['available'] = False
        else:
            tmp_book['available'] = True

        return tmp_book

    def update_book(self, isbn: str, title: str, author: str, book_type: str) -> bool:
        """
        Mettre à jour un livre
        :param isbn:
        :param title:
        :param author:
        :param book_type:
        :return: bool
        """
        is_updated: bool = self.book.update_book(isbn, title, author, book_type)
        return is_updated
