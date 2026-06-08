# exception_handling/08_best_practices.py
"""
EXCEPTION HANDLING BEST PRACTICES
=================================

What is it?
-----------
Guidelines for writing effective and maintainable exception handling code.

When to use it?
---------------
Always follow these practices when writing exception handling code.

How to identify it?
-------------------
Look for these patterns in well-written Python code.
"""

# Practice 1: Be specific about exceptions
print("=== BE SPECIFIC ABOUT EXCEPTIONS ===")

# Bad practice: Catching all exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except:
    print("Something went wrong")

# Good practice: Catch specific exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Practice 2: Use else for success cases
print("\n=== USE ELSE FOR SUCCESS CASES ===")

# Without else
try:
    file = open("data.txt", "r")
    content = file.read()
    # This print is inside the try block
    print("File read successfully")
except IOError:
    print("Error reading file")
finally:
    file.close()

# With else (better)
try:
    file = open("data.txt", "r")
except IOError:
    print("Error opening file")
else:
    # This only runs if no exception occurred
    content = file.read()
    print("File read successfully")
finally:
    file.close()

# Practice 3: Don't use exceptions for control flow
print("\n=== DON'T USE EXCEPTIONS FOR CONTROL FLOW ===")

# Bad practice: Using exceptions for normal flow
# try:
#     value = my_dict[key]
# except KeyError:
#     value = default_value

# # Good practice: Use get() method
# value = my_dict.get(key, default_value)

# Practice 4: Create meaningful error messages
print("\n=== CREATE MEANINGFUL ERROR MESSAGES ===")

class InvalidInputError(Exception):
    def __init__(self, input_value, expected_type):
        self.input_value = input_value
        self.expected_type = expected_type
        super().__init__(f"Invalid input: {input_value}. Expected {expected_type}")

def process_input(value):
    if not isinstance(value, int):
        raise InvalidInputError(value, "integer")
    return value * 2

try:
    result = process_input("not a number")
except InvalidInputError as e:
    print(f"Error: {e}")

# Practice 5: Use finally for cleanup
print("\n=== USE FINALLY FOR CLEANUP ===")

# Without finally (problematic)
file = open("data.txt", "w")
try:
    file.write("Some data")
    # If an error occurs here, file might not be closed
    # risky_operation()
except Exception as e:
    print(f"Error: {e}")
file.close()  # This might not execute if an exception occurs

# With finally (better)
file = open("data.txt", "w")
try:
    file.write("Some data")
    # risky_operation()
except Exception as e:
    print(f"Error: {e}")
finally:
    file.close()  # This always executes

"""
Key Points:
- Be specific about which exceptions you catch
- Use else for code that should only run on success
- Don't use exceptions for normal control flow
- Create meaningful error messages
- Always use finally for cleanup operations
- Follow these practices for maintainable code
"""
