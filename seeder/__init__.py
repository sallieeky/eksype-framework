from seeder.userseeder import Userseeder


module_list = [
    Userseeder
]


def seed_all():
    for module in module_list:
        module.seed()
    return True


def make_seeder(file_name):
    if "seeder" not in file_name.lower():
        file_name = file_name + "seeder"

    with open('default/seeder.py', 'r') as reader:
        with open(f'seeder/{file_name.lower()}.py', 'w') as writer:
            for line in reader:
                if 'class ClassName:' in line:
                    line = line.replace('class ClassName:',
                                        f'class {file_name.capitalize()}:')

                writer.write(line)
