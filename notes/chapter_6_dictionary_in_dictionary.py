users = {
    'dowens': {
        'first': 'david',
        'last': 'owens',
        'location': 'raleigh',
    },
    'nmejias': {
        'first': 'nicole',
        'last': 'mejias',
        'location': 'morrisville',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
    location = user_info['location'].title()

    print(f"\tFull name: {full_name}\n"
          f"\tLocation: {location}")