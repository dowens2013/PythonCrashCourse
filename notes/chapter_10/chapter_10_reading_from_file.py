from pathlib import Path

# path = Path('c:\\dev\\code\\pythonCrashCourse\\notes\\pi_digits.txt')
path = Path(r'c:/dev/code/pythonCrashCourse/notes/pi_digits.txt')
contents = path.read_text().rstrip()

print(contents)
print('test')
