# users to verify

unconfirmed_users = ['Nicole', 'Robert', 'Quin', 'David']
confirmed_users = []

# verify all users until there are no more unconfirmed users

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# display confirmed users

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print("\nThe following users have NOT been confirmed: ")
for unconfirmed_user in unconfirmed_users:
    print(unconfirmed_user.title())
