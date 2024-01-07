class Employee:
    """Class for a employee"""

    def __init__(self, name, position, pay):
        """Initial attributes"""
        self.name = name
        self.position = position
        self.pay = pay
        self.details = {'name': name, 'position': position, 'pay': pay}

    def give_raise(self, pay_raise=0):
        """Add raise for employee"""
        try:
            if pay_raise > 0:
                self.details['pay'] = self.details['pay'] + pay_raise
            else:
                self.details['pay'] = self.details['pay'] + 5000
        except TypeError:
            print("Only use integers")

    def show_employee_details(self):
        for x, y in self.details.items():
            print(f"{x.title()}: {y}")






