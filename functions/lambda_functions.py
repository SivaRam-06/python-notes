# LAMBDA FUNCTIONS - Anonymous Functions

# =============================================================================
# 1. WHAT ARE LAMBDA FUNCTIONS?
# =============================================================================

"""
LAMBDA = Small anonymous function (function without a name)
Used for simple, one-time use functions

Syntax: lambda parameters: expression

Like regular functions but:
- No name (anonymous)
- Single expression only
- Returns result automatically
"""


# =============================================================================
# 2. BASIC LAMBDA FUNCTION
# =============================================================================

# Regular function
def add_regular(x, y):
    return x + y

# Lambda equivalent
add_lambda = lambda x, y: x + y

print(add_regular(5, 3))  # Output: 8
print(add_lambda(5, 3))   # Output: 8


# =============================================================================
# 3. LAMBDA WITH SINGLE PARAMETER
# =============================================================================

square = lambda x: x ** 2
cube = lambda x: x ** 3

print(square(5))  # Output: 25
print(cube(5))    # Output: 125


# =============================================================================
# 4. LAMBDA WITH NO PARAMETERS
# =============================================================================

get_message = lambda: "Hello from Lambda!"
print(get_message())  # Output: Hello from Lambda!


# =============================================================================
# 5. LAMBDA WITH DEFAULT PARAMETER
# =============================================================================

greet = lambda name="Guest": f"Hello, {name}!"

print(greet())           # Output: Hello, Guest!
print(greet("Alice"))    # Output: Hello, Alice!


# =============================================================================
# 6. LAMBDA WITH CONDITIONAL (Ternary Operator)
# =============================================================================

# Lambda can use conditional expressions
max_value = lambda a, b: a if a > b else b
status = lambda age: "Adult" if age >= 18 else "Minor"

print(max_value(10, 20))  # Output: 20
print(status(25))         # Output: Adult
print(status(15))         # Output: Minor


# =============================================================================
# 7. LAMBDA WITH map() - Apply function to all elements
# =============================================================================

numbers = [1, 2, 3, 4, 5]

# Using regular function
def double(x):
    return x * 2

doubled_regular = list(map(double, numbers))
print(f"Using function: {doubled_regular}")  # [2, 4, 6, 8, 10]

# Using lambda - more concise
doubled_lambda = list(map(lambda x: x * 2, numbers))
print(f"Using lambda: {doubled_lambda}")     # [2, 4, 6, 8, 10]


# =============================================================================
# 8. LAMBDA WITH filter() - Keep elements that match condition
# =============================================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using regular function
def is_even(x):
    return x % 2 == 0

evens_regular = list(filter(is_even, numbers))
print(f"Using function: {evens_regular}")  # [2, 4, 6, 8, 10]

# Using lambda
evens_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Using lambda: {evens_lambda}")     # [2, 4, 6, 8, 10]

# More examples
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(f"Odd numbers: {odds}")              # [1, 3, 5, 7, 9]

larger_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Greater than 5: {larger_than_5}") # [6, 7, 8, 9, 10]


# =============================================================================
# 9. LAMBDA WITH sorted() - Custom sorting
# =============================================================================

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 88}
]

# Sort by grade (highest first)
sorted_by_grade = sorted(students, key=lambda s: s["grade"], reverse=True)
print("Sorted by grade (high to low):")
for student in sorted_by_grade:
    print(f"  {student['name']}: {student['grade']}")

print()

# Sort by name
sorted_by_name = sorted(students, key=lambda s: s["name"])
print("Sorted by name:")
for student in sorted_by_name:
    print(f"  {student['name']}: {student['grade']}")


# =============================================================================
# 10. LAMBDA WITH reduce() - Cumulative calculation
# =============================================================================

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Calculate product (1 * 2 * 3 * 4 * 5)
product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")  # Output: 120

# Calculate sum (alternative to sum())
total = reduce(lambda x, y: x + y, numbers)
print(f"Sum: {total}")        # Output: 15

# With starting value
running_sum = reduce(lambda x, y: x + y, numbers, 100)
print(f"Sum with start 100: {running_sum}")  # Output: 115


# =============================================================================
# 11. PRACTICAL EXAMPLE - DATA PROCESSING
# =============================================================================

data = [
    {"name": "Product A", "price": 10, "quantity": 5},
    {"name": "Product B", "price": 20, "quantity": 3},
    {"name": "Product C", "price": 15, "quantity": 2}
]

# Get total value of each product
totals = list(map(lambda item: item["price"] * item["quantity"], data))
print(f"Total value per product: {totals}")

# Filter expensive items (price > 12)
expensive = list(filter(lambda item: item["price"] > 12, data))
print(f"Expensive items: {[item['name'] for item in expensive]}")

# Sort by total value
sorted_by_value = sorted(data, key=lambda item: item["price"] * item["quantity"], reverse=True)
print(f"Most valuable: {sorted_by_value[0]['name']}")


# =============================================================================
# 12. PRACTICAL EXAMPLE - STRING PROCESSING
# =============================================================================

words = ["python", "lambda", "function", "code"]

# Convert to title case
titled = list(map(lambda w: w.title(), words))
print(f"Titled: {titled}")

# Filter words with length > 5
long_words = list(filter(lambda w: len(w) > 5, words))
print(f"Words > 5 chars: {long_words}")

# Sort by length (longest first)
by_length = sorted(words, key=lambda w: len(w), reverse=True)
print(f"By length: {by_length}")


# =============================================================================
# 13. WHEN NOT TO USE LAMBDA
# =============================================================================

# ❌ Too complex for lambda
# Complex logic should use regular function
# compare_complex = lambda x, y: (
#     "x is bigger" if x > y 
#     else "y is bigger" if y > x 
#     else "equal"
# )

# ✅ Use regular function for complex logic
def compare_complex(x, y):
    """Compare two numbers"""
    if x > y:
        return "x is bigger"
    elif y > x:
        return "y is bigger"
    else:
        return "equal"


# =============================================================================
# 14. LAMBDA GOTCHAS
# =============================================================================

# ❌ Gotcha 1: Lambda in loop (closure problem)
functions = []
for i in range(3):
    functions.append(lambda x: x + i)  # All use same 'i'!

print(f"Calling with 10:")
print(f"  func[0]: {functions[0](10)}")  # Output: 12 (not 10!)
print(f"  func[1]: {functions[1](10)}")  # Output: 12 (not 11!)
print(f"  func[2]: {functions[2](10)}")  # Output: 12 (correct)

# ✅ Fix: Use default parameter to capture current value
functions_fixed = []
for i in range(3):
    functions_fixed.append(lambda x, i=i: x + i)  # Capture i with default

print(f"Fixed with 10:")
print(f"  func[0]: {functions_fixed[0](10)}")  # Output: 10
print(f"  func[1]: {functions_fixed[1](10)}")  # Output: 11
print(f"  func[2]: {functions_fixed[2](10)}")  # Output: 12


# =============================================================================
# 15. LAMBDA vs REGULAR FUNCTION
# =============================================================================

# Lambda
simple_lambda = lambda x: x * 2

# Regular function
def simple_regular(x):
    return x * 2

print(simple_lambda(5))    # Output: 10
print(simple_regular(5))   # Output: 10

"""
When to use LAMBDA:
- Simple operations
- One-time use functions
- With map(), filter(), sorted()
- Short expressions that fit in one line

When to use REGULAR FUNCTION:
- Complex logic
- Multiple statements
- Reused multiple times
- Need comments/documentation
- Function will be called from different places
"""


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================

# ❌ MISTAKE 1: Lambda should be single expression
# bad_lambda = lambda x: (
#     print(x),
#     return x * 2
# )  # Can't have print and return!

# ✅ Correct: Single expression only
good_lambda = lambda x: x * 2


# ❌ MISTAKE 2: Using lambda for statement
# wrong = lambda x: if x > 5: print("big")  # ERROR: can't use if as statement


# ✅ Correct: Use if as expression
correct = lambda x: "big" if x > 5 else "small"


# ❌ MISTAKE 3: Overcomplicated lambda
# complicated = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"

# ✅ Better: Use regular function for complexity
def categorize(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "zero"


# =============================================================================
# KEY POINTS SUMMARY
# =============================================================================

"""
✅ LAMBDA = Anonymous function (no name)
✅ Syntax: lambda parameters: expression
✅ Returns result automatically
✅ Single expression only

✅ COMMON USES:
   - map() - apply function to elements
   - filter() - keep elements matching condition
   - sorted() - custom sorting key
   - reduce() - cumulative calculation

✅ BEST FOR:
   - Simple, short operations
   - One-time use functions
   - With higher-order functions

❌ AVOID FOR:
   - Complex logic
   - Multiple statements
   - Functions used in many places
   - Anything that needs comments

Lambda makes code concise but keep it readable!
"""
