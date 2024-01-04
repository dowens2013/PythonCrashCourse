from pathlib import Path
import json


def greet_user():
    """Greet the user by name"""
    path = Path('username_3.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}")
    else:
        username = input("What is your username? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"Username stored, {username}")


greet_user()