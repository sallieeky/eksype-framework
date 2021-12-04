from migration.mahasiswa import Mahasiswa
from migration.migrations import Migrations

module_list = [
    Migrations,
    Mahasiswa
]


def migrate(table_name):
    return eval(table_name.capitalize()).create()


def migrate_all():
    module_return = []
    for i in module_list:
        module_return.append(i().create())

    return module_return


def drop(table_name):
    return eval(table_name.capitalize()).drop()


def make_migration(file_name):
    with open('default/migration.py', 'r') as reader:
        with open(f'migration/{file_name.lower()}.py', 'w') as writer:
            for line in reader:
                if 'class ClassName(Schema):' in line:
                    line = line.replace('class ClassName(Schema):',
                                        f'class {file_name.capitalize()}(Schema):')
                if 'table_name' in line:
                    line = line.replace('table_name', f'{file_name.lower()}')
                if "DROP TABLE IF EXISTS table_name;" in line:
                    line = line.replace(
                        "DROP TABLE IF EXISTS table_name;", f"DROP TABLE IF EXISTS {file_name.lower()};")
                writer.write(line)
