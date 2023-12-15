# store information about a person

details_nicole = {
    'first_name': 'Nicole',
    'last_name': 'Mejias',
    'city': 'Morrisville',
    'age': 31,
}

details_david = {
    'first_name': 'david',
    'last_name': 'owens',
    'city': 'raleigh',
    'age': 31,
}

people = [details_nicole, details_david]

for x in people:
    print(f""
          f"First Name: {x['first_name'].title()}\n"
          f"Last Name: {x['last_name'].title()}\n"
          f"City: {x['city'].title()}\n"
          f"Age: {x['age']}\n")



