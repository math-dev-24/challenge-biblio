from Model.db import DbModel
from hashlib import sha256
from tinydb import where


class User(DbModel):
    def __init__(self, first_name: str, last_name: str, password: str, email: str):
        super().__init__()
        self.user_table = self.instance.table('users')
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.password: str = password
        self.email: str = email

    def get_next_id(self) -> int:
        last_record = self.user_table.all()[-1] if len(self.user_table) > 0 else None
        return last_record.doc_id + 1 if last_record else 1

    def save(self) -> int:
        data: dict = self.get_json()
        data['password'] = self.has_password()
        return self.user_table.insert(data)

    def has_password(self) -> str:
        salt: str = "efdg"
        tmp_password: str = self.password + salt
        hash_password = salt + sha256(tmp_password.encode()).hexdigest()
        return hash_password

    def get_json(self) -> dict:
        return {
            'id': self.get_next_id(),
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }

    def get_all_users(self) -> list:
        return self.user_table.all()

    def delete_user(self, user_id: str) -> bool:
        deleted_user: list = self.user_table.remove(where('id') == int(user_id))
        return len(deleted_user) > 0

    def get_user_by_id(self, user_id: int) -> list:
        return self.user_table.search(where('id') == user_id)

    def get_user_by_email(self, email: str) -> list:
        return self.user_table.search(where('email') == email)
