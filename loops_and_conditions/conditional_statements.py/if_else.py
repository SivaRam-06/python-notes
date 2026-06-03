# ═════════════════════════════════════════════════════════════════════════════
# 2. IF-ELSE STATEMENT
# ═════════════════════════════════════════════════════════════════════════════
"""
IF-ELSE:
    Syntax:
        if condition:
            # Code if TRUE
        else:
            # Code if FALSE
    
    • Use ELSE to handle the opposite case
    • Either IF block OR ELSE block will run - never both
    • One path must be taken
"""
print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                   SECTION 2: IF-ELSE STATEMENT                        ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

print("2. IF-ELSE STATEMENT")
print("-" * 60)

# Example 1: Check if age is adult or not
age = 15
if age >= 18:
    print(f"Age is {age}. You are an adult!")
else:
    print(f"Age is {age}. You are a minor!")

print()

# Example 2: Check if number is even or odd
number = 7
if number % 2 == 0:
    print(f"{number} is an EVEN number")
else:
    print(f"{number} is an ODD number")

print()

# Example 3: Check if temperature is hot or cold
temperature = 15
if temperature > 25:
    print(f"Temperature is {temperature}°C. It's HOT!")
else:
    print(f"Temperature is {temperature}°C. It's COLD!")

print()

# Example 4: Check if user is logged in
is_logged_in = False
if is_logged_in:
    print("Welcome back! You are logged in.")
else:
    print("Please log in to continue.")

print("\n")
