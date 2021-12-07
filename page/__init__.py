def make_page(file_name):
    with open('default/page.py', 'r') as reader:
        with open(f'page/{file_name.lower()}.py', 'w') as writer:
            for line in reader:
                if 'class ClassName(Page):' in line:
                    line = line.replace('class ClassName(Page):',
                                        f'class {file_name.capitalize()}(Page):')
                writer.write(line)
