def build_profile (first, last, **user_data):
    """Build a user profile"""
    user_data['first_name'] = first.title()
    user_data['last_name'] = last.title()
    return user_data


david = build_profile('david', 'owens', hobby='BJJ', location='Raleigh', age=31)
for x, y in david.items():
    print(y)
