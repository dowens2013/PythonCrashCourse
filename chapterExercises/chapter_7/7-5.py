prompt = "What is your age? "

answer = input(prompt)
answer = int(answer)

if answer < 3:
    print('Your ticket is free')
elif (answer > 3 and answer) < 12:
    print('Your ticket is $10')
elif answer > 12:
    print('Your ticket is $15')


