#ordinal numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if numbers:
    for number in numbers:
        if number == 1:
            print(f'{number}st')
        elif number == 2:
            print(f'{number}nd')
        elif number == 3:
            print(f'{number}rd')
        elif number in [4, 5, 6, 7, 8, 9]:
            print(f'{number}th')
else:
    print('empty list')