# write a function called t_shirt that accepts a size and the text to be printed on a shirt
# modify the function so that large shirts are default

def t_shirt_details(text, size='l'):
    """Get t-shirt details"""
    print(f"Your shirt size is {size.title()}.")
    print(f"The text to be printed on your shirt is: {text}")


t_shirt_details('testing')
t_shirt_details(size='m', text='testing 2')