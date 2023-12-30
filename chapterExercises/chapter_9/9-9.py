# you can break large classes into smaller classes that work together, known as 'composition'

class Car:
    """Simple way to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23_500

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement about the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Update the mileage.
        Reject change if it attempts to roll odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """Add the given miles to the odometer reading"""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represents aspects of a car, specific to EV"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery(battery_size=40)


class Battery:
    """Model a battery for an electrical car"""

    def __init__(self, battery_size=40):
        """Initial attributes for battery"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Describe the battery"""
        print(f"Your battery size is {self.battery_size}-kWh.")

    def get_range(self):
        """Show the range of the battery"""
        if self.battery_size == 40:
            driving_range = 150
        elif self.battery_size == 65:
            driving_range = 225

        print(f"This car can go about {driving_range} miles")

    def upgrade_battery(self):
        """Upgrade batteries"""
        if self.battery_size != 65:
            self.battery_size = 65


car = ElectricCar('tesla', 'model 3', 2016)
print(car.get_descriptive_name())
car.battery.describe_battery()
car.battery.upgrade_battery()
car.battery.describe_battery()