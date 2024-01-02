from pathlib import Path

path = Path('writing.txt')

contents = "\nKimura"
contents += "\nSingle-X"
contents += "\nArm Bar"

read_file = path.read_text()

path.write_text(contents)

print(read_file)
