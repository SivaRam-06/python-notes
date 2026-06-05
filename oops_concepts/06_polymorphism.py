"""
================================================================================
                        POLYMORPHISM - INTERMEDIATE 3
================================================================================

CONCEPT:
  Polymorphism = "Many forms"
  Same method name, different implementations in different classes
  Objects of different types respond to same method call differently

MOTTO: "One interface, multiple implementations"

ANALOGY:
  Method "move()" means different things:
  - For Fish: move in water
  - For Bird: move through sky
  - For Car: move on road
  Each moves differently, but all understand "move()"

================================================================================
                        WHEN TO USE?
================================================================================
Use Polymorphism when:
1. Multiple classes have same method name but different behavior
2. Want to use objects interchangeably
3. Write flexible code that works with different object types
4. Create extensible systems

================================================================================
                        HOW TO USE?
================================================================================
TYPES OF POLYMORPHISM:

1. METHOD OVERRIDING (Inheritance-based)
   - Child class provides different implementation of parent's method

2. METHOD OVERLOADING (Same method, different parameters)
   - Python: Use *args, **kwargs (doesn't support true overloading)

3. DUCK TYPING
   - If it walks like a duck and quacks like a duck, treat it as a duck
   - Python specific - focus on behavior, not type

================================================================================
"""

# ================================================================================
# SECTION 1: BASIC POLYMORPHISM (METHOD OVERRIDING)
# ================================================================================

print("=" * 80)
print("SECTION 1: BASIC POLYMORPHISM - METHOD OVERRIDING")
print("=" * 80)

# PARENT CLASS
class Animal:
    """Parent class"""
    def speak(self):
        print("Animal makes a sound")


# CHILD CLASSES
class Dog(Animal):
    """Child - overrides speak()"""
    def speak(self):
        print("Dog barks: Woof! Woof!")


class Cat(Animal):
    """Child - overrides speak()"""
    def speak(self):
        print("Cat meows: Meow! Meow!")


class Cow(Animal):
    """Child - overrides speak()"""
    def speak(self):
        print("Cow moos: Moo! Moo!")


# POLYMORPHISM IN ACTION
# Same method name, different behaviors!

dog = Dog()
cat = Cat()
cow = Cow()

dog.speak()
cat.speak()
cow.speak()

print("""
KEY POINT:
- All objects have speak() method
- Each implements it differently
- We can call speak() without knowing the exact type!
""")


# ================================================================================
# SECTION 2: POLYMORPHISM WITH LOOPS
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 2: POLYMORPHISM WITH COLLECTION")
print("=" * 80)

class Shape:
    """Parent class"""
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height


# Create different shapes
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4),
    Circle(2),
    Rectangle(5, 5)
]

# POLYMORPHISM: Same method call, different results!
print("Calculating areas:")
for shape in shapes:
    # Each shape's area() behaves differently
    area = shape.area()
    shape_type = type(shape).__name__
    print(f"{shape_type}: {area:.2f}")

print("""
ADVANTAGE OF POLYMORPHISM:
- We DON'T need to check type of each shape
- We DON'T need separate if-else for each shape
- We DON'T need different method names
- Just call area() on any shape object
""")


# ================================================================================
# SECTION 3: DUCK TYPING (PYTHON SPECIFIC)
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 3: DUCK TYPING")
print("=" * 80)

# Classes don't need to inherit from same parent!
class Guitar:
    """Guitar - no parent class"""
    def play(self):
        print("Guitar: Strummm...")


class Drum:
    """Drum - different class"""
    def play(self):
        print("Drum: Boom! Boom!")


class Flute:
    """Flute - yet another class"""
    def play(self):
        print("Flute: Toot! Toot!")


def make_music(instruments):
    """
    DUCK TYPING in action!
    We don't care WHAT type - just that it can play()
    """
    for instrument in instruments:
        instrument.play()


print("Making music:")
instruments = [Guitar(), Drum(), Flute()]
make_music(instruments)

print("""
DUCK TYPING ("If it quacks like a duck..."):
- We don't check object type
- We don't require inheritance
- We just call the method we expect
- If it has the method, it works!
- If it doesn't, error happens

This is VERY Pythonic!
""")


# ================================================================================
# SECTION 4: POLYMORPHISM WITH FUNCTION PARAMETERS
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 4: POLYMORPHIC FUNCTIONS")
print("=" * 80)

class Employee:
    """Parent class"""
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_bonus(self):
        """Calculate bonus - different for each type"""
        pass


class Manager(Employee):
    def get_bonus(self):
        return self.salary * 0.20  # 20% bonus


class Developer(Employee):
    def get_bonus(self):
        return self.salary * 0.15  # 15% bonus


class Intern(Employee):
    def get_bonus(self):
        return self.salary * 0.05  # 5% bonus


def calculate_total_bonuses(employees):
    """
    POLYMORPHIC FUNCTION
    Works with any Employee type
    """
    total = 0
    for emp in employees:
        bonus = emp.get_bonus()
        print(f"{emp.name}: {bonus}")
        total += bonus
    return total


# Create employees
employees = [
    Manager("Ahmed", 100000),
    Developer("Fatima", 80000),
    Developer("Hassan", 75000),
    Intern("Zainab", 20000)
]

print("Employee Bonuses:")
total_bonus = calculate_total_bonuses(employees)
print(f"Total Bonus Payout: {total_bonus}")

print("""
POLYMORPHIC FUNCTION:
- Takes parameter of type Employee
- Works with Manager, Developer, Intern, etc.
- Each subclass's get_bonus() is called
- Function doesn't need to know specific type
""")


# ================================================================================
# SECTION 5: REAL WORLD - PAYMENT SYSTEMS
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 5: REAL WORLD - PAYMENT PROCESSING")
print("=" * 80)

class PaymentMethod:
    """Abstract concept - different payment types"""
    
    def validate(self):
        """Validate payment method"""
        pass
    
    def process_payment(self, amount):
        """Process payment"""
        pass


class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number
    
    def validate(self):
        return len(self.card_number) == 16
    
    def process_payment(self, amount):
        print(f"Processing credit card payment: {amount}")
        print(f"Card: ****{self.card_number[-4:]}")


class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email
    
    def validate(self):
        return "@" in self.email
    
    def process_payment(self, amount):
        print(f"Processing PayPal payment: {amount}")
        print(f"Account: {self.email}")


class BankTransfer(PaymentMethod):
    def __init__(self, account_number):
        self.account_number = account_number
    
    def validate(self):
        return len(self.account_number) == 10
    
    def process_payment(self, amount):
        print(f"Processing bank transfer: {amount}")
        print(f"Account: {self.account_number}")


class ShoppingCart:
    """
    Uses polymorphism to handle different payment methods
    """
    
    def __init__(self, total):
        self.total = total
    
    def checkout(self, payment_method):
        """
        POLYMORPHIC METHOD
        Works with ANY payment method
        """
        if not payment_method.validate():
            print("Invalid payment method!")
            return False
        
        print("--- Checkout ---")
        print(f"Total Amount: {self.total}")
        payment_method.process_payment(self.total)
        print("Payment successful!\n")
        return True


# Use polymorphism
cart = ShoppingCart(5000)

# Same checkout() works with different payment types!
credit_card = CreditCard("1234567890123456")
cart.checkout(credit_card)

paypal = PayPal("user@example.com")
cart.checkout(paypal)

bank = BankTransfer("1234567890")
cart.checkout(bank)

print("""
REAL WORLD BENEFIT:
- ShoppingCart.checkout() works with ANY payment method
- Add new payment type? Just create new PaymentMethod subclass
- No changes needed to ShoppingCart or checkout()
- System is extensible and maintainable!
""")


# ================================================================================
# SECTION 6: POLYMORPHISM WITH isinstance() AND type()
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 6: TYPE CHECKING WITH POLYMORPHISM")
print("=" * 80)

class Vehicle:
    pass

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

car = Car()
bike = Bike()
vehicle = Vehicle()

# isinstance() - check if object is instance (including inherited)
print(f"car is instance of Car: {isinstance(car, Car)}")
print(f"car is instance of Vehicle: {isinstance(car, Vehicle)}")
print(f"bike is instance of Vehicle: {isinstance(bike, Vehicle)}")

# type() - check exact type (not inherited)
print(f"\ntype(car) == Car: {type(car) == Car}")
print(f"type(car) == Vehicle: {type(car) == Vehicle}")

print("""
isinstance() vs type():
- isinstance(): Returns True if object is instance or subclass
- type(): Returns True only for exact type match

Best practice:
- Use isinstance() for polymorphic code
- Avoid type() unless you specifically need exact type
""")


# ================================================================================
# SECTION 9: DETAILED METHOD EXAMPLES AND PATTERNS
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 9: DETAILED METHOD EXAMPLES AND PATTERNS")
print("=" * 80)

# PATTERN 1: Polymorphic Factory Pattern
print("\n--- PATTERN 1: Polymorphic Factory ---")

class Document:
    """Base document class"""
    def __init__(self, title):
        self.title = title
    
    def render(self):
        """To be overridden"""
        pass
    
    def save(self):
        """To be overridden"""
        pass

class PDFDocument(Document):
    def render(self):
        return f"Rendering PDF: {self.title}"
    
    def save(self):
        return f"Saving PDF file: {self.title}.pdf"

class WordDocument(Document):
    def render(self):
        return f"Rendering Word: {self.title}"
    
    def save(self):
        return f"Saving Word file: {self.title}.docx"

class HTMLDocument(Document):
    def render(self):
        return f"Rendering HTML: {self.title}"
    
    def save(self):
        return f"Saving HTML file: {self.title}.html"

class DocumentFactory:
    """Polymorphic factory - creates different document types"""
    
    @staticmethod
    def create_document(doc_type, title):
        """Returns appropriate document type"""
        types = {
            "pdf": PDFDocument,
            "word": WordDocument,
            "html": HTMLDocument
        }
        
        doc_class = types.get(doc_type.lower())
        if doc_class:
            return doc_class(title)
        raise ValueError(f"Unknown document type: {doc_type}")

# Polymorphic usage
documents = []
for doc_info in [("pdf", "Report"), ("word", "Letter"), ("html", "Webpage")]:
    doc = DocumentFactory.create_document(*doc_info)
    documents.append(doc)

print("Processing documents polymorphically:")
for doc in documents:
    print(doc.render())
    print(doc.save())
    print()

# PATTERN 2: Strategy Pattern with Polymorphism
print("\n--- PATTERN 2: Strategy Pattern ---")

class SortStrategy:
    """Abstract strategy"""
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Using Bubble Sort")
        return sorted(data)  # Simplified

class QuickSort(SortStrategy):
    def sort(self, data):
        print("Using Quick Sort")
        return sorted(data)  # Simplified

class MergeSort(SortStrategy):
    def sort(self, data):
        print("Using Merge Sort")
        return sorted(data)  # Simplified

class Sorter:
    """Context that uses different strategies polymorphically"""
    
    def __init__(self, strategy):
        self.strategy = strategy
    
    def sort_data(self, data):
        return self.strategy.sort(data)

# Polymorphic usage
data = [3, 1, 4, 1, 5, 9, 2, 6]

sorters = [
    Sorter(BubbleSort()),
    Sorter(QuickSort()),
    Sorter(MergeSort())
]

for sorter in sorters:
    result = sorter.sort_data(data.copy())
    print(f"Result: {result}\n")

# PATTERN 3: Command Pattern
print("\n--- PATTERN 3: Command Pattern ---")

class Command:
    """Abstract command"""
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_off()

class Light:
    def turn_on(self):
        print("Light is ON")
    
    def turn_off(self):
        print("Light is OFF")

class RemoteControl:
    """Invoker - uses commands polymorphically"""
    
    def __init__(self):
        self.commands = []
    
    def add_command(self, command):
        self.commands.append(command)
    
    def execute_all(self):
        for cmd in self.commands:
            cmd.execute()

# Polymorphic usage
light = Light()
remote = RemoteControl()

remote.add_command(LightOnCommand(light))
remote.add_command(LightOffCommand(light))
remote.add_command(LightOnCommand(light))

remote.execute_all()

print("""
DESIGN PATTERNS WITH POLYMORPHISM:

1. FACTORY PATTERN:
   - Create objects without specifying exact class
   - Polymorphic object creation
   - Easy to add new types

2. STRATEGY PATTERN:
   - Encapsulate algorithms
   - Make them interchangeable
   - Change behavior at runtime

3. COMMAND PATTERN:
   - Encapsulate requests as objects
   - Parameterize clients with different requests
   - Support undo operations
""")

# ================================================================================
# SECTION 10: ADVANCED POLYMORPHISM TECHNIQUES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 10: ADVANCED POLYMORPHISM TECHNIQUES")
print("=" * 80)

# TECHNIQUE 1: Polymorphism with Abstract Base Classes
print("\n--- TECHNIQUE 1: ABC with Polymorphism ---")

from abc import ABC, abstractmethod

class Database(ABC):
    """Abstract database interface"""
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def query(self, sql):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Connected to MySQL"
    
    def query(self, sql):
        return f"MySQL result for: {sql}"
    
    def disconnect(self):
        return "Disconnected from MySQL"

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connected to PostgreSQL"
    
    def query(self, sql):
        return f"PostgreSQL result for: {sql}"
    
    def disconnect(self):
        return "Disconnected from PostgreSQL"

def execute_database_operations(db):
    """Polymorphic function - works with any Database"""
    print(db.connect())
    result = db.query("SELECT * FROM users")
    print(result)
    print(db.disconnect())
    print()

# Polymorphic usage
databases = [MySQLDatabase(), PostgreSQLDatabase()]

for db in databases:
    execute_database_operations(db)

# TECHNIQUE 2: Polymorphism with Mixins
print("\n--- TECHNIQUE 2: Polymorphic Mixins ---")

class LoggerMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class SerializerMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)
    
    def from_json(self, json_str):
        import json
        self.__dict__.update(json.loads(json_str))

class ValidatorMixin:
    def validate(self):
        """Polymorphic validation"""
        for attr, value in self.__dict__.items():
            if not self._validate_field(attr, value):
                return False
        return True
    
    def _validate_field(self, attr, value):
        """To be overridden by subclasses"""
        return True

class User(LoggerMixin, SerializerMixin, ValidatorMixin):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def _validate_field(self, attr, value):
        if attr == 'age' and not isinstance(value, int):
            return False
        if attr == 'email' and '@' not in value:
            return False
        return True

class Product(LoggerMixin, SerializerMixin, ValidatorMixin):
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def _validate_field(self, attr, value):
        if attr == 'price' and value < 0:
            return False
        if attr == 'stock' and value < 0:
            return False
        return True

# Polymorphic usage
user = User("Ali", "ali@example.com", 25)
product = Product("Laptop", 999.99, 10)

objects = [user, product]

for obj in objects:
    obj.log("Created")
    print(f"Valid: {obj.validate()}")
    print(f"JSON: {obj.to_json()}")
    print()

# TECHNIQUE 3: Runtime Polymorphism
print("\n--- TECHNIQUE 3: Runtime Polymorphism ---")

class NotificationService:
    """Service that can send different types of notifications"""
    
    def __init__(self, sender):
        self.sender = sender
    
    def send_notification(self, message, recipients):
        """Polymorphic method - sender determines notification type"""
        for recipient in recipients:
            self.sender.send(message, recipient)

class EmailSender:
    def send(self, message, recipient):
        print(f"Email to {recipient}: {message}")

class SMSSender:
    def send(self, message, recipient):
        print(f"SMS to {recipient}: {message}")

class PushSender:
    def send(self, message, recipient):
        print(f"Push to {recipient}: {message}")

# Runtime polymorphism - change behavior at runtime
service = NotificationService(EmailSender())
service.send_notification("Hello!", ["user1@example.com", "user2@example.com"])

service.sender = SMSSender()  # Change sender at runtime!
service.send_notification("Alert!", ["+1234567890"])

print("""
ADVANCED TECHNIQUES:

1. ABSTRACT BASE CLASSES:
   - Define contracts with @abstractmethod
   - Force implementation in subclasses
   - Enable polymorphic behavior

2. MIXINS:
   - Multiple inheritance for functionality
   - Combine different behaviors
   - Reusable across classes

3. RUNTIME POLYMORPHISM:
   - Change object behavior at runtime
   - Strategy pattern implementation
   - Flexible system design
""")

# ================================================================================
# SECTION 11: POLYMORPHISM BEST PRACTICES AND PITFALLS
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 11: BEST PRACTICES AND COMMON MISTAKES")
print("=" * 80)

print("""
✓ BEST PRACTICES:

1. CONSISTENT INTERFACES:
   - Same method names across related classes
   - Consistent parameter signatures
   - Predictable return types

2. USE DUCK TYPING:
   - Focus on behavior, not inheritance
   - Pythonic approach
   - More flexible than strict typing

3. DESIGN FOR EXTENSIBILITY:
   - Make it easy to add new polymorphic types
   - Follow Open/Closed Principle

4. DOCUMENT POLYMORPHIC METHODS:
   - Clear docstrings for abstract methods
   - Explain expected behavior

5. USE ABC FOR CRITICAL INTERFACES:
   - When you need guaranteed implementation
   - For complex systems

✗ COMMON MISTAKES:

1. INCONSISTENT METHOD SIGNATURES:
   ❌ class Dog: def speak(self, volume): pass
   ❌ class Cat: def speak(self): pass
   
   ✅ class Dog: def speak(self): pass
   ✅ class Cat: def speak(self): pass

2. TYPE CHECKING INSTEAD OF POLYMORPHISM:
   ❌ def make_sound(animal):
       if isinstance(animal, Dog):
           animal.bark()
       elif isinstance(animal, Cat):
           animal.meow()
   
   ✅ def make_sound(animal):
       animal.speak()  # Polymorphic!

3. FORGETTING TO OVERRIDE METHODS:
   ❌ class Child(Parent):
       # Forgot to implement required method
       pass
   
   ✅ class Child(Parent):
       def required_method(self):
           return "Implementation"

4. MIXING POLYMORPHISM WITH TYPE CHECKS:
   ❌ def process(obj):
       if isinstance(obj, TypeA):
           obj.method_a()
       else:
           obj.method_b()  # Still type checking!
   
   ✅ def process(obj):
       obj.process()  # Pure polymorphism

5. DEEP INHERITANCE CHAINS:
   ❌ GrandChild(Child(Parent)) - too complex
   
   ✅ Use composition or simpler inheritance
""")

# ================================================================================
# SECTION 12: PRACTICAL POLYMORPHISM EXAMPLES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 12: PRACTICAL EXAMPLES")
print("=" * 80)

# EXAMPLE 1: File Processing System
print("\n--- EXAMPLE 1: File Processing System ---")

class FileProcessor:
    """Abstract file processor"""
    def __init__(self, filename):
        self.filename = filename
    
    def process(self):
        """Template method"""
        data = self.read_file()
        processed = self.transform_data(data)
        self.write_file(processed)
    
    def read_file(self):
        """To be overridden"""
        pass
    
    def transform_data(self, data):
        """To be overridden"""
        pass
    
    def write_file(self, data):
        """To be overridden"""
        pass

class TextFileProcessor(FileProcessor):
    def read_file(self):
        return f"Reading text from {self.filename}"
    
    def transform_data(self, data):
        return data.upper()
    
    def write_file(self, data):
        print(f"Writing text to {self.filename}: {data}")

class CSVFileProcessor(FileProcessor):
    def read_file(self):
        return f"Reading CSV from {self.filename}"
    
    def transform_data(self, data):
        return data + " (processed as CSV)"
    
    def write_file(self, data):
        print(f"Writing CSV to {self.filename}: {data}")

class JSONFileProcessor(FileProcessor):
    def read_file(self):
        return f"Reading JSON from {self.filename}"
    
    def transform_data(self, data):
        return data + " (processed as JSON)"
    
    def write_file(self, data):
        print(f"Writing JSON to {self.filename}: {data}")

# Polymorphic processing
processors = [
    TextFileProcessor("data.txt"),
    CSVFileProcessor("data.csv"),
    JSONFileProcessor("data.json")
]

for processor in processors:
    processor.process()
    print()

# EXAMPLE 2: Game Character System
print("\n--- EXAMPLE 2: Game Character Abilities ---")

class Ability:
    """Abstract ability"""
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    
    def use(self, caster, target):
        """Polymorphic method"""
        pass

class Fireball(Ability):
    def use(self, caster, target):
        print(f"{caster} casts {self.name} on {target} for {self.damage} fire damage!")

class Healing(Ability):
    def use(self, caster, target):
        print(f"{caster} heals {target} for {self.damage} health!")

class Teleport(Ability):
    def use(self, caster, target):
        print(f"{caster} teleports {target} to safety!")

class Character:
    def __init__(self, name):
        self.name = name
        self.abilities = []
    
    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def use_ability(self, ability_index, target):
        if 0 <= ability_index < len(self.abilities):
            self.abilities[ability_index].use(self.name, target)

# Create characters with different abilities
wizard = Character("Merlin")
warrior = Character("Conan")

wizard.add_ability(Fireball("Fire Blast", 50))
wizard.add_ability(Healing("Heal", 30))
wizard.add_ability(Teleport("Blink", 0))

warrior.add_ability(Fireball("Sword Strike", 40))
warrior.add_ability(Healing("Bandage", 20))

characters = [wizard, warrior]

print("Battle simulation:")
for char in characters:
    print(f"\n{char.name}'s abilities:")
    for i, ability in enumerate(char.abilities):
        char.use_ability(i, "Enemy")

print("""
POLYMORPHISM IN GAMES:

1. ABILITIES:
   - Same use() method for all abilities
   - Different behavior for each ability type
   - Easy to add new abilities

2. CHARACTERS:
   - Same interface for all character types
   - Different abilities and stats
   - Flexible combat system
""")

# ================================================================================
# SUMMARY
# ================================================================================

print("\n" + "=" * 80)
print("POLYMORPHISM SUMMARY")
print("=" * 80)

print("""
WHAT YOU LEARNED:

1. BASIC POLYMORPHISM:
   - Same method name, different implementations
   - Method overriding in inheritance
   - Polymorphic collections and loops

2. DUCK TYPING:
   - Python-specific approach
   - Focus on behavior, not type
   - No inheritance required

3. POLYMORPHIC FUNCTIONS:
   - Functions that work with multiple types
   - Extensible design
   - Clean, maintainable code

4. DESIGN PATTERNS:
   - Factory Pattern for object creation
   - Strategy Pattern for algorithms
   - Command Pattern for actions

5. ADVANCED TECHNIQUES:
   - Abstract Base Classes
   - Mixins for functionality
   - Runtime polymorphism

6. BEST PRACTICES:
   - Consistent interfaces
   - Duck typing over type checking
   - Design for extensibility

KEY TAKEAWAYS:
- Polymorphism enables flexible, extensible code
- Same interface, multiple implementations
- Duck typing is very Pythonic
- Avoid type checking in polymorphic code
- Use ABC when you need guaranteed contracts

NEXT: Learn about Abstraction (file 07)
""")


# ================================================================================
# SECTION 8: ADVANTAGES OF POLYMORPHISM
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 8: ADVANTAGES AND BEST PRACTICES")
print("=" * 80)

print("""
ADVANTAGES:

1. FLEXIBILITY:
   ✓ Write code that works with multiple types
   ✓ Avoid complex if-else chains
   ✓ Add new types without changing existing code

2. EXTENSIBILITY:
   ✓ System grows easily
   ✓ New features don't break old code
   ✓ Open/Closed Principle

3. MAINTAINABILITY:
   ✓ Cleaner code
   ✓ Easier to understand
   ✓ Better organization

4. REUSABILITY:
   ✓ Write once, use with many types
   ✓ Reduce code duplication

BEST PRACTICES:

1. CONSISTENT INTERFACE:
   ✓ Same method names across related classes
   ✓ Same parameter types
   ✓ Same return types

2. USE INHERITANCE EFFECTIVELY:
   ✓ Parent class defines interface
   ✓ Children implement specific behavior
   ✓ Keep inheritance clear and logical

3. DUCK TYPING:
   ✓ Focus on behavior, not type
   ✓ Use polymorphic functions
   ✓ Pythonic approach

4. AVOID TYPE CHECKING IN LOOPS:
   ✗ WRONG - Type checking
   if isinstance(obj, Dog):
       obj.bark()
   elif isinstance(obj, Cat):
       obj.meow()
   
   ✓ RIGHT - Polymorphism
   obj.speak()  # Works for all types

EXAMPLE - WRONG vs RIGHT:

# WRONG - Too specific
def process_animals(animals):
    for animal in animals:
        if type(animal) == Dog:
            animal.bark()
        elif type(animal) == Cat:
            animal.meow()

# RIGHT - Polymorphic
def process_animals(animals):
    for animal in animals:
        animal.speak()  # Polymorphism!
""")
