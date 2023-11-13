# my pizza, your pizzas

preferred_pizza = ['Hawaiian', 'Supreme', 'Four Cheese']

for pizza in preferred_pizza:
    print(f'I like {pizza} pizza')

print('\nPizza is great')

friend_pizza = preferred_pizza[:]

preferred_pizza.append('Veggie')
friend_pizza.append('White')

for pizza in preferred_pizza:
    print(f'My preferred pizza is: {pizza}')

for pizza in friend_pizza:
    print(f"My friend's favorite pizza is: {pizza}")