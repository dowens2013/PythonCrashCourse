class Restaurant:
    """A class to define a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and attributes"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        print(f"The restaurant's name is: {self.restaurant_name}"
              f"\nThe restaurant's cuisine is: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")


restaurant = Restaurant(restaurant_name="david's shack", cuisine_type='american')

print(f"Name: {restaurant.restaurant_name}"
      f"\nCuisine: {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()
