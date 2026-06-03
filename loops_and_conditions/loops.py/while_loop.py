# ═════════════════════════════════════════════════════════════════════════════
# 5. WHILE LOOP - Loop Until Condition Becomes False
# ═════════════════════════════════════════════════════════════════════════════
"""
WHILE LOOP:
    Syntax:
        while condition:
            # Code to repeat
            # Must change something to eventually make condition FALSE
    
    • Repeat WHILE condition is TRUE
    • When condition becomes FALSE, loop stops
    • YOU must change something inside loop
    • DANGER: Infinite loop if you forget to change condition!
"""

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                    SECTION 5: WHILE LOOPS                             ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

print("5. WHILE LOOP - Repeat Until Condition is False")
print("-" * 60)

# Example 1: Count up to 5
print("Count from 1 to 5:")
number = 1
while number <= 5:
    print(number, end=" ")
    number = number + 1  # IMPORTANT: Change the condition variable!
print("\n")

# Example 2: Countdown from 10 to 1
print("Countdown from 10 to 1:")
countdown = 10
while countdown > 0:
    print(countdown, end=" ")
    countdown = countdown - 1
print("\n")

# Example 3: Keep asking for password until correct
print("\nExample 3: Keep asking for password until correct")
print("-" * 60)
correct_password = "secret123"
entered_password = ""
attempts = 0

while entered_password != correct_password:
    entered_password = input("Enter password: ")
    attempts = attempts + 1
    if entered_password != correct_password:
        print("❌ Wrong password! Try again.")
    else:
        print(f"✓ Correct! You took {attempts} attempt(s).")

print()

# Example 4: Game lives example
print("Example 4: Game Lives - Keep playing while you have lives")
print("-" * 60)
lives = 3
level = 1

while lives > 0:
    print(f"Level {level} - Lives remaining: {lives}")
    print(f"  Try to complete the level...")
    # Simulate: Did you pass?
    if level % 2 == 0:  # Pass on even levels
        print(f"  ✓ Passed Level {level}!")
        level = level + 1
    else:  # Fail on odd levels
        print(f"  ✗ Failed Level {level}. You lost 1 life!")
        lives = lives - 1
    print()

if lives == 0:
    print("Game Over! You lost all your lives.")
else:
    print(f"You completed all levels! Congratulations!")

print("\n")

# Example 5: Sum numbers until user enters 0
print("Example 5: Sum numbers until user enters 0")
print("-" * 60)
total_sum = 0
number = 1

while number != 0:
    number = int(input("Enter a number (0 to stop): "))
    if number != 0:
        total_sum = total_sum + number
        print(f"Added {number}, Running total: {total_sum}")

print(f"Final sum: {total_sum}")

print("\n")
