class User:
    """User information"""
    def __init__(self, first_name, last_name, date_of_birth, location):
        """Initialize name and attributes"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.date_of_birth = date_of_birth
        self.location = location.title()

    def describe_user(self):
        print(f"User details:"
              f"\nFirst Name: {self.first_name}"
              f"\nLast Name: {self.last_name}"
              f"\nDate of Birth: {self.date_of_birth}"
              f"\nLocation: {self.location}")

    def greet_user(self):
        print(f"Greetings {self.first_name}")


user_1 = User(first_name='david', last_name='owens', date_of_birth='01/01/1900', location='anon')
user_2 = User(first_name='john', last_name='smith', date_of_birth='01/02/1900', location='lake michigan')
user_3 = User(first_name='smith', last_name='john', date_of_birth='02/01/1900', location='space')

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()