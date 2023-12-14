# looping through dictionaries

rivers = {
    'tar': 'united states',
    'nile': 'egypt',
    'amazon': 'brazil',
}

for x,y in rivers.items():
    print(f"\nRiver: {x}\nCountry: {y}\n")

for x in rivers.keys():
    print(f'{x.title()}\n')

for x in rivers.values():
    print(f'{x.title()}')