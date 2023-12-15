cat = {
    'owner': 'bill',
    'pet_age': '12',
    'pet_breed': 'tabby',
    'pet_name': 'tim',
}

dog = {
    'owner': 'john',
    'pet_breed': 'husky',
    'pet_age': '13',
    'pet_name': 'rocky',
}

pets = [cat, dog]

for x in pets:
    print(f"Owner Name: {x['owner'].title()}\n"
          f"Pet Age: {x['pet_age'].title()}\n"
          f"Pet Breed: {x['pet_breed'].title()}\n"
          f"Pet Name: {x['pet_name'].title()}\n")