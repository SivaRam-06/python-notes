# VARIABLE LENGTH ARGUMENTS - *args and **kwargs

# =============================================================================
# 1. UNDERSTANDING THE PROBLEM
# =============================================================================

# What if you don't know how many arguments will be passed?

def add_two(a, b):
    """Only adds two numbers - limited"""
    return a + b

print(add_two(1, 2))           # Output: 3
# print(add_two(1, 2, 3))      # ERROR: too many arguments
# print(add_two(1, 2, 3, 4))   # ERROR: too many arguments


# =============================================================================
# 2. *args - NON-KEYWORD VARIABLE LENGTH ARGUMENTS
# =============================================================================

"""
*args = allows function to accept any number of positional arguments
'args' is a TUPLE containing all the arguments
The asterisk (*) is what matters, 'args' is just a convention
"""

def add_numbers(*args):
    """Add any number of arguments"""
    print(f"Type of args: {type(args)}")  # <class 'tuple'>
    print(f"Arguments: {args}")
    total = sum(args)
    return total

print(add_numbers(1, 2))              # Output: 3
print(add_numbers(1, 2, 3))           # Output: 6
print(add_numbers(1, 2, 3, 4, 5))     # Output: 15


# =============================================================================
# 3. ITERATING OVER *args
# =============================================================================

def print_all_arguments(*items):
    """Print each argument on a new line"""
    print("Items received:")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")
    print()

print_all_arguments("Python")
print_all_arguments("Python", "Java", "C++")
print_all_arguments("A", "B", "C", "D", "E")


# =============================================================================
# 4. **kwargs - KEYWORD VARIABLE LENGTH ARGUMENTS
# =============================================================================

"""
**kwargs = allows function to accept any number of keyword arguments
'kwargs' is a DICTIONARY containing all the keyword arguments
The double asterisk (**) is what matters, 'kwargs' is just a convention
"""

def print_user_info(**kwargs):
    """Print user information from keyword arguments"""
    print(f"Type of kwargs: {type(kwargs)}")  # <class 'dict'>
    print(f"Data: {kwargs}")
    
    for key, value in kwargs.items():
        print(f"  {key}: {value}")
    print()

print_user_info(name="Alice", age=25)
print_user_info(name="Bob", age=30, city="New York", job="Engineer")
print_user_info(color="red", size="large", price=99.99)


# =============================================================================
# 5. COMBINING *args AND **kwargs
# =============================================================================

"""
Order matters: regular params > *args > **kwargs
def function(regular, *args, **kwargs)
"""

def create_profile(name, age, *hobbies, **details):
    """
    Create profile with required params, optional args, and optional kwargs
    """
    print(f"Name: {name}")
    print(f"Age: {age}")
    
    print(f"Hobbies: {hobbies}")
    if hobbies:
        for hobby in hobbies:
            print(f"  - {hobby}")
    
    print(f"Other Details:")
    for key, value in details.items():
        print(f"  {key}: {value}")
    print()

create_profile("Alice", 25)
create_profile("Bob", 30, "Reading", "Gaming", city="New York", job="Engineer")
create_profile("Charlie", 20, "Coding", "Music", "Sports", country="Canada", education="Bachelor")


# =============================================================================
# 6. PRACTICAL EXAMPLE - FUNCTION WITH FLEXIBLE PARAMETERS
# =============================================================================

def greet_people(*names, **settings):
    """Greet multiple people with custom settings"""
    greeting = settings.get("greeting", "Hello")
    punctuation = settings.get("punctuation", "!")
    
    for name in names:
        print(f"{greeting}, {name}{punctuation}")
    print()

greet_people("Alice", "Bob", "Charlie")
greet_people("Diana", "Eve", greeting="Hi", punctuation=".")
greet_people("Frank", "Grace", "Henry", greeting="Hey", punctuation=" 👋")


# =============================================================================
# 7. *args WITH DEFAULT PARAMETERS
# =============================================================================

def format_message(prefix="Message", *items, suffix="---"):
    """
    Format message with prefix, items, and suffix
    Note: When using *args, keyword args after it must use keyword syntax
    """
    print(f"{prefix}")
    for item in items:
        print(f"  • {item}")
    print(suffix)
    print()

format_message()
format_message("Tasks", "Buy milk", "Do homework", "Call mom")
format_message("Report", "Step 1", "Step 2", "Step 3", suffix="END REPORT")


# =============================================================================
# 8. UNPACKING ARGUMENTS WITH * AND **
# =============================================================================

# Unpacking lists/tuples with *
def multiply(a, b, c):
    return a * b * c

numbers = [2, 3, 4]
result = multiply(*numbers)  # Unpacks to multiply(2, 3, 4)
print(f"Multiply: {result}")  # Output: 24

# Unpacking dictionaries with **
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

person_info = {"name": "Alice", "age": 25, "city": "New York"}
describe_person(**person_info)  # Unpacks to function(name="Alice", age=25, city="New York")


# =============================================================================
# 9. COLLECTING EXCESS ARGUMENTS
# =============================================================================

def process(first, second, *rest):
    """Process first two args separately, collect the rest"""
    print(f"First: {first}")
    print(f"Second: {second}")
    print(f"Rest: {rest}")
    print(f"Number of remaining items: {len(rest)}")
    print()

process(1, 2)
process(1, 2, 3)
process(1, 2, 3, 4, 5, 6)


# =============================================================================
# 10. PRACTICAL EXAMPLE - DATA LOGGER
# =============================================================================

def log_event(event_type, *data, **metadata):
    """Log an event with data and metadata"""
    print(f"[{event_type.upper()}]")
    
    if data:
        print("Data:")
        for item in data:
            print(f"  - {item}")
    
    if metadata:
        print("Metadata:")
        for key, value in metadata.items():
            print(f"  {key}: {value}")
    print()

log_event("ERROR", "Database connection failed", "Timeout after 30s")
log_event("INFO", "User logged in", "Session started", 
          user_id=123, username="alice", timestamp="2024-02-18 10:30")


# =============================================================================
# 11. WHEN TO USE *args vs **kwargs
# =============================================================================

# Use *args when:
# - You want to accept varying number of positional arguments
# - The order matters
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))  # Order matters, all same type


# Use **kwargs when:
# - You want to accept keyword arguments
# - The order doesn't matter
# - You want named access to the arguments
def build_url(base, **params):
    """Build URL with query parameters"""
    query = "&".join([f"{k}={v}" for k, v in params.items()])
    return f"{base}?{query}"

url = build_url("http://api.example.com", page=1, limit=10, sort="date")
print(url)  # Order doesn't matter for URL params


# =============================================================================
# 12. COMMON PATTERNS WITH *args AND **kwargs
# =============================================================================

# Pattern 1: Forward arguments to another function
def wrapper_function(*args, **kwargs):
    """Wrapper that passes everything to real function"""
    print("Before function call")
    # Call another function with same arguments
    # real_function(*args, **kwargs)
    print("After function call")

wrapper_function(1, 2, 3, name="test")


# Pattern 2: Function factory
def create_logger(name, *categories, **options):
    """Create a logger with various configurations"""
    logger_config = {
        "name": name,
        "categories": categories,
        "level": options.get("level", "INFO"),
        "format": options.get("format", "simple")
    }
    return logger_config

logger = create_logger("MyLogger", "DEBUG", "INFO", 
                      level="DEBUG", format="detailed")
print(logger)


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================

# ❌ MISTAKE 1: Wrong order of parameters
# def wrong(a, *args, b=5, **kwargs):  # This actually works
#     pass
# But: def wrong(*args, b, **kwargs):  # This requires 'b' to be passed as keyword

# ✅ Correct order: regular > *args > **kwargs


# ❌ MISTAKE 2: Using tuple syntax incorrectly
numbers = [1, 2, 3]
# add(*numbers)          # ✅ Correct - unpacks
# add(numbers)           # ❌ Wrong - passes whole list as one arg
# add(*numbers, *more)   # ✅ Can unpack multiple times


# ❌ MISTAKE 3: Forgetting to iterate over *args
def process_items(*items):
    print(items)    # Prints tuple: (1, 2, 3)
    # Not individual items!
    
    # ✅ Correct way
    for item in items:
        print(item)  # Prints each item


# =============================================================================
# KEY POINTS SUMMARY
# =============================================================================

"""
✅ *args - tuple of positional arguments
✅ **kwargs - dictionary of keyword arguments
✅ Order: regular params > *args > **kwargs

✅ *args used to:
   - Accept variable number of positional arguments
   - Unpack lists/tuples when calling functions

✅ **kwargs used to:
   - Accept variable number of keyword arguments
   - Unpack dictionaries when calling functions

✅ Can use both together for maximum flexibility
✅ The names 'args' and 'kwargs' are just conventions

Common patterns:
- Wrapper functions that forward arguments
- Flexible APIs that accept various inputs
- Function factories with custom configuration

*args and **kwargs make functions very flexible!
"""
