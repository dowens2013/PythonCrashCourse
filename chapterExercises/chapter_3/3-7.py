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


print('I can only invite two people to dinner due to a issue with my table delivery')

print(guest_list)

removed_guest_1 = guest_list.pop(0)
print(f'I apologize {removed_guest_1} but I am unable to invite you to dinner due to a issue with the delivery of my table')

removed_guest_2 = guest_list.pop(1)
print(f'I apologize {removed_guest_2} but I am unable to invite you to dinner due to a issue with the delivery of my table')

removed_guest_3 = guest_list.pop(2)
print(f'I apologize {removed_guest_3} but I am unable to invite you to dinner due to a issue with the delivery of my table')

removed_guest_4 = guest_list.pop(2)
print(f'I apologize {removed_guest_4} but I am unable to invite you to dinner due to a issue with the delivery of my table')

removed_guest_5 = guest_list.pop(2)
print(f'I apologize {removed_guest_5} but I am unable to invite you to dinner due to a issue with the delivery of my table')


print(guest_list)

print(f"\n {guest_list[0]} and {guest_list[1]} I'm excited for dinner with you tomorrow")