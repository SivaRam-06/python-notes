"""
================================================================================
                    ATTRIBUTES AND METHODS - BASIC 2
================================================================================

CONCEPTS:
  ATTRIBUTES (Variables) - Store data about an object
  METHODS (Functions)    - Define behaviors/actions of an object

ANALOGY:
  Attributes = Properties (e.g., color, size of a car)
  Methods    = Actions (e.g., start, stop, accelerate)

================================================================================
                        WHEN TO USE?
================================================================================
Use attributes to:
  - Store information about the object
  - Keep track of object's state/status

Use methods to:
  - Perform actions on data
  - Change object's state
  - Return information about object

================================================================================
                        HOW TO USE?
================================================================================
SYNTAX:

class MyClass:
    def __init__(self, attribute):
        self.attribute = attribute      # Attribute
    
    def method_name(self, parameters):
        # Do something
        return result                    # Method

obj = MyClass(value)
value = obj.attribute                   # Access attribute
obj.method_name(parameters)             # Call method
================================================================================
"""

# ================================================================================
# SECTION 1: UNDERSTANDING ATTRIBUTES
# ================================================================================

print("=" * 80)
print("SECTION 1: ATTRIBUTES (VARIABLES IN A CLASS)")
print("=" * 80)

class Hero:
    """
    Hero class with different types of attributes
    """
    
    def __init__(self, name, health, power):
        # Instance Attributes - belong to specific object
        self.name = name
        self.health = health
        self.power = power


# Create hero objects
hero1 = Hero("Thor", 100, 85)
hero2 = Hero("Iron Man", 80, 90)

print(f"Hero 1: Name={hero1.name}, Health={hero1.health}, Power={hero1.power}")
print(f"Hero 2: Name={hero2.name}, Health={hero2.health}, Power={hero2.power}")

# Modify attributes
hero1.health = 95
print(f"\nAfter modification - Hero 1 Health: {hero1.health}")

print("""
KEY POINTS:
- Each attribute belongs to a specific object
- hero1.name is different from hero2.name
- Can modify attributes anytime
- Each object has its own copy of attributes
""")


# ================================================================================
# SECTION 2: TYPES OF ATTRIBUTES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 2: TYPES OF ATTRIBUTES")
print("=" * 80)

# TYPE 1: INSTANCE ATTRIBUTES (Unique to each object)
print("\n--- TYPE 1: INSTANCE ATTRIBUTES ---")

class Book:
    """Instance attributes - unique to each book"""
    
    def __init__(self, title, author, pages):
        self.title = title      # Instance attribute
        self.author = author    # Instance attribute
        self.pages = pages      # Instance attribute


book1 = Book("Python Basics", "John Doe", 300)
book2 = Book("Data Science", "Jane Smith", 450)

print(f"Book 1: {book1.title} by {book1.author}")
print(f"Book 2: {book2.title} by {book2.author}")
print("Each book has its own title, author, pages")


# TYPE 2: CLASS ATTRIBUTES (Shared by all objects)
print("\n--- TYPE 2: CLASS ATTRIBUTES ---")

class Animal:
    """Class attributes - shared by all animals"""
    
    species_count = 0  # Class attribute - shared by ALL objects!
    
    def __init__(self, name, age):
        self.name = name        # Instance attribute
        self.age = age          # Instance attribute
        Animal.species_count += 1


dog = Animal("Buddy", 5)
cat = Animal("Whiskers", 3)
bird = Animal("Tweety", 1)

print(f"Dog: {dog.name}, Age: {dog.age}")
print(f"Cat: {cat.name}, Age: {cat.age}")
print(f"Bird: {bird.name}, Age: {bird.age}")
print(f"Total animals created: {Animal.species_count}")

print("""
Key Difference:
- Instance attributes: Each object has its own copy
- Class attributes: ALL objects share the same copy
""")


# ================================================================================
# SECTION 3: UNDERSTANDING METHODS
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 3: METHODS (FUNCTIONS IN A CLASS)")
print("=" * 80)

class Calculator:
    """
    Calculator class with methods
    Methods perform operations
    """
    
    def __init__(self, name):
        self.name = name
    
    # METHOD 1: No parameters, no return value
    def introduction(self):
        """Just print something"""
        print(f"I am {self.name} Calculator")
    
    # METHOD 2: Takes parameters, no return value
    def add(self, a, b):
        """Perform addition and print result"""
        result = a + b
        print(f"{a} + {b} = {result}")
    
    # METHOD 3: Takes parameters, returns value
    def multiply(self, a, b):
        """Perform multiplication and return result"""
        return a * b
    
    # METHOD 4: Uses instance attributes
    def get_info(self):
        """Uses self.attribute inside method"""
        return f"This is {self.name}"


calc = Calculator("MyCalc")

# Calling methods
calc.introduction()
calc.add(5, 3)
result = calc.multiply(4, 6)
print(f"4 * 6 = {result}")
print(calc.get_info())

print("""
Method Types:
1. No parameters, no return  - Just perform action
2. Parameters, no return     - Take data, perform action
3. Parameters, return value  - Take data, return result
4. No parameters, return     - Return computed value
""")


# ================================================================================
# SECTION 4: INSTANCE METHODS IN DETAIL
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 4: INSTANCE METHODS WITH 'self'")
print("=" * 80)

class BankAccount:
    """
    Bank Account with methods that modify state
    """
    
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
    
    def deposit(self, amount):
        """Add money to account"""
        if amount > 0:
            self.balance += amount
            print(f"{self.holder} deposited: {amount}")
        else:
            print("Amount must be positive")
    
    def withdraw(self, amount):
        """Remove money from account"""
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print(f"{self.holder} withdrew: {amount}")
        else:
            print("Insufficient balance or invalid amount")
    
    def get_balance(self):
        """Return current balance"""
        return self.balance
    
    def display_statement(self):
        """Display account statement"""
        print(f"\n--- Account Statement ---")
        print(f"Holder: {self.holder}")
        print(f"Balance: {self.balance}")
        print("---" * 10)


# Use the account
account = BankAccount("Ahmed", 50000)
account.display_statement()

account.deposit(10000)
account.withdraw(5000)
account.display_statement()

print(f"Current balance: {account.get_balance()}")


# ================================================================================
# SECTION 5: METHODS THAT USE MULTIPLE ATTRIBUTES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 5: USING MULTIPLE ATTRIBUTES IN METHODS")
print("=" * 80)

class Rectangle:
    """
    Rectangle with methods using multiple attributes
    """
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate area using both attributes"""
        return self.length * self.width
    
    def perimeter(self):
        """Calculate perimeter using both attributes"""
        return 2 * (self.length + self.width)
    
    def is_square(self):
        """Check if length equals width"""
        return self.length == self.width
    
    def resize(self, new_length, new_width):
        """Modify both attributes"""
        self.length = new_length
        self.width = new_width
        print(f"Resized to {self.length} x {self.width}")
    
    def display(self):
        """Display rectangle info"""
        print(f"\nLength: {self.length}, Width: {self.width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")
        print(f"Is Square: {self.is_square()}")


rect1 = Rectangle(5, 3)
rect1.display()

rect2 = Rectangle(4, 4)
rect2.display()

rect1.resize(6, 4)
rect1.display()


# ================================================================================
# SECTION 6: REAL-WORLD EXAMPLE - STUDENT MANAGEMENT
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 6: REAL-WORLD EXAMPLE - STUDENT")
print("=" * 80)

class Student:
    """
    Student class with attributes and methods
    """
    
    total_students = 0  # Class attribute
    
    def __init__(self, roll_no, name, marks1, marks2, marks3):
        # Instance attributes
        self.roll_no = roll_no
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        
        # Increment total students
        Student.total_students += 1
    
    def get_total_marks(self):
        """Calculate total marks"""
        return self.marks1 + self.marks2 + self.marks3
    
    def get_average(self):
        """Calculate average marks"""
        return self.get_total_marks() / 3
    
    def get_grade(self):
        """Get grade based on average"""
        avg = self.get_average()
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "F"
    
    def is_passed(self):
        """Check if passed (average >= 40)"""
        return self.get_average() >= 40
    
    def display_result(self):
        """Display complete result"""
        print(f"\n--- Student Result ---")
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks1}, {self.marks2}, {self.marks3}")
        print(f"Total: {self.get_total_marks()}")
        print(f"Average: {self.get_average():.2f}")
        print(f"Grade: {self.get_grade()}")
        print(f"Status: {'Passed' if self.is_passed() else 'Failed'}")


# Create students
s1 = Student(1, "Ali", 85, 90, 88)
s2 = Student(2, "Fatima", 92, 88, 95)
s3 = Student(3, "Hassan", 45, 50, 48)

# Display results
s1.display_result()
s2.display_result()
s3.display_result()

print(f"\n\nTotal Students: {Student.total_students}")


# ================================================================================
# SECTION 7: BEST PRACTICES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 7: BEST PRACTICES FOR ATTRIBUTES AND METHODS")
print("=" * 80)

print("""
BEST PRACTICES:

1. ATTRIBUTES:
   ✓ Use descriptive names (not x, y, z)
   ✓ Initialize all attributes in __init__
   ✓ Use instance attributes for object-specific data
   ✓ Use class attributes for shared data

2. METHODS:
   ✓ Use descriptive names that explain action (get_age, calculate_total)
   ✓ Keep methods focused - one responsibility
   ✓ Use parameters instead of hardcoding values
   ✓ Return values when appropriate
   ✓ Use self to access attributes and other methods

3. ORGANIZATION:
   ✓ Group related attributes and methods
   ✓ New features = New class or extend existing
   ✓ Use descriptive docstrings for clarity

4. NAMING CONVENTIONS:
   ✓ Classes: PascalCase (Student, BankAccount, Rectangle)
   ✓ Attributes: snake_case (first_name, account_balance)
   ✓ Methods: snake_case with verbs (get_balance, calculate_area)
""")
