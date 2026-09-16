while True:
    print("ARITHMETIC CALCULATOR")
    print("1. Addition          2. Subtraction       3. Multiplication")
    print("4. Division          5. Modulus           6. Increment")
    print("7. Decrement")

    while True:
        try:
            operation = int(input("\nSelect an arithmetic operation: "))

            if 1 <= operation <= 7:
                break
            else:
                print("Invalid option. Please select a number from 1 to 7.")
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 7.")

    if operation in [1, 2, 3, 4, 5]:
        while True:
            try:
                x = float(input("Enter the value of x: "))
                y = float(input("Enter the value of y: "))
                break
            except ValueError:
                print("Invalid input. Please enter numbers.")

        print(f"\nVariable Values: x = {x}, y = {y}")

        if operation == 1:
            result = x + y
            print(f"Addition: x + y = {result}")

        elif operation == 2:
            result = x - y
            print(f"Subtraction: x - y = {result}")

        elif operation == 3:
            result = x * y
            print(f"Multiplication: x * y = {result}")

        elif operation == 4:
            if y == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = x / y
                print(f"Division: x / y = {result}")

        elif operation == 5:
            if y == 0:
                print("Error: Modulus by zero is not allowed.")
            else:
                result = x % y
                print(f"Modulus: x % y = {result}")

    elif operation == 6:
        while True:
            try:
                x = float(input("Enter the value of x: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        result = x + 1
        print(f"\nVariable Values: x = {x}")
        print(f"Increment: x + 1 = {result}")

    elif operation == 7:
        while True:
            try:
                x = float(input("Enter the value of x: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        result = x - 1
        print(f"\nVariable Values: x = {x}")
        print(f"Decrement: x - 1 = {result}")
        
    while True:
        choice = input("\nDo you want to continue? (YES/NO): ").strip().upper()

        if choice == "YES":
            break
        elif choice == "NO":
            print("Program terminated. Thank you!")
            exit()
        else:
            print("Invalid input. Please enter YES or NO.")