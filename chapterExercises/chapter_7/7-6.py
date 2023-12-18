prompt = "\nEnter your pizza toppings: "

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(message)



