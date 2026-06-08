# exception_handling/03_else_clause.py
"""
THE ELSE CLAUSE
===============

What is it?
-----------
The else clause runs only if the try block completes without errors.

When to use it?
---------------
Use else when you have code that should run only if no errors occurred,
but doesn't belong in the try block.

How to identify it?
-------------------
Look for code that should only execute if the try block succeeds.
"""

# Example 1: Basic else clause
print("=== BASIC ELSE CLAUSE ===")

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    # This runs only if no errors occurred
    print(f"10 divided by {num} is {result}")

# Example 2: Why use else?
print("\n=== WHY USE ELSE? ===")

try:
    # This might fail
    num = int(input("Enter a number: "))
    result = 10 / num
    # This print statement only runs if no errors
    print("Calculation successful!")
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero!")

# The same code with else (better practice)
try:
    num = int(input("Enter another number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero!")
else:
    # This only runs if no errors
    print("Calculation successful!")
    print(f"10 divided by {num} is {result}")

# Example 3: Real-world example
print("\n=== REAL-WORLD EXAMPLE ===")

try:
    filename = input("Enter a filename: ")
    with open(filename, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    # This only runs if the file was successfully opened and read
    print("File read successfully!")
    print(f"Content length: {len(content)} characters")

"""
Key Points:
- Else clause runs only if try block succeeds
- It separates error handling from success logic
- Makes code clearer and easier to maintain
- Use it for code that should only run on success
"""
