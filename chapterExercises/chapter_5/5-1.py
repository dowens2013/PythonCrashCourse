# Conditional tests
# Write a series of conditional tests. Print a statement describing each test and my prediction.

game = 'Overwatch'
print("\nIs game == 'call of duty'? I predict 'False'.")
print ("game == 'Overwatch'")

print("\nIs game == 'Overwatch'? I predict 'True'")
print("game == 'Overwatch'")

# Create five tests that evaluate to true

cities = ['Las Vegas', 'Raleigh', 'New York', 'Greenville', 'Charlotte']

if 'Las Vegas' in cities:
    print('\nLas Vegas confirmed. True.')
else:
    print('\nLas Vegas not confirmed')

if 'Raleigh' in cities:
    print ('Raleigh confirmed. True.')
else:
    print('Raleigh not confirmed')

if 'New York' in cities:
    print('New York confirmed. True.')
else:
    print('New York not confirmed')

if 'Greenville' in cities:
    print('Greenville confirmed. True.')
else:
    print('Greenville not confirmed')

if 'Charlotte' in cities:
    print('Charlotte confirmed. True.')
else:
    print('Charlotte not confirmed')

# Create 5 tests that evaluate to false

age = 15
name = 'John'
numbers = range(0, 5)
day = 'Monday'
result = age + 5

if age == 21:
    print('\nOut of range')
else:
    print('\nOptimal age. False.')

if name != 'John':
    print('Not John')
else:
    print('John. False.')

if 10 in numbers:
    print('10 available')
else:
    print('10 not included. False.')

if day == 'Tuesday':
    print('Tuesday')
else:
    print('Not Tuesday. False.')

if result > 21:
    print('Over 21')
else:
    print('Under 21. False.')
