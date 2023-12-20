# functions continued

def describe_city(city_name, city_country="The United States"):
    print(f"The name of the city is {city_name.title()}")
    print(f"The country of {city_name.title()} is {city_country.title()}\n")


describe_city('atlanta')
describe_city(city_name='Paris', city_country='France')
describe_city('Barcelona', 'Spain')


