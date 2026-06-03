# ═════════════════════════════════════════════════════════════════════════════
# 2. CONTINUE STATEMENT - Skip Current Iteration
# ═════════════════════════════════════════════════════════════════════════════
"""
CONTINUE:
    • Skips the rest of current iteration
    • Jumps to the next iteration
    • Code after continue is NOT executed for this iteration
    • Loop continues normally
"""

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                    SECTION 2: CONTINUE STATEMENT                      ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

print("2. CONTINUE STATEMENT - Skip Current Iteration")
print("-" * 60)

# Example 1: Skip odd numbers
print("Example 1: Print only even numbers (skip odd ones)")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 1:  # If odd
        continue  # Skip this one, go to next number
    
    print(number, end=" ")

print("\n")

# Example 2: Skip negative numbers
print("Example 2: Sum only positive numbers")
values = [10, -5, 20, -3, 15, -8, 25]
total = 0

for value in values:
    if value < 0:  # If negative
        print(f"Skipping {value} (negative)")
        continue  # Skip to next number
    
    print(f"Adding {value}")
    total = total + value

print(f"Total sum of positive numbers: {total}\n")

# Example 3: Skip empty strings
print("Example 3: Print only non-empty names")
names = ["Ali", "", "Bhavna", "", "Chirag", "Deepa", ""]

for name in names:
    if name == "":  # If empty
        continue  # Skip empty name
    
    print(f"Student: {name}")

print()

# Example 4: Skip invalid input
print("Example 4: Process numbers, skip non-numeric")
print("-" * 40)
items = [10, "abc", 20, "xyz", 30, 40, "invalid"]
total = 0

for item in items:
    if not isinstance(item, int):  # If NOT a number
        print(f"Skipping '{item}' (not a number)")
        continue  # Skip non-numbers
    
    print(f"Processing {item}")
    total = total + item

print(f"Total: {total}\n")

# Example 5: Continue with nested loop
print("Example 5: Skip certain students in grade calculation")
students = ["Ali", "Bhavna", "Chirag", "Deepa"]
grades = [85, 0, 92, 88]  # 0 means absent

print("Grade Report (skip absent students):")
for index in range(len(students)):
    name = students[index]
    grade = grades[index]
    
    if grade == 0:  # If absent
        print(f"{name}: ABSENT - Skipping")
        continue
    
    if grade >= 90:
        status = "Excellent"
    elif grade >= 80:
        status = "Good"
    else:
        status = "Average"
    
    print(f"{name}: {grade} ({status})")

print("\n")