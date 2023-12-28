class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name.title()} is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name.title()} rolled over!")


my_dog = Dog(name='rocky', age=2)

print(f"My dog's name is: {my_dog.name.title()}")
print(f"My dog's age is: {my_dog.age}")

my_dog.sit()
my_dog.roll_over()
