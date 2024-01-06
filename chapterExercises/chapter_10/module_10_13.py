from pathlib import Path
import json


def get_user_details(path):
    """Get the user details"""
    if path.exists():
        contents = path.read_text()
        user_details = json.loads(contents)
        return user_details
    else:
        return None


def greet_user():
    """Greet the user by name"""
    path = Path('username_4.json')
    user_details = get_user_details(path)
    if user_details:
        print(f"Welcome back {user_details}")
    else:
        user_details = get_new_user_details(path)
        print(f"We'll remember your username when you come back, {user_details}")


def get_new_user_details(path):
    """Get new user details"""

    while True:
        username = input("What is your username? ")
        first_name = input("What is your first name? ")
        last_name = input("What is your last name? ")
        try:
            security_pin = int(input("What is your 4 digit security pin? (Numbers only!)" ))
            break
        except ValueError:
            print("Integers only")
    user_details = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'security_pin': security_pin,
        }
    contents = json.dumps(user_details)
    path.write_text(contents)
    active = False
    return user_details



greet_user()



