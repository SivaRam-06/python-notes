# ═════════════════════════════════════════════════════════════════════════════
# 8. REAL-WORLD EXAMPLES
# ═════════════════════════════════════════════════════════════════════════════

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                  SECTION 8: REAL-WORLD EXAMPLES                       ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

print("EXAMPLE 1: ATM Withdrawal with Multiple Options")
print("-" * 60)
balance = 1000
while True:
    print(f"\nYour balance: ${balance}")
    choice = input("1. Withdraw  2. Deposit  3. Exit: ")
    
    if choice == "1":
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance = balance - amount
            print(f"✓ Withdrawn ${amount}. New balance: ${balance}")
        else:
            print("✗ Insufficient balance!")
    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print(f"✓ Deposited ${amount}. New balance: ${balance}")
    elif choice == "3":
        print("Thank you for using ATM. Goodbye!")
        break
    else:
        print("Invalid choice!")

print("\n")

print("EXAMPLE 2: Student Grade Report")
print("-" * 60)
students = {
    "Ali": [85, 90, 88],
    "Bhavna": [92, 88, 95],
    "Chirag": [78, 82, 80],
    "Deepa": [95, 92, 98]
}

print("Grade Report:")
print("-" * 60)
for name, marks in students.items():
    total = 0
    for mark in marks:
        total = total + mark
    average = total / len(marks)
    
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    else:
        grade = "C"
    
    print(f"{name:10} | Average: {average:5.2f} | Grade: {grade}")

print("\n")