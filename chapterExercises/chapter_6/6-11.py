cities = {
    'Orlando': {
        'Country': 'United States',
        'Population': 309154,
        'Fact': 'Home of Disney World'
    },
    'New York City': {
        'Country': 'United States',
        'Population': 8468000,
        'Fact': 'Home of Statue of Liberty'
    },
    'Raleigh': {
        'Country': 'United States',
        'Population': 469124,
        'Fact': 'Home of Acorns'
    },
}

for city, facts in cities.items():
    print(f"{city}: ")
    country = facts['Country']
    population = facts['Population']
    fact = facts['Fact']
    print(f"\tCountry: {country}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")