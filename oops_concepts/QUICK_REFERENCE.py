"""
================================================================================
                    OOPS QUICK REFERENCE - CHEAT SHEET
================================================================================

A quick lookup guide for common OOP concepts and syntax.
For detailed explanations, see the full files.

================================================================================
                        SYNTAX QUICK REFERENCE
================================================================================

# 1. BASIC CLASS STRUCTURE
class ClassName:
    # Class variable (shared by all instances)
    class_var = "value"
    
    # Constructor
    def __init__(self, param1, param2):
        # Instance variables (specific to each object)
        self.instance_var1 = param1
        self.instance_var2 = param2
    
    # Instance method
    def method_name(self):
        pass
    
    # Class method
    @classmethod
    def class_method(cls):
        pass
    
    # Static method
    @staticmethod
    def static_method():
        pass
    
    # String representation
    def __str__(self):
        return f"Representation of {self.instance_var1}"

# Create object (instance)
obj = ClassName("value1", "value2")

---

# 2. INHERITANCE
class ParentClass:
    def __init__(self, param):
        self.param = param
    
    def method(self):
        return "Parent"

class ChildClass(ParentClass):
    def __init__(self, param, extra):
        super().__init__(param)  # Call parent's __init__
        self.extra = extra
    
    def method(self):  # Override parent method
        parent_result = super().method()  # Use parent's result
        return parent_result + " + Child"

---

# 3. ENCAPSULATION (Access Control)
class MyClass:
    def __init__(self):
        self.public_attr = "accessible everywhere"
        self._protected_attr = "hint: use in subclasses only"
        self.__private_attr = "inaccessible from outside"
    
    def public_method(self):
        pass
    
    def _protected_method(self):
        pass
    
    def __private_method(self):
        pass

---

# 4. PROPERTIES
class MyClass:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        # Getter - access like: obj.value
        return self._value
    
    @value.setter
    def value(self, new_value):
        # Setter - modify like: obj.value = 10
        if new_value >= 0:
            self._value = new_value
        else:
            raise ValueError("Value must be positive")

---

# 5. ABSTRACT CLASSES
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def required_method(self):
        # Child MUST implement this
        pass
    
    def regular_method(self):
        # Child can inherit this
        pass

class ConcreteClass(AbstractClass):
    def required_method(self):
        return "Implementation"

---

# 6. DECORATORS
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def my_function():
    print("During")

---

# 7. OPERATOR OVERLOADING
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return MyClass(self.value + other.value)
    
    def __sub__(self, other):
        return MyClass(self.value - other.value)
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __len__(self):
        return self.value
    
    def __str__(self):
        return str(self.value)
    
    def __call__(self):
        return self.value

# Usage:
obj1 = MyClass(5)
obj2 = MyClass(3)
obj3 = obj1 + obj2  # Uses __add__
print(obj1 == obj2)  # Uses __eq__
print(len(obj1))     # Uses __len__

---

# 8. COMPOSITION
class Component:
    def do_something(self):
        pass

class CompositeClass:
    def __init__(self):
        self.component = Component()  # HAS-A relationship
    
    def method(self):
        self.component.do_something()

---

# 9. POLYMORPHISM
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

# Polymorphic function
def make_speak(animal):
    animal.speak()  # Works with any object that has speak()

---

# 10. FACTORY PATTERN
class Factory:
    @staticmethod
    def create_object(type_name):
        if type_name == "typeA":
            return ClassA()
        elif type_name == "typeB":
            return ClassB()
        return None

================================================================================
                        WHEN TO USE WHAT?
================================================================================

PUBLIC ATTRIBUTE?
Use when: Data doesn't need protection
Example: person.name = "Ali"

PROTECTED ATTRIBUTE (_)?
Use when: Data for subclasses only
Example: self._internal_state

PRIVATE ATTRIBUTE (__)?
Use when: Sensitive data/calculations
Example: self.__password

PROPERTY?
Use when: Need validation or computation
Example: @property def age(self):

CLASS METHOD?
Use when: Need class-level data or alternative constructor
Example: @classmethod def from_string(cls, data):

STATIC METHOD?
Use when: Utility function related to class
Example: @staticmethod def is_valid_email(email):

INHERITANCE?
Use when: TRUE IS-A relationship
Example: Dog IS-A Animal

COMPOSITION?
Use when: HAS-A relationship
Example: Car HAS-A Engine

ABSTRACT CLASS?
Use when: Define contract for subclasses
Example: All subclasses MUST implement

POLYMORPHISM?
Use when: Same method, different behaviors
Example: Different animals speak differently

DECORATOR?
Use when: Add behavior to function
Example: Timing, logging, validation

================================================================================
                        COMMON ERRORS & FIXES
================================================================================

ERROR 1: AttributeError on __init__
❌ class MyClass:
    def __init__(x):  # Missing 'self'!
        x.value = 10

✅ class MyClass:
    def __init__(self):
        self.value = 10

---

ERROR 2: super() in non-child class
❌ class Parent:
    def __init__(self):
        super().__init__()  # Parent has no parent!

✅ class Child(Parent):
    def __init__(self):
        super().__init__()

---

ERROR 3: Accidentally calling parent's parent
❌ class GrandChild(Child):
    def __init__(self):
        super().__init__()  # Calls Child.__init__, then Parent.__init__

✅ class GrandChild(Child):
    def __init__(self):
        super().__init__()  # Correct!

---

ERROR 4: Modifying class variable in __init__
❌ class MyClass:
    my_list = []
    
    def __init__(self):
        self.my_list.append("value")  # Modifies CLASS list!

✅ class MyClass:
    def __init__(self):
        self.my_list = []  # Create INSTANCE list

---

ERROR 5: Forgetting pass in empty method
❌ class MyClass:
    def method():
        # SyntaxError!

✅ class MyClass:
    def method(self):
        pass

---

ERROR 6: Not implementing abstract method
❌ class MyClass(AbstractClass):
    pass  # TypeError: Can't instantiate!

✅ class MyClass(AbstractClass):
    def required_method(self):
        return "Implementation"

================================================================================
                        QUICK DECISION TREE
================================================================================

Need to store data?
  → Use CLASS

Need to group related data and functions?
  → Use CLASS

Need to reuse code?
  → Use INHERITANCE (IS-A) or COMPOSITION (HAS-A)

Two classes very similar but different?
  → Use INHERITANCE

Object contains another object?
  → Use COMPOSITION

Need to control data access?
  → Use PROPERTIES or ENCAPSULATION

Need multiple algorithms?
  → Use POLYMORPHISM or STRATEGY PATTERN

Need single instance globally?
  → Use SINGLETON PATTERN

Need to create different object types?
  → Use FACTORY PATTERN

Need to add behavior to existing objects?
  → Use DECORATOR PATTERN or COMPOSITION

Need to track changes in object?
  → Use OBSERVER PATTERN

================================================================================
                        COMMON PATTERNS QUICK REF
================================================================================

SINGLETON (only one instance):
class Singleton:
    __instance = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

---

FACTORY (create objects):
class Factory:
    @staticmethod
    def create(type_name):
        classes = {"A": ClassA, "B": ClassB}
        return classes[type_name]()

---

OBSERVER (watch for changes):
class Subject:
    def __init__(self):
        self.observers = []
    
    def attach(self, observer):
        self.observers.append(observer)
    
    def notify(self):
        for observer in self.observers:
            observer.update(self)

---

STRATEGY (choose algorithm):
class Context:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def execute(self):
        return self.strategy.do_something()

---

DECORATOR (add behavior):
def decorator(func):
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper

================================================================================
                        ACCESS MODIFIERS AT A GLANCE
================================================================================

┌──────────────┬────────┬──────────┬───────────┬──────────────┐
│ Type         │ Syntax │ Class    │ Subclass  │ Outside      │
├──────────────┼────────┼──────────┼───────────┼──────────────┤
│ Public       │ name   │   ✓      │    ✓      │      ✓       │
│ Protected    │ _name  │   ✓      │    ✓      │   ✓ (don't)  │
│ Private      │ __name │   ✓      │    ✗      │      ✗       │
└──────────────┴────────┴──────────┴───────────┴──────────────┘

================================================================================
                        METHOD TYPES AT A GLANCE
================================================================================

┌─────────────────┬──────────┬───────────┬──────────────────────┐
│ Method Type     │ Decorator│ Parameter │ When to Use          │
├─────────────────┼──────────┼───────────┼──────────────────────┤
│ Instance        │ None     │ self      │ Work with instance   │
│ Class           │ @classm  │ cls       │ Work with class      │
│ Static          │ @static  │ None      │ Utility function     │
└─────────────────┴──────────┴───────────┴──────────────────────┘

================================================================================
                        KEY DUNDER METHODS
================================================================================

__init__()          Constructor (initialize)
__del__()           Destructor (cleanup)
__str__()           String representation (print)
__repr__()          Developer representation
__len__()           Length (len())
__getitem__()       Indexing (obj[key])
__setitem__()       Assignment (obj[key] = value)
__call__()          Calling object ()
__add__()           Addition (+)
__sub__()           Subtraction (-)
__mul__()           Multiplication (*)
__truediv__()       Division (/)
__eq__()            Equality (==)
__ne__()            Not equal (!=)
__lt__()            Less than (<)
__le__()            Less than or equal (<=)
__gt__()            Greater than (>)
__ge__()            Greater than or equal (>=)
__contains__()      Membership (in)
__enter__()         Context manager (with)
__exit__()          Context manager cleanup

================================================================================
                        NAMING CONVENTIONS
================================================================================

Classes:        PascalCase      (MyClass, BankAccount)
Functions:      snake_case      (my_function, calculate_total)
Variables:      snake_case      (my_variable, account_balance)
Constants:      UPPER_CASE      (MAX_SIZE, DEFAULT_TIMEOUT)
Protected:      _leading        (_internal_method)
Private:        __double        (__private_method)
Methods:        snake_case      (get_value, set_balance)
Boolean vars:   is_/has_        (is_active, has_items)

================================================================================
                        BEST PRACTICES SUMMARY
================================================================================

✓ Use meaningful names
✓ Keep classes focused (SRP)
✓ Use encapsulation liberally  
✓ Prefer composition over inheritance
✓ Code to interfaces, not implementations
✓ Use decorators for cross-cutting concerns
✓ Follow SOLID principles
✓ Write tests for your classes
✓ Document complex methods
✓ Review others' code

✗ Don't use globals
✗ Don't create god classes
✗ Don't have deep inheritance chains
✗ Don't violate encapsulation
✗ Don't ignore type hints
✗ Don't write undocumented complex logic
✗ Don't skip testing
✗ Don't premature optimize

================================================================================
                        REMEMBER
================================================================================

1. CLARITY > Cleverness
   Write clear code, not fancy code

2. SIMPLICITY > Complexity
   Start simple, add complexity only when needed

3. REUSE > Duplication
   DRY principle: Don't Repeat Yourself

4. DESIGN > Implementation
   Think before coding

5. PRACTICE > Theory
   You learn by doing, not reading

6. REVIEW > First-draft
   Always refactor your code

7. TESTING > Hope
   Test your code thoroughly

8. DOCUMENTATION > Assumption
   Write clear docs for future you

HAPPY CODING! 🚀

Remember: Every expert was once a beginner who didn't give up!
================================================================================
"""

if __name__ == "__main__":
    print(__doc__)
