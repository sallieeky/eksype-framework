from model.migrations import Migrations


class MigrationsSeeder:
    def __init__(self):
        pass

    def seed():

        data = Migrations().create({
            "name": "migration_1",
            "alamat": "dwad"
        })

        return data
