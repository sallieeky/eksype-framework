from migration.schema import Schema


class ClassName(Schema):
    def __init__(self):
        Schema.__init__(self)

    def schema(self):
        self.query += Schema.id()
        # insert additional schema here
        self.query += Schema.timestamps()
        return self.query

    def create(self):
        return f"""
        CREATE TABLE IF NOT EXISTS 
        table_name 
        (
            {self.schema()}
        );
        """

    def drop():
        return """
        DROP TABLE IF EXISTS table_name;
        """
