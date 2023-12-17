prompt = "\nType 'quit' to end this program: "

while True:

    message = input(prompt)

    if message == 'quit' or message == 'Quit':
        break
    else:
        print(message)

# break statements work with any Python loop