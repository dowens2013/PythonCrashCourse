# write a class for an ice cream stand that inherits from the restaurant class I wrote in 9-1

from module_9_1 import Restaurant


class IceCreamStand(Restaurant):
    """Create a class for the ice cream stand at the restaurant"""

    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        """Initialize name and attributes"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['rocky road', 'vanilla', 'chocolate']

    def display_flavors(self):
        """Displays flavors available"""
        print(f"The following flavors are available: ")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream_stand = IceCreamStand('The Sweet Cone')
ice_cream_stand.display_flavors()
