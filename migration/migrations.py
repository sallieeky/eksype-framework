from migration.schema import Schema


class Migrations(Schema):
    def __init__(self):
        Schema.__init__(self)

    def schema(self):
        self.query += Schema().id()
        self.query += Schema().varchar("name")
        self.query += Schema().timestamps()
        return self.query

    def create(self):
        return f"""
        CREATE TABLE IF NOT EXISTS 
        migrations 
        (
            {self.schema()}
        );
        """

    def drop():
        return """
        DROP TABLE IF EXISTS migrations;
        """
