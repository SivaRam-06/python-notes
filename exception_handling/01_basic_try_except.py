# exception_handling/01_basic_try_except.py
"""
BASIC TRY-EXCEPT BLOCKS
=======================

What is it?
-----------
A try-except block lets you "try" code that might cause an error,
and "except" (catch) that error so your program doesn't crash.

When to use it?
---------------
Use try-except when:
1. Reading user input
2. Working with files
3. Making network requests
4. Any operation that might fail

How to identify it?
-------------------
Look for operations that could potentially fail or cause errors.
"""

# Example 1: Basic try-except
print("=== BASIC TRY-EXCEPT ===")

try:
    # Code that might cause an error
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"10 divided by {number} is {result}")
except:
    # What to do if an error occurs
    print("Something went wrong!")

# Example 2: Handling specific errors
print("\n=== HANDLING SPECIFIC ERRORS ===")

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"10 divided by {number} is {result}")
except ValueError:
    # Handles only conversion errors
    print("Please enter a valid number!")
except ZeroDivisionError:
    # Handles only division by zero
    print("You can't divide by zero!")

# Example 3: Getting error information
print("\n=== GETTING ERROR INFORMATION ===")

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"10 divided by {number} is {result}")
except Exception as e:
    # 'e' contains information about the error
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")

"""
Key Points:
- Try-except prevents program crashes
- You can handle specific errors or all errors
- Always try to handle specific errors when possible
- Use Exception as e to get error details
"""
