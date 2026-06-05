"""
================================================================================
                    OOPS BEST PRACTICES - MASTERY 2
================================================================================

GUIDELINES:
Essential practices for writing professional, maintainable OOP code
Guidelines to use in real-world projects

================================================================================
"""

print("=" * 80)
print("SECTION 1: DESIGN PRINCIPLES")
print("=" * 80)

print("""
SOLID PRINCIPLES:

1. SINGLE RESPONSIBILITY PRINCIPLE (SRP)
   "A class should have only one reason to change"
   
   WRONG:
   class User:
       def save_to_db(self):
           pass
       def send_email(self):
           pass
       def validate_email(self):
           pass
   
   RIGHT:
   class User:
       def validate_email(self):
           pass
   
   class UserRepository:
       def save_to_db(self, user):
           pass
   
   class EmailService:
       def send_email(self, user):
           pass

   BENEFIT: Each class has single responsibility

---

2. OPEN/CLOSED PRINCIPLE (OCP)
   "Open for extension, closed for modification"
   
   WRONG:
   def calculate_discount(product_type, price):
       if product_type == "book":
           return price * 0.1
       elif product_type == "electronic":
           return price * 0.05
       # Must modify this function for new types!
   
   RIGHT:
   class DiscountStrategy:
       def get_discount(self, price):
           pass
   
   class BookDiscount(DiscountStrategy):
       def get_discount(self, price):
           return price * 0.1
   
   # Add new type without modifying existing code!

   BENEFIT: Extensible without changing existing code

---

3. LISKOV SUBSTITUTION PRINCIPLE (LSP)
   "Child classes should be substitutable for parent classes"
   
   WRONG:
   class Bird:
       def fly(self):
           pass
   
   class Penguin(Bird):
       def fly(self):
           raise Exception("Can't fly!")  # Violates contract!
   
   RIGHT:
   class Bird:
       pass
   
   class FlyingBird(Bird):
       def fly(self):
           pass
   
   class Penguin(Bird):
       pass  # Doesn't inherit fly()

   BENEFIT: Predictable inheritance behavior

---

4. INTERFACE SEGREGATION PRINCIPLE (ISP)
   "Many specific interfaces better than one general"
   
   WRONG:
   class Animal:
       def walk(self):
           pass
       def fly(self):
           pass
       def swim(self):
           pass
   
   class Dog(Animal):
       def fly(self):
           raise Exception()  # Doesn't need this!
   
   RIGHT:
   class Walker:
       def walk(self):
           pass
   
   class Flyer:
       def fly(self):
           pass
   
   class Dog(Walker):
       pass  # Only what it needs

   BENEFIT: Classes only depend on what they use

---

5. DEPENDENCY INVERSION PRINCIPLE (DIP)
   "Depend on abstractions, not concretions"
   
   WRONG:
   class EmailService:
       pass
   
   class UserService:
       def __init__(self):
           self.email = EmailService()  # Direct dependency
   
   RIGHT:
   class Notifier:
       def notify(self):
           pass
   
   class UserService:
       def __init__(self, notifier):  # Injected dependency
           self.notifier = notifier

   BENEFIT: Loosely coupled, testable code
""")


print("\n" + "=" * 80)
print("SECTION 2: NAMING CONVENTIONS")
print("=" * 80)

print("""
PYTHON NAMING STANDARDS (PEP 8):

1. CLASSES - PascalCase
   class UserAccount:
       pass
   
   class PaymentProcessor:
       pass
   
   class HTTPServer:
       pass

2. FUNCTIONS & METHODS - lowercase_with_underscores
   def calculate_total():
       pass
   
   def get_user_by_id():
       pass
   
   def save_to_database():
       pass

3. ATTRIBUTES - lowercase_with_underscores
   self.user_name
   self.account_number
   self.is_active

4. CONSTANTS - UPPERCASE_WITH_UNDERSCORES
   MAX_RETRIES = 3
   DEFAULT_TIMEOUT = 30
   API_KEY = "..."

5. PRIVATE - Leading underscore
   self._private_attribute
   def _private_method():
       pass

6. VERY PRIVATE - Double underscore (rarely used)
   self.__very_private = "..."

NAMING QUALITY:
✓ self_descriptive: user_count (not uc)
✓ Meaningful: calculate_total (not calc_t)
✓ Avoid abbreviations: get_user_account (not usr_acc)
✓ Verb-noun pairs: send_email, process_payment

ANTI-PATTERNS:
✗ Single letter: x, y, z (except loop counters)
✗ Cryptic: usr_mgmt_svc
✗ Not descriptive: temp, data, obj
✗ Too long: get_the_user_account_from_database_using_userid
""")


print("\n" + "=" * 80)
print("SECTION 3: CODE ORGANIZATION")
print("=" * 80)

print("""
CLASS ORGANIZATION:

class MyClass:
    # 1. Class variables (if any)
    class_var = "value"
    
    # 2. Constructor
    def __init__(self, param):
        self.param = param
    
    # 3. String representation
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    # 4. Public methods (API)
    def public_method(self):
        pass
    
    # 5. Protected methods (internal use)
    def _protected_method(self):
        pass
    
    # 6. Private methods (class only)
    def __private_method(self):
        pass
    
    # 7. Properties (if using)
    @property
    def some_property(self):
        pass
    
    # 8. Static/Class methods (if any)
    @staticmethod
    def static_method():
        pass
    
    @classmethod
    def class_method(cls):
        pass

PROJECT STRUCTURE:
project/
├── main.py              # Entry point
├── config.py            # Configuration
├── classes/
│   ├── models.py        # Data models
│   ├── services.py      # Business logic
│   └── utils.py         # Utilities
├── tests/
│   ├── test_models.py
│   └── test_services.py
└── README.md

FILE ORGANIZATION:
✓ One class per file (small classes) or related classes (large files)
✓ Logical grouping by functionality
✓ Clear module names
""")


print("\n" + "=" * 80)
print("SECTION 4: ENCAPSULATION - BEST PRACTICES")
print("=" * 80)

print("""
PROPER ENCAPSULATION:

1. PRIVATE IMPLEMENTATION DETAILS:
   - Use __ for calculations, helpers
   - Use _ for internal methods
   
   class BankAccount:
       def __init__(self, balance):
           self._balance = balance
       
       def _validate_amount(self, amount):
           return amount > 0
       
       def deposit(self, amount):
           if self._validate_amount(amount):
               self._balance += amount

2. PUBLIC INTERFACE:
   - Only necessary methods exposed
   - Hide implementation
   
   class PaymentProcessor:
       # Public interface
       def process_payment(self, amount):
           self._validate_payment(amount)
           self._charge_card(amount)
           self._notify_user()
       
       # Private implementation
       def _validate_payment(self, amount):
           pass
       
       def _charge_card(self, amount):
           pass

3. USE PROPERTIES FOR VALIDATION:
   class User:
       def __init__(self, age):
           self._age = None
           self.age = age  # Use setter
       
       @property
       def age(self):
           return self._age
       
       @age.setter
       def age(self, value):
           if 0 < value < 150:
               self._age = value
           else:
               raise ValueError("Invalid age")

4. READ-ONLY ATTRIBUTES:
   @property
   def created_date(self):  # No setter = read-only
       return self._created_date

AVOID:
✗ Public attributes that should be private
✗ Getter/Setter for simple access (use @property)
✗ Changing interface frequently
""")


print("\n" + "=" * 80)
print("SECTION 5: INHERITANCE - BEST PRACTICES")
print("=" * 80)

print("""
INHERITANCE RULES:

1. USE INHERITANCE FOR IS-A RELATIONSHIPS:
   ✓ Dog IS-A Animal
   ✓ Manager IS-A Employee
   ✗ Car IS-A Engine (WRONG - use composition)

2. KEEP INHERITANCE SHALLOW:
   ✓ Good:
   Animal → Mammal → Dog
   
   ✗ Avoid:
   Animal → Mammal → DomesticMammal → Dog → ServiceDog → etc.

3. USE super() PROPERLY:
   class Child(Parent):
       def __init__(self, param1, param2):
           super().__init__(param1)
           self.param2 = param2
       
       def method(self):
           super().method()
           # Child-specific code

4. AVOID MULTIPLE INHERITANCE (usually):
   ✓ Composition:
   class Car:
       def __init__(self, engine, wheels):
           self.engine = engine
           self.wheels = wheels
   
   ✗ Multiple Inheritance:
   class Car(Vehicle, Machine, Equipment):
       pass  # Confusing!

5. OVERRIDE THOUGHTFULLY:
   - Same method name
   - Compatible parameters
   - Document changes
   
   class Parent:
       def process(self, data):
           return data.upper()
   
   class Child(Parent):
       def process(self, data):
           result = super().process(data)
           return result + "!"

WHEN TO REFACTOR:
- Inheritance chain > 3 levels? Consider composition
- Child doesn't use parent methods? Wrong hierarchy
- Multiple if-else by type? Use inheritance or polymorphism
""")


print("\n" + "=" * 80)
print("SECTION 6: TESTING & QUALITY")
print("=" * 80)

print("""
DESIGN FOR TESTABILITY:

1. DEPENDENCY INJECTION:
   # Easy to test
   class UserService:
       def __init__(self, db_connection):
           self.db = db_connection  # Injected
   
   # Test with mock
   mock_db = MockDatabase()
   service = UserService(mock_db)

2. SMALL, FOCUSED CLASSES:
   # Easy to test individual classes
   class UserValidator:
       def validate_email(self, email):
           pass
   
   class UserRepository:
       def save(self, user):
           pass

3. PURE FUNCTIONS:
   # No side effects - easy to test
   def calculate_discount(price):
       return price * 0.1

4. AVOID GLOBAL STATE:
   ✗ Global variables
   ✗ Static mutable state
   ✓ Dependency injection

QUALITY METRICS:
- Cyclomatic complexity: Keep methods simple
- Code coverage: > 80% recommended
- Duplication: Keep similar code < 3 times
- Method length: 1-30 lines ideal

TESTING PYRAMID:
Unit tests:     70% - Test individual classes
Integration:    20% - Test class interactions
End-to-end:     10% - Test full workflow
""")


print("\n" + "=" * 80)
print("SECTION 7: DOCUMENTATION")
print("=" * 80)

print("""
DOCSTRINGS - PYTHON STANDARD:

1. CLASS DOCSTRING:
   class BankAccount:
       '''
       Represents a bank account with deposit/withdraw functionality.
       
       Attributes:
           holder (str): Account holder name
           balance (float): Current balance in PKR
       '''

2. METHOD DOCSTRING:
   def withdraw(self, amount):
       '''
       Withdraw money from account.
       
       Args:
           amount (float): Amount to withdraw in PKR
       
       Returns:
           bool: True if successful, False otherwise
       
       Raises:
           ValueError: If amount is invalid
       '''

3. MEANINGFUL COMMENTS:
   # Calculate compound interest for 5 years
   final_amount = principal * (1 + rate/100) ** 5
   
   ✗ Bad comment:
   # Add 5 to x
   x = x + 5

4. EXAMPLE IN DOCSTRING:
   def add(a, b):
       '''
       Add two numbers.
       
       >>> add(2, 3)
       5
       '''
       return a + b

AVOID:
✗ Over-commenting obvious code
✗ Outdated comments
✗ Replacing clear code with comments
""")


print("\n" + "=" * 80)
print("SECTION 8: COMMON ANTI-PATTERNS TO AVOID")
print("=" * 80)

print("""
ANTI-PATTERN 1: GOD CLASSES
PROBLEM: One class does everything
class User:
    def validate()
    def save_to_db()
    def send_email()
    def generate_report()
    def log_activity()

SOLUTION: Split responsibilities
class User: # Just data
    pass

class UserValidator:
    def validate():
        pass

---

ANTI-PATTERN 2: DEEP INHERITANCE
PROBLEM: Many levels of hierarchy
Animal → Mammal → Carnivore → Cat → PersianCat → WildPersianCat

SOLUTION: Flatten or use composition
class Cat: # Base class
    pass

class PersianCat(Cat):
    pass

---

ANTI-PATTERN 3: MIXED PUBLIC/PRIVATE
PROBLEM: No clear encapsulation
class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # Public - can change directly!

SOLUTION: Use properties
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance

---

ANTI-PATTERN 4: CIRCULAR DEPENDENCIES
PROBLEM: Class A needs Class B, B needs A
class User:
    def __init__(self, account: Account):
        pass

class Account:
    def __init__(self, user: User):
        pass

SOLUTION: Use dependency injection or refactor

---

ANTI-PATTERN 5: VIOLATING LISKOV PRINCIPLE
PROBLEM: Child doesn't truly substitute parent
class Bird:
    def fly(self):
        pass

class Penguin(Bird):
    def fly(self):
        raise Exception()  # Can't this!

SOLUTION: Better hierarchy
class Animal:
    pass

class Bird(Animal):
    def fly(self):
        pass

class Penguin(Animal):
    pass
""")


print("\n" + "=" * 80)
print("SECTION 9: PERFORMANCE TIPS")
print("=" * 80)

print("""
OPTIMIZATION GUIDELINES:

1. LAZY INITIALIZATION:
   # Bad - create all upfront
   def __init__(self):
       self.expensive_resource = ExpensiveObject()
   
   # Good - create on demand
   @property
   def expensive_resource(self):
       if not hasattr(self, '_resource'):
           self._resource = ExpensiveObject()
       return self._resource

2. CACHING RESULTS:
   def expensive_calculation(self):
       if not hasattr(self, '_cached_result'):
           self._cached_result = complex_calculation()
       return self._cached_result

3. AVOID UNNECESSARY OBJECT CREATION:
   # Bad - creates new object each loop
   for i in range(1000000):
       obj = MyClass()
   
   # Good - reuse if possible
   obj = MyClass()
   for i in range(1000000):
       obj.reset()

4. USE GENERATORS FOR LARGE DATA:
   # Bad - loads all in memory
   def get_users():
       return [load_user(i) for i in range(1000000)]
   
   # Good - lazy loading
   def get_users():
       for i in range(1000000):
           yield load_user(i)

REMEMBER:
- Profile before optimizing
- Premature optimization is evil
- Readable code > Optimized code
""")


print("\n" + "=" * 80)
print("SECTION 10: SUMMARY - CHECKLIST")
print("=" * 80)

print("""
BEFORE SUBMITTING CODE:

DESIGN:
☐ Single responsibility per class
☐ Clear, meaningful names
☐ Proper encapsulation
☐ Logical inheritance (if used)
☐ SOLID principles followed

CODE QUALITY:
☐ No code duplication
☐ Simple, readable methods
☐ Proper error handling
☐ Edge cases handled
☐ Comments where needed

TESTING:
☐ Unit tests written
☐ > 80% coverage
☐ Edge cases tested
☐ Integration tests done
☐ Performance acceptable

DOCUMENTATION:
☐ Docstrings complete
☐ README updated
☐ Complex logic explained
☐ Usage examples provided

PERFORMANCE:
☐ No obvious inefficiencies
☐ Algorithms suitable for input size
☐ Memory usage reasonable
☐ Profiled if needed

MAINTAINABILITY:
☐ Team can understand code
☐ Future changes easy
☐ Dependencies clear
☐ Testability high

KEY TAKEAWAYS:
1. KISS - Keep It Simple, Stupid
2. DRY - Don't Repeat Yourself
3. YAGNI - You Aren't Gonna Need It
4. SOLID principles
5. Read others' code
6. Refactor regularly
7. Test thoroughly
8. Document clearly
9. Optimize when needed
10. Learn from mistakes
""")
