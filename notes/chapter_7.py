# user input

prompt = "What is your full name? "

name = input(prompt)

age = input('How old are you? ')
age = int(age)

print(f"\nName: {name.title()}")
print(f"Age: {age}")

if age >= 21:
    print(f"Hi {name}, welcome to the event. Enjoy yourself. Remember that there is an open bar for adults over 21")
else:
    print(f"Hi {name}, welcome to the event. Enjoy yourself. Remember that you are not old enough to drink")

if (age % age) == 0:
    print("Your age is a even number")
else:
    print("Your age is a odd number")
