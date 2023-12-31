def get_formatted_name(first, last, middle=""):
    """get formatted full name"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

formatted_name = get_formatted_name('david', 'owens', 'gerald')
print(formatted_name)
