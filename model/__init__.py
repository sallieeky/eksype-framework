def make_model(file_name):
    with open('default/model.py', 'r') as reader:
        with open(f'model/{file_name.lower()}.py', 'w') as writer:
            for line in reader:
                if 'class ClassName(Model):' in line:
                    line = line.replace('class ClassName(Model):',
                                        f'class {file_name.capitalize()}(Model):')
                if 'Model.__init__(self, "table_name")' in line:
                    line = line.replace(
                        'Model.__init__(self, "table_name")', f'Model.__init__(self, "{file_name.lower()}")')
                writer.write(line)
