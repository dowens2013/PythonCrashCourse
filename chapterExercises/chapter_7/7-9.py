# deli
# item not available

sandwich_orders = ['Italian', 'Meatball', 'Tuna', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print('Sandwiches to make')
print('The deli has run out of Pastrami')

for y in sandwich_orders:
    print(y.title())

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")



while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"Making sandwich order: {current_order}")

    finished_sandwiches.append(current_order)

print('\nFinished orders:')
for x in finished_sandwiches:
    print(x.title())