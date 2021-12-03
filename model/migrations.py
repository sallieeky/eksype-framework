from model.model import Model


class Migrations(Model):
    def __init__(self):
        Model.__init__(self, "migrations")
