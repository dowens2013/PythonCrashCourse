# write a function called t_shirt that accepts a size and the text to be printed on a shirt

def t_shirt_details(size, text):
    """Get t-shirt details"""
    print(f"Your shirt size is {size.title()}.")
    print(f"The text to be printed on your shirt is: {text}")


t_shirt_details('l', 'testing')
t_shirt_details(size='l', text='testing 2')