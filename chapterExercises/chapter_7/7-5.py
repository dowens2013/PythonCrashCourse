prompt = "What is your age? "

active = True

while active:
    try:
        answer = input(prompt)
        answer = int(answer)

        if answer < 3:
            print('Your ticket is free')
            active = False
        elif 3 < answer < 12:
            print('Your ticket is $10')
            active = False
        elif answer >= 12:
            print('Your ticket is $15')
            active = False
    except ValueError:
        print("Please enter a valid age in numbers")


