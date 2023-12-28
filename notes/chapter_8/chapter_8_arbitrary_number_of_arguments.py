def make_pizza(size, crust, *toppings):
    """Print the toppings that have been requested"""
    print(f"\nMaking a {size.title()} {crust.title()} crust pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping.title()}")


make_pizza('large', 'thin', 'pepperoni', 'sausage', 'ham')

