"""
================================================================================
        METHOD OVERLOADING AND OVERRIDING - ADVANCED 3
================================================================================

CONCEPTS:
  OVERRIDING  - Child provides different implementation of parent's method
  OVERLOADING - Same method name, different parameters (Python doesn't support)
                Alternative: Use *args, **kwargs or default parameters

================================================================================
                        WHEN TO USE?
================================================================================

USE OVERRIDING WHEN:
  - Child class needs different behavior for parent method
  - Customizing inherited functionality
  - Polymorphism requirement

USE OVERLOADING WHEN:
  - Need same method name with different parameters
  - Python alternative: Use default parameters or *args

================================================================================
"""

# ================================================================================
# SECTION 1: METHOD OVERRIDING (Inheritance-based)
# ================================================================================

print("=" * 80)
print("SECTION 1: METHOD OVERRIDING")
print("=" * 80)

class Vehicle:
    """Parent class"""
    
    def start(self):
        print("Vehicle starting...")
    
    def sound(self):
        print("Generic vehicle sound")


class Car(Vehicle):
    """Child - OVERRIDES methods"""
    
    def start(self):
        """Override parent method"""
        print("Car starting... Vroooom!")
    
    def sound(self):
        """Override parent method"""
        print("Car sound: Honk! Honk!")


class Bike(Vehicle):
    """Another child - OVERRIDES methods"""
    
    def start(self):
        print("Bike starting... Kachaka!")
    
    def sound(self):
        print("Bike sound: Ahem! Ahem!")


# Demonstrate overriding
vehicle = Vehicle()
vehicle.start()
vehicle.sound()

print()
car = Car()
car.start()
car.sound()

print()
bike = Bike()
bike.start()
bike.sound()

print("""
METHOD OVERRIDING:
- Parent: Defines general behavior
- Child: Provides specific behavior
- Same method name, different implementation
- Called polymorphism
""")


# ================================================================================
# SECTION 2: CALLING PARENT METHOD USING super()
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 2: REUSING PARENT METHOD WITH super()")
print("=" * 80)

class Animal:
    def eat(self):
        print("Animal eating food")


class Dog(Animal):
    def eat(self):
        """Override but also call parent"""
        super().eat()  # Call parent method
        print("Dog eating dog food from bowl")


dog = Dog()
dog.eat()

print("""
super() KEYWORD:
- Calls parent class's method
- Useful for extending (not replacing) parent behavior
- Avoids code duplication
""")


# ================================================================================
# SECTION 3: PYTHON DOESN'T SUPPORT TRUE METHOD OVERLOADING
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 3: METHOD OVERLOADING (Python Alternative)")
print("=" * 80)

print("""
PYTHON LIMITATION:
Python doesn't support true method overloading
because Python uses dynamic typing

In Java/C++:
void add(int a, int b)     // Different from:
void add(int a, int b, int c)

Python:
def add(a, b):
def add(a, b, c):  # This REPLACES the previous one!

Only the LAST definition is kept!
""")

# WRONG WAY - doesn't work as intended
class Calculator_Wrong:
    """This won't work as expected"""
    
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):
        return a + b + c  # This replaces the previous method!


calc = Calculator_Wrong()
# Can only call with 3 parameters now!
# calc.add(1, 2)  # ERROR!
result = calc.add(1, 2, 3)
print(f"WRONG: {result}")


# SOLUTION 1: DEFAULT PARAMETERS
print("\n--- SOLUTION 1: DEFAULT PARAMETERS ---")

class Calculator_Default:
    """Using default parameters"""
    
    def add(self, a, b, c=0):
        """If c is not provided, it defaults to 0"""
        return a + b + c


calc = Calculator_Default()
print(f"add(2, 3) = {calc.add(2, 3)}")
print(f"add(2, 3, 4) = {calc.add(2, 3, 4)}")


# SOLUTION 2: VARIABLE LENGTH ARGUMENTS (*args)
print("\n--- SOLUTION 2: *args (FLEXIBLE) ---")

class Calculator_Args:
    """Using *args for variable number of arguments"""
    
    def add(self, *args):
        """Accepts any number of arguments"""
        return sum(args)


calc = Calculator_Args()
print(f"add(5) = {calc.add(5)}")
print(f"add(5, 10) = {calc.add(5, 10)}")
print(f"add(5, 10, 15) = {calc.add(5, 10, 15)}")
print(f"add(5, 10, 15, 20) = {calc.add(5, 10, 15, 20)}")


# SOLUTION 3: KEYWORD ARGUMENTS (**kwargs)
print("\n--- SOLUTION 3: **kwargs (NAMED ARGUMENTS) ---")

class Database:
    """Using **kwargs for optional named arguments"""
    
    def query(self, table, **filters):
        """table is required, filters are optional"""
        query_str = f"SELECT * FROM {table}"
        
        if filters:
            conditions = [f"{k} = {v}" for k, v in filters.items()]
            query_str += " WHERE " + " AND ".join(conditions)
        
        return query_str


db = Database()
print(db.query("users"))
print(db.query("users", age=25))
print(db.query("users", age=25, city="NYC"))


# SOLUTION 4: TYPE CHECKING (ADVANCED)
print("\n--- SOLUTION 4: TYPE CHECKING ---")

class Printer:
    """Using isinstance to handle different types"""
    
    def print_content(self, content):
        """Handle different input types"""
        if isinstance(content, list):
            for item in content:
                print(f"  - {item}")
        elif isinstance(content, dict):
            for key, value in content.items():
                print(f"  {key}: {value}")
        elif isinstance(content, str):
            print(f"  {content}")
        else:
            print(f"  {content}")


printer = Printer()

print("List:")
printer.print_content(["apple", "banana", "orange"])

print("\nDict:")
printer.print_content({"name": "Ali", "age": 25})

print("\nString:")
printer.print_content("Hello World")


# ================================================================================
# SECTION 4: REAL WORLD - PAYMENT SYSTEM
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 4: REAL WORLD - PAYMENT SYSTEM")
print("=" * 80)

class PaymentMethod:
    """Base payment class"""
    
    def __init__(self, amount):
        self.amount = amount
    
    def validate(self):
        """Default validation"""
        return self.amount > 0
    
    def process(self):
        """Default process"""
        print(f"Processing generic payment: {self.amount}")


class CreditCard(PaymentMethod):
    """Override process method"""
    
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number
    
    def validate(self):
        """Custom validation"""
        if not super().validate():
            return False
        return len(self.card_number) == 16
    
    def process(self):
        """Override with specific implementation"""
        if self.validate():
            print(f"Processing credit card payment: {self.amount}")
            print(f"Card: ****{self.card_number[-4:]}")
        else:
            print("Invalid credit card!")


class UPI(PaymentMethod):
    """Override process method"""
    
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id
    
    def validate(self):
        """Custom validation"""
        if not super().validate():
            return False
        return "@" in self.upi_id
    
    def process(self):
        """Override with specific implementation"""
        if self.validate():
            print(f"Processing UPI payment: {self.amount}")
            print(f"UPI: {self.upi_id}")
        else:
            print("Invalid UPI ID!")


# Test different payment methods
print("--- Credit Card ---")
card = CreditCard(5000, "1234567890123456")
card.process()

print("\n--- UPI ---")
upi = UPI(3000, "user@paytm")
upi.process()

print("\n--- Invalid UPI ---")
upi_bad = UPI(2000, "invalid-upi")
upi_bad.process()


# ================================================================================
# SECTION 6: ADVANCED METHOD OVERRIDING TECHNIQUES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 6: ADVANCED METHOD OVERRIDING TECHNIQUES")
print("=" * 80)

# TECHNIQUE 1: Partial Overriding with super()
print("\n--- TECHNIQUE 1: Partial Overriding ---")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_info(self):
        return f"Employee: {self.name}, Salary: {self.salary}"
    
    def calculate_bonus(self):
        return self.salary * 0.1

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def get_info(self):
        # Extend parent's method
        parent_info = super().get_info()
        return f"{parent_info}, Department: {self.department}"
    
    def calculate_bonus(self):
        # Extend parent's calculation
        base_bonus = super().calculate_bonus()
        return base_bonus + (self.salary * 0.1)  # Extra 10%

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    
    def get_info(self):
        parent_info = super().get_info()
        return f"{parent_info}, Language: {self.language}"
    
    def calculate_bonus(self):
        # Different calculation for developers
        return self.salary * 0.15

# Test partial overriding
manager = Manager("Ahmed", 80000, "IT")
developer = Developer("Fatima", 70000, "Python")

print("Manager:")
print(manager.get_info())
print(f"Bonus: {manager.calculate_bonus()}")

print("\nDeveloper:")
print(developer.get_info())
print(f"Bonus: {developer.calculate_bonus()}")

# TECHNIQUE 2: Multiple Inheritance with Method Resolution Order
print("\n--- TECHNIQUE 2: Multiple Inheritance MRO ---")

class Flyable:
    def move(self):
        return "Flying through the air"

class Swimmable:
    def move(self):
        return "Swimming in water"

class Duck(Flyable, Swimmable):
    def move(self):
        # Duck can do both!
        fly = super().move()  # Calls Flyable.move()
        return f"Duck: {fly} and swimming too!"

duck = Duck()
print(f"Duck movement: {duck.move()}")
print(f"MRO: {Duck.__mro__}")

# TECHNIQUE 3: Abstract Method Overriding
print("\n--- TECHNIQUE 3: Abstract Method Overriding ---")

from abc import ABC, abstractmethod

class Database(ABC):
    def __init__(self, connection_string):
        self.connection_string = connection_string
    
    @abstractmethod
    def connect(self):
        """Must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def execute_query(self, query):
        """Must be implemented by subclasses"""
        pass
    
    def log_operation(self, operation):
        """Common method - can be used as-is or overridden"""
        print(f"[{self.__class__.__name__}] {operation}")

class MySQLDatabase(Database):
    def connect(self):
        return f"MySQL connected to {self.connection_string}"
    
    def execute_query(self, query):
        result = f"MySQL executed: {query}"
        self.log_operation("Query executed")
        return result

class PostgreSQLDatabase(Database):
    def connect(self):
        return f"PostgreSQL connected to {self.connection_string}"
    
    def execute_query(self, query):
        result = f"PostgreSQL executed: {query}"
        self.log_operation("Query executed")
        return result
    
    def log_operation(self, operation):
        # Override logging for PostgreSQL
        print(f"[POSTGRES] {operation} - Advanced logging")

# Test abstract overriding
mysql = MySQLDatabase("localhost:3306")
postgres = PostgreSQLDatabase("localhost:5432")

print("MySQL:")
print(mysql.connect())
print(mysql.execute_query("SELECT * FROM users"))

print("\nPostgreSQL:")
print(postgres.connect())
print(postgres.execute_query("SELECT * FROM users"))

print("""
ADVANCED OVERRIDING TECHNIQUES:

1. PARTIAL OVERRIDING:
   - Call super() to get parent behavior
   - Add or modify the result
   - Maintain parent functionality

2. MULTIPLE INHERITANCE:
   - Check MRO with __mro__
   - Use super() to follow resolution order
   - Avoid diamond problem

3. ABSTRACT METHODS:
   - Must be implemented by subclasses
   - Use @abstractmethod decorator
   - Define contracts for subclasses
""")

# ================================================================================
# SECTION 7: ADVANCED PYTHON OVERLOADING ALTERNATIVES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 7: ADVANCED PYTHON OVERLOADING ALTERNATIVES")
print("=" * 80)

# ALTERNATIVE 1: Using functools.singledispatch
print("\n--- ALTERNATIVE 1: singledispatch (FUNCTION OVERLOADING) ---")

from functools import singledispatch

@singledispatch
def process_data(data):
    """Base function for any type"""
    return f"Processing generic data: {data}"

@process_data.register
def _(data: int):
    """Handle integers"""
    return f"Processing integer: {data * 2}"

@process_data.register
def _(data: str):
    """Handle strings"""
    return f"Processing string: {data.upper()}"

@process_data.register
def _(data: list):
    """Handle lists"""
    return f"Processing list with {len(data)} items"

print("singledispatch examples:")
print(process_data(42))        # int
print(process_data("hello"))   # str
print(process_data([1, 2, 3])) # list
print(process_data(3.14))      # generic

# ALTERNATIVE 2: Method overloading with decorators
print("\n--- ALTERNATIVE 2: Custom Overloading Decorator ---")

def overload(func):
    """Custom overloading decorator"""
    registry = {}
    
    def dispatcher(*args, **kwargs):
        # Create signature based on argument types
        sig = tuple(type(arg).__name__ for arg in args)
        
        if sig in registry:
            return registry[sig](*args, **kwargs)
        else:
            # Try to find compatible signature
            for reg_sig, reg_func in registry.items():
                if len(reg_sig) == len(sig):
                    return reg_func(*args, **kwargs)
            raise TypeError(f"No matching overload for {sig}")
    
    def register(signature):
        def decorator(impl):
            registry[signature] = impl
            return impl
        return decorator
    
    dispatcher.register = register
    return dispatcher

@overload
def calculate():
    pass

@calculate.register(("int", "int"))
def _(a, b):
    return a + b

@calculate.register(("str", "str"))
def _(a, b):
    return a + b

@calculate.register(("list", "list"))
def _(a, b):
    return a + b

print("Custom overloading examples:")
print(f"Int: {calculate(5, 3)}")
print(f"Str: {calculate('Hello', ' World')}")
print(f"List: {calculate([1, 2], [3, 4])}")

# ALTERNATIVE 3: Class-based overloading
print("\n--- ALTERNATIVE 3: Class-based Overloading ---")

class Calculator:
    """Calculator with method overloading simulation"""
    
    def __init__(self):
        self._methods = {}
    
    def add_method(self, types, method):
        """Register a method for specific types"""
        self._methods[types] = method
    
    def add(self, *args):
        """Dispatch to appropriate method"""
        types = tuple(type(arg).__name__ for arg in args)
        
        if types in self._methods:
            return self._methods[types](*args)
        else:
            raise TypeError(f"No method for types: {types}")

# Create calculator and add methods
calc = Calculator()

def add_ints(a, b):
    return a + b

def add_strings(a, b):
    return a + b

def add_lists(a, b):
    return a + b

def add_three_nums(a, b, c):
    return a + b + c

calc.add_method(("int", "int"), add_ints)
calc.add_method(("str", "str"), add_strings)
calc.add_method(("list", "list"), add_lists)
calc.add_method(("int", "int", "int"), add_three_nums)

print("Class-based overloading:")
print(f"Ints: {calc.add(5, 3)}")
print(f"Strings: {calc.add('Hello', ' World')}")
print(f"Lists: {calc.add([1, 2], [3, 4])}")
print(f"Three numbers: {calc.add(1, 2, 3)}")

print("""
ADVANCED OVERLOADING ALTERNATIVES:

1. singledispatch:
   - Function-based overloading
   - Register different implementations
   - Type-based dispatch

2. Custom Decorator:
   - Create your own overloading system
   - Flexible signature matching
   - Full control over dispatch

3. Class-based:
   - Method registry approach
   - Explicit type registration
   - Clear and maintainable
""")

# ================================================================================
# SECTION 8: PRACTICAL EXAMPLES AND PATTERNS
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 8: PRACTICAL EXAMPLES AND PATTERNS")
print("=" * 80)

# EXAMPLE 1: HTTP Request Handler
print("\n--- EXAMPLE 1: HTTP Request Handler ---")

class HTTPHandler:
    def __init__(self):
        self.routes = {}
    
    def route(self, path, methods=None):
        """Decorator to register routes"""
        if methods is None:
            methods = ['GET']
        
        def decorator(func):
            for method in methods:
                key = (method, path)
                self.routes[key] = func
            return func
        return decorator
    
    def handle_request(self, method, path, *args, **kwargs):
        """Handle HTTP request - polymorphic dispatch"""
        key = (method, path)
        if key in self.routes:
            return self.routes[key](*args, **kwargs)
        return "404 Not Found"

# Create handler
handler = HTTPHandler()

@handler.route('/users')
def get_users():
    return "List of users"

@handler.route('/users', methods=['POST'])
def create_user():
    return "User created"

@handler.route('/users/<id>')
def get_user(user_id):
    return f"User {user_id}"

# Test polymorphic routing
print("HTTP Routing:")
print(f"GET /users: {handler.handle_request('GET', '/users')}")
print(f"POST /users: {handler.handle_request('POST', '/users')}")
print(f"GET /users/123: {handler.handle_request('GET', '/users/<id>', '123')}")

# EXAMPLE 2: Game Character Abilities
print("\n--- EXAMPLE 2: Game Character Abilities ---")

class Ability:
    """Base ability class"""
    def __init__(self, name, cooldown=0):
        self.name = name
        self.cooldown = cooldown
    
    def use(self, caster, target):
        """Base use method"""
        print(f"{caster} uses {self.name}")
        return 0

class DamageAbility(Ability):
    def __init__(self, name, damage, cooldown=0):
        super().__init__(name, cooldown)
        self.damage = damage
    
    def use(self, caster, target):
        super().use(caster, target)
        print(f"Deals {self.damage} damage to {target}")
        return self.damage

class HealAbility(Ability):
    def __init__(self, name, heal_amount, cooldown=0):
        super().__init__(name, cooldown)
        self.heal_amount = heal_amount
    
    def use(self, caster, target):
        super().use(caster, target)
        print(f"Heals {target} for {self.heal_amount} HP")
        return self.heal_amount

class BuffAbility(Ability):
    def __init__(self, name, buff_type, duration, cooldown=0):
        super().__init__(name, cooldown)
        self.buff_type = buff_type
        self.duration = duration
    
    def use(self, caster, target):
        super().use(caster, target)
        print(f"Applies {self.buff_type} buff to {target} for {self.duration} turns")
        return self.duration

class Character:
    def __init__(self, name):
        self.name = name
        self.abilities = []
    
    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def use_ability(self, index, target):
        if 0 <= index < len(self.abilities):
            return self.abilities[index].use(self.name, target)

# Create characters
warrior = Character("Conan")
mage = Character("Merlin")

warrior.add_ability(DamageAbility("Sword Strike", 50))
warrior.add_ability(DamageAbility("Power Attack", 80, 2))

mage.add_ability(DamageAbility("Fireball", 60, 1))
mage.add_ability(HealAbility("Heal", 40, 3))
mage.add_ability(BuffAbility("Haste", "speed", 3, 4))

print("Battle:")
warrior.use_ability(0, "Goblin")
mage.use_ability(0, "Goblin")
mage.use_ability(1, "Conan")

print("""
PRACTICAL PATTERNS:

1. HTTP HANDLER:
   - Route registration with decorators
   - Polymorphic request handling
   - Method-based dispatch

2. GAME ABILITIES:
   - Base Ability class with use() method
   - Different ability types override use()
   - Polymorphic ability system
""")

# ================================================================================
# SECTION 9: BEST PRACTICES AND COMMON MISTAKES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 9: BEST PRACTICES AND COMMON MISTAKES")
print("=" * 80)

print("""
✓ BEST PRACTICES:

1. USE super() FOR PARTIAL OVERRIDING:
   - Call parent method when extending
   - Maintain parent functionality
   - Avoid code duplication

2. CHECK MRO FOR MULTIPLE INHERITANCE:
   - Always check __mro__ 
   - Understand resolution order
   - Avoid diamond problem issues

3. USE MEANINGFUL METHOD NAMES:
   - Override with same name and purpose
   - Don't change method semantics
   - Keep interface consistent

4. DOCUMENT OVERRIDDEN METHODS:
   - Explain how it differs from parent
   - Document parameters and return values
   - Note any side effects

5. USE ABC FOR CRITICAL OVERRIDES:
   - When method must be implemented
   - For interface contracts
   - When polymorphism is required

✗ COMMON MISTAKES:

1. FORGETTING super().__init__():
   ❌ class Child(Parent):
       def __init__(self, param):
           self.child_attr = param  # Parent not initialized!
   
   ✅ class Child(Parent):
       def __init__(self, param):
           super().__init__()
           self.child_attr = param

2. OVERRIDING WITHOUT EXTENDING:
   ❌ class Child(Parent):
       def method(self):
           # Completely ignores parent
           pass
   
   ✅ class Child(Parent):
       def method(self):
           super().method()  # Use parent behavior
           # Add child behavior

3. CHANGING METHOD SIGNATURE:
   ❌ class Parent:
       def method(self, a, b): pass
   class Child(Parent):
       def method(self, a): pass  # Different signature!
   
   ✅ class Child(Parent):
       def method(self, a, b=None):  # Compatible signature
           pass

4. IGNORING MRO IN MULTIPLE INHERITANCE:
   ❌ class C(A, B):
       def method(self):
           A.method(self)  # Hardcoded call!
   
   ✅ class C(A, B):
       def method(self):
           super().method()  # Follows MRO

5. NOT IMPLEMENTING ABSTRACT METHODS:
   ❌ class Child(AbstractParent):
       pass  # TypeError at runtime!
   
   ✅ class Child(AbstractParent):
       def required_method(self):
           return "Implementation"
""")

# ================================================================================
# SUMMARY
# ================================================================================

print("\n" + "=" * 80)
print("METHOD OVERLOADING AND OVERRIDING SUMMARY")
print("=" * 80)

print("""
WHAT YOU LEARNED:

1. METHOD OVERRIDING:
   - Child provides different implementation
   - Same method name, different behavior
   - Use super() to call parent methods

2. PYTHON OVERLOADING LIMITATIONS:
   - No true method overloading
   - Last definition wins
   - Use alternatives instead

3. OVERLOADING ALTERNATIVES:
   - Default parameters (c=0)
   - *args for variable arguments
   - **kwargs for named arguments
   - Type checking with isinstance()
   - singledispatch decorator
   - Custom overloading systems

4. ADVANCED TECHNIQUES:
   - Partial overriding with super()
   - Multiple inheritance with MRO
   - Abstract method overriding
   - Cooperative inheritance

5. PRACTICAL PATTERNS:
   - HTTP request routing
   - Game ability systems
   - Polymorphic dispatch

KEY TAKEAWAYS:
- Overriding enables polymorphism
- Python doesn't support true overloading
- Use super() for cooperative inheritance
- Check MRO for multiple inheritance
- Choose appropriate overloading alternative

NEXT: Learn about Operator Overloading (file 10)
""")
# - Easy to add new shapes!
""")


# ================================================================================
# SECTION 6: BEST PRACTICES
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 6: BEST PRACTICES")
print("=" * 80)

"""
"""
FOR METHOD OVERRIDING:

1. WHEN TO OVERRIDE:
   ✓ Provide specific behavior for subclass
   ✓ Specialize parent's method
   ✓ Implement abstract method from parent

2. KEEP CONSISTENT:
   ✓ Same method name and purpose
   ✓ Similar parameter types
   ✓ Same return type if possible

3. DOCUMENT CHANGES:
   ✓ Write docstring explaining override
   ✓ Explain why behavior is different

4. USE super() WHEN:
   ✓ Want to keep parent behavior AND add more
   ✓ Want to initialize parent class
   ✓ Avoid code duplication

FOR METHOD OVERLOADING WORKAROUNDS:

1. DEFAULT PARAMETERS:
   def method(self, a, b, c=0):
   - Simple and clear
   - Use for few variations

2. *args for VARIABLE arguments:
   def method(self, *args):
   - Flexible
   - Good for "any number of arguments"

3. **kwargs for OPTIONAL named arguments:
   def method(self, **kwargs):
   - Flexible
   - Good for many optional parameters

4. COMBINATION - MIX AND MATCH:
   def method(self, required, *args, **kwargs):
   - Most flexible
   - Can handle almost any call

EXAMPLE - GOOD OVERRIDING:

class Parent:
    def process(self, data):
        # General processing
        return data.upper()

class Child(Parent):
    def process(self, data):
        # Specialized processing
        # First call parent
        result = super().process(data)
        # Then add child-specific behavior
        return result + "!"

EXAMPLE - GOOD OVERLOADING WORKAROUND:

class FileHandler:
    def read(self, filename, encoding='utf-8', max_lines=None):
        # Read with optional parameters
        pass
"""
