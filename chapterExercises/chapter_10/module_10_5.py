# collect names for 10 guests and save it to a file
from pathlib import Path

# Define the file path to write to
path = Path('10_5_write.txt')

# Create a flag to control the loop
active = True

# Create a list to store guests in
guests = []

# Add guests to the guest list
while active:
    # Get the guest information
    name = input("What is your name? ")
    guests.append(name)

    # Determine if there are more guests
    more_guests = input("Are there more guests? ")
    if more_guests != 'yes':
        break

# write the guest list to the file
with path.open('w') as file:
    for x in guests:
        file.write(x + '\n')

print(path.read_text())


