# move each message to a list for sent messages after it's sent

# from exercise 8-9
def show_messages(messages, sent_messages):
    """Show text messages"""
    while messages:
        message = messages.pop()
        print(f"Current message: {message}")
        sent_messages.append(message)


def sent_messages(sent_messages):
    for message in sent_messages:
        print(f"\nSent message: {message}")


texts = ['hello', 'lol', 'goodbye']
sent_texts = []

show_messages(texts, sent_texts)
sent_messages(sent_texts)

print(texts)
print(sent_texts)
