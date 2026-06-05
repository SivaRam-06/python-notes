"""
================================================================================
            CONSTRUCTORS AND DESTRUCTORS - BASIC 3
================================================================================

CONCEPTS:
  CONSTRUCTOR (__init__)   - Special method that runs when object is CREATED
  DESTRUCTOR (__del__)     - Special method that runs when object is DELETED

WHY?
  Constructor: Initialize object with initial values
  Destructor: Clean up resources (rarely used in Python)

================================================================================
                        WHEN TO USE?
================================================================================
USE CONSTRUCTORS WHEN:
  - Need to initialize attributes
  - Need to set up initial state
  - Need to validate input at creation time
  - Need to perform setup operations

USE DESTRUCTORS WHEN:
  - Need to close files or connections
  - Need to release resources
  - Need to perform cleanup operations
  (Rarely needed in Python - garbage collection handles this)

================================================================================
                        HOW TO USE?
================================================================================
SYNTAX:

class MyClass:
    def __init__(self, parameters):
        # Initialize attributes here
        self.attribute = parameter
    
    def __del__(self):
        # Cleanup code here
        print("Object deleted")

obj = MyClass(value)   # __init__ is called automatically
del obj                # __del__ is called automatically (or by garbage collection)

================================================================================
"""

# ================================================================================
# SECTION 1: BASIC CONSTRUCTOR (__init__)
# ================================================================================

print("=" * 80)
print("SECTION 1: BASIC CONSTRUCTOR")
print("=" * 80)

class Dog:
    """
    Simple Dog class with constructor
    __init__ runs automatically when object is created
    """
    
    def __init__(self, name, age=0):
        # Initialize attributes
        self.name = name
        self.age = age
        print(f"Dog '{self.name}' created!")


# When object is created, __init__ is automatically called
dog1 = Dog("Buddy", 5)
dog2 = Dog("Max")
dog3 = Dog("Charlie", 3)

print("""
KEY POINT:
__init__ is AUTOMATICALLY called as soon as object is created
You DON'T call it manually: dog = Dog("Buddy", 5)(__init__ is called!)
""")


# ================================================================================
# SECTION 2: CONSTRUCTOR WITH DIFFERENT SCENARIOS
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 2: CONSTRUCTOR SCENARIOS")
print("=" * 80)

# SCENARIO 1: Required parameters
print("\n--- SCENARIO 1: Required Parameters ---")

class Person:
    """All parameters are required"""
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def display(self):
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}")


person1 = Person("John", "Doe", 25)
person1.display()

# SCENARIO 2: Optional parameters with default values
print("\n--- SCENARIO 2: Optional Parameters with Defaults ---")

class Car:
    """Color has a default value"""
    
    def __init__(self, brand, model, year=2024, color="Black"):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
    
    def display(self):
        print(f"{self.year} {self.brand} {self.model} - {self.color}")


car1 = Car("Toyota", "Camry")  # Uses default year and color
car2 = Car("Honda", "Civic", 2023, "Red")  # All specified


car1.display()
car2.display()

# SCENARIO 3: Parameters with validation
print("\n--- SCENARIO 3: Constructor with Validation ---")

class Student:
    """Validate input during initialization"""
    
    def __init__(self, roll_no, name, age, marks):
        # Validate roll number
        if roll_no <= 0:
            print("ERROR: Roll number must be positive!")
            return
        
        # Validate age
        if age < 5 or age > 100:
            print("ERROR: Invalid age!")
            return
        
        # Validate marks
        if marks < 0 or marks > 100:
            print("ERROR: Marks must be between 0-100!")
            return
        
        # If all validations pass
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.marks = marks
        print("Student created successfully!")


s1 = Student(1, "Ali", 18, 85)
s2 = Student(-5, "Fatima", 19, 90)  # Invalid roll number
s3 = Student(3, "Hassan", 150, 95)  # Invalid age


# SCENARIO 4: Constructor with multiple related attributes
print("\n--- SCENARIO 4: Initialization with Calculations ---")

class Rectangle:
    """Initialize related attributes together"""
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width  # Calculate once at init
        self.perimeter = 2 * (length + width)
    
    def display(self):
        print(f"Length: {self.length}, Width: {self.width}")
        print(f"Area: {self.area}, Perimeter: {self.perimeter}")


rect = Rectangle(5, 3)
rect.display()


# ================================================================================
# SECTION 3: CONSTRUCTOR WITH DATABASE/FILE INITIALIZATION
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 3: CONSTRUCTOR FOR SETUP/INITIALIZATION")
print("=" * 80)

class BankAccount:
    """
    Constructor sets up account
    Useful for initializing complex state
    """
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []  # Empty list for transactions
        self.created_date = "2024-01-15"
        
        # Record initial deposit as transaction
        if initial_balance > 0:
            self.transactions.append(f"Initial deposit: {initial_balance}")
        
        print(f"Account created for {self.account_holder}")
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount}")
    
    def display_details(self):
        print(f"\nAccount: {self.account_holder}")
        print(f"Created: {self.created_date}")
        print(f"Balance: {self.balance}")
        print("Transactions:")
        for trans in self.transactions:
            print(f"  - {trans}")


account = BankAccount("Ahmed", 5000)
account.deposit(2000)
account.deposit(1000)
account.display_details()


# ================================================================================
# SECTION 4: PARENT CLASS CONSTRUCTOR (INHERITANCE)
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 4: CONSTRUCTOR IN INHERITANCE")
print("=" * 80)

class Vehicle:
    """Parent class constructor"""
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        print(f"Vehicle '{self.name}' initialized")


class Bike(Vehicle):
    """Child class with its own constructor"""
    
    def __init__(self, name, speed, bike_type):
        # Call parent constructor
        super().__init__(name, speed)
        self.bike_type = bike_type
        print(f"Bike type: {self.bike_type}")


bike = Bike("Royal Enfield", 200, "Cruiser")
print(f"Bike: {bike.name}, Speed: {bike.speed}, Type: {bike.bike_type}")

print("""
KEY POINT:
When child class has __init__, call parent's __init__ using super()
This ensures parent initialization happens first
""")


# ================================================================================
# SECTION 5: DESTRUCTOR (__del__)
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 5: DESTRUCTOR (__del__)")
print("=" * 80)

class File:
    """
    Example of destructor - cleanup when object is destroyed
    """
    
    def __init__(self, filename):
        self.filename = filename
        print(f"Opening file: {self.filename}")
    
    def __del__(self):
        print(f"Closing file: {self.filename} [Destructor called]")


print("Creating file object...")
file1 = File("data.txt")

print("File object still exists...")

print("Deleting file object...")
del file1

print("File object deleted!")

print("""
KEY POINT:
__del__ is called when:
1. You use 'del' object
2. Object goes out of scope
3. Program ends
4. Garbage collector runs

In Python, __del__ is RARELY needed because Python has garbage collection
""")


# ================================================================================
# SECTION 6: COMMON PATTERNS - COUNTER
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 6: COMMON PATTERNS - OBJECT COUNTER")
print("=" * 80)

class Counter:
    """
    Count total objects created
    Constructor increments, Destructor decrements
    """
    
    total_objects = 0
    
    def __init__(self, name):
        self.name = name
        Counter.total_objects += 1
        print(f"Counter '{self.name}' created. Total: {Counter.total_objects}")
    
    def __del__(self):
        Counter.total_objects -= 1
        print(f"Counter '{self.name}' deleted. Total: {Counter.total_objects}")


print("Creating counters...")
c1 = Counter("Count1")
c2 = Counter("Count2")
c3 = Counter("Count3")

print(f"\nTotal before deletion: {Counter.total_objects}")

print("\nDeleting counters...")
del c1
print(f"Total after deleting c1: {Counter.total_objects}")

del c2
print(f"Total after deleting c2: {Counter.total_objects}")


# ================================================================================
# SECTION 7: REAL WORLD EXAMPLE - DATABASE CONNECTION
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 7: REAL WORLD - DATABASE CONNECTION")
print("=" * 80)

class DatabaseConnection:
    """
    Simulates database connection
    Constructor connects, Destructor disconnects
    """
    
    def __init__(self, db_name, username):
        self.db_name = db_name
        self.username = username
        print(f"\n[DATABASE] Connecting to '{db_name}' as '{username}'...")
        self.is_connected = True
    
    def query(self, sql):
        if self.is_connected:
            print(f"[DATABASE] Executing: {sql}")
        else:
            print("[DATABASE] ERROR: Not connected!")
    
    def __del__(self):
        print(f"[DATABASE] Disconnecting from '{self.db_name}'...")
        self.is_connected = False


print("Creating database connection...")
db = DatabaseConnection("UserDB", "admin")
db.query("SELECT * FROM users")

print("Deleting connection...")
del db

print("\n[DATABASE] Connection closed!")


# ================================================================================
# SECTION 8: BEST PRACTICES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 8: BEST PRACTICES")
print("=" * 80)

print("""
CONSTRUCTOR BEST PRACTICES:

1. INITIALIZATION:
   ✓ Initialize all attributes in __init__
   ✓ Always call super().__init__() in child classes
   ✗ Don't create attributes outside __init__

2. PARAMETERS:
   ✓ Use meaningful parameter names
   ✓ Provide default values for optional parameters
   ✓ Validate parameters in constructor

3. VALIDATION:
   ✓ Validate input data at creation time
   ✓ Raise exceptions for invalid data (covered later)
   ✓ Provide helpful error messages

4. CLEANUP:
   ✓ Use __del__ only when necessary (file/connection cleanup)
   ✓ Don't rely on __del__ - use context managers instead
   ✓ Keep destructors simple

EXAMPLE OF VALIDATION:

class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.balance = balance

# Good practice with try-except
try:
    account = BankAccount(-100)
except ValueError as e:
    print(f"Error: {e}")
""")
