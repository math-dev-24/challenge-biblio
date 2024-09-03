from faker import Faker
from Controller.BookController import BookController

if __name__ == '__main__':
    BookController: BookController = BookController()
    faker = Faker(locale="fr_FR")
    for i in range(20):
        BookController.create_book(
            faker.bothify(text='Livre ???'), faker.name(), faker.numerify(text='########'), "paper"
        )
