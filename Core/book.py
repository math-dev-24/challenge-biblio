from Core.printer import Message
from Model.book import Paperback, NumericBook

def create_book():
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
            tmp_book: Paperback = Paperback(title, author, isbn)
            tmp_book.register()
            break
        elif book_type == "2":
            tmp_book: NumericBook = NumericBook(title, author, isbn)
            tmp_book.register()
            break
        else:
            Message.warning("Type de livre non reconnu")