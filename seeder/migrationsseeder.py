from model.migrations import Migrations


class MigrationsSeeder:
    def __init__(self):
        pass

    def seed():
        Migrations().create({
            "name": "migration_1",
            "alamat": "dwad"
        })
        Migrations().create({
            "name": "migration_2",
            "alamat": "jl. Ahmad Yani"
        })
        Migrations().create({
            "name": "migration_3",
            "alamat": "Jalan Jend Soedirman"
        })

        return True
