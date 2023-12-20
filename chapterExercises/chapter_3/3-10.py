# Every function in chapter 3

spices = ['rosemary', 'Turmeric', 'Oregano', 'Thyme']

print(spices[2])

message = f'Lemon chicken requires {spices[0].title()}'
print(message)

spices[2] = "Pepper"
print(spices[2])

spices.append('Oregano')
print(spices)

spices.insert(1, "Cumin")
print(f'\n{spices}')

del spices[4]
print(f'\n{spices}')

popped_spice = spices.pop(0)
print(popped_spice)
print(spices)

spices.remove("Pepper")
print(spices)

print(sorted(spices))
print(spices)
spices.sort()
print(spices)
spices.reverse()
print(spices)
spices.sort(reverse=True)
print(spices)

# create error
print(spices[4])
