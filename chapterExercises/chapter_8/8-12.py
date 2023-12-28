# sandwich toppings

def get_toppings(*toppings):
    """Get sandwich toppings from customer"""
    print("\nSandwich toppings: ")
    for topping in toppings:
        print(f"- {topping.title()}")


get_toppings('ham', 'lettuce', 'mayo', 'cheese')
get_toppings('turkey', 'cheese', 'mustard', 'tomato')
get_toppings('tuna', 'cheese', 'jalapenos')