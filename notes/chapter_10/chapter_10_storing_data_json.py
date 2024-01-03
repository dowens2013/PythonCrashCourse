# store a set of numbers to be read by another program
from pathlib import Path
import json

numbers = list(range(1, 11))

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)
