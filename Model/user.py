from db import DbModel


class User(DbModel):
    def __init__(self, first_name: str, last_name: str):
        super().__init__()
        self.first_name: str = first_name
        self.last_name: str = last_name
