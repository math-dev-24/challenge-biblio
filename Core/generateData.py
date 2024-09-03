from faker import Faker
from Controller.BookController import BookController
from Controller.UserController import UserController


def generate_book():
    book_controller: BookController = BookController()
    faker = Faker(locale="fr_FR")
    for i in range(20):
        book_controller.create_book(faker.bothify(text='Livre ???'), faker.name(), faker.numerify(text='########'), "paper")


def generate_user():
    user_controller: UserController = UserController()
    faker = Faker(locale="fr_FR")
    for i in range(35):
        user_controller.create_user(faker.first_name(), faker.last_name(), faker.password(length=8), faker.email())


if __name__ == '__main__':
    generate_book()
    generate_user()
