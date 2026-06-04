# TYPES OF FUNCTIONS - Different Function Categories

# =============================================================================
# 1. BUILT-IN FUNCTIONS (Provided by Python)
# =============================================================================

"""
Built-in functions are provided by Python itself.
You don't need to define them, just use them.
"""

# Common built-in functions
print("Hello")                    # Print to console
length = len([1, 2, 3])          # Get length
maximum = max([1, 5, 3])         # Find maximum
total = sum([1, 2, 3, 4])        # Sum values
rounded = round(3.14159, 2)      # Round number
converted = str(42)              # Convert to string

print(f"Type of print: {type(print)}")  # <class 'builtin_function_or_method'>


# =============================================================================
# 2. USER-DEFINED FUNCTIONS (Functions You Create)
# =============================================================================

"""
Functions you write yourself for specific tasks.
"""

def greet(name):
    """Simple user-defined function"""
    return f"Hello, {name}!"

def calculate_total(items):
    """Calculate total cost"""
    return sum(items)

print(greet("Alice"))              # Output: Hello, Alice!
print(calculate_total([10, 20, 30]))  # Output: 60


# =============================================================================
# 3. LAMBDA FUNCTIONS (Anonymous Functions)
# =============================================================================

"""
Small, unnamed functions defined with lambda keyword.
Used for simple, one-time operations.
"""

square = lambda x: x ** 2
add = lambda x, y: x + y
greet_lambda = lambda name: f"Hi, {name}!"

print(square(5))                  # Output: 25
print(add(3, 4))                  # Output: 7
print(greet_lambda("Bob"))        # Output: Hi, Bob!

# Lambda with built-ins
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)                    # Output: [2, 4, 6, 8, 10]


# =============================================================================
# 4. RECURSIVE FUNCTIONS (Functions Calling Themselves)
# =============================================================================

"""
A function that calls itself to solve a problem.
Must have a base case to stop.
"""

def factorial(n):
    """Calculate factorial with recursion"""
    if n <= 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

def fibonacci(n):
    """Get nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"5! = {factorial(5)}")      # Output: 120
print(f"F(6) = {fibonacci(6)}")    # Output: 8


# =============================================================================
# 5. NESTED FUNCTIONS (Functions Inside Functions)
# =============================================================================

"""
Functions defined inside other functions.
Inner function can access outer function's variables.
"""

def outer_function(x):
    """Outer function"""
    print(f"Outer: x = {x}")
    
    def inner_function(y):
        """Inner function (nested)"""
        print(f"Inner: y = {y}")
        print(f"Inner can access outer's x: {x}")
        return x + y
    
    result = inner_function(10)
    return result

print(outer_function(5))
# Output:
# Outer: x = 5
# Inner: y = 10
# Inner can access outer's x: 5
# 15


# =============================================================================
# 6. HIGHER-ORDER FUNCTIONS
# =============================================================================

"""
Functions that:
- Take other functions as arguments, OR
- Return functions as results

These are powerful for functional programming.
"""

# Function that takes another function as argument
def apply_operation(func, x, y):
    """Higher-order function taking a function as argument"""
    return func(x, y)

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

print(apply_operation(add_numbers, 5, 3))      # Output: 8
print(apply_operation(multiply_numbers, 5, 3)) # Output: 15

# Function that returns another function
def make_multiplier(factor):
    """Higher-order function returning a function"""
    def multiplier(x):
        return x * factor
    return multiplier

times_3 = make_multiplier(3)
times_5 = make_multiplier(5)

print(times_3(10))  # Output: 30
print(times_5(10))  # Output: 50


# =============================================================================
# 7. GENERATOR FUNCTIONS (Functions with yield)
# =============================================================================

"""
Functions using 'yield' instead of 'return'.
They generate values one at a time, saving memory.
"""

def count_up_to(n):
    """Generator function"""
    i = 0
    while i < n:
        yield i  # Pause here and return value
        i += 1

# Using generator
print("Generator output:")
for num in count_up_to(5):
    print(num)  # Prints: 0, 1, 2, 3, 4

# Generator for Fibonacci
def fibonacci_generator(limit):
    """Generate Fibonacci numbers up to limit"""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print("nFibonacci sequence:")
for fib in fibonacci_generator(100):
    print(fib, end=" ")
print()

# Generator is more memory efficient than storing all values
def large_range(n):
    """Generate large range without storing all in memory"""
    for i in range(n):
        yield i

total = sum(large_range(1000000))  # Efficient!


# =============================================================================
# 8. DECORATOR FUNCTIONS (Advanced)
# =============================================================================

"""
Functions that modify other functions or classes.
Add functionality without changing the original function.
"""

def my_decorator(func):
    """Decorator that wraps a function"""
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """Function with decorator"""
    print(f"Hello, {name}!")
    return f"Greeted {name}"

print(say_hello("Alice"))
# Output:
# Before function call
# Hello, Alice!
# After function call
# Greeted Alice


# =============================================================================
# 9. CALLBACK FUNCTIONS
# =============================================================================

"""
Functions passed to other functions to be called later.
Common in event handling and asynchronous programming.
"""

def process_data(data, callback):
    """Function that calls a callback function"""
    processed = data * 2
    return callback(processed)

def print_result(result):
    """Callback function"""
    print(f"Result is: {result}")
    return result

process_data(5, print_result)  # Output: Result is: 10


# =============================================================================
# 10. PURE FUNCTIONS VS IMPURE FUNCTIONS
# =============================================================================

"""
PURE FUNCTION:
- Same input always produces same output
- No side effects
- Doesn't modify external state

IMPURE FUNCTION:
- Can produce different outputs with same input
- Has side effects
- Modifies external state
"""

# ❌ IMPURE FUNCTION
external_value = 10

def impure_function(x):
    """Impure: depends on and modifies external state"""
    global external_value
    external_value += 1
    return x + external_value

print(impure_function(5))  # Output: 16
print(impure_function(5))  # Output: 17 (different with same input!)

# ✅ PURE FUNCTION
def pure_function(x, y):
    """Pure: same input always same output"""
    return x + y

print(pure_function(5, 10))  # Output: 15
print(pure_function(5, 10))  # Output: 15 (always same)


# =============================================================================
# 11. VARIADIC FUNCTIONS (*args and **kwargs)
# =============================================================================

"""
Functions that accept variable number of arguments.
"""

def sum_all(*args):
    """Variadic function using *args"""
    return sum(args)

def print_config(**kwargs):
    """Variadic function using **kwargs"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(sum_all(1, 2, 3, 4, 5))      # Output: 15
print_config(host="localhost", port=8000, debug=True)
# Output:
# host: localhost
# port: 8000
# debug: True


# =============================================================================
# 12. CLOSURE FUNCTIONS
# =============================================================================

"""
Functions that 'remember' variables from outer scope.
Inner function has access to outer function's variables.
"""

def make_adder(x):
    """Closure: inner function remembers x"""
    def adder(y):
        return x + y  # Remembers x from outer scope
    return adder

add_5 = make_adder(5)
add_10 = make_adder(10)

print(add_5(3))   # Output: 8 (remembers x=5)
print(add_10(3))  # Output: 13 (remembers x=10)


# =============================================================================
# COMPARISON TABLE
# =============================================================================

"""
Type of Function | When to Use | Example
===============================================================================
Built-in         | Common tasks | len(), print(), sum()
User-defined     | Custom logic | calculate_total(), validate_email()
Lambda           | Simple, one-time | map(lambda x: x*2, list)
Recursive        | Hierarchical problems | factorial(), tree traversal
Nested           | Helper functions | Inner function doing specific task
Higher-order     | Function manipulation | map(), filter(), decorators
Generator        | Memory efficiency | Yielding large sequences
Decorator        | Add functionality | @decorator
Callback         | Asynchronous tasks | setTimeout(callback)
Pure             | Predictable code | Mathematical functions
Impure           | State changes | Database updates, file I/O
Variadic         | Flexible arguments | sum(*args), config(**kwargs)
Closure          | Remember context | Function factories
"""


# =============================================================================
# PRACTICAL EXAMPLES - COMBINING FUNCTION TYPES
# =============================================================================

print("n--- PRACTICAL EXAMPLES ---n")

# Example 1: Higher-order function with lambda
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort using higher-order function with lambda
sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)
print("Sorted by grade:")
for student in sorted_students:
    print(f"  {student['name']}: {student['grade']}")

# Example 2: Function that returns nested function (closure)
def make_validator(min_value, max_value):
    """Returns a validation function (closure)"""
    def validator(value):
        if min_value <= value <= max_value:
            return True
        return False
    return validator

age_validator = make_validator(0, 150)
salary_validator = make_validator(0, 1000000)

print(f"nAge 25 valid: {age_validator(25)}")        # True
print(f"Age 200 valid: {age_validator(200)}")        # False
print(f"Salary 50000 valid: {salary_validator(50000)}")  # True

# Example 3: Generator for data processing
def process_large_file():
    """Generator that yields processed lines"""
    for i in range(1000000):  # Imagine reading from file
        if i % 2 == 0:  # Only yield even numbers
            yield i

# Use generator without loading all in memory
first_10_even = []
for num in process_large_file():
    if len(first_10_even) < 10:
        first_10_even.append(num)
    else:
        break

print(f"nFirst 10 even numbers: {first_10_even}")


# =============================================================================
# CHOOSING THE RIGHT FUNCTION TYPE
# =============================================================================

"""
Question: What type of function should I use?

1. Is it a simple, one-time operation?
   → Use LAMBDA

2. Does it need helper functions?
   → Use NESTED FUNCTIONS

3. Does it call itself with simpler inputs?
   → Use RECURSIVE FUNCTIONS

4. Does it take other functions as input?
   → Use HIGHER-ORDER FUNCTIONS

5. Do you need to process large amounts of data?
   → Use GENERATOR FUNCTIONS

6. Do you want to modify another function?
   → Use DECORATORS

7. Is it a standard operation?
   → Use BUILT-IN FUNCTIONS

8. Is it domain-specific logic?
   → Use USER-DEFINED FUNCTIONS

9. Do you need different implementations of same logic?
   → Use CALLBACKS or HIGHER-ORDER FUNCTIONS

10. Does it need to remember state?
    → Use CLOSURES
"""


# =============================================================================
# KEY POINTS SUMMARY
# =============================================================================

"""
✅ FUNCTION TYPES:

Built-in Functions:
   - Provided by Python
   - Ready to use: print(), len(), sum()

User-Defined Functions:
   - You write them
   - Specific to your needs

Lambda Functions:
   - Anonymous, one-line functions
   - For simple operations

Recursive Functions:
   - Call themselves
   - Must have base case

Nested Functions:
   - Functions inside functions
   - Inner accesses outer's scope

Higher-Order Functions:
   - Take functions as arguments
   - Return functions as results

Generator Functions:
   - Use 'yield' instead of 'return'
   - Memory efficient

Decorators:
   - Modify other functions
   - Add functionality

Closures:
   - Inner functions remember outer variables
   - Create function factories

Each type has specific uses. Pick the right one for your problem!
"""
