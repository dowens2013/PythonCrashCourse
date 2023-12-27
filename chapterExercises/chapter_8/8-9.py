# make a list containing a series of messages. Pass the list to a function. Print each text.

def show_messages(messages):
    """Show text messages"""
    for message in messages:
        print(f"Message: {message}")


texts = ['hello', 'lol', 'goodbye']

show_messages(texts)
