class Schema:
    def __init__(self):
        self.query = ""

    def id(self, field='id'):
        return f"{field} INTEGER PRIMARY KEY AUTO_INCREMENT,"

    def timestamps(self):
        return "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"

    def varchar(self, field, length=255, null=False):
        return f"{field} VARCHAR({length}) {'NOT NULL' if null == False else ''},"

    def integer(self, field, length=20, null=False):
        return f"{field} INT({length}) {'NOT NULL' if null == False else ''},"

    def char(self, field, length=255, null=False):
        return f"{field} CHAR({length}) {'NOT NULL' if null == False else ''},"

    def text(self, field, null=False):
        return f"{field} TEXT {'NOT NULL' if null == False else ''},"

    def boolean(self, field, null=False):
        return f"{field} BOOLEAN {'NOT NULL' if null == False else ''},"

    def float(self, field, null=False):
        return f"{field} FLOAT {'NOT NULL' if null == False else ''},"

    def datetime(self, field, null=False):
        return f"{field} DATETIME {'NOT NULL' if null == False else ''},"

    def date(self, field, null=False):
        return f"{field} DATE {'NOT NULL' if null == False else ''},"
