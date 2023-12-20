pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'sausage', 'onion'],
}

print(f"You ordered a {pizza['crust']} crust pizza with the following toppings: ")

for topping in pizza['toppings']:
    print(f"\t{topping}")

favorite_languages = {
    'david': ['python', 'java', 'c'],
    'nicole': ['rust'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")