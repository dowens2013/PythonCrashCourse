from random import randint


class Die:
    """Class for a die"""

    def __init__(self, sides=6):
        """Initiate attributes"""
        self.sides = sides

    def roll_die(self):
        """Roll dice randomly"""
        number = randint(1, self.sides)
        print(number)


choose_sides = 10

my_die = Die(choose_sides)

my_die.roll_die()
