class User:
    """User information"""
    def __init__(self, first_name, last_name, date_of_birth, location):
        """Initialize name and attributes"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.date_of_birth = date_of_birth
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f"User details:"
              f"\nFirst Name: {self.first_name}"
              f"\nLast Name: {self.last_name}"
              f"\nDate of Birth: {self.date_of_birth}"
              f"\nLocation: {self.location}")

    def greet_user(self):
        print(f"Greetings {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User(first_name='david', last_name='owens', date_of_birth='01/01/1900', location='anon')

user_1.increment_login_attempts()
print(f"Login Attempts: {user_1.login_attempts}")
user_1.increment_login_attempts()
print(f"Login Attempts: {user_1.login_attempts}")
user_1.increment_login_attempts()
print(f"Login Attempts: {user_1.login_attempts}")
user_1.reset_login_attempts()
print(f"Login Attempts: {user_1.login_attempts}")