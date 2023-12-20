# keyword arguments use a name-value pair that you pass to a function

def describe_pet(animal_type, pet_name):
    """Describe pets"""
    print(f"I have a {animal_type.title()}. ")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}")


describe_pet(pet_name="zatarra", animal_type="hamster")