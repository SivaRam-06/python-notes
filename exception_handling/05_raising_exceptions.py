# exception_handling/05_raising_exceptions.py
"""
RAISING EXCEPTIONS
==================

What is it?
-----------
Manually creating and throwing exceptions in your code.

When to use it?
---------------
Use raise when:
1. You want to signal an error condition
2. Input validation fails
3. A function receives invalid parameters
4. You want to convert one error type to another

How to identify it?
-------------------
Look for situations where you need to signal that something went wrong.
"""

# Example 1: Basic raise
print("=== BASIC RAISE ===")

def calculate_square_root(number):
    if number < 0:
        # Raise an error for invalid input
        raise ValueError("Cannot calculate square root of negative number")
    return number ** 0.5

try:
    result = calculate_square_root(-9)
    print(f"Square root: {result}")
except ValueError as e:
    print(f"Error: {e}")

# Example 2: Re-raising exceptions
print("\n=== RE-RAISING EXCEPTIONS ===")

def process_data(data):
    try:
        # Try to process the data
        if not data:
            raise ValueError("Data is empty")
        return data.upper()
    except ValueError as e:
        print(f"Error in process_data: {e}")
        # Re-raise the exception for higher-level handling
        raise

try:
    result = process_data("")
    print(f"Processed data: {result}")
except ValueError as e:
    print(f"Higher-level error handling: {e}")

# Example 3: Creating custom exceptions
print("\n=== CREATING CUSTOM EXCEPTIONS ===")

class InvalidEmailError(Exception):
    """Exception raised for invalid email addresses"""
    def __init__(self, email, message="Invalid email address"):
        self.email = email
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message}: {self.email}"

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError(email)
    return True

try:
    validate_email("invalid-email")
    print("Email is valid")
except InvalidEmailError as e:
    print(f"Email validation failed: {e}")

"""
Key Points:
- Use raise to signal errors in your code
- You can raise built-in or custom exceptions
- Re-raising allows higher-level error handling
- Custom exceptions make error handling more specific
"""
