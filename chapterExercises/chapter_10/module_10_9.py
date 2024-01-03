from pathlib import Path

file_names = ['cat.txt', 'dog.txt']

for x in file_names:
    try:
        path = Path(x)
        contents = path.read_text()
        print(contents)
    except FileNotFoundError:
        pass

