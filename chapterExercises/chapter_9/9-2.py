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


restaurant_1 = Restaurant(restaurant_name="david's shack", cuisine_type='american')
restaurant_2 = Restaurant(restaurant_name="nicole's shack", cuisine_type='mexican')
restaurant_3 = Restaurant(restaurant_name="tom's shack", cuisine_type='italian')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

