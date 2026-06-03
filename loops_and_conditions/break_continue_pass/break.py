"""
╔════════════════════════════════════════════════════════════════════════════╗
║          BREAK, CONTINUE, PASS & LOOP CONTROL - COMPLETE GUIDE            ║
║                    Master Loop Control Statements                         ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

# ═════════════════════════════════════════════════════════════════════════════
# 1. WHAT ARE BREAK, CONTINUE, AND PASS?
# ═════════════════════════════════════════════════════════════════════════════
"""
These are special statements used INSIDE loops to control loop behavior:

BREAK:
    • Stops the loop immediately
    • Exits from the loop
    • Jumps to code after the loop
    
CONTINUE:
    • Skips the rest of current iteration
    • Goes directly to next iteration
    • Rest of loop code is NOT executed for this iteration
    
PASS:
    • Does nothing (placeholder)
    • Used when you need a statement but have nothing to do
    • Doesn't affect loop, just passes control to next line

WHY?
    • break: Exit loop when condition is met (search found, user quit, etc.)
    • continue: Skip certain items (skip negative numbers, invalid input, etc.)
    • pass: Create empty code blocks that will be filled later
"""

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                      SECTION 1: BREAK STATEMENT                       ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

# ═════════════════════════════════════════════════════════════════════════════
# 1. BREAK STATEMENT - Exit Loop Immediately
# ═════════════════════════════════════════════════════════════════════════════
"""
BREAK:
    • Immediately stops the loop
    • Exits to code after the loop
    • Used to stop when you find what you're looking for
    • Works in FOR and WHILE loops
"""

print("1. BREAK STATEMENT - Exit Loop Immediately")
print("-" * 60)

# Example 1: Find a number in a list
print("Example 1: Find number 7 in list")
numbers = [2, 4, 6, 7, 8, 9, 10]
print(f"List: {numbers}")

for number in numbers:
    if number == 7:
        print(f"Found 7! Stopping search.")
        break  # Stop here, don't check 8, 9, 10
    else:
        print(f"Checking {number}... not found yet")

print("Search completed!\n")

# Example 2: User enters correct password
print("Example 2: User enters password (correct = 'password123')")
password = "password123"

for attempt in range(1, 4):  # Maximum 3 attempts
    entered = input(f"Attempt {attempt}: Enter password: ")
    if entered == password:
        print("✓ Password correct! Welcome!")
        break  # Exit loop when correct
    else:
        if attempt < 3:
            print("✗ Wrong password. Try again.")
        else:
            print("✗ Wrong password. No more attempts!")

print()

# Example 3: Search in range
print("Example 3: Find first even number starting from 15")
print("Numbers: 15, 16, 17, 18, 19...")

for number in range(15, 25):
    if number % 2 == 0:
        print(f"Found even number: {number}")
        break  # Stop when we find first even

print()

# Example 4: Stop when inventory is empty
print("Example 4: Sell items until sold out")
inventory = 5

for day in range(1, 10):
    if inventory == 0:
        print("Day", day, ": Store closed - sold out!")
        break  # Stop selling when no stock
    
    print(f"Day {day}: Sold 1 item. Remaining: {inventory - 1}")
    inventory = inventory - 1

print()

# Example 5: Exit infinite loop with break
print("Example 5: Keep asking until user says 'stop'")
user_input = ""

while True:  # Infinite loop
    user_input = input("Enter command (or 'stop' to quit): ")
    if user_input.lower() == "stop":
        print("Exiting program...")
        break  # This is the ONLY way to exit the while True loop
    else:
        print(f"You entered: {user_input}")

print("\n")
