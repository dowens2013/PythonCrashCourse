favorite_numbers = {
    'Ben': ['1', '2', '10'],
    'Sally': ['2', '4', '6'],
    'Sue': ['3', '21', '23'],
    'Joe': ['4', '6', '23'],
    'John': ['5', '13', '30'],
}

for name, number in favorite_numbers.items():
  if len(number) <= 1:
    print(f"{name}'s favorite number is: ")

    for x in number:
        print(f"\t{x}")
  else:
      print(f"{name}'s favorite numbers are: ")

      for x in number:
          print(f"\t{x}")