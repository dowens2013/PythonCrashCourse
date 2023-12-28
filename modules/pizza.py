def make_pizza(size, *toppings):
    """Summarize pizza order"""
    print(f"\nPizza details"
          f"\nSize: \n - {size}-inch"
          f"\nToppings: ")
    for topping in toppings:
        print(f"- {topping.title()}")
