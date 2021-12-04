from migration.schema import Schema


class User(Schema):
    def __init__(self):
        Schema.__init__(self)

    def schema(self):
        self.query += Schema().id()
        self.query += Schema().varchar("username")
        self.query += Schema().varchar("password")
        self.query += Schema().timestamps()
        return self.query

    def create(self):
        return f"""
        CREATE TABLE IF NOT EXISTS 
        user 
        (
            {self.schema()}
        );
        """

    def drop():
        return """
        DROP TABLE IF EXISTS user;
        """
