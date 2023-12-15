# restaurant seating

prompt = "How many people are in your party? "

party_size = input(prompt)

party_size = int(party_size)

if party_size > 8:
    print('You will have to wait for a table')
else:
    print('We can seat you now')