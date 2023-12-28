
def build_persona(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info


user_profile = build_persona('david', 'owens', location='raleigh', field='fin ops')

print(user_profile)