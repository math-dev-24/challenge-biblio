from Model.user import User
from Model.movement import MovementBook
from math import ceil

class UserController:
    def __init__(self):
        self.user = User("test", "test", "test", "test@test.com")
        self.movement: MovementBook = MovementBook("ISBN", 1, "date", "date")

    @staticmethod
    def create_user(first_name: str, last_name: str, password: str, email: str):
        user = User(first_name, last_name, password, email)
        user.save()
        return user

    def get_all_users(self, page: int, per_page: int):
        users = self.user.get_all_users()
        for user in users:
            user['movements'] = self.movement.get_all_movements_by_user_id(str(user['id']))

        data = {
            "page": page,
            "per_page": per_page,
            "nb_pages": ceil(len(users) / per_page),
            "list_users": users[per_page * (page - 1): per_page * page]
        }
        return data

    def delete_user(self, user_id: str):
        is_deleted: bool = self.user.delete_user(user_id)
        is_deleted_mov: bool = False
        if is_deleted:
            is_deleted_mov = self.movement.delete_movement_by_user_id(user_id)
        return is_deleted and is_deleted_mov

    def get_user_by_id(self, user_id: int):
        return self.user.get_user_by_id(user_id)[0]

    def get_user_by_email(self, email: str):
        return self.user.get_user_by_email(email)[0]
