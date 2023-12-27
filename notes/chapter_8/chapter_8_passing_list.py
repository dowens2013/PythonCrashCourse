def greet_users(names):
    """Print a simple greeting"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['david', 'nicole', 'robert']

greet_users(usernames)