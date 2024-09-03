from db import DbModel


class User(DbModel):
    def __init__(self, first_name: str, last_name: str):
        super().__init__()
        self.user_table = self.instance.table('users')
        self.first_name: str = first_name
        self.last_name: str = last_name

    def get_next_id(self):
        last_record = self.user_table.all()[-1] if len(self.user_table) > 0 else None
        return last_record.doc_id + 1 if last_record else 1

    def save(self):
        self.user_table.insert(self.get_json)

    def get_json(self):
        return {
            'id': self.get_next_id(),
            'first_name': self.first_name,
            'last_name': self.last_name
        }
