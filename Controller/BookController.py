from Model.book import Book


class BookController:
    def __init__(self):
        self.book: Book = Book("Titre", "Auteur", "ISBN", "paper")

    def get_all_books(self):
        list_books = self.book.get_all_books()
        available_books = self.available_books()
        for book in list_books:
            if book not in available_books:
                book['available'] = False
            else:
                book['available'] = True

        list_books.sort(key=lambda x: x['available'], reverse=True)
        return list_books

    def available_books(self) -> list:
        return self.book.get_available_book()

    @staticmethod
    def create_book(title: str, author: str, isbn: str, book_type: str):
        tmp_book: Book = Book(title, author, isbn, book_type)
        tmp_book.register()

    def delete_book(self, isbn: str):
        self.book.delete_book(isbn)
        return True

    def get_book(self, isbn: str):
        tmp_book = self.book.get_book(isbn)
        available_books = self.available_books()
        if tmp_book not in available_books:
            tmp_book['available'] = False
        else:
            tmp_book['available'] = True

        return tmp_book

