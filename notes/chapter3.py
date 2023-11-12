#creating a list of items
currentGames = ['Overwatch', 'Starfield', 'Warzone', 'Cyberpunk 2077']

#print(currentGames)

#printing the third item
#print(currentGames[2])

#adding an item
#currentGames.append('Overwatch 2')
#print(currentGames)

#removing an item
# currentGames[0]
#print(currentGames)

#popping an item
#popped_games = currentGames.pop()
#print(currentGames)
#print(popped_games)

#first_game = currentGames.pop(0)

#lastGame = f'The last game I played was {popped_games.title()}.'
#firstGame = f'The first game I played was {first_game.title()}.'

#print(f'Current games: {currentGames}')

#print(lastGame)
#print(firstGame)

#find a specific game by its value not position
#currentGames.remove('Starfield')
#print(currentGames)

#print an item as I remove it from a list by its value
#bad_player_base = 'Warzone'
#currentGames.remove(bad_player_base)
#print(currentGames)
#print(f'\n {bad_player_base} has a bad player base')

# 11/12/20231
# Sorting Permanently and Temporarily

# Permanently
currentGames.sort()
statement = f'The alphabetical order of currentGames is: {currentGames}'
print(f'\n{statement}')

currentGames.sort(reverse=True)
statement = f'The reverse alphabetical order of currentGames is: {currentGames}'
print(f'\n{statement}')

# Temporarily
cars = ['M3', 'GT-500', 'CT-V', 'Tesla X']
print(f'\nUnsorted: {cars}')

print(f'\nSorted cars: {sorted(cars)}')

# Printing list in reverse order
cars.reverse()
print(f'\n{cars}')

# Finding length of list
length = len(cars)
print(f'\n{length}')





