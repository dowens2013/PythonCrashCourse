# functions can have default values for parameters

# animal_type = 'dog' is the default value
def describe_pet(pet_name, animal_type='dog'):
    """Describe pet"""
    print(f"I have a {animal_type.title()}. ")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}")


describe_pet(pet_name='Russ')
describe_pet(animal_type='cat', pet_name='russ')
describe_pet('willie')
