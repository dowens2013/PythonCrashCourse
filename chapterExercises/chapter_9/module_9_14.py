from random import choice

lottery_range = range(1, 11)

lottery_numbers = list(lottery_range) + ['A', 'Z', 'Y', 'T', 'K']

winners = []

while len(winners) < 4:
    winner = choice(lottery_numbers)
    if winner not in winners:
        winners.append(winner)

print(f"\nAny ticket with these characters wins the lottery: ")
for x in winners:
    print(x)






