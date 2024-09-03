from Core.printer import Message
from Model.book import Book


class BookController:
    def __init__(self):
        self.book: Book = Book("Titre", "Auteur", "ISBN", "paper")

    @staticmethod
    def question_create_book():
        while True:
            Message.question("Quel est le titre du livre ?")
            title: str = Message.input()
            if title:
                break
            else:
                Message.warning("Le titre du livre est obligatoire")

        while True:
            Message.question("Quel est l'auteur du livre ?")
            author: str = Message.input()
            if author:
                break
            else:
                Message.warning("L'auteur du livre est obligatoire")

        while True:
            Message.question("Quel est l'ISBN du livre ?")
            isbn: str = Message.input()
            if isbn:
                break
            else:
                Message.warning("L'ISBN du livre est obligatoire")

        while True:
            Message.question("Quel type de livre voulez-vous ?")
            Message.info("1. Paperback")
            Message.info("2. Numeric")
            book_type: str = Message.input()

            if book_type == "1":
                BookController.create_book(title, author, isbn, "paper")
                break
            elif book_type == "2":
                BookController.create_book(title, author, isbn, "numeric")
                break
            else:
                Message.warning("Type de livre non reconnu")

    def question_delete_book(self):
        while True:
            Message.question("Quel est le numéros ISBN du livre ?")
            isbn: str = Message.input()
            if isbn == "return":
                break
            if isbn and self.book.isbn_exist(isbn):
                self.book.delete_book(isbn)
                break
            else:
                Message.warning("Le numéros ISBN est obligatoire et/ou invalide")

    def question_update_book(self):
        while True:
            Message.question("Quel est le numéros ISBN du livre ?")
            isbn: str = Message.input()
            if isbn == "return":
                break
            if isbn and self.book.isbn_exist(isbn):
                break
            else:
                Message.warning("Le numéros ISBN est obligatoire et/ou invalide")

        tmp_book: Book = self.book.get_book(isbn)
        Message.info(f"{tmp_book}")

        Message.question("Nouveau titre du livre : (entrer pour conserver l'ancien)")
        title: str = Message.input()
        if not title:
            title = tmp_book.title
        Message.question("Nouveau auteur du livre : (entrer pour conserver l'ancien)")
        author: str = Message.input()
        if not author:
            author = tmp_book.author

        new_book: Book = Book(title, author, tmp_book.isbn, tmp_book.book_type)
        new_book.register()
        Message.info("Modification effectuée")

    def get_all_books(self):
        print("\n")
        Message.title("Liste des livres")
        list_books: list = self.book.get_all_books()
        for i, book in enumerate(list_books):
            Message.msg(f"{i + 1} | {book}")
        print("\n")

    @staticmethod
    def create_book(title: str, author: str, isbn: str, book_type: str):
        tmp_book: Book = Book(title, author, isbn, book_type)
        tmp_book.register()
