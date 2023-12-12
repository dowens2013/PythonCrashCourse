# Greet each user on a website
# ensure that list is not empty

usernames = ['Admin', 'David', 'Nicole', 'Emmanuel', 'Andrew']

if usernames:
    for username in usernames:
        if username ==  'Admin':
            print('Hello Admin')
        else:
            print(f'{username} is logged in')
else:
    print('The list is empty')