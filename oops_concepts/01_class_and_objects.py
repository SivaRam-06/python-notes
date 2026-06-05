"""
================================================================================
                        CLASSES AND OBJECTS - BASIC 1
================================================================================

CONCEPT OVERVIEW:
  A CLASS is a blueprint/template for creating objects
  An OBJECT is an instance of a class (real thing created from the blueprint)

ANALOGY:
  Class = Cookie Cutter (template/design)
  Object = Individual Cookies (actual things made from the cutter)

================================================================================
                            WHEN TO USE?
================================================================================
Use classes when you need to:
1. Model real-world things (Person, Car, Bank Account)
2. Group related data and functions together
3. Create multiple similar objects with different values
4. Organize code into logical units

================================================================================
                            HOW TO USE?
================================================================================
SYNTAX:

class ClassName:
    # Class body goes here
    pass

object = ClassName()  # Creating an object from a class

================================================================================
"""

# ================================================================================
# SECTION 1: BASIC CLASS AND OBJECT CREATION
# ================================================================================

print("=" * 80)
print("SECTION 1: BASIC CLASS CREATION AND OBJECTS")
print("=" * 80)

# Define a simple class
class Car:
    """This is a simple Car class"""
    pass


# Create objects from the Car class
car1 = Car()
car2 = Car()
car3 = Car()

print(f"car1: {car1}")
print(f"car2: {car2}")
print(f"car3: {car3}")
print("\nNote: Each object is DIFFERENT (different memory address) even if created from same class")


# ================================================================================
# SECTION 2: CLASS WITH ATTRIBUTES (Variables)
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 2: ADDING ATTRIBUTES (DATA) TO CLASS")
print("=" * 80)

class Laptop:
    """
    Laptop class with attributes
    
    Attributes are variables that belong to the object
    """
    pass


# Create objects and add attributes manually
laptop1 = Laptop()
laptop1.brand = "Dell"
laptop1.price = 50000
laptop1.color = "Silver"

laptop2 = Laptop()
laptop2.brand = "HP"
laptop2.price = 45000
laptop2.color = "Black"

print(f"Laptop 1: {laptop1.brand}, Price: {laptop1.price}, Color: {laptop1.color}")
print(f"Laptop 2: {laptop2.brand}, Price: {laptop2.price}, Color: {laptop2.color}")

print("\nWARNING: Manually adding attributes is NOT recommended!")
print("         Better way: Use __init__ method (covered next)")


# ================================================================================
# SECTION 3: INITIALIZING OBJECTS WITH __init__ METHOD
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 3: USING __init__ FOR INITIALIZATION (RECOMMENDED)")
print("=" * 80)

class Phone:
    """
    Phone class with proper initialization
    
    __init__ is a special method that runs when object is created
    It's called CONSTRUCTOR or INITIALIZER
    self represents the object itself
    """
    
    def __init__(self, brand, price, color):
        # self.attribute = parameter
        self.brand = brand
        self.price = price
        self.color = color


# Create objects - much cleaner!
phone1 = Phone("iPhone", 80000, "Gold")
phone2 = Phone("Samsung", 40000, "Blue")
phone3 = Phone("OnePlus", 35000, "Black")

print(f"Phone 1: {phone1.brand}, Price: {phone1.price}, Color: {phone1.color}")
print(f"Phone 2: {phone2.brand}, Price: {phone2.price}, Color: {phone2.color}")
print(f"Phone 3: {phone3.brand}, Price: {phone3.price}, Color: {phone3.color}")


# ================================================================================
# SECTION 4: CLASS WITH METHODS (Functions in Class)
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 4: ADDING METHODS (BEHAVIOR) TO CLASS")
print("=" * 80)

class BankAccount:
    """
    BankAccount class with attributes AND methods
    
    Attribute: account_number, balance
    Method: deposit(), withdraw(), display_balance()
    """
    
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self, amount):
        """Method to deposit money"""
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        """Method to withdraw money"""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance!")
    
    def display_balance(self):
        """Method to show current balance"""
        print(f"Account: {self.account_number}, Balance: {self.balance}")


# Create and use objects
account1 = BankAccount("ACC001", 10000)
account1.display_balance()
account1.deposit(5000)
account1.withdraw(3000)
account1.display_balance()

print("\n")
account2 = BankAccount("ACC002", 20000)
account2.display_balance()
account2.withdraw(5000)


# ================================================================================
# SECTION 5: REAL-WORLD EXAMPLE
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 5: REAL-WORLD EXAMPLE - STUDENT MANAGEMENT")
print("=" * 80)

class Student:
    """
    Student class - represents a student in a school
    """
    
    def __init__(self, roll_no, name, age, percentage):
        # Attributes
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.percentage = percentage
    
    def display_info(self):
        """Display student information"""
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Age: {self.age}, Percentage: {self.percentage}%")
    
    def is_passed(self):
        """Check if student passed (percentage >= 40)"""
        return self.percentage >= 40
    
    def get_grade(self):
        """Get grade based on percentage"""
        if self.percentage >= 90:
            return "A+"
        elif self.percentage >= 80:
            return "A"
        elif self.percentage >= 70:
            return "B"
        elif self.percentage >= 60:
            return "C"
        elif self.percentage >= 40:
            return "D"
        else:
            return "F"


# Create multiple student objects
students = [
    Student(1, "Ali", 18, 92),
    Student(2, "Fatima", 19, 78),
    Student(3, "Hassan", 18, 35),
    Student(4, "Zainab", 19, 88)
]

print("Student Information:")
for student in students:
    student.display_info()
    status = "Passed" if student.is_passed() else "Failed"
    print(f"  Status: {status}, Grade: {student.get_grade()}\n")


# ================================================================================
# SECTION 6: IMPORTANT POINTS TO REMEMBER
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 6: KEY POINTS TO REMEMBER")
print("=" * 80)
print("""
1. CLASS is a TEMPLATE/BLUEPRINT, OBJECT is a real instance
   
2. Multiple objects from one class = Different identities, separate data
   
3. __init__ method:
   - Called automatically when object is created
   - Used for initialization
   - First parameter is always 'self'
   
4. self keyword:
   - Represents the object itself
   - Used inside class to access attributes and methods
   - DON'T pass 'self' when calling method (Python does it automatically)
   
5. Attributes:
   - Store data (variables inside class)
   - Access using object.attribute
   
6. Methods:
   - Perform actions (functions inside class)
   - Access using object.method()
   - First parameter is always 'self'

7. Each object has its OWN DATA
   - Changes in one object don't affect others
""")


# ================================================================================
# SECTION 7: COMMON MISTAKES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 7: COMMON MISTAKES TO AVOID")
print("=" * 80)

# MISTAKE 1: Forgetting 'self' parameter
print("\nMISTAKE 1: Forgetting 'self' in method definition")
print("WRONG:")
print("""
class Wrong:
    def method(x):  # Missing 'self'
        pass
""")
print("CORRECT:")
print("""
class Correct:
    def method(self):  # Include 'self'
        pass
""")

# MISTAKE 2: Not using __init__
print("\n\nMISTAKE 2: Not using __init__ for initialization")
print("INEFFICIENT: Manually setting attributes")
print("""
obj = MyClass()
obj.attr1 = value1
obj.attr2 = value2
""")
print("BETTER: Use __init__")
print("""
class MyClass:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

obj = MyClass(value1, value2)
""")

# MISTAKE 3: Passing 'self' when calling method
print("\n\nMISTAKE 3: Passing 'self' when calling method")
print("WRONG: obj.method(obj)")
print("CORRECT: obj.method()  # Python handles 'self' automatically")
