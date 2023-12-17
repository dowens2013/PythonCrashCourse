# while loop

number = 1

while number <= 5:
    print(number)
    number += 1

prompt = "\nType 'quit' to end this program: "

message = ""

while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)