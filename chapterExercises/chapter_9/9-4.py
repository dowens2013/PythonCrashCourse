class Restaurant:
    """A class to define a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and attributes"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 15

    def describe_restaurant(self):
        print(f"The restaurant's name is: {self.restaurant_name}"
              f"\nThe restaurant's cuisine is: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment


restaurant = Restaurant(restaurant_name="david's shack", cuisine_type='american')

restaurant.increment_number_served(5)

print(f"Name: {restaurant.restaurant_name}"
      f"\nCuisine: {restaurant.cuisine_type}"
      f"\nNumber served: {restaurant.number_served}")



