# save favorite numbers to a file
from pathlib import Path
import json


def get_favorite_number():
    """Get favorite number"""
    while True:
        try:
            path = Path('favorite_number.json')
            favorite_number = float(input("What is your favorite number? "))
            contents = json.dumps(favorite_number)
            path.write_text(contents)
            break
        except ValueError:
            print("Integers only")


get_favorite_number()
