"""
================================================================================
                        ENCAPSULATION - INTERMEDIATE 1
================================================================================

CONCEPT:
  Encapsulation = Bundling data (attributes) and functions (methods) together
                + Hiding internal details from outside world

MOTTO: "Data Hiding + Controlled Access"

ANALOGY:
  Like a car:
  - You see buttons (public interface)
  - You don't see engine inside (private details)
  - You control it through buttons, not by touching engine directly

================================================================================
                        WHEN TO USE?
================================================================================
Use Encapsulation when you need to:
1. Protect data from unauthorized access
2. Validate data before modifications
3. Hide implementation details
4. Control how data is accessed
5. Maintain object integrity

================================================================================
                        HOW TO USE?
================================================================================
ACCESS MODIFIERS:

1. PUBLIC (no underscore)
   - Accessible from anywhere
   - attribute.name
   - Use for: Normal data/methods

2. PROTECTED (single underscore _)
   - Intended for internal use
   - Should not access from outside
   - Use for: Subclasses

3. PRIVATE (double underscore __)
   - Accessible only within the class
   - Cannot access from outside
   - Use for: Sensitive operations

================================================================================
"""

# ================================================================================
# SECTION 1: UNDERSTANDING THE PROBLEM
# ================================================================================

print("=" * 80)
print("SECTION 1: THE PROBLEM WITHOUT ENCAPSULATION")
print("=" * 80)

# WITHOUT ENCAPSULATION - PROBLEMS
class BadBankAccount:
    """
    Bad practice: No encapsulation
    Anyone can change balance directly!
    """
    
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance  # Public - anyone can change!


account = BadBankAccount("Ali", 10000)
print(f"Original balance: {account.balance}")

# PROBLEM: Anyone can change balance directly!
account.balance = 999999  # Hacker manipulates!
print(f"After hacking: {account.balance}")

print("""
PROBLEMS WITHOUT ENCAPSULATION:
1. Data can be changed directly without validation
2. No control over what values are assigned
3. Impossible to track changes
4. Breaks object integrity
5. Easy for hackers to manipulate
""")


# ================================================================================
# SECTION 2: PUBLIC ATTRIBUTES AND METHODS
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 2: PUBLIC (OPEN ACCESS)")
print("=" * 80)

class Rectangle:
    """
    Public attributes - accessible from anywhere
    Use when data doesn't need protection
    """
    
    def __init__(self, length, width):
        self.length = length  # Public
        self.width = width    # Public
    
    def area(self):  # Public method
        return self.length * self.width
    
    def perimeter(self):  # Public method
        return 2 * (self.length + self.width)


rect = Rectangle(5, 3)
print(f"Length: {rect.length}, Width: {rect.width}")
print(f"Area: {rect.area()}")

# Can modify directly (but not recommended for sensitive data)
rect.length = 10
print(f"Modified Length: {rect.length}")

print("""
PUBLIC ACCESS:
- No underscore: attribute_name
- Can be accessed and modified from anywhere
- Use for: Non-sensitive, simple data
""")


# ================================================================================
# SECTION 3: PROTECTED ATTRIBUTES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 3: PROTECTED (SINGLE UNDERSCORE _)")
print("=" * 80)

class Student:
    """
    Protected attributes - use single underscore _
    Signals "internal use only" - but Python doesn't enforce it
    """
    
    def __init__(self, name, marks):
        self.name = name           # Public
        self._marks = marks        # Protected - signals internal use
        self._is_passed = marks >= 40  # Protected
    
    def _check_validity(self, marks):
        """Protected method - for internal use"""
        return 0 <= marks <= 100
    
    def get_marks(self):
        """Public method to access protected data safely"""
        return self._marks
    
    def set_marks(self, marks):
        """Public method to modify protected data with validation"""
        if self._check_validity(marks):
            self._marks = marks
        else:
            print("Invalid marks!")


student = Student("Ali", 85)

# Can access, but shouldn't (Python allows it - convention only)
print(f"Marks (via method): {student.get_marks()}")

# Modify with validation
student.set_marks(90)
print(f"After modification: {student.get_marks()}")

# Try invalid
student.set_marks(150)

print("""
PROTECTED ACCESS:
- Single underscore: _attribute_name
- Python ALLOWS access (it's just a convention)
- Signals to other programmers: "Don't use from outside"
- Used for: Subclass-related data
- Use getter/setter methods for safe access

PRINCIPLE:
'We're not going to stop you, but please don't do it'
""")


# ================================================================================
# SECTION 4: PRIVATE ATTRIBUTES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 4: PRIVATE (DOUBLE UNDERSCORE __)")
print("=" * 80)

class BankAccount:
    """
    Private attributes - use double underscore __
    Python ENFORCES this - cannot access from outside
    """
    
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance      # Private - cannot access from outside!
        self.__pin = "1234"           # Private
    
    def __validate_amount(self, amount):
        """Private method - only for internal use"""
        return amount > 0 and amount <= self.__balance
    
    def get_balance(self):
        """Public method to safely access private data"""
        return self.__balance
    
    def deposit(self, amount):
        """Public method to modify private data safely"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid amount!")
    
    def withdraw(self, amount):
        """Public method with validation"""
        if self.__validate_amount(amount):
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
            return True
        else:
            print("Insufficient balance or invalid amount!")
            return False


account = BankAccount("Ahmed", 50000)
print(f"Holder: {account.holder}")
print(f"Balance: {account.get_balance()}")

# Try to access private attribute directly - WILL FAIL!
print("\nTrying to access private attribute directly...")
try:
    print(account.__balance)
except AttributeError as e:
    print(f"ERROR: {e}")
    print("\nReason: __balance is PRIVATE and cannot be accessed!")

# Use public methods instead
account.deposit(5000)
print(f"After deposit: {account.get_balance()}")

account.withdraw(10000)
print(f"After withdrawal: {account.get_balance()}")

# Try invalid withdrawal
account.withdraw(100000)

print("""
PRIVATE ACCESS:
- Double underscore: __attribute_name
- Python PREVENTS access from outside (name mangling)
- Most secure - strongest data protection
- Use for: Sensitive operations and critical data
- Must use public methods to access/modify

PRINCIPLE:
'You absolutely cannot access this from outside'
""")


# ================================================================================
# SECTION 5: NAME MANGLING EXPLANATION
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 5: NAME MANGLING (HOW PYTHON HIDES PRIVATE)")
print("=" * 80)

class Secret:
    """
    Demonstrate name mangling
    Python changes name of private attributes
    """
    
    def __init__(self):
        self.public = "I'm public"
        self._protected = "I'm protected"
        self.__private = "I'm private"


obj = Secret()

# Public - accessible
print(f"Public: {obj.public}")

# Protected - accessible (but shouldn't)
print(f"Protected: {obj._protected}")

# Private - NOT directly accessible by name
print("\nTrying to access private attribute by name __private:")
try:
    print(obj.__private)
except AttributeError as e:
    print(f"ERROR: {e}")

# Python renames it to _ClassName__attribute
print("\nBut Python renamed it internally to _Secret__private:")
print(f"Via mangled name: {obj._Secret__private}")

print("""
NAME MANGLING:
Python automatically renames __attribute to _ClassName__attribute
This prevents accidental access but isn't unbreakable
It's about preventing MISTAKES, not preventing CRIMINALS

If someone really wants to access: obj._BankAccount__balance
They can, but it signals they're doing something wrong
""")


# ================================================================================
# SECTION 6: GETTERS AND SETTERS (PROPERTIES)
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 6: GETTERS AND SETTERS")
print("=" * 80)

class Person:
    """
    Using getter and setter methods for controlled access
    """
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    # GETTER - returns the value
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    # SETTER - sets the value with validation
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            print("Invalid name!")
    
    def set_age(self, age):
        if isinstance(age, int) and 0 < age < 150:
            self.__age = age
        else:
            print("Invalid age!")


person = Person("Ali", 25)

# Get values via getter
print(f"Name: {person.get_name()}, Age: {person.get_age()}")

# Set values via setter with validation
person.set_age(30)
print(f"After setting age to 30: {person.get_age()}")

# Try invalid value
person.set_age(200)
print(f"Age after invalid set: {person.get_age()}")

print("""
GETTERS AND SETTERS:
- Getter: Read-only access to private data
- Setter: Write access with validation
- Allows control over what gets stored
- Better than making data public
""")


# ================================================================================
# SECTION 7: REAL WORLD EXAMPLE
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 7: REAL WORLD - EMPLOYEE MANAGEMENT")
print("=" * 80)

class Employee:
    """
    Employee with proper encapsulation
    Balance company needs with employee privacy
    """
    
    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id              # Private
        self.__name = name                  # Private
        self.__salary = salary              # Private - sensitive!
        self.__is_active = True             # Private
    
    def __validate_salary(self, salary):
        """Private validation method"""
        return salary > 0 and salary < 10000000
    
    def get_emp_id(self):
        """Public getter - safe to expose"""
        return self.__emp_id
    
    def get_name(self):
        """Public getter"""
        return self.__name
    
    def get_salary(self):
        """Public getter - only for authorized users"""
        return self.__salary
    
    def set_salary(self, new_salary):
        """Public setter - with validation"""
        if self.__validate_salary(new_salary):
            self.__salary = new_salary
            print(f"Salary updated to {new_salary}")
        else:
            print("Invalid salary!")
    
    def promote(self, increment):
        """Modify salary safely through specific method"""
        new_salary = self.__salary + increment
        if self.__validate_salary(new_salary):
            self.__salary = new_salary
            print(f"Promoted! New salary: {self.__salary}")
        else:
            print("Promotion amount is invalid!")
    
    def display_info(self):
        """Display employee information"""
        print(f"\n--- Employee Info ---")
        print(f"ID: {self.__emp_id}")
        print(f"Name: {self.__name}")
        print(f"Salary: {self.__salary}")
        print(f"Active: {self.__is_active}")


emp1 = Employee(101, "Ahmed", 50000)
emp1.display_info()

emp1.promote(10000)
emp1.display_info()

# Try invalid
emp1.set_salary(999999999)
emp1.display_info()


# ================================================================================
# SECTION 8: COMPARISON TABLE
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 8: COMPARISON OF ACCESS MODIFIERS")
print("=" * 80)

print("""
╔═══════════════╦════════════════╦═══════════════╦══════════════╗
║    Type       ║    Syntax      ║  Access From  ║    Use For   ║
║               ║                ║    Outside    ║              ║
╠═══════════════╬════════════════╬═══════════════╬══════════════╣
║ Public        ║ name           ║ Yes (Direct)  ║ Normal data  ║
╟───────────────╫────────────────╫───────────────╫──────────────╢
║ Protected     ║ _name          ║ Yes (But Don't)║ For subclass╢
╟───────────────╫────────────────╫───────────────╫──────────────╢
║ Private       ║ __name         ║ No (Blocked)   ║ Critical    ║
║               ║                ║                ║ data/methods║
╚═══════════════╩════════════════╩═══════════════╩══════════════╝

WHEN TO USE WHICH:

1. PUBLIC (no prefix):
   - Colors in RGB object
   - Player name in game
   - Rectangle dimensions
   - Non-sensitive data

2. PROTECTED (_prefix):
   - Internal helper methods
   - Data meant for subclasses
   - Implementation details

3. PRIVATE (__prefix):
   - Passwords, API keys
   - Bank account balance
   - Critical calculations
   - Security-sensitive data
""")


# ================================================================================
# SECTION 9: ENCAPSULATION BENEFITS
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 9: BENEFITS OF ENCAPSULATION")
print("=" * 80)

print("""
BENEFITS:

1. DATA INTEGRITY:
   ✓ Data can only be modified through validated methods
   ✓ Prevents invalid states
   ✓ Maintains object consistency

2. SECURITY:
   ✓ Sensitive data is protected
   ✓ Controlled access prevents hacking
   ✓ Only authorized operations allowed

3. FLEXIBILITY:
   ✓ Can change internal implementation
   ✓ External code doesn't break
   ✓ Can add validation later without affecting external code

4. MAINTAINABILITY:
   ✓ Easier to debug
   ✓ Clear interface (public methods)
   ✓ Less coupling between classes

EXAMPLE - WHY FLEXIBILITY MATTERS:

OLD CODE:
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

NEW CODE (no public API changed):
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        self.__transaction_log = []
    
    def get_balance(self):
        return self.__balance
    
    # Users still call get_balance() - their code doesn't break!
""")
