# write a program to save usernames to file
from pathlib import Path

path = Path('10_4_write.txt')

name = input("What is your name? ")

path.write_text(name)

print(path.read_text())




