# RETURN VALUES - Getting Data Back From Functions

# =============================================================================
# 1. FUNCTION WITHOUT RETURN (Returns None)
# =============================================================================

def print_message(message):
    """This function prints but doesn't return anything"""
    print(f"Message: {message}")

result = print_message("Hello")
print(f"Result: {result}")  # Output: None (no return statement)


# =============================================================================
# 2. FUNCTION WITH SINGLE RETURN VALUE
# =============================================================================

def add(a, b):
    """Calculate sum and return it"""
    total = a + b
    return total  # Send value back

result = add(5, 3)
print(f"5 + 3 = {result}")  # Output: 5 + 3 = 8


# =============================================================================
# 3. RETURN vs PRINT - MAJOR DIFFERENCE
# =============================================================================

# ❌ Using PRINT (not good for reuse)
def add_with_print(x, y):
    """This prints but doesn't return"""
    print(x + y)  # Prints to screen but doesn't return value

add_with_print(10, 20)  # Prints: 30
value1 = add_with_print(10, 20)  # Prints: 30, but value1 = None
print(value1)  # Output: None (can't reuse)


# ✅ Using RETURN (better for reuse)
def add_with_return(x, y):
    """This returns the value"""
    return x + y  # Send value back

result = add_with_return(10, 20)  # Doesn't print, but returns 30
print(result)  # Output: 30 (we can reuse the value)
doubled = add_with_return(10, 20) * 2  # Can use in calculations
print(doubled)  # Output: 60


# =============================================================================
# 4. EARLY RETURN (Return Before End of Function)
# =============================================================================

def check_age(age):
    """Early return exits function immediately"""
    if age < 0:
        return "Age cannot be negative"  # Exit here
    
    if age < 18:
        return "You are a minor"  # Exit here
    
    if age >= 65:
        return "You are a senior"  # Exit here
    
    return "You are an adult"  # Default return

print(check_age(-5))   # Output: Age cannot be negative
print(check_age(10))   # Output: You are a minor
print(check_age(25))   # Output: You are an adult
print(check_age(70))   # Output: You are a senior


# =============================================================================
# 5. RETURNING MULTIPLE VALUES (AS TUPLE)
# =============================================================================

def get_coordinates():
    """Return multiple values (automatically creates tuple)"""
    x = 10
    y = 20
    return x, y  # Returns a tuple (10, 20)

coordinates = get_coordinates()
print(coordinates)      # Output: (10, 20)
print(type(coordinates))  # Output: <class 'tuple'>

# Unpack the tuple
x, y = get_coordinates()
print(f"X: {x}, Y: {y}")  # Output: X: 10, Y: 20


# =============================================================================
# 6. RETURNING MULTIPLE VALUES - UNPACKING
# =============================================================================

def get_student_info(student_id):
    """Return multiple pieces of information about a student"""
    name = "Alice"
    age = 20
    grade = "A"
    gpa = 3.8
    
    return name, age, grade, gpa  # Return as tuple

# Unpack all values
name, age, grade, gpa = get_student_info(1)
print(f"Name: {name}, Age: {age}, Grade: {grade}, GPA: {gpa}")

# No unpacking - get as tuple
all_info = get_student_info(1)
print(all_info)  # Output: ('Alice', 20, 'A', 3.8)

# Partial unpacking
name, *rest = get_student_info(1)
print(f"Name: {name}, Other info: {rest}")


# =============================================================================
# 7. RETURNING DIFFERENT TYPES
# =============================================================================

def process_number(n):
    """Return different types based on input"""
    if n < 0:
        return "number is negative"        # Returns string
    elif n == 0:
        return [0, 0, 0]                   # Returns list
    elif n < 10:
        return n * 2                       # Returns integer
    elif n < 100:
        return {"value": n, "square": n**2}  # Returns dictionary
    else:
        return (n, n**2, n**3)             # Returns tuple

print(process_number(-5))    # Output: number is negative
print(process_number(0))     # Output: [0, 0, 0]
print(process_number(5))     # Output: 10
print(process_number(15))    # Output: {'value': 15, 'square': 225}
print(process_number(100))   # Output: (100, 10000, 1000000)


# =============================================================================
# 8. RETURNING COMPLEX DATA STRUCTURES
# =============================================================================

def get_user_profile():
    """Return a dictionary with user information"""
    profile = {
        "username": "alice123",
        "email": "alice@email.com",
        "age": 25,
        "skills": ["Python", "JavaScript", "SQL"],
        "social": {
            "twitter": "@alice",
            "github": "alice-dev"
        }
    }
    return profile

user = get_user_profile()
print(user["username"])              # Output: alice123
print(user["skills"][0])             # Output: Python
print(user["social"]["twitter"])     # Output: @alice


# =============================================================================
# 9. PRACTICAL EXAMPLE - CALCULATOR FUNCTIONS
# =============================================================================

def calculate_bmi(weight, height):
    """Calculate Body Mass Index and return interpretation"""
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category  # Return calculated value and category

# Using the function
bmi_value, status = calculate_bmi(70, 1.75)
print(f"BMI: {bmi_value:.2f}")  # Output: BMI: 22.86
print(f"Status: {status}")       # Output: Status: Normal weight


# =============================================================================
# 10. RETURNING LIST/DICTIONARY FOR MULTIPLE VALUES
# =============================================================================

def calculate_stats(numbers):
    """Return multiple statistics as dictionary"""
    stats = {
        "sum": sum(numbers),
        "count": len(numbers),
        "average": sum(numbers) / len(numbers),
        "minimum": min(numbers),
        "maximum": max(numbers)
    }
    return stats

data = [10, 20, 30, 40, 50]
results = calculate_stats(data)

print(f"Sum: {results['sum']}")        # Output: Sum: 150
print(f"Average: {results['average']}")  # Output: Average: 30.0
print(f"Min: {results['minimum']}")    # Output: Min: 10
print(f"Max: {results['maximum']}")    # Output: Max: 50


# =============================================================================
# 11. CHAINING FUNCTION RETURNS
# =============================================================================

def get_price():
    """Return a price"""
    return 100

def add_tax(price):
    """Add 10% tax to price"""
    return price * 1.10

def apply_discount(price, discount):
    """Apply discount percentage"""
    return price * (1 - discount / 100)

# Chain the functions
price = get_price()                    # 100
price_with_tax = add_tax(price)        # 110
final_price = apply_discount(price_with_tax, 10)  # 99

print(f"Original: {price}")            # Output: Original: 100
print(f"With Tax: {price_with_tax}")   # Output: With Tax: 110
print(f"Final: {final_price}")         # Output: Final: 99.0


# =============================================================================
# 12. OPTIONAL RETURN (Could Return None or Value)
# =============================================================================

def find_student(names, target):
    """Find student and return position, or None if not found"""
    for i, name in enumerate(names):
        if name == target:
            return i  # Found it, return position
    
    return None  # Not found

students = ["Alice", "Bob", "Charlie", "Diana"]

position1 = find_student(students, "Bob")
print(f"Bob's position: {position1}")  # Output: Bob's position: 1

position2 = find_student(students, "Eve")
if position2 is None:
    print("Eve not found")  # Output: Eve not found
else:
    print(f"Eve's position: {position2}")


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================

# ❌ MISTAKE 1: Confusing RETURN and PRINT
def wrong_function():
    print(42)  # This prints but doesn't return
    
result = wrong_function()  # result will be None
# print(result + 1)  # ERROR: can't add int to None


# ✅ Correct: Use RETURN
def right_function():
    return 42  # This actually returns the value

result = right_function()
print(result + 1)  # Output: 43


# ❌ MISTAKE 2: Return inside vs outside loop
def sum_with_wrong_return(numbers):
    for num in numbers:
        return num  # Returns immediately on first number!

# ✅ Correct: Return after loop
def sum_with_right_return(numbers):
    total = 0
    for num in numbers:
        total += num
    return total  # Returns after processing all

print(sum_with_wrong_return([1, 2, 3]))   # Output: 1 (wrong!)
print(sum_with_right_return([1, 2, 3]))   # Output: 6 (correct!)


# ❌ MISTAKE 3: Using undefined return
def problematic():
    x = 5
    # No return statement

# If no return, function returns None automatically


# =============================================================================
# KEY POINTS SUMMARY
# =============================================================================

"""
✅ RETURN - sends value back from function
✅ No return = None is returned
✅ return stops function execution immediately

✅ Single value: return value
✅ Multiple values: return val1, val2, val3 (becomes tuple)
✅ Unpack: a, b, c = function()

✅ RETURN > PRINT (for reusable functions)
✅ Early return - exit function before end
✅ Can return any type: int, str, list, dict, tuple

Functions are powerful when they RETURN values for reuse!
"""
