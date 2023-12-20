# slices

cubes = [value**3 for value in range(1,10)]

for item in cubes:
    print(item)

print(f'The first three items in this list are: {cubes[:3]}')
print(f'Three items from the middle of the list are: {cubes[3:6]}')
print(f'The last three items are: {cubes[6:]}')