item1_cost = float(input("Enter the cost of the first item: "))
item2_cost = float(input("Enter the cost of the second item: "))
payment = float(input("Enter your payment amount: "))

total_cost = item1_cost + item2_cost

if payment < total_cost:
    amount_owed = total_cost - payment
    print(f"Short payment. You still owe: ${amount_owed:.2f}")
else:
    change = payment - total_cost
    print(f"Thank you for your payment! Your change is: ${change:.2f}")
