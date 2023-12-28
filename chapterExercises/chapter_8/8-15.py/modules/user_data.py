def user_information(first, last, **details):
    details['first_name'] = first
    details['last_name'] = last
    return details
