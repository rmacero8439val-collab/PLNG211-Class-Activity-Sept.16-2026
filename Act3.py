number_input = input("Enter a multiple of 5 between 1 and 100: ")

if not number_input.isdigit():
    print("Invalid input. Please enter a whole number.")
else:
    number = int(number_input)
    if 1 <= number <= 100 and number % 5 == 0:
        print("Valid number! It is a multiple of 5 between 1 and 100.")
    else:
        print("Invalid number. It must be between 1 and 100 and a multiple of 5.")
