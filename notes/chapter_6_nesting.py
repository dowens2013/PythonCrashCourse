alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'blue', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(f'{alien}')

print("\n")

# using range to generate aliens

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
   if alien['color'] == 'green':
       alien['color'] = 'yellow'
       alien['speed'] = 'medium'
       alien['points'] = 10

for alien in aliens[:5]:
    print(alien)

print('...')
print(f"\nTotal number of aliens: {len(aliens)}")