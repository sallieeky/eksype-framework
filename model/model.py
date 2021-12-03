import config

db, cursor = config.connect()


class Model:
    def __init__(self, table_name):
        self.table_name = table_name

    def all(self):
        cursor.execute(f"SELECT * FROM {self.table_name}")
        return cursor.fetchall()

    def find(self, id):
        cursor.execute(f"SELECT * FROM {self.table_name} WHERE id = '{id}'")
        return cursor.fetchone()

    def first(self):
        cursor.execute(f"SELECT * FROM {self.table_name} LIMIT 1")
        return cursor.fetchone()

    def last(self):
        cursor.execute(
            f"SELECT * FROM {self.table_name} ORDER BY id DESC LIMIT 1")
        return cursor.fetchone()

    def whereMany(self, column, operator, value):
        cursor.execute(
            f"SELECT * FROM {self.table_name} WHERE {column} {operator} '{value}'")
        return cursor.fetchall()

    def whereOnly(self, column, operator, value):
        cursor.execute(
            f"SELECT * FROM {self.table_name} WHERE {column} {operator} '{value}' LIMIT 1")
        return cursor.fetchone()
