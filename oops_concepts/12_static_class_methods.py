"""
================================================================================
        STATIC AND CLASS METHODS - ADVANCED 6
================================================================================

CONCEPTS:
  STATIC METHODS  - Don't need instance (no self), don't need class (no cls)
  CLASS METHODS   - Work with class, not instance (have cls parameter)
  INSTANCE METHODS - Normal methods (have self)

================================================================================
                        WHEN TO USE?
================================================================================

INSTANCE METHODS:
  - Operate on instance data
  - Use: obj.method()
  - Have self parameter

CLASS METHODS:
  - Work with class-level data
  - Called on class or instance: ClassName.method() or obj.method()
  - Have cls parameter
  - Often used for alternative constructors

STATIC METHODS:
  - Utility functions related to class
  - No access to self or cls
  - Called on class or instance
  - Like regular functions but grouped in class

================================================================================
"""

# ===============================================================================
# SECTION 1: INSTANCE vs CLASS vs STATIC METHODS
# ===============================================================================

print("=" * 80)
print("SECTION 1: THREE TYPES OF METHODS")
print("=" * 80)

class MyClass:
    class_var = "I'm a class variable"
    
    def __init__(self, instance_var):
        self.instance_var = instance_var
    
    # METHOD 1: INSTANCE METHOD
    def instance_method(self):
        """Works with instance data (self)"""
        print(f"Instance method: {self.instance_var}")
        print(f"Can access class: {self.class_var}")
    
    # METHOD 2: CLASS METHOD
    @classmethod
    def class_method(cls):
        """Works with class data (cls)"""
        print(f"Class method: {cls.class_var}")
        print(f"Class name: {cls.__name__}")
    
    # METHOD 3: STATIC METHOD
    @staticmethod
    def static_method(x, y):
        """Utility function (no self or cls)"""
        return x + y


obj = MyClass("Instance data")

print("--- INSTANCE METHOD ---")
obj.instance_method()

print("\n--- CLASS METHOD ---")
obj.class_method()
MyClass.class_method()  # Can also call on class

print("\n--- STATIC METHOD ---")
result = obj.static_method(5, 3)
print(f"Static method result: {result}")

result2 = MyClass.static_method(10, 20)
print(f"Static method result: {result2}")


# ===============================================================================
# SECTION 2: CLASS METHODS - ALTERNATIVE CONSTRUCTORS
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 2: CLASS METHODS AS ALTERNATIVE CONSTRUCTORS")
print("=" * 80)

class Date:
    """Date with multiple ways to create"""
    
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    @classmethod
    def today(cls):
        """Alternative constructor - create today's date"""
        # In real code, get actual date
        return cls(20, 3, 2024)
    
    @classmethod
    def from_string(cls, date_string):
        """Alternative constructor - parse string"""
        day, month, year = map(int, date_string.split("-"))
        return cls(day, month, year)
    
    def __str__(self):
        return f"{self.day}-{self.month}-{self.year}"


# Multiple ways to create Date
date1 = Date(15, 3, 2024)
print(f"Normal constructor: {date1}")

date2 = Date.today()
print(f"Using today(): {date2}")

date3 = Date.from_string("25-12-2024")
print(f"From string: {date3}")

print("""
CLASS METHOD AS CONSTRUCTOR:
- Provides alternative ways to create objects
- Common in libraries (e.g., dict.fromkeys())
- Better than overloading (Python doesn't support it)
""")


# ===============================================================================
# SECTION 3: CLASS VARIABLES AND CLASS METHODS
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 3: CLASS VARIABLES WITH CLASS METHODS")
print("=" * 80)

class Product:
    """Tracking product count using class variable"""
    
    total_products = 0  # Class variable
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.total_products += 1  # Increment class variable
    
    @classmethod
    def get_total_products(cls):
        """Class method to access class variable"""
        return cls.total_products
    
    @classmethod
    def reset_count(cls):
        """Reset counter"""
        cls.total_products = 0


p1 = Product("Laptop", 50000)
p2 = Product("Phone", 30000)
p3 = Product("Tablet", 20000)

print(f"Total products: {Product.get_total_products()}")

Product.reset_count()
print(f"After reset: {Product.get_total_products()}")


# ===============================================================================
# SECTION 4: STATIC METHODS - UTILITY FUNCTIONS
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 4: STATIC METHODS - UTILITY FUNCTIONS")
print("=" * 80)

class MathUtils:
    """Collection of math utilities"""
    
    @staticmethod
    def is_even(n):
        """Check if number is even"""
        return n % 2 == 0
    
    @staticmethod
    def is_prime(n):
        """Check if number is prime"""
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def factorial(n):
        """Calculate factorial"""
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)


print(f"Is 4 even? {MathUtils.is_even(4)}")
print(f"Is 5 even? {MathUtils.is_even(5)}")

print(f"Is 7 prime? {MathUtils.is_prime(7)}")
print(f"Is 9 prime? {MathUtils.is_prime(9)}")

print(f"5 factorial: {MathUtils.factorial(5)}")

print("""
STATIC METHODS:
- Utility functions grouped in class
- No dependency on instance or class state
- Like regular functions, but organized
- Make code organization clearer
""")


# ===============================================================================
# SECTION 5: REAL WORLD - USER MANAGEMENT
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 5: REAL WORLD - USER MANAGEMENT SYSTEM")
print("=" * 80)

class User:
    """User with different method types"""
    
    # Class variables
    all_users = []
    user_id_counter = 0
    
    def __init__(self, name, email):
        # Instance variables
        self.name = name
        self.email = email
        self.user_id = User.user_id_counter
        User.user_id_counter += 1
        User.all_users.append(self)
    
    # INSTANCE METHOD
    def display_info(self):
        """Show user info"""
        print(f"ID: {self.user_id}, Name: {self.name}, Email: {self.email}")
    
    # CLASS METHOD - Alternative constructor
    @classmethod
    def from_string(cls, user_string):
        """Create user from string format"""
        name, email = user_string.split(",")
        return cls(name.strip(), email.strip())
    
    # CLASS METHOD - Access class data
    @classmethod
    def get_all_users(cls):
        """Get all users"""
        return cls.all_users
    
    # CLASS METHOD - Factory method
    @classmethod
    def create_admin(cls, name):
        """Create special admin user"""
        user = cls(name, f"{name.lower()}@admin.com")
        return user
    
    # STATIC METHOD - Utility
    @staticmethod
    def is_valid_email(email):
        """Validate email format"""
        return "@" in email and "." in email


# Create users
u1 = User("Ali", "ali@email.com")
u2 = User.from_string("Fatima, fatima@email.com")
u3 = User.create_admin("Admin")

print("All users:")
for user in User.get_all_users():
    user.display_info()

print(f"\nIs 'ali@email.com' valid? {User.is_valid_email('ali@email.com')}")
print(f"Is 'invalid' valid? {User.is_valid_email('invalid')}")

print("""
COMBINED USAGE:
- Instance method: Display individual user info
- Class method: Create alternate forms, manage all users
- Static method: Utility validation function
""")


# ===============================================================================
# SECTION 6: REAL WORLD - BANKING SYSTEM
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 6: REAL WORLD - BANK ACCOUNT SYSTEM")
print("=" * 80)

class BankAccount:
    """Bank account with all method types"""
    
    # Class variables
    exchange_rate = 1.8  # PKR to some other currency
    total_accounts = 0
    
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
        BankAccount.total_accounts += 1
    
    # INSTANCE METHOD
    def deposit(self, amount):
        """Deposit money"""
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"
    
    # INSTANCE METHOD
    def withdraw(self, amount):
        """Withdraw money"""
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Insufficient balance!"
    
    # CLASS METHOD - Update exchange rate
    @classmethod
    def update_exchange_rate(cls, new_rate):
        """Update global exchange rate"""
        cls.exchange_rate = new_rate
    
    # CLASS METHOD - Get total accounts
    @classmethod
    def get_total_accounts(cls):
        """Get number of accounts"""
        return cls.total_accounts
    
    # CLASS METHOD - Factory method
    @classmethod
    def create_with_initial_credit(cls, holder, initial_credit):
        """Create account with initial credit"""
        return cls(holder, initial_credit)
    
    # STATIC METHOD - Convert currency
    @staticmethod
    def convert_to_foreign(pkr_amount, rate):
        """Convert PKR to another currency"""
        return pkr_amount * rate
    
    # INSTANCE METHOD using class method result
    def convert_balance_to_foreign(self):
        """Convert this account's balance"""
        return self.convert_to_foreign(self.balance, self.exchange_rate)


# Use different method types
acc1 = BankAccount("Ahmed", 10000)
acc2 = BankAccount.create_with_initial_credit("Fatima", 20000)

print("Accounts created:")
print(f"Total accounts: {BankAccount.get_total_accounts()}")

print(f"\nacc1.deposit(5000):")
print(acc1.deposit(5000))

print(f"\nExchange rate: {BankAccount.exchange_rate}")
print(f"acc1 balance in foreign currency: {acc1.convert_balance_to_foreign():.2f}")

BankAccount.update_exchange_rate(2.0)
print(f"\nAfter rate update to 2.0:")
print(f"acc1 balance in foreign currency: {acc1.convert_balance_to_foreign():.2f}")


# ===============================================================================
# SECTION 7: BEST PRACTICES
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 7: BEST PRACTICES")
print("=" * 80)

print("""
WHEN TO USE EACH:

INSTANCE METHODS:
✓ Work with individual object's data
✓ Use when: Need to access or modify self
✓ Default choice for most methods

def __init__(self, name):
    self.name = name

def display(self):  # Instance method
    print(self.name)


CLASS METHODS:
✓ Alternative constructors (factory methods)
✓ Work with class-level data
✓ Use when: Creating different object creation ways

@classmethod
def from_dict(cls, data):
    return cls(data['name'])


STATIC METHODS:
✓ Utility functions related to class
✓ No need for instance or class state
✓ Use when: Grouping related functions

@staticmethod
def is_valid_email(email):
    return "@" in email


DECISION TREE:

Does method need self? → YES → Use instance method
         ↓ NO
Does method need cls? → YES → Use class method
         ↓ NO
                    → Use static method


COMMON PATTERNS:

Pattern 1: Factory Methods
@classmethod
def from_json(cls, json_string):
    data = json.loads(json_string)
    return cls(**data)

Pattern 2: Class-level Operations
@classmethod
def reset_all(cls):
    cls.instances = []

Pattern 3: Utility Functions
@staticmethod
def format_phone(number):
    return f"{number[:3]}-{number[3:]}"

Pattern 4: Tracking
class MyClass:
    total = 0
    
    def __init__(self):
        MyClass.total += 1
    
    @classmethod
    def get_total(cls):
        return cls.total
""")
