# FUNCTIONS - TIPS AND BEST PRACTICES

# =============================================================================
# TIPS FOR WRITING GOOD FUNCTIONS
# =============================================================================

# TIP 1: Use Descriptive Names
# ❌ Bad names
def f(x):
    return x * 2

def calc(a, b):
    return a + b

# ✅ Good names
def double_value(number):
    return number * 2

def add_numbers(first, second):
    return first + second


# TIP 2: Keep Functions Small and Focused
# ❌ Function doing too much
def process_user_data(user):
    # Validate
    if not user.get("name"):
        raise ValueError("Name required")
    # Process
    name = user["name"].strip().title()
    # Save to database
    # ... lots of code
    # Send email
    # ... more code

# ✅ Break into smaller functions
def validate_user(user):
    if not user.get("name"):
        raise ValueError("Name required")
    return True

def format_name(user):
    return user["name"].strip().title()

def save_to_database(user):
    pass  # Save logic

def send_email(user):
    pass  # Email logic


# TIP 3: Use Default Parameters Wisely
# ❌ Too many required parameters
def create_report(title, data, format, sort, filter, limit):
    pass

# ✅ Use defaults for optional ones
def create_report(title, data, format="pdf", sort="date", 
                 filter=None, limit=100):
    pass


# TIP 4: Return Values Instead of Side Effects
# ❌ Using print in function (hard to reuse)
def calculate_bad(a, b):
    print(a + b)  # Can't reuse the result!

# ✅ Return the value
def calculate_good(a, b):
    return a + b  # Can use result in calculations


# TIP 5: Document with Docstrings
# ❌ No documentation
def process(x, y, z):
    return x * y / z

# ✅ Clear documentation
def calculate_rate(numerator, denominator, scale_factor=1):
    """
    Calculate the rate between two values.
    
    Parameters:
        numerator (float): The top value
        denominator (float): The bottom value
        scale_factor (float): Factor to scale result. Default: 1
    
    Returns:
        float: The calculated rate
    
    Raises:
        ZeroDivisionError: If denominator is 0
    """
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return (numerator / denominator) * scale_factor


# TIP 6: Handle Edge Cases
# ❌ Doesn't handle empty list
def get_average(numbers):
    return sum(numbers) / len(numbers)

# ✅ Handle edge cases
def get_average_safe(numbers):
    if not numbers:
        return 0  # or raise an error
    return sum(numbers) / len(numbers)


# TIP 7: Early Return to Reduce Nesting
# ❌ Nested if statements
def validate_password(password):
    if len(password) >= 8:
        if any(c.isupper() for c in password):
            if any(c.isdigit() for c in password):
                return True
    return False

# ✅ Early return (more readable)
def validate_password_good(password):
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True


# TIP 8: Use *args and **kwargs for Flexibility
# ❌ Limited to specific parameters
def log_v1(level, message, context):
    print(f"[{level}] {message} - {context}")

# ✅ Flexible argument handling
def log(*args, **kwargs):
    level = kwargs.get("level", "INFO")
    print(f"[{level}] {' '.join(str(arg) for arg in args)}")


# TIP 9: Clarify Intent with Type Hints (Python 3.5+)
# ❌ Unclear what types are expected
def calculate(x, y):
    return x + y

# ✅ Type hints make it clear
def calculate_typed(x: float, y: float) -> float:
    return x + y


# TIP 10: Pure Functions (No Side Effects)
# ❌ Function modifies external state
results = []

def add_result_bad(value):
    results.append(value)  # Modifies external list

# ✅ Pure function
def add_result_good(results_list, value):
    return results_list + [value]  # Returns new list


# =============================================================================
# COMMON MISTAKES AND HOW TO FIX THEM
# =============================================================================

# MISTAKE 1: Using mutable default arguments
print("n--- MISTAKE 1: Mutable Defaults ---")

# ❌ WRONG
def append_wrong(item, my_list=[]):
    my_list.append(item)
    return my_list

result1 = append_wrong(1)
result2 = append_wrong(2)
print(f"Wrong way: result1={result1}, result2={result2}")  # Both are [1, 2]!

# ✅ CORRECT
def append_right(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

result1 = append_right(1)
result2 = append_right(2)
print(f"Right way: result1={result1}, result2={result2}")  # [1] and [2]


# MISTAKE 2: Modifying arguments (unexpected behavior)
print("n--- MISTAKE 2: Modifying Arguments ---")

# ❌ Modifying input list
def process_list_bad(items):
    items.append(999)  # Modifies the original!
    return items

original = [1, 2, 3]
result = process_list_bad(original)
print(f"Original after: {original}")  # Changed!

# ✅ Create new list
def process_list_good(items):
    new_items = items + [999]  # Doesn't modify original
    return new_items

original = [1, 2, 3]
result = process_list_good(original)
print(f"Original after: {original}")  # Unchanged!


# MISTAKE 3: Not Validating Input
print("n--- MISTAKE 3: No Input Validation ---")

# ❌ No validation
def divide_bad(a, b):
    return a / b

# divide_bad(10, 0)  # Crashes with ZeroDivisionError

# ✅ Validate input
def divide_good(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be a number")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be a number")
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b

try:
    result = divide_good(10, 2)
    print(f"10 / 2 = {result}")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")


# MISTAKE 4: Mixing Return and Print
print("n--- MISTAKE 4: Return vs Print ---")

# ❌ Print instead of return
def calculate_wrong():
    result = 5 + 3
    print(result)  # Just prints, doesn't return

value = calculate_wrong()  # value is None
# Can't use the result for further calculations

# ✅ Return the value
def calculate_right():
    result = 5 + 3
    return result

value = calculate_right()  # value is 8
doubled = value * 2  # Can use it!
print(f"Result: {value}, Doubled: {doubled}")


# MISTAKE 5: Variable Shadowing
print("n--- MISTAKE 5: Variable Shadowing ---")

total = 100  # Global

def calculate_bad():
    total = 5 + 3  # Creates LOCAL total, shadows global!
    return total

def calculate_good():
    amount = 5 + 3  # Use different name
    return amount
    # Or explicitly use global if needed: global total

result = calculate_bad()
print(f"Global total: {total}")  # Still 100
print(f"Returned: {result}")     # 8


# MISTAKE 6: Deep Recursion Without Base Case
print("n--- MISTAKE 6: Recursion Problems ---")

# ❌ Missing base case causes stack overflow
# def infinite_recursion(n):
#     return infinite_recursion(n - 1)  # No base case!

# ✅ Always have a base case
def correct_recursion(n):
    if n <= 0:  # BASE CASE
        return 0
    return n + correct_recursion(n - 1)

print(f"Sum 1 to 5: {correct_recursion(5)}")


# MISTAKE 7: Forgetting Parentheses When Calling
print("n--- MISTAKE 7: Function Call Syntax ---")

def get_message():
    return "Hello"

# ❌ Without parentheses (references function, doesn't call it)
message = get_message
print(type(message))  # <class 'function'>

# ✅ With parentheses (calls function)
message = get_message()
print(type(message))  # <class 'str'>


# =============================================================================
# DEBUGGING FUNCTIONS
# =============================================================================

print("n--- DEBUGGING TIPS ---")

# TIP 1: Print intermediate values
def debug_function(x, y):
    result1 = x * 2
    print(f"Debug: result1 = {result1}")  # Print to see intermediate value
    
    result2 = result1 + y
    print(f"Debug: result2 = {result2}")
    
    return result2

debug_function(5, 3)


# TIP 2: Use assert for validation
def process_number(n):
    assert isinstance(n, int), "n must be an integer"
    assert n > 0, "n must be positive"
    return n * 2

try:
    process_number(-5)
except AssertionError as e:
    print(f"Assertion failed: {e}")


# =============================================================================
# PERFORMANCE TIPS
# =============================================================================

print("n--- PERFORMANCE TIPS ---")

# TIP 1: Avoid unnecessary loops in functions
# ❌ Inefficient
def count_even_slow(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

# ✅ More efficient
def count_even_fast(numbers):
    return len([n for n in numbers if n % 2 == 0])

# ✅ Or even better
def count_even_best(numbers):
    return sum(1 for n in numbers if n % 2 == 0)


# TIP 2: Cache results for expensive operations
cache = {}

def expensive_calculation(n):
    if n in cache:
        return cache[n]
    
    result = sum(i for i in range(n))
    cache[n] = result
    return result


# =============================================================================
# FUNCTION DESIGN PRINCIPLES
# =============================================================================

"""
DRY (Don't Repeat Yourself)
- Extract repeated code into functions
- Reuse functions instead of copying code

KISS (Keep It Simple, Stupid)
- Functions should do ONE thing well
- Avoid over-engineering

YAGNI (You Aren't Gonna Need It)
- Don't add features you don't need yet
- Keep functions focused

SRP (Single Responsibility Principle)
- Each function should have one reason to change
- One job per function

Clean Code
- Use meaningful names
- Keep functions small
- Document with docstrings
- Handle errors gracefully
"""

print("n✅ Study these tips and practices to write better functions!")
