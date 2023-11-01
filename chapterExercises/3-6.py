#Create a guest list of at least people to invite to dinner
guest_list = ['Nicole', 'Bethany', 'James', 'Robert']

#Print a custom message to each member on the list
print(f'Hi {guest_list[0]} would you like to come have dinner at my place tomorrow night?')
print(f'Hi {guest_list[1]} would you like to come have dinner at my place tomorrow night?')
print(f'Hi {guest_list[2]} would you like to come have dinner at my place tomorrow night?')
print(f'Hi {guest_list[3]} would you like to come have dinner at my place tomorrow night?')

no_list = 'James'
print(f'\n Attendee who cannot attend: {no_list}')

#modify list to include new attendee
guest_list[2] = 'Khalil'
print(f'\n Updated guest list: {guest_list}')

print(f'\nHi {guest_list[0]} would you like to come have dinner at my place tomorrow night?')
print(f'Hi {guest_list[1]} would you like to come have dinner at my place tomorrow night?')
print(f'Hi {guest_list[2]} would you like to come have dinner at my place tomorrow night?')
print(f'Hi {guest_list[3]} would you like to come have dinner at my place tomorrow night?')



print('We have found a bigger table')

guest_list.insert(0, 'Andrew')
guest_list.insert(2,'Kyle')
guest_list.append('Shanna')

print(f'\n Updated guest list: {guest_list}')

print('Updated invitations:')
print(f'\nHi {guest_list[0]} would you like to come have dinner at my place tomorrow night?')
print(f'Hi {guest_list[1]} would you like to come have dinner at my place tomorrow night?')
print(f'Hi {guest_list[2]} would you like to come have dinner at my place tomorrow night?')
print(f'Hi {guest_list[3]} would you like to come have dinner at my place tomorrow night?')
print(f'Hi {guest_list[4]} would you like to come have dinner at my place tomorrow night?')
print(f'Hi {guest_list[5]} would you like to come have dinner at my place tomorrow night?')
print(f'Hi {guest_list[6]} would you like to come have dinner at my place tomorrow night?')