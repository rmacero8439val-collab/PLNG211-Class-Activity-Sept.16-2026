while True:
    print(" STUDENT GRADE PROGRAM")
    
    try:
        java_score = float(input("Enter Java Programming score: "))
        c_score = float(input("Enter C Programming score: "))
        database_score = float(input("Enter Database Handling score: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    average = (java_score + c_score + database_score) / 3

    if 90 <= average <= 100:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 75:
        grade = 'C'
    else:
        grade = 'F'

    print("\nOUTPUT")
    print(f"Average: {average:.4f}")
    print(f"Grade: {grade}")

    continue_program = input("\nDo you want to continue: YES / NO: ")
    if continue_program.strip().upper() != "YES":
        break

print("\nProgram terminated.")
