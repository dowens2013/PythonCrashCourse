#buffet

foods = ('sushi', 'salad', 'tacos', 'steak', "mac n' cheese")

for item in foods:
    print(item.title())

# try to modify an item
# popped_food = foods.pop(0)
# del foods[3]

foods = ('pancakes', 'bacon', 'tacos', 'steak', "mac n' cheese")

print("\nNew items:\n")

for item in foods:
    print(item.title())