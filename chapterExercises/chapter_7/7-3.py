prompt = "Enter a number: "

number = input(prompt)

number = int(number)

if number % 10 == 0:
    print("This is a multiple of 10")
else:
    print("This is not a multiple of 10")