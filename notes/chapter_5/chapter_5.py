# If statements allow you to examine the current state of a program and respond appropirately to that state.

# Simple example

cars = ['bmw', 'audi', 'toyota', 'honda']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# Conditional tests use 'True' and 'False' to evaluate an if statement

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print(f'\nHold the anchovies!')

answer = 18

if answer != 50:
    print("\nWrong answer!")

# Conditional test using AND

age_1 = 20
age_2 = 21

if (age_1 >= 21) and (age_2 >= 21):
    print("\nLegal to drink")
else:
    print("\nIllegal to drink")

# Conditional test using OR

age_3 = 21
age_4 = 25

if (age_3 >= 25) or (age_4 >= 25):
    print('\nCar rental available')
else:
    print('\nUnable to rent car')

# Checking a value in a list

video_games = ['Halo', 'call of duty', 'overwatch', 'battlefield']

if 'overwatch' in video_games:
    print('\nGame is available to play')
else:
    print('\nGame is rented out')

banned_people = ['Marie', 'Jorge', 'Justin', 'Dustin']

if 'Nicole' not in banned_people:
    print('\nNot banned')
else:
    print('\nBanned')



