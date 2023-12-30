# create an admin class for the user class written in 9-3

from module_9_5 import User as u

class Admin(u):
    """Create admin class based on inherited User class"""

    def __init__(self, first_name, last_name, date_of_birth, location):
        """Establish initial attributes for Admin"""
        super().__init__(first_name, last_name, date_of_birth, location)
        if self.admin:
            self.privileges = ['can add post', 'can delete post', 'can ban user']
        elif not self.admin:
            self.privileges = ['can add post', 'can delete post']


    def show_privileges(self):
        """Show privileges of user"""
        print(f"User privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin_user = Admin('david', 'owens', '05/18/1992', 'raleigh')
admin_user.show_privileges()
admin_user.describe_user()
admin_user.greet_user()