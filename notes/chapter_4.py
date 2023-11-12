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