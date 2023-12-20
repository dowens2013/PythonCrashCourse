# return values takes a statement from inside the function and sends it back to the line that called the function

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f'{first_name} {last_name}'
    return full_name.title()

# return values require assignment to a variable. In this case the variable is 'athlete'
athlete = get_formatted_name('david', 'owens')
print(athlete)