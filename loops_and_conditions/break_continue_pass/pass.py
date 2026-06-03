# ═════════════════════════════════════════════════════════════════════════════
# 3. PASS STATEMENT - Do Nothing
# ═════════════════════════════════════════════════════════════════════════════
"""
PASS:
    • A placeholder that does nothing
    • Used when syntax requires a statement but you have nothing to do
    • Used while developing code (will add code later)
    • Does NOT affect loop
"""

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                      SECTION 3: PASS STATEMENT                        ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

print("3. PASS STATEMENT - Do Nothing (Placeholder)")
print("-" * 60)

# Example 1: Empty if block (will add code later)
print("Example 1: Using pass as placeholder")
age = 25

if age >= 18:
    pass  # TODO: Add code to check if verified member
else:
    print("Too young")

print("Code executed successfully\n")

# Example 2: Empty loop (for testing)
print("Example 2: Empty loop for testing")
for i in range(3):
    pass  # Does nothing, just loops

print("Loop completed\n")

# Example 3: Intentionally do nothing for certain values
print("Example 3: Do nothing for certain values, process others")
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 2 or number == 4:
        pass  # Do nothing for 2 and 4
    else:
        print(f"Processing: {number}")

print()

# Example 4: Empty function definition (will add code later)
print("Example 4: Creating empty function (will implement later)")
# def calculate_discount():
#     pass  # TODO: Implement discount logic

print("Code structure ready for implementation\n")

# Example 5: Common use - skip specific conditions
print("Example 5: Process data, skip some values")
data = [10, 20, 30, 40, 50]

for item in data:
    if item == 20 or item == 40:
        pass  # Skip processing for these values
    else:
        print(f"Item: {item}")

print("\n")
