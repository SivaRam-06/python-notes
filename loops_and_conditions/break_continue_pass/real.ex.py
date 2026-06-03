# ═════════════════════════════════════════════════════════════════════════════
# 6. REAL-WORLD EXAMPLES
# ═════════════════════════════════════════════════════════════════════════════
print("EXAMPLE 1: Student Attendance System (skip absent)")
print("-" * 60)
attendance = [True, False, True, True, False, True, True]

present_count = 0
for day, is_present in enumerate(attendance, start=1):
    if not is_present:
        continue  # Skip if absent
    
    present_count = present_count + 1
    print(f"Day {day}: Present")

total_days = len(attendance)
absent_days = total_days - present_count
print(f"\nPresent: {present_count} days")
print(f"Absent: {absent_days} days")
print(f"Attendance: {(present_count/total_days)*100:.1f}%")

print("\n")

print("EXAMPLE 2: Login System with Limited Attempts")
print("-" * 60)
correct_password = "secret123"
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    password = input(f"Attempt {attempt}/{max_attempts}: Enter password: ")
    
    if password == correct_password:
        print("✓ Login successful! Welcome!")
        break  # Exit loop when password is correct
    elif attempt < max_attempts:
        print("✗ Wrong password. Try again.")
    else:
        print("✗ Maximum attempts reached. Account locked!")

print()

print("EXAMPLE 3: Process data, skip invalid entries")
print("-" * 60)
"""
Skip negative numbers and zeros
Calculate average of valid numbers
"""
numbers_list = [10, -5, 20, 0, 15, -8, 25, 30]
total = 0
count = 0

print(f"Processing: {numbers_list}")
for num in numbers_list:
    if num <= 0:
        print(f"  Skipping {num} (invalid)")
        continue  # Skip zero and negative numbers
    
    print(f"  Adding {num}")
    total = total + num
    count = count + 1

if count > 0:
    average = total / count
    print(f"\nValid numbers: {count}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
else:
    print("No valid numbers!")

print("\n")

print("EXAMPLE 4: Find item in inventory (stop when found)")
print("-" * 60)
inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 0,
    "mango": 45,
    "grape": 20
}

search_item = "mango"
found = False

for item, quantity in inventory.items():
    if item == search_item:
        print(f"Found '{search_item}'!")
        print(f"Quantity in stock: {quantity}")
        found = True
        break  # Stop searching once found
    else:
        print(f"Checking '{item}'...")

if not found:
    print(f"'{search_item}' not found in inventory")

print("\n")