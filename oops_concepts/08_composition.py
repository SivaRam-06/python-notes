"""
================================================================================
                        COMPOSITION - ADVANCED 2
================================================================================

CONCEPT:
  Composition = Building complex objects by combining simpler objects
  Relationship: "HAS-A" (Car HAS-A Engine, not "IS-A" Engine)

MOTTO: "Compose objects, don't inherit"

WHY?
  - More flexible than inheritance
  - Easier to change behavior at runtime
  - Avoids tight coupling
  - Better for real-world modeling

================================================================================
                        COMPOSITION vs INHERITANCE
================================================================================

INHERITANCE (IS-A):
  Employee → Manager (Manager IS-A Employee)
  Car → ElectricCar (ElectricCar IS-A Car)
  
COMPOSITION (HAS-A):
  Car HAS-A Engine
  Employee HAS-A Address
  Computer HAS-A Processor

================================================================================
                        WHEN TO USE?
================================================================================

USE COMPOSITION WHEN:
1. "Has-a" relationship is clearer than "is-a"
2. Want to change behavior at runtime
3. Avoiding deep inheritance hierarchies
4. Multiple different objects work together

USE INHERITANCE WHEN:
1. True "is-a" relationship
2. Sharing common interface
3. Enforcing contract through abstract classes

RULE: "Prefer composition over inheritance"

================================================================================
"""

# ================================================================================
# SECTION 1: COMPOSITION BASICS
# ================================================================================

print("=" * 80)
print("SECTION 1: BASIC COMPOSITION")
print("=" * 80)

# SIMPLE OBJECTS (Building blocks)
class Engine:
    """Simple Engine component"""
    def __init__(self, power):
        self.power = power
    
    def start(self):
        print(f"Engine started: {self.power}hp")


class Wheel:
    """Simple Wheel component"""
    def __init__(self, size):
        self.size = size
    
    def rotate(self):
        print(f"Wheel rotating: {self.size} inch")


# COMPOSITE OBJECT (Made of multiple simple objects)
class Car:
    """Car is COMPOSED of engine and wheels"""
    
    def __init__(self, name, engine_power, wheel_size):
        self.name = name
        self.engine = Engine(engine_power)  # COMPOSITION
        self.wheels = [
            Wheel(wheel_size),
            Wheel(wheel_size),
            Wheel(wheel_size),
            Wheel(wheel_size)
        ]
    
    def start(self):
        print(f"Car '{self.name}' starting")
        self.engine.start()
    
    def drive(self):
        for wheel in self.wheels:
            wheel.rotate()


# Use composition
car = Car("Toyota", 150, 18)
car.start()
car.drive()

print("""
COMPOSITION STRUCTURE:
Car
├── Engine (power: 150)
└── Wheels (4x)

Car CONTAINS these objects
Car USES these objects
Car HAS-A Engine, HAS-A Wheel
""")


# ================================================================================
# SECTION 2: COMPOSITION vs INHERITANCE
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 2: COMPOSITION vs INHERITANCE")
print("=" * 80)

print("\n--- APPROACH 1: INHERITANCE (Less Flexible) ---")

class Animal:
    def eat(self):
        print("Animal eating")


class Bird(Animal):
    def fly(self):
        print("Bird flying")


class Airplane(Bird):  # PROBLEM: Airplane IS NOT REALLY A Bird!
    def fly(self):
        print("Airplane flying")


# This works but is wrong - Airplane is not a Bird!
plane = Airplane()
plane.fly()

print("""
PROBLEM WITH INHERITANCE HERE:
- Airplane inherits from Bird
- But Airplane IS NOT A Bird!
- Just happens to fly
- Confusing and wrong design
""")

print("\n--- APPROACH 2: COMPOSITION (Better) ---")

class Wing:
    def generate_lift(self):
        print("Wings generating lift")


class Propeller:
    def rotate(self):
        print("Propeller rotating")


class PlaneBetter:
    """Airplane is composed of parts"""
    def __init__(self):
        self.wings = [Wing(), Wing()]
        self.propeller = Propeller()
    
    def fly(self):
        for wing in self.wings:
            wing.generate_lift()
        self.propeller.rotate()


plane_better = PlaneBetter()
plane_better.fly()

print("""
COMPOSITION IS CLEARER:
- Airplane HAS-A Wing (correct!)
- Airplane HAS-A Propeller (correct!)
- No confusing inheritance
- More realistic model
- More flexible design
""")


# ================================================================================
# SECTION 3: RUNTIME BEHAVIOR CHANGES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 3: CHANGING BEHAVIOR AT RUNTIME")
print("=" * 80)

print("With INHERITANCE - hard to change:")

class Vehicle:
    def __init__(self):
        self.speed = 100


class Car_Inherits(Vehicle):
    pass


# Can't change parent class at runtime!


print("\nWith COMPOSITION - easy to change:")

class Engine_V1:
    def power(self):
        return 100


class Engine_V2:
    def power(self):
        return 200


class Car_Composed:
    """Engine can be swapped!"""
    def __init__(self, engine):
        self.engine = engine
    
    def get_power(self):
        return self.engine.power()


car1 = Car_Composed(Engine_V1())
print(f"Car1 power: {car1.get_power()}hp")

car2 = Car_Composed(Engine_V2())
print(f"Car2 power: {car2.get_power()}hp")

# Can even change at runtime!
car1.engine = Engine_V2()
print(f"Car1 power after upgrade: {car1.get_power()}hp")

print("""
COMPOSITION ADVANTAGE:
- Can swap components easily
- Can change behavior at runtime
- More flexible and adaptable
""")


# ================================================================================
# SECTION 4: REAL WORLD - COMPUTER
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 4: REAL WORLD - COMPUTER COMPOSITION")
print("=" * 80)

class Processor:
    def __init__(self, model, cores):
        self.model = model
        self.cores = cores
    
    def calculate(self):
        print(f"Processing with {self.cores} cores")


class RAM:
    def __init__(self, capacity):
        self.capacity = capacity
    
    def store(self):
        print(f"Storing data in {self.capacity}GB RAM")


class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
    
    def save_file(self, filename):
        print(f"Saving {filename} to {self.capacity}GB storage")


class Computer:
    """Computer is composed of processor, RAM, storage"""
    
    def __init__(self, processor, ram, storage):
        self.processor = processor
        self.ram = ram
        self.storage = storage
    
    def run_program(self, program_name):
        print(f"\n--- Running {program_name} ---")
        self.processor.calculate()
        self.ram.store()
    
    def save_project(self, filename):
        self.storage.save_file(filename)
    
    def display_specs(self):
        print(f"\nComputer Specs:")
        print(f"Processor: {self.processor.model} ({self.processor.cores} cores)")
        print(f"RAM: {self.ram.capacity}GB")
        print(f"Storage: {self.storage.capacity}GB")


# Build complex computer from simple components
gaming_pc = Computer(
    Processor("Intel i9", 12),
    RAM(64),
    Storage(2000)
)

gaming_pc.display_specs()
gaming_pc.run_program("Game Engine")
gaming_pc.save_project("game_project.exe")

print("\n" + "="*50)

office_pc = Computer(
    Processor("AMD Ryzen 5", 6),
    RAM(16),
    Storage(512)
)

office_pc.display_specs()
office_pc.run_program("Office Suite")


# ================================================================================
# SECTION 5: REAL WORLD - RESTAURANT
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 5: REAL WORLD - RESTAURANT ORDER SYSTEM")
print("=" * 80)

class MenuItem:
    """Individual menu item"""
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def display(self):
        return f"{self.name}: ${self.price}"


class Address:
    """Delivery address"""
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code


class Customer:
    """Customer with address"""
    def __init__(self, name, address):  # COMPOSITION
        self.name = name
        self.address = address


class Order:
    """Order composed of customer, items, and delivery address"""
    
    def __init__(self, customer):
        self.customer = customer  # Has-a Customer
        self.items = []           # Will compose MenuItems
        self.total = 0
    
    def add_item(self, item):
        """Add menu item to order"""
        self.items.append(item)
        self.total += item.price
    
    def display_order(self):
        print(f"\n--- Order for {self.customer.name} ---")
        print("Items ordered:")
        for item in self.items:
            print(f"  - {item.display()}")
        print(f"Delivery to: {self.customer.address.street}, {self.customer.address.city}")
        print(f"Total: ${self.total}")


# Build order from components
address = Address("123 Main St", "New York", "10001")
customer = Customer("Ahmed", address)
order = Order(customer)

order.add_item(MenuItem("Pizza", 250))
order.add_item(MenuItem("Coke", 50))
order.add_item(MenuItem("Dessert", 100))

order.display_order()

print("""
COMPOSITION STRUCTURE:
Order
├── Customer
│   └── Address
└── Items (List of MenuItem)

Each component is reusable and independent!
""")


# ================================================================================
# SECTION 6: DEPENDENCY INJECTION
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 6: DEPENDENCY INJECTION (ADVANCED)")
print("=" * 80)

print("""
DEPENDENCY INJECTION:
- Pass dependencies to constructor
- Object receives what it needs
- More flexible and testable
- Part of composition pattern
""")

class Logger:
    def log(self, message):
        print(f"LOG: {message}")


class FileLogger(Logger):
    def log(self, message):
        print(f"FILE LOG: {message}")


class Application:
    """Application receives logger as dependency"""
    def __init__(self, logger):
        self.logger = logger  # INJECTED dependency
    
    def run(self):
        self.logger.log("Application started")
        self.logger.log("Processing data")
        self.logger.log("Application finished")


# Can inject different loggers!
app1 = Application(Logger())
app1.run()

print()

app2 = Application(FileLogger())
app2.run()

print("""
DEPENDENCY INJECTION BENEFITS:
- Easy to swap implementations
- Easy to test (inject mock objects)
- Loose coupling
- More flexible code
""")


# ================================================================================
# SECTION 7: BEST PRACTICES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 7: COMPOSITION BEST PRACTICES")
print("=" * 80)

print("""
BEST PRACTICES:

1. USE COMPOSITION WHEN:
   ✓ "Has-a" relationship is natural
   ✓ Object contains other objects
   ✓ Want runtime flexibility
   ✓ Avoiding complex inheritance

2. DEPENDENCY INJECTION:
   ✓ Pass dependencies to constructor
   ✓ Don't create dependencies inside
   ✓ Makes code testable and flexible

3. KEEP COMPONENTS FOCUSED:
   ✓ Each component has single responsibility
   ✓ Components are reusable
   ✓ Easy to test individually

4. AVOID:
   ✗ Deep composition chains
   ✗ Circular dependencies
   ✗ Too many composed objects

COMPOSITION OVER INHERITANCE RULE:
- When in doubt, use composition
- Prefer flexibility over hierarchy
- More maintainable long-term

EXAMPLE - GOOD DESIGN:

class Engine:
    pass

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition

EXAMPLE - PROBLEMATIC:

class Vehicle:
    pass

class Car(Vehicle):
    pass

class ElectricCar(Car):
    pass

class SolarCar(ElectricCar):  # Too deep!
    pass
""")


# ================================================================================
# SECTION 8: COMPARISON TABLE
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 8: INHERITANCE vs COMPOSITION")
print("=" * 80)

print("""
┌─────────────────┬──────────────────────┬──────────────────────┐
│   Aspect        │   Inheritance        │    Composition       │
├─────────────────┼──────────────────────┼──────────────────────┤
│ Relationship    │ IS-A (Dog is Animal) │ HAS-A (Car has Engine)
│ Flexibility     │ Hard to change       │ Easy to change       │
│ Runtime change  │ Not possible         │ Possible             │
│ Code reuse      │ Through hierarchy    │ Through objects      │
│ Coupling        │ Tight                │ Loose                │
│ Testing         │ Hard to mock         │ Easy to inject       │
│ Depth           │ Can get deep         │ Usually shallow      │
│ Real-world fit  │ Sometimes wrong      │ Usually more natural │
└─────────────────┴──────────────────────┴──────────────────────┘

WHEN TO USE EACH:

USE INHERITANCE:
- True IS-A relationship
- Creating type hierarchy
- Template Method pattern
- Shared implementation

USE COMPOSITION:
- HAS-A relationship
- Need runtime flexibility
- Multiple different types involved
- Want to avoid deep hierarchies
- Making testable code

GOLDEN RULE:
Composition > Inheritance
Default to composition, use inheritance only when IS-A is truly natural
""")
