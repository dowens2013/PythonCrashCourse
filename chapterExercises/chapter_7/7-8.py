# deli

sandwich_orders = ['Italian', 'Meatball', 'Tuna']
finished_sandwiches = []

print('Sandwiches to make')
for y in sandwich_orders:
    print(y.title())

print("\n")

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"Making sandwich order: {current_order}")

    finished_sandwiches.append(current_order)

print('\nFinished orders:')
for x in finished_sandwiches:
    print(x.title())