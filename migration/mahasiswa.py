from migration.schema import Schema


class Mahasiswa(Schema):
    def __init__(self):
        Schema.__init__(self)

    def schema(self):
        self.query += Schema().id()
        self.query += Schema().timestamps()
        return self.query

    def create(self):
        return f"""
        CREATE TABLE IF NOT EXISTS 
        mahasiswa 
        (
            {self.schema()}
        );
        """

    def drop():
        return """
        DROP TABLE IF EXISTS mahasiswa;
        """
