# PARAMETERS AND ARGUMENTS - Understanding Function Inputs

# =============================================================================
# CONCEPT: PARAMETERS vs ARGUMENTS
# =============================================================================

"""
PARAMETER = Variable in function definition
ARGUMENT = Value passed to the function when calling it

def greet(name):           # 'name' is a PARAMETER
    print(f"Hello, {name}")

greet("Alice")             # "Alice" is an ARGUMENT
"""


# =============================================================================
# 1. POSITIONAL ARGUMENTS
# =============================================================================

"""
Order matters!
Arguments are matched to parameters by position (left to right)
"""

def introduce(name, age, city):
    """Takes three positional arguments in order"""
    print(f"{name} is {age} years old and lives in {city}")

# ✅ Correct - arguments in same order as parameters
introduce("Alice", 25, "New York")
# Output: Alice is 25 years old and lives in New York

# ❌ Wrong order = wrong output
introduce("New York", 25, "Alice")  
# Output: New York is 25 years old and lives in Alice (wrong!)


# =============================================================================
# 2. KEYWORD ARGUMENTS
# =============================================================================

"""
You can use parameter names when calling
Order doesn't matter with keyword arguments
More readable and less error-prone
"""

def create_profile(name, age, job):
    """Function with parameters"""
    print(f"Name: {name}, Age: {age}, Job: {job}")

# ✅ Using keyword arguments - order doesn't matter
create_profile(name="Bob", age=30, job="Engineer")
create_profile(job="Teacher", age=28, name="Charlie")
create_profile(age=35, name="Diana", job="Doctor")

# All produce correct output regardless of order!


# =============================================================================
# 3. MIXING POSITIONAL AND KEYWORD ARGUMENTS
# =============================================================================

def book_flight(passenger_name, destination, seats=1, class_type="economy"):
    """Can mix positional (required) and keyword (optional)"""
    print(f"Passenger: {passenger_name}")
    print(f"From: Departure, To: {destination}")
    print(f"Seats: {seats}, Class: {class_type}")
    print()

# ✅ All valid
book_flight("Alice", "Paris")                              # Positional only
book_flight("Bob", "London", 2)                           # Positional + positional
book_flight("Charlie", "Tokyo", seats=3)                  # Positional + keyword
book_flight("Diana", "Dubai", 2, "business")              # All positional
book_flight("Eve", "Rome", class_type="first")            # Positional + keyword

# ❌ MISTAKE: Positional AFTER keyword (not allowed)
# book_flight("Frank", class_type="premium", "Berlin")   # ERROR!


# =============================================================================
# 4. UNDERSTANDING PARAMETER SCOPE
# =============================================================================

def display_info(x, y):
    """Parameters are local to the function"""
    print(f"Inside function: x={x}, y={y}")
    return x + y

result = display_info(10, 20)
print(f"Result: {result}")

# ❌ Can't access parameters outside function
# print(x)  # NameError: name 'x' is not defined


# =============================================================================
# 5. MODIFYING PARAMETERS INSIDE FUNCTION
# =============================================================================

def modify_list(my_list):
    """Lists are mutable - changes affect original"""
    my_list.append("new item")
    print(f"Inside function: {my_list}")

original = [1, 2, 3]
print(f"Before: {original}")
modify_list(original)
print(f"After: {original}")  # List was modified!

# Mutable types (list, dict, set) - changes persist
# Immutable types (int, str, tuple) - changes don't persist


# =============================================================================
# 6. PRACTICAL EXAMPLE - STUDENT GRADES
# =============================================================================

def calculate_grade(name, math_score, english_score, science_score):
    """Calculate student's overall grade"""
    total = math_score + english_score + science_score
    average = total / 3
    
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    else:
        grade = 'F'
    
    print(f"Student: {name}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}\n")

# Calling with positional arguments
calculate_grade("Alice", 95, 88, 92)

# Calling with keyword arguments (more readable)
calculate_grade(
    name="Bob",
    math_score=78,
    english_score=82,
    science_score=80
)

# Calling with mixed arguments
calculate_grade("Charlie", 88, science_score=85, english_score=90)


# =============================================================================
# 7. PARAMETER NAMING BEST PRACTICES
# =============================================================================

# ❌ Bad: Unclear parameter names
def calc(a, b, c):
    return a + b + c

# ✅ Good: Descriptive parameter names
def calculate_total(salary, bonus, allowance):
    return salary + bonus + allowance

# Makes code more readable
monthly_total = calculate_total(
    salary=5000,
    bonus=1000,
    allowance=500
)
print(f"Monthly Total: {monthly_total}")


# =============================================================================
# 8. FUNCTION WITH MANY PARAMETERS
# =============================================================================

# ❌ Too many parameters makes function hard to use
def bad_function(a, b, c, d, e, f, g, h):
    pass

# ✅ Better: Use dictionary or class for related data
def good_function(user_data):
    """Takes one parameter with all data"""
    name = user_data['name']
    email = user_data['email']
    age = user_data['age']
    # ... use the data

user = {
    'name': 'Alice',
    'email': 'alice@email.com',
    'age': 25
}
good_function(user)


# =============================================================================
# 9. HOW FUNCTION CALLS WORK - ORDER OF EXECUTION
# =============================================================================

def demo_execution(x):
    """Show how parameters get values"""
    print(f"1. Function called with argument: {x}")
    print(f"2. Parameter x receives value: {x}")
    print(f"3. Inside function body")
    return x * 2

print("Step 1: Before function call")
result = demo_execution(5)
print(f"Step 2: After function call, result: {result}")


# =============================================================================
# 10. PARAMETER VALIDATION
# =============================================================================

def divide(numerator, denominator):
    """Validate parameters before using them"""
    # Check if parameters are numbers
    if not isinstance(numerator, (int, float)):
        return "Error: numerator must be a number"
    
    if not isinstance(denominator, (int, float)):
        return "Error: denominator must be a number"
    
    # Check if denominator is not zero
    if denominator == 0:
        return "Error: cannot divide by zero"
    
    return numerator / denominator

print(divide(10, 2))       # Output: 5.0
print(divide(10, 0))       # Output: Error: cannot divide by zero
print(divide("ten", 2))    # Output: Error: numerator must be a number


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================

# ❌ MISTAKE 1: Wrong number of arguments
def needs_two(a, b):
    return a + b

# needs_two(5)              # ERROR: Missing argument
# needs_two(5, 10, 15)      # ERROR: Too many arguments

# ✅ Correct: Provide exactly the right number
result = needs_two(5, 10)


# ❌ MISTAKE 2: Using undefined parameters
def wrong_params(name):
    # print(age)  # ERROR: 'age' was never passed
    print(name)

# ✅ Correct: Only use parameters that are passed
wrong_params("Alice")


# ❌ MISTAKE 3: Forgetting parentheses in function call
def get_value():
    return 42

value = get_value  # References function, doesn't call it
print(value)       # Prints: <function get_value at 0x...>

# ✅ Correct: Use parentheses to call
value = get_value()  # Actually calls the function
print(value)         # Prints: 42


# =============================================================================
# KEY POINTS SUMMARY
# =============================================================================

"""
✅ PARAMETERS - variables in function definition
✅ ARGUMENTS - actual values passed to function

✅ POSITIONAL ARGUMENTS - order matters
✅ KEYWORD ARGUMENTS - use parameter names, order doesn't matter
✅ CAN MIX - positional first, then keyword

✅ Positional args must come before keyword args
✅ Use descriptive parameter names
✅ Validate parameters when necessary
✅ Always use () to call a function

Functions help organize code and make it reusable!
"""
