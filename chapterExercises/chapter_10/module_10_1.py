from pathlib import Path

path = Path('module_10_1_file.txt')
contents = path.read_text()
lines = contents.splitlines()
list_1 = []

for line in lines:
    list_1.append(line)

for x in list_1:
    print(f'- {x}')

print(f'\n{contents}')
