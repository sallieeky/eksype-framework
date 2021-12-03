from seeder.migrationsseeder import MigrationsSeeder


module_list = [
    MigrationsSeeder
]


def seed_all():
    module_return = []
    for module in module_list:
        module_return.append(module.seed())
    return module_return


def make_seeder(file_name):
    with open('default/seeder.py', 'r') as reader:
        with open(f'seeder/{file_name.lower()}.py', 'w') as writer:
            for line in reader:
                if 'class ClassName:' in line:
                    line = line.replace('class ClassName:',
                                        f'class {file_name.capitalize()}:')
                if 'INSERT INTO table_name' in line:
                    line = line.replace(
                        'INSERT INTO table_name', f'INSERT INTO {file_name.lower()}')
                writer.write(line)
