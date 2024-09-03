from Model.user import User


class UserController:
    def __init__(self):
        self.user = User("test", "test", "test", "test@test.com")

    @staticmethod
    def create_user(first_name: str, last_name: str, password: str, email: str):
        user = User(first_name, last_name, password, email)
        user.save()
        return user

    def get_all_users(self):
        return self.user.get_all_users()

    def delete_user(self, user_id: int):
        return self.user.delete_user(user_id)

