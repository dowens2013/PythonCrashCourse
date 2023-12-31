class User:
    """User information"""
    def __init__(self, first_name, last_name, date_of_birth, location):
        """Initialize name and attributes"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.date_of_birth = date_of_birth
        self.location = location.title()
        self.login_attempts = 0
        self.admin = False

    def assign_admin(self):
        self.admin = True

    def remove_admin(self):
        self.admin = False

    def describe_user(self):
        print(f"User details:"
              f"\nFirst Name: {self.first_name}"
              f"\nLast Name: {self.last_name}"
              f"\nDate of Birth: {self.date_of_birth}"
              f"\nLocation: {self.location}"
              f"\nAdmin: {self.admin}")

    def greet_user(self):
        print(f"Greetings {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    """Create admin class based on inherited User class"""

    def __init__(self, first_name, last_name, date_of_birth, location):
        """Establish initial attributes for Admin"""
        super().__init__(first_name, last_name, date_of_birth, location)
        self.privileges = Privileges()


class Privileges:
    """Class for privileges"""

    def __init__(self):
        """Initial attributes"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Show privileges of user"""
        print(f"User privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
