# looping through a dictionary

techniques = {
    'Mount': 'Head and arm choke',
    'Guard': 'Leg triangle',
    'X-Guard': 'Straight Ankle',
    'North-South': 'Kimura',
    'Side Control': 'Americana',
}

for x, y in techniques.items():
    print(f"\nPosition: {x} \nSubmission: {y}")