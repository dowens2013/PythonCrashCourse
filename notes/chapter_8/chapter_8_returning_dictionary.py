# a function can return a complex data structure like a dictionary

def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first': first_name.title(), 'last': last_name.title()}
    return person

athlete = build_person('david', 'owens')

print(athlete)