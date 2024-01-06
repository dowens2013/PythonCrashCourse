from pathlib import Path
import json


def get_favorite_number():
    """Get favorite number"""
    path = Path('favorite_number.json')
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        print(f"Your favorite number is {favorite_number}")
    else:
        while True:
            try:
                favorite_number = float(input("What is your favorite number? "))
                contents = json.dumps(favorite_number)
                path.write_text(contents)
                print(f"Your favorite number is {favorite_number}")
                break
            except ValueError:
                print("Float number only.")


get_favorite_number()
