# FUNCTION BASICS - How to Define and Call Functions

# =============================================================================
# 1. DEFINING A SIMPLE FUNCTION
# =============================================================================

# Basic structure:
# def function_name():
#     code here
#     return value (optional)

def say_hello():
    """This function prints a greeting"""
    print("Hello, World!")

# Call the function
say_hello()  # Output: Hello, World!


# =============================================================================
# 2. FUNCTION WITH PARAMETERS
# =============================================================================

def greet(name):
    """Function that takes one parameter"""
    print(f"Hello, {name}!")

greet("Alice")    # Output: Hello, Alice!
greet("Bob")      # Output: Hello, Bob!


# =============================================================================
# 3. FUNCTION WITH MULTIPLE PARAMETERS
# =============================================================================

def add_numbers(a, b):
    """Function that adds two numbers"""
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)   # Output: 5 + 3 = 8
add_numbers(10, 20) # Output: 10 + 20 = 30


# =============================================================================
# 4. FUNCTION WITH RETURN STATEMENT
# =============================================================================

def multiply(x, y):
    """Function that returns a value"""
    return x * y

result = multiply(4, 5)
print(f"Result: {result}")  # Output: Result: 20


# =============================================================================
# 5. FUNCTION WITH NO PARAMETERS AND NO RETURN
# =============================================================================

def describe_function():
    """Function with no input or output"""
    print("This function takes no parameters")
    print("And returns nothing")

describe_function()


# =============================================================================
# 6. DOCSTRINGS - EXPLAINING YOUR FUNCTION
# =============================================================================

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length (int/float): The length of the rectangle
        width (int/float): The width of the rectangle
    
    Returns:
        int/float: The area of the rectangle
    
    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width

print(calculate_area(5, 3))  # Output: 15


# =============================================================================
# 7. FUNCTION ANATOMY
# =============================================================================

def full_example(parameter1, parameter2):
    """
    This explains all parts of a function.
    
    This is the DOCSTRING - explains what function does
    """
    # This is the FUNCTION BODY - actual code
    result = parameter1 + parameter2
    print(f"Sum: {result}")
    
    # This is the RETURN STATEMENT - sends value back
    return result

# This is a FUNCTION CALL - execute the function
output = full_example(10, 20)


# =============================================================================
# 8. IMPORTANT DISTINCTIONS
# =============================================================================

# Function definition (creating the function)
def say_goodbye():
    return "Goodbye!"

# Function call (using the function)
message = say_goodbye()
print(message)  # Output: Goodbye!

# WITHOUT parentheses = refers to the function object (doesn't run)
function_reference = say_goodbye
print(function_reference)  # Output: <function say_goodbye at 0x...>

# WITH parentheses = calls the function (runs it)
function_result = say_goodbye()
print(function_result)     # Output: Goodbye!


# =============================================================================
# 9. PRACTICAL EXAMPLE - USER REGISTRATION
# =============================================================================

def create_user(username, email, age):
    """Create a new user account"""
    if age < 18:
        return "Must be 18 years old"
    
    user_info = {
        "username": username,
        "email": email,
        "age": age
    }
    return user_info

# Using the function
user1 = create_user("john_doe", "john@email.com", 25)
print(user1)  # Output: {'username': 'john_doe', 'email': 'john@email.com', 'age': 25}

user2 = create_user("teen_user", "teen@email.com", 15)
print(user2)  # Output: Must be 18 years old


# =============================================================================
# 10. FUNCTION RETURNING MULTIPLE VALUES
# =============================================================================

def get_student_info(name, marks):
    """Get student name, marks and pass/fail status"""
    total = sum(marks)
    average = total / len(marks)
    status = "Pass" if average >= 40 else "Fail"
    
    return name, total, average, status

# Calling function that returns multiple values
name, total, avg, status = get_student_info("Alice", [85, 90, 78])
print(f"Name: {name}")
print(f"Total: {total}")
print(f"Average: {avg}")
print(f"Status: {status}")


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================

# ❌ MISTAKE 1: Forgetting to call the function
def hello():
    return "Hello!"

hello        # This doesn't print anything (just references the function)
print(hello())  # ✅ This actually calls it


# ❌ MISTAKE 2: Returning inside vs outside function
def wrong_return():
    x = 5
    # return statement MUST be inside the function body
    # If indented here, it won't run

# ✅ Correct: return is indented (inside function)
def right_return():
    x = 5
    return x


# ❌ MISTAKE 3: Not using returned value
def calculate():
    return 10 + 5  # This calculates but result is lost

calculate()  # Result disappears, not stored

# ✅ Correct: Store the returned value
result = calculate()
print(result)  # Now we can use it


# =============================================================================
# KEY POINTS SUMMARY
# =============================================================================

"""
✅ def keyword - starts a function definition
✅ function_name - choose descriptive names
✅ parameters - inputs to the function
✅ docstring - explain what function does
✅ return - send value back to caller
✅ call with () - always use parentheses to call

Functions make code:
- Reusable (define once, use many times)
- Organized (split into logical parts)
- Maintainable (easy to update)
- Readable (clear purpose)
"""
