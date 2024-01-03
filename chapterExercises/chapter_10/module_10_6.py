# write addition calculator. catch exception for value error
print("Addition Calculator")
print("Add two numbers. Enter 'q' to quit the program.")


while True:
    number_1 = input("Enter first number: ")
    if number_1 == 'q':
        break
    number_2 = input("Enter second number: ")
    if number_2 == 'q':
        break
    try:
        total = int(number_1) + int(number_2)
        print(f"Total: {total}")
    except ValueError:
        print("Error: Only use whole numbers")
