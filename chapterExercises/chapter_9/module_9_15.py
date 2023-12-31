from random import choice

lottery_range = range(1, 5)

lottery_numbers = [2, 3, 4, 5, 6, 19, 20, 30, 'A', 'B', 'C', 'D', 'E', 'F']

winners = []

while len(winners) < 4:
    winner = choice(lottery_numbers)
    if winner not in winners:
        winners.append(winner)

my_ticket = [2, 3, 4, 'A']

count = 0

run_loop = True

print(f"\nMy ticket: {my_ticket}")
print(f"\nThe winning numbers are: {winners}")

while run_loop:
    if all(item in winners for item in my_ticket):
        print("\nI won!")
        print(count)
        run_loop = False
    else:
        print("\nI lost :(")
        count += 1






