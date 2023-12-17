prompt = "\nType 'quit' to end this program: "

active = True

while active:

    message = input(prompt)

    if message == 'quit' or message == 'Quit':
        active = False
    else:
        print(message)