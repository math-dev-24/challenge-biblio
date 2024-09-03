from tinydb import TinyDB, Query, where
import os


class DbModel:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(base_dir, "db.json")
        self.instance = TinyDB(self.db_path)
