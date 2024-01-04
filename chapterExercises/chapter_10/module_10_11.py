# save favorite numbers to a file
from pathlib import Path
import json


def get_favorite_number():
    """Get favorite number"""
    path = Path('favorite_number.json')
    favorite_number = input("What is your favorite number? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    print(f"Your favorite number is {favorite_number}")


get_favorite_number()