# poll users on their dream vacation

responses = {}

polling_active = True

while polling_active:

    name = input("What is your name? ")
    response = input("What is your dream vacation? ")

    responses[name] = response

    repeat = input("Should we allow someone else to take the poll? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("--- Polling Results ---")
for x, y in responses.items():
    print(f"{x} has a dream vacation of {y}")



