while True:
    print("\nSTUDENT GRADE CALCULATOR")
    while True:
        try:
            java_score = float(input("Java Programming Score: "))
            if 0 <= java_score <= 100:
                break
            print("Please enter a score from 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            c_score = float(input("C Programming Score: "))
            if 0 <= c_score <= 100:
                break
            print("Please enter a score from 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            database_score = float(input("Database Handling Score: "))
            if 0 <= database_score <= 100:
                break
            print("Please enter a score from 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    average = (java_score + c_score + database_score) / 3

    if average >= 90:
        grade = "A"
        reason = "the average is between 90 and 100"
    elif average >= 80:
        grade = "B"
        reason = "the average is between 80 and 89"
    elif average >= 75:
        grade = "C"
        reason = "the average is between 75 and 79"
    else:
        grade = "F"
        reason = "the average is below 75"

    print(f"\nAverage: {average:.2f}")
    print(f"Grade: {grade} because {reason}")

    while True:
        choice = input("\nDo you want to continue? (YES/NO): ").strip().upper()

        if choice == "YES":
            break
        elif choice == "NO":
            print("Program terminated. Thank you!")
            exit()
        else:
            print("Invalid input. Please enter YES or NO.")