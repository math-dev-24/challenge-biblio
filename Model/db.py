from tinydb import TinyDB, Query, where
import os


class DbModel:
    def __init__(self):
        self.db_path = os.path.join("./db.json")
        self.instance = TinyDB(self.db_path)
