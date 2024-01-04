from pathlib import Path
import json


def get_username(path):
    """Get the username"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def greet_user():
    """Greet the user by name"""
    path = Path('username_4.json')
    username = get_username(path)
    if username:
        print(f"Welcome back, {username}")
    else:
        username = get_new_username(path)
        print(f"We'll remember your username when you come back, {username}")


def get_new_username(path):
    """Get new username"""
    username = input("What is your username? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username



