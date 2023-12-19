# create a poll where each pass through a loop prompts for a name and response

# dictionary to hold respondent details
responses = {}

# flag to indicate that polling is active
polling_active = True

while polling_active:

    # prompt to get users name and response

    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # store the response in the dictionary
    responses[name] = response

    # determine if we should keep the poll running
    repeat = input("Should we allow another person to respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

# polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


