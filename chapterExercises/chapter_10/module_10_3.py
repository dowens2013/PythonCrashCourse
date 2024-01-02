from pathlib import Path

path = Path('module_10_1_file.txt')
contents = path.read_text().replace('Python', 'C')

list_1 = []

for line in contents.splitlines():
    list_1.append(line)

for x in list_1:
    print(f'- {x}')

print(f'\n{contents}')
