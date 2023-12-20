# arguments passed to paramaters based on order

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"I have a {animal_type}. "
          f"\nMy {animal_type}'s name is {pet_name}")


describe_pet('cat', "T'Challa")
describe_pet('hamster', 'Zatarra')