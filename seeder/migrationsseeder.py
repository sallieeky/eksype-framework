from model.migrations import Migrations


class MigrationsSeeder:
    def __init__(self):
        pass

    def seed():
        Migrations().create({
            "name": "migration_1",
        })

        return True
