# for loop

colors = ['Green', 'Red', 'Blue', 'Orange']

for color in colors:
    print(f'Your selected color is: {color}.')
    print(f"The color {color} is a good choice.\n")

print('Those are all of the colors selected.')

# making numerical lists

for value in range(11):
    print(value)

number = list(range(6))
print(number)

#even numbers

even_numbers = list(range(0,11,2))
print(even_numbers)

#square roots

squares = []

for value in range(1,11):
    squares.append(value**2)

print(squares)

print(min(number))
print(max(number))
print(sum(number))

# list comprehension
# combines the for loop and creation of new elements in one line

squares = [value**2 for value in range(1,11)]
print(squares)

# slicing a list

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
print(days[0:3])
print(days[:2])

for day in days[:3]:
    print(day)

# copy a list

copy_of_days = days[:]
print(copy_of_days)

days.append("Friday")
print(days)
copy_of_days.append("Saturday")
print(copy_of_days)