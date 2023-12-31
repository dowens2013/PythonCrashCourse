from user import Admin

user_1 = Admin('david', 'owens', '05/18/1992', 'raleigh')
user_1.privileges.show_privileges()
user_1.describe_user()
user_1.assign_admin()
user_1.describe_user()
user_1.remove_admin()
user_1.describe_user()
