# details about a car

def car_details(manufacturer, model, **details):
    details['manufacturer'] = manufacturer.title()
    details['model'] = model.title()
    return details


car_1 = car_details(
    'ford',
    'escape',
    color='black',
    awd='y',
    mileage=136000
)

print(car_1)