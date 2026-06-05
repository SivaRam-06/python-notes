"""
================================================================================
        PROPERTIES AND DECORATORS - ADVANCED 5
================================================================================

CONCEPTS:
  PROPERTY - Control attribute access (get, set, delete)
  DECORATOR - Function modifier that changes behavior

MOTTO: "Controlled access with cleaner syntax"

WHY?
  - Encapsulation: Data hiding with validation
  - Cleaner API: obj.age vs obj.get_age()
  - Change implementation later without breaking external code

================================================================================
                        WHEN TO USE?
================================================================================

USE PROPERTIES WHEN:
  - Need validation before setting
  - Need to compute value (not just store)
  - Need read-only attributes
  - Want cleaner syntax than getters/setters

USE DECORATORS WHEN:
  - Want to modify function behavior
  - Need reusable modifications
  - Want to log, cache, or validate

================================================================================
"""

# ===============================================================================
# SECTION 1: UNDERSTANDING PROPERTIES
# ===============================================================================

print("=" * 80)
print("SECTION 1: @property - GETTER")
print("=" * 80)

# WITHOUT PROPERTY - Awkward
class Circle_Old:
    def __init__(self, radius):
        self._radius = radius
    
    def get_radius(self):
        """Awkward getter"""
        return self._radius
    
    def get_area(self):
        return 3.14 * self._radius ** 2


circle_old = Circle_Old(5)
print(f"Awkward - Radius: {circle_old.get_radius()}")
print(f"Awkward - Area: {circle_old.get_area()}")

print("\n--- NOW WITH @property ---\n")

# WITH PROPERTY - Clean!
class Circle_New:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """Property - looks like attribute, is actually method"""
        return self._radius
    
    @property
    def area(self):
        """Computed property"""
        return 3.14 * self._radius ** 2


circle_new = Circle_New(5)
print(f"Clean - Radius: {circle_new.radius}")
print(f"Clean - Area: {circle_new.area}")

print("""
@property BENEFIT:
- Access like attribute: obj.radius
- But runs custom code
- Can add validation later without changing external code
""")


# ===============================================================================
# SECTION 2: PROPERTY WITH GETTER, SETTER, DELETER
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 2: @property.setter and @property.deleter")
print("=" * 80)

class Temperature:
    """Temperature with controlled access"""
    
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter - read the value"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter - write with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Another property (read-only)"""
        return self._celsius * 9/5 + 32
    
    @property
    def kelvin(self):
        """Another property (read-only)"""
        return self._celsius + 273.15


temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")
print(f"Kelvin: {temp.kelvin}K")

# Use setter
temp.celsius = 30
print(f"\nAfter setting to 30°C:")
print(f"Fahrenheit: {temp.fahrenheit}°F")

# Try invalid value
try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")

print("""
PROPERTY COMPONENTS:
1. @property - Getter (read value)
2. @attr.setter - Setter (write with validation)
3. @attr.deleter - Deleter (delete value) - rare

FLOW:
temp.celsius = 30  →  calls celsius.setter()
x = temp.celsius   →  calls @property celsius()
""")


# ===============================================================================
# SECTION 3: REAL WORLD - BANK ACCOUNT
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 3: REAL WORLD - PROTECTED ACCESS WITH PROPERTIES")
print("=" * 80)

class BankAccount:
    """Bank account with property-based access control"""
    
    def __init__(self, holder, balance):
        self._holder = holder  # Private
        self._balance = balance  # Private with validation
    
    @property
    def holder(self):
        """Read-only property"""
        return self._holder
    
    @property
    def balance(self):
        """Read-only property"""
        return self._balance
    
    @balance.setter
    def balance(self, value):
        """Setter with validation"""
        if value < 0:
            raise ValueError("Balance cannot be negative!")
        self._balance = value
    
    def deposit(self, amount):
        """Public method for deposit"""
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        self.balance += amount
        return f"Deposited {amount}. Balance: {self._balance}"
    
    def withdraw(self, amount):
        """Public method for withdrawal"""
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        if amount > self._balance:
            raise ValueError("Insufficient balance!")
        self.balance -= amount
        return f"Withdrawn {amount}. Balance: {self._balance}"


account = BankAccount("Ahmed", 10000)
print(f"Holder: {account.holder}")
print(f"Balance: {account.balance}")

print("\nDeposit 5000:")
print(account.deposit(5000))

print("\nWithdraw 3000:")
print(account.withdraw(3000))

# Try invalid
try:
    account.withdraw(20000)
except ValueError as e:
    print(f"Error: {e}")


# ===============================================================================
# SECTION 4: LAZY PROPERTIES (COMPUTED ON DEMAND)
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 4: LAZY PROPERTIES (EXPENSIVE COMPUTATION)")
print("=" * 80)

class DataProcessor:
    """Lazy computation - compute only when needed"""
    
    def __init__(self, data):
        self.data = data
        self._result = None  # Cache
        self._processed = False
    
    @property
    def result(self):
        """Compute result only when accessed"""
        if not self._processed:
            print("Computing result (expensive operation)...")
            self._result = sum(self.data) * 2  # Expensive computation
            self._processed = True
        return self._result


processor = DataProcessor([1, 2, 3, 4, 5])

print("Created processor")
print("Accessing result first time:")
print(f"Result: {processor.result}")

print("\nAccessing result second time (cached):")
print(f"Result: {processor.result}")  # No "Computing..." - uses cache

print("""
LAZY EVALUATION:
- Computation happens only when accessed
- Result is cached for future access
- Saves resources if property might not be used
""")


# ===============================================================================
# SECTION 5: DECORATORS
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 5: CUSTOM DECORATORS")
print("=" * 80)

def simple_decorator(func):
    """Simple decorator that wraps a function"""
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper


@simple_decorator
def greet():
    print("Hello!")


greet()

print("\n--- DECORATOR WITH ARGUMENTS ---\n")

def decorator_with_args(func):
    """Decorator that passes arguments to function"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper


@decorator_with_args
def add(a, b):
    return a + b


add(5, 3)


# ===============================================================================
# SECTION 6: PRACTICAL DECORATORS
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 6: PRACTICAL DECORATORS")
print("=" * 80)

# DECORATOR 1: TIMING
import time

def timing_decorator(func):
    """Measures execution time"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


@timing_decorator
def slow_function():
    time.sleep(0.5)
    print("Function executed")


slow_function()

# DECORATOR 2: MEMOIZATION (CACHING)
print("\n--- MEMOIZATION DECORATOR ---\n")

def memoize(func):
    """Cache function results"""
    cache = {}
    
    def wrapper(n):
        if n not in cache:
            print(f"Computing {func.__name__}({n})")
            cache[n] = func(n)
        else:
            print(f"Using cached value for {func.__name__}({n})")
        return cache[n]
    
    return wrapper


@memoize
def fibonacci(n):
    """Expensive calculation"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(f"fib(5) = {fibonacci(5)}")
print(f"fib(6) = {fibonacci(6)}")  # Uses cache for lower values


# DECORATOR 3: VALIDATION
print("\n--- VALIDATION DECORATOR ---\n")

def validate_types(**type_checks):
    """Validate argument types"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Check types (simplified)
            for arg_name, expected_type in type_checks.items():
                if arg_name in kwargs:
                    if not isinstance(kwargs[arg_name], expected_type):
                        raise TypeError(f"{arg_name} must be {expected_type}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@validate_types(age=int, name=str)
def create_user(name, age):
    print(f"User {name} created, age {age}")


create_user("Ali", 25)

try:
    create_user("Fatima", "25")
except TypeError as e:
    print(f"Error: {e}")


# ===============================================================================
# SECTION 7: READ-ONLY PROPERTIES
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 7: READ-ONLY PROPERTIES (NO SETTER)")
print("=" * 80)

class Immutable:
    """Read-only properties"""
    
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        """Read-only - no setter"""
        return self._value
    
    @property
    def double(self):
        """Computed, read-only"""
        return self._value * 2


obj = Immutable(10)
print(f"Value: {obj.value}")
print(f"Double: {obj.double}")

# Try to modify - WILL FAIL
try:
    obj.value = 20
except AttributeError as e:
    print(f"Error: Cannot modify - {e}")


# ===============================================================================
# SECTION 8: BEST PRACTICES
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 8: BEST PRACTICES")
print("=" * 80)

print("""
PROPERTIES - BEST PRACTICES:

1. USE PROPERTIES WHEN:
   ✓ Need validation for setter
   ✓ Computing value from other attributes
   ✓ Want read-only attributes
   ✓ Hide implementation details

2. NAMING:
   ✓ Use actual attribute name after @property
   ✓ Use _private for storage

3. AVOID:
   ✗ Heavy computation in getter (use methods instead)
   ✗ Side effects in getter (should be read-only)
   ✗ Too many properties (can be confusing)

4. USE WITH ENCAPSULATION:
   class BankAccount:
       def __init__(self, balance):
           self._balance = balance  # Private
       
       @property
       def balance(self):           # Public interface
           return self._balance
       
       @balance.setter
       def balance(self, value):
           if value >= 0:
               self._balance = value

DECORATORS - BEST PRACTICES:

1. USE DECORATORS FOR:
   ✓ Cross-cutting concerns (logging, timing)
   ✓ Validation
   ✓ Caching/memoization
   ✓ Authorization/authentication

2. KEEP DECORATORS:
   ✓ Simple and focused
   ✓ Well-documented
   ✓ Reusable across functions

3. AVOID:
   ✗ Overly complex decorators
   ✗ Decorators that change behavior drastically
   ✗ Stacking too many decorators

COMMON PATTERN - PROPERTY WITH VALIDATION:

class User:
    def __init__(self, email):
        self._email = None
        self.email = email  # Use setter for validation!
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError("Invalid email!")
        self._email = value
""")
