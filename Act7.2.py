def main():
    x = float(input("Enter value of x: "))
    y = float(input("Enter value of y: "))
    result = 0.0

    print("\nVariable values:")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"result = {result}")

   
    print("\nSelect an Arithmetic Operation:")
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[5] Modulus")
    print("[6] Increment & Decrement x")
    
    try:
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    print("\nResult:")
    match choice:
        case 1:
            result = x + y
            print(f"Addition: x + y = {result}")
        case 2:
            result = x - y
            print(f"Subtraction: x - y = {result}")
        case 3:
            result = x * y
            print(f"Multiplication: x * y = {result}")
        case 4:
            if y != 0:
                result = x / y
                print(f"Division: x / y = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        case 5:
            if y != 0:
                result = x % y
                print(f"Modulus: x % y = {result}")
            else:
                print("Error: Modulus by zero is not allowed.")
        case 6:
            x += 1
            print(f"Increment: x + 1 = {x}")
            x -= 1 
            x -= 1
            print(f"Decrement: x - 1 = {x}")
        case _:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
