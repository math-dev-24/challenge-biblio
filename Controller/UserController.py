from Model.user import User
from Model.movement import MovementBook
from math import ceil


class UserController:
    def __init__(self):
        """
        Constructor -> init model
        """
        self.user = User("test", "test", "test", "test@test.com")
        self.movement: MovementBook = MovementBook("ISBN", 1, "date", "date")

    @staticmethod
    def create_user(first_name: str, last_name: str, password: str, email: str):
        """
        Create a new user
        :param first_name: first name of the user
        :param last_name: last name of the user
        :param password: password of the user
        :param email: email of the user
        :return: the created user
        """
        user = User(first_name, last_name, password, email)
        user.save()
        return user

    def get_all_users(self) -> list:
        """
        Get all users
        :return: list of users
        """
        return self.user.get_all_users()

    def get_all_users_page(self, page: int, per_page: int) -> dict:
        """
        Get all users
        :param page: page number
        :param per_page: number of users per page
        :return: list of users
        """
        users = self.get_all_users()
        for user in users:
            user['movements'] = self.movement.get_all_movements_by_user_id(str(user['id']))

        data = {
            "page": page,
            "per_page": per_page,
            "nb_users": len(users),
            "nb_pages": ceil(len(users) / per_page),
            "list_users": users[per_page * (page - 1): per_page * page]
        }
        return data

    def delete_user(self, user_id: str) -> bool:
        """
        Delete a user
        :param user_id:
        :return: bool
        """
        is_deleted: bool = self.user.delete_user(user_id)
        is_deleted_mov: bool = False
        if is_deleted:
            is_deleted_mov = self.movement.delete_movement_by_user_id(int(user_id))
        return is_deleted and is_deleted_mov

    def get_user_by_id(self, user_id: int) -> dict:
        """
        Get a user by id
        :param user_id: id of the user
        :return: user
        """
        return self.user.get_user_by_id(user_id)[0]

    def get_user_by_email(self, email: str) -> dict:
        """
        Get a user by email
        :param email: email of the user
        :return: user
        """
        return self.user.get_user_by_email(email)[0]

    def update_user(self, user_id: int, first_name: str, last_name: str, email: str) -> bool:
        """
        Update a user
        :param user_id: id of the user
        :param first_name: first name of the user
        :param last_name: last name of the user
        :param email: email of the user
        :return: bool
        """
        is_updated: bool = self.user.update_user(user_id, first_name, last_name, email)
        return is_updated
