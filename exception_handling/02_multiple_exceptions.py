# exception_handling/02_multiple_exceptions.py
"""
HANDLING MULTIPLE EXCEPTIONS
============================

What is it?
-----------
Handling different types of errors in the same try block with
multiple except clauses.

When to use it?
---------------
Use when a single operation can cause different types of errors
that need different handling.

How to identify it?
-------------------
Look for operations that can fail in multiple ways.
"""

# Example 1: Handling different errors separately
print("=== HANDLING DIFFERENT ERRORS SEPARATELY ===")

try:
    # This can cause different errors
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"100 divided by {num} is {result}")
except ValueError:
    # Handle conversion error
    print("That's not a valid number!")
except ZeroDivisionError:
    # Handle division by zero
    print("You can't divide by zero!")
except Exception as e:
    # Handle any other errors
    print(f"An unexpected error occurred: {e}")

# Example 2: Handling multiple errors the same way
print("\n=== HANDLING MULTIPLE ERRORS THE SAME WAY ===")

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"100 divided by {num} is {result}")
except (ValueError, ZeroDivisionError):
    # Handle both errors the same way
    print("Please enter a valid non-zero number!")

# Example 3: Real-world file handling
print("\n=== REAL-WORLD FILE HANDLING ===")

filename = input("Enter a filename: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print(f"File content:\n{content}")
except FileNotFoundError:
    print(f"File '{filename}' not found!")
except PermissionError:
    print(f"You don't have permission to read '{filename}'!")
except IsADirectoryError:
    print(f"'{filename}' is a directory, not a file!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

"""
Key Points:
- Handle different errors with separate except blocks
- Group similar errors with parentheses
- Always handle specific errors first, then general ones
- Real-world code often needs to handle multiple error types
"""
