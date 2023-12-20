current_users = ['David', 'Nicole', 'Quin', 'Robert', 'Bethany']

new_users = ['David', 'Nicole', 'Ben', 'Timothy', 'Reno']

for user in new_users:
    if user in current_users:
        print(f'username {user} in use')
    else:
        print(f'username {user} available')