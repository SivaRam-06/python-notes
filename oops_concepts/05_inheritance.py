"""
================================================================================
                        INHERITANCE - INTERMEDIATE 2
================================================================================

CONCEPT:
  Inheritance = Creating new classes from existing classes
  New class inherits attributes and methods from parent class

MOTTO: "Reuse code, extend functionality"

ANALOGY:
  Parent class = General template (Animal)
  Child class = Specific variant (Dog, Cat, Bird)
  Child gets features from parent + adds its own

================================================================================
                        WHEN TO USE?
================================================================================
Use Inheritance when:
1. You have common code used by multiple classes
2. You want to create specialized versions of a class
3. You have an IS-A relationship (Dog IS-A Animal)
4. You want to reuse and extend functionality

================================================================================
                        HOW TO USE?
================================================================================
SYNTAX:

class ParentClass:
    def __init__(self, param1):
        self.param1 = param1
    
    def method1(self):
        pass

class ChildClass(ParentClass):  # Inherits from ParentClass
    def __init__(self, param1, param2):
        super().__init__(param1)         # Call parent's __init__
        self.param2 = param2
    
    def method2(self):                   # Child's own method
        pass

================================================================================
"""

# ================================================================================
# SECTION 1: BASIC INHERITANCE
# ================================================================================

print("=" * 80)
print("SECTION 1: BASIC INHERITANCE CONCEPT")
print("=" * 80)

# PARENT CLASS
class Animal:
    """Parent class with common attributes and methods"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
    def eat(self):
        print(f"{self.name} is eating...")
    
    def sleep(self):
        print(f"{self.name} is sleeping...")


# CHILD CLASS 1
class Dog(Animal):
    """Child class inherits from Animal"""
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call parent's __init__
        self.breed = breed           # Dog-specific attribute
    
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")


# CHILD CLASS 2
class Cat(Animal):
    """Another child class"""
    
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def meow(self):
        print(f"{self.name} says: Meow! Meow!")


# Create objects
dog = Dog("Buddy", 5, "Labrador")
cat = Cat("Whiskers", 3, "Orange")

# Dog can use both inherited and own methods
print("--- DOG ---")
dog.display_info()  # From parent
dog.eat()           # From parent
dog.sleep()         # From parent
dog.bark()          # Own method

print("\n--- CAT ---")
cat.display_info()  # From parent
cat.eat()           # From parent
cat.sleep()         # From parent
cat.meow()          # Own method

print("""
KEY POINTS:
1. Dog inherits display_info(), eat(), sleep() from Animal
2. Dog adds its own bark() method
3. Each child can add specialized behavior
4. No code duplication!
""")


# ================================================================================
# SECTION 2: TYPES OF INHERITANCE
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 2: TYPES OF INHERITANCE")
print("=" * 80)

# TYPE 1: SINGLE INHERITANCE (One parent, one child)
print("\n--- TYPE 1: SINGLE INHERITANCE ---")

class Vehicle:
    """Parent"""
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    """Child - inherits from one parent"""
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


car = Car("Toyota", "Camry")
print(f"Car: {car.brand} {car.model}")


# TYPE 2: MULTI-LEVEL INHERITANCE
print("\n--- TYPE 2: MULTI-LEVEL INHERITANCE ---")

class LivingBeing:
    """Level 1 - Grandparent"""
    def __init__(self, name):
        self.name = name


class Mammal(LivingBeing):
    """Level 2 - Parent"""
    def __init__(self, name, warm_blooded=True):
        super().__init__(name)
        self.warm_blooded = warm_blooded


class Human(Mammal):
    """Level 3 - Child"""
    def __init__(self, name, occupation):
        super().__init__(name)
        self.occupation = occupation


human = Human("Alice", "Engineer")
print(f"Person: {human.name}, Occupation: {human.occupation}, Warm-blooded: {human.warm_blooded}")


# TYPE 3: MULTIPLE INHERITANCE
print("\n--- TYPE 3: MULTIPLE INHERITANCE ---")

class Teacher:
    """First parent"""
    def teach(self):
        print("Teaching students...")


class Researcher:
    """Second parent"""
    def research(self):
        print("Conducting research...")


class Professor(Teacher, Researcher):
    """Child inherits from TWO parents"""
    def __init__(self, name):
        self.name = name


prof = Professor("Dr. Smith")
prof.teach()       # From Teacher
prof.research()    # From Researcher


# TYPE 4: HIERARCHICAL INHERITANCE
print("\n--- TYPE 4: HIERARCHICAL INHERITANCE ---")

class Shape:
    """Parent"""
    def area(self):
        print("Calculating area...")


class Circle(Shape):
    """Child 1"""
    pass


class Square(Shape):
    """Child 2"""
    pass


circle = Circle()
square = Square()
circle.area()
square.area()

print("""
INHERITANCE TYPES:

1. Single: One parent, one child
   Child ← Parent

2. Multi-level: Chain of inheritance
   Grandchild ← Child ← Parent

3. Multiple: One child, multiple parents
   Child ← Parent1, Parent2

4. Hierarchical: One parent, multiple children
   Child1 ← Parent → Child2

5. Hybrid: Combination of above
""")


# ================================================================================
# SECTION 3: METHOD OVERRIDING
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 3: METHOD OVERRIDING")
print("=" * 80)

class Bird:
    """Parent class"""
    
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        """General sound method"""
        print(f"{self.name} makes a sound")


class Parrot(Bird):
    """Child - OVERRIDES parent's method"""
    
    def sound(self):
        # Override - provide different implementation
        print(f"{self.name} says: Hello! Hello!")


class Crow(Bird):
    """Another child - OVERRIDES parent's method"""
    
    def sound(self):
        print(f"{self.name} says: Caw! Caw!")


# Test
bird = Bird("Generic Bird")
bird.sound()

parrot = Parrot("Polly")
parrot.sound()  # Uses overridden method

crow = Crow("Blacky")
crow.sound()    # Uses overridden method

print("""
METHOD OVERRIDING:
- Child provides its own implementation of parent's method
- Same method name, different behavior
- Each class implements what makes sense for it
- Example: Base class fly() - but each bird flies differently
""")


# ================================================================================
# SECTION 4: USING super() KEYWORD
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 4: USING super() KEYWORD")
print("=" * 80)

class Employee:
    """Parent class"""
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


class Manager(Employee):
    """Child class"""
    
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Call parent's __init__
        self.department = department
    
    def display(self):
        super().display()  # Call parent's display
        print(f"Department: {self.department}")


manager = Manager("Ahmed", 80000, "IT")
manager.display()

print("""
super() KEYWORD:
- Calls parent class's method
- Used in __init__ to initialize parent
- Used in overridden methods to keep parent behavior
- Avoids code duplication

SYNTAX: super().method_name()
""")


# ================================================================================
# SECTION 5: ISINSTANCE() AND ISSUBCLASS()
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 5: CHECKING INHERITANCE")
print("=" * 80)

class Vehicle:
    pass

class Bike(Vehicle):
    pass

car = Vehicle()
bike = Bike()

# Check if object is instance of class
print(f"bike is instance of Bike: {isinstance(bike, Bike)}")
print(f"bike is instance of Vehicle: {isinstance(bike, Vehicle)}")
print(f"car is instance of Bike: {isinstance(car, Bike)}")

# Check if class inherits from another class
print(f"\nBike is subclass of Vehicle: {issubclass(Bike, Vehicle)}")
print(f"Vehicle is subclass of Bike: {issubclass(Vehicle, Bike)}")

print("""
isinstance(object, class):
- Returns True if object is instance of class
- Works with inherited classes too

issubclass(class1, class2):
- Returns True if class1 inherits from class2
- Works with inheritance hierarchy
""")


# ================================================================================
# SECTION 6: REAL WORLD EXAMPLE
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 6: REAL WORLD - BANK ACCOUNTS")
print("=" * 80)

class BankAccount:
    """Parent class - Basic account"""
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = "Basic"
    
    def deposit(self, amount):
        """Deposit money"""
        self.balance += amount
        print(f"{self.account_holder} deposited: {amount}")
    
    def withdraw(self, amount):
        """Withdraw money"""
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.account_holder} withdrew: {amount}")
        else:
            print("Insufficient balance!")
    
    def display_statement(self):
        print(f"\n--- {self.account_type} Account ---")
        print(f"Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


class SavingsAccount(BankAccount):
    """Child class - Savings account with interest"""
    
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.account_type = "Savings"
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        """Apply interest - new behavior"""
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest applied: {interest}")
    
    def display_statement(self):
        super().display_statement()  # Call parent
        print(f"Interest Rate: {self.interest_rate}%")


class CheckingAccount(BankAccount):
    """Child class - Checking account with daily limit"""
    
    def __init__(self, account_holder, balance, daily_limit):
        super().__init__(account_holder, balance)
        self.account_type = "Checking"
        self.daily_limit = daily_limit
        self.daily_withdrawn = 0
    
    def withdraw(self, amount):
        """Override - check daily limit"""
        if self.daily_withdrawn + amount <= self.daily_limit:
            super().withdraw(amount)  # Call parent
            self.daily_withdrawn += amount
        else:
            print("Daily limit exceeded!")
    
    def reset_daily_limit(self):
        """Reset daily counter - new behavior"""
        self.daily_withdrawn = 0
    
    def display_statement(self):
        super().display_statement()
        print(f"Daily Limit: {self.daily_limit}")
        print(f"Already Withdrawn Today: {self.daily_withdrawn}")


# Create different account types
savings = SavingsAccount("Ali", 50000, 5)
checking = CheckingAccount("Fatima", 30000, 10000)

# Use accounts
savings.deposit(10000)
savings.apply_interest()
savings.display_statement()

print()

checking.withdraw(5000)
checking.withdraw(4000)
checking.withdraw(2000)  # Should fail
checking.display_statement()


# ================================================================================
# SECTION 7: ADVANTAGES OF INHERITANCE
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 7: ADVANTAGES OF INHERITANCE")
print("=" * 80)

print("""
ADVANTAGES:

1. CODE REUSABILITY:
   ✓ Write once, use in multiple child classes
   ✓ Reduce code duplication
   ✓ Easier maintenance

2. HIERARCHY AND ORGANIZATION:
   ✓ Represent real-world relationships
   ✓ Organize code logically
   ✓ Clear structure

3. EXTENSIBILITY:
   ✓ Easy to add new child classes
   ✓ New classes inherit existing behavior
   ✓ Add specialized features without changing parent

4. POLYMORPHISM:
   ✓ Use objects of different types interchangeably
   ✓ Same method, different behaviors

DISADVANTAGES TO WATCH FOR:

1. COMPLEXITY:
   ✗ Can make code harder to follow
   ✗ Deep inheritance chains are problematic

2. TIGHT COUPLING:
   ✗ Child depends on parent
   ✗ Changes to parent affect all children

3. FRAGILE BASE CLASS PROBLEM:
   ✗ Changes to parent may break children
   ✗ Need careful design

BEST PRACTICE:
- Use 2-3 levels maximum
- Don't create deep inheritance chains
- Prefer composition over inheritance when unclear
""")


# ================================================================================
# SECTION 9: METHOD RESOLUTION ORDER (MRO) - CRITICAL CONCEPT
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 9: METHOD RESOLUTION ORDER (MRO)")
print("=" * 80)

print("""
WHAT IS MRO?
- Method Resolution Order = Order in which Python looks for methods
- Crucial for multiple inheritance
- Determines which method gets called when multiple parents have same method
- Uses C3 Linearization algorithm (complex but smart!)

WHY IMPORTANT?
- Multiple inheritance can create 'diamond problem'
- MRO ensures consistent, predictable method resolution
- Prevents ambiguity in method calls
""")

# EXAMPLE 1: Simple Multiple Inheritance
print("\n--- EXAMPLE 1: Simple Multiple Inheritance ---")

class A:
    def method(self):
        print("Method from A")

class B:
    def method(self):
        print("Method from B")

class C(A, B):  # C inherits from A and B
    pass

c = C()
c.method()  # Which method gets called?

print(f"MRO for C: {C.__mro__}")
print("C looks for method in order: C → A → B → object")

# EXAMPLE 2: Diamond Problem
print("\n--- EXAMPLE 2: Diamond Problem ---")

class GrandParent:
    def method(self):
        print("Method from GrandParent")

class Parent1(GrandParent):
    def method(self):
        print("Method from Parent1")

class Parent2(GrandParent):
    def method(self):
        print("Method from Parent2")

class Child(Parent1, Parent2):  # Multiple inheritance
    pass

child = Child()
child.method()  # Which method gets called?

print(f"MRO for Child: {Child.__mro__}")
print("Order: Child → Parent1 → Parent2 → GrandParent → object")
print("Python chooses Parent1's method (first in inheritance list)")

# EXAMPLE 3: Using super() with MRO
print("\n--- EXAMPLE 3: super() follows MRO ---")

class X:
    def __init__(self):
        print("X.__init__ called")
        self.x = "X"

class Y:
    def __init__(self):
        print("Y.__init__ called")
        self.y = "Y"

class Z(X, Y):
    def __init__(self):
        print("Z.__init__ called")
        super().__init__()  # Calls X.__init__ (first in MRO)
        print(f"Z has: x={self.x}, y={self.y}")

z = Z()
print(f"MRO for Z: {Z.__mro__}")

# EXAMPLE 4: Complex MRO
print("\n--- EXAMPLE 4: Complex MRO Scenario ---")

class Animal:
    def speak(self):
        return "Animal sound"

class Mammal(Animal):
    def speak(self):
        return "Mammal sound"

class Bird(Animal):
    def speak(self):
        return "Bird sound"

class Bat(Mammal, Bird):  # Multiple inheritance
    pass

bat = Bat()
print(f"Bat speaks: {bat.speak()}")  # Which speak()?
print(f"MRO for Bat: {Bat.__mro__}")
print("Order: Bat → Mammal → Bird → Animal → object")
print("Bat gets Mammal's speak() (first in inheritance list)")

# EXAMPLE 5: MRO with super() chain
print("\n--- EXAMPLE 5: super() follows MRO chain ---")

class A:
    def __init__(self):
        print("A.__init__")
        super().__init__()

class B:
    def __init__(self):
        print("B.__init__")
        super().__init__()

class C(A, B):
    def __init__(self):
        print("C.__init__")
        super().__init__()

c = C()
print(f"MRO: {C.__mro__}")
print("super() calls: C → A → B → object")

print("""
MRO RULES:
1. Child classes come before parents
2. Parents maintain order specified in class definition
3. No class appears twice (except object)
4. Algorithm ensures consistency

HOW TO CHECK MRO:
- ClassName.__mro__ (tuple of classes in resolution order)
- ClassName.mro() (same as __mro__)

WHEN TO USE:
- Always check MRO when using multiple inheritance
- Use super() to follow MRO properly
- Avoid method name conflicts in multiple inheritance
""")

# ================================================================================
# SECTION 10: ADVANCED INHERITANCE TECHNIQUES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 10: ADVANCED INHERITANCE TECHNIQUES")
print("=" * 80)

# TECHNIQUE 1: Cooperative Inheritance with super()
print("\n--- TECHNIQUE 1: Cooperative Inheritance ---")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    
    def introduce(self):
        parent_intro = super().introduce()
        return f"{parent_intro}. I earn {self.salary}"

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department
    
    def introduce(self):
        parent_intro = super().introduce()
        return f"{parent_intro}. I manage {self.department}"

manager = Manager("Ahmed", 35, 80000, "IT")
print(manager.introduce())

# TECHNIQUE 2: Mixin Classes
print("\n--- TECHNIQUE 2: Mixin Classes ---")

class LoggerMixin:
    """Mixin for logging functionality"""
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class SerializerMixin:
    """Mixin for serialization"""
    def to_dict(self):
        return self.__dict__
    
    def from_dict(self, data):
        self.__dict__.update(data)

class User(LoggerMixin, SerializerMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email

user = User("Ali", "ali@example.com")
user.log("User created")
print(f"Serialized: {user.to_dict()}")

# TECHNIQUE 3: Abstract Base Classes with Inheritance
print("\n--- TECHNIQUE 3: Abstract Base Classes ---")

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand
    
    @abstractmethod
    def move(self):
        pass
    
    def honk(self):
        print("Honk! Honk!")

class Car(Vehicle):
    def move(self):
        print(f"{self.brand} car is driving")

class Boat(Vehicle):
    def move(self):
        print(f"{self.brand} boat is sailing")

car = Car("Toyota")
boat = Boat("Yamaha")
car.move()
boat.move()
car.honk()

print("""
ADVANCED TECHNIQUES:

1. Cooperative Inheritance:
   - Use super() to call parent methods
   - Chain method calls through inheritance hierarchy

2. Mixin Classes:
   - Small classes providing specific functionality
   - Multiple inheritance for combining features
   - No instantiation needed

3. Abstract Base Classes:
   - Define interfaces with @abstractmethod
   - Force child classes to implement methods
   - Combine with regular inheritance
""")

# ================================================================================
# SECTION 11: INHERITANCE BEST PRACTICES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 11: INHERITANCE BEST PRACTICES")
print("=" * 80)

print("""
✓ DO THIS:

1. USE IS-A RELATIONSHIP:
   - Dog IS-A Animal ✓
   - Car IS-A Vehicle ✓
   - Manager IS-A Employee ✓

2. KEEP INHERITANCE SHALLOW:
   - Maximum 2-3 levels deep
   - Avoid deep inheritance chains

3. USE super() CONSISTENTLY:
   - Always call super().__init__()
   - Follow MRO properly

4. DOCUMENT INHERITANCE INTENT:
   - Comment why you're inheriting
   - Explain relationship

5. PREFER COMPOSITION WHEN UNCLEAR:
   - HAS-A relationship: Use composition
   - IS-A relationship: Use inheritance

✗ DON'T DO THIS:

1. DEEP INHERITANCE CHAINS:
   - GrandChild(Child(Parent)) - too deep!

2. INHERIT JUST TO REUSE CODE:
   - If no IS-A relationship, use composition

3. OVERRIDE METHODS WITHOUT CALLING super():
   - May break parent functionality

4. MULTIPLE INHERITANCE WITHOUT MRO KNOWLEDGE:
   - Always check __mro__

5. CHANGE PARENT METHOD SIGNATURES:
   - Breaks child classes
""")

# ================================================================================
# SECTION 12: COMMON MISTAKES AND SOLUTIONS
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 12: COMMON MISTAKES AND SOLUTIONS")
print("=" * 80)

print("""
MISTAKE 1: Forgetting super().__init__()
❌ class Child(Parent):
    def __init__(self, parent_param, child_param):
        self.child_param = child_param  # Parent not initialized!

✅ class Child(Parent):
    def __init__(self, parent_param, child_param):
        super().__init__(parent_param)  # Initialize parent first
        self.child_param = child_param

---

MISTAKE 2: Wrong super() call order
❌ class Child(Parent):
    def __init__(self, param):
        self.child_attr = "value"  # Set child attr first
        super().__init__(param)     # Then parent - WRONG!

✅ class Child(Parent):
    def __init__(self, param):
        super().__init__(param)     # Parent first
        self.child_attr = "value"   # Then child

---

MISTAKE 3: Not understanding MRO
❌ class D(A, B):
    pass
# Assumes A.method() will be called

✅ class D(A, B):
    pass
print(D.__mro__)  # Check actual order!

---

MISTAKE 4: Method name conflicts in multiple inheritance
❌ class A:
    def method(self): pass
class B:
    def method(self): pass
class C(A, B):  # Which method?
    pass

✅ class A:
    def method_a(self): pass
class B:
    def method_b(self): pass
class C(A, B):  # No conflict
    pass

---

MISTAKE 5: Overriding without extending
❌ class Child(Parent):
    def method(self):
        # Completely different implementation
        pass

✅ class Child(Parent):
    def method(self):
        # Extend parent behavior
        super().method()
        # Add child-specific code
        pass
""")

# ================================================================================
# SECTION 13: PRACTICAL EXAMPLES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 13: PRACTICAL EXAMPLES")
print("=" * 80)

# EXAMPLE 1: GUI Framework
print("\n--- EXAMPLE 1: GUI Framework ---")

class Widget:
    """Base widget class"""
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
    
    def draw(self):
        print(f"Drawing widget at ({self.x}, {self.y})")

class Button(Widget):
    """Button inherits from Widget"""
    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height)
        self.text = text
    
    def draw(self):
        super().draw()
        print(f"Button text: {self.text}")
    
    def click(self):
        print(f"Button '{self.text}' clicked!")

class TextBox(Widget):
    """TextBox inherits from Widget"""
    def __init__(self, x, y, width, height, placeholder=""):
        super().__init__(x, y, width, height)
        self.text = ""
        self.placeholder = placeholder
    
    def draw(self):
        super().draw()
        content = self.text if self.text else self.placeholder
        print(f"TextBox content: '{content}'")

button = Button(10, 20, 100, 30, "Submit")
textbox = TextBox(10, 60, 200, 25, "Enter text...")

button.draw()
button.click()
textbox.draw()

# EXAMPLE 2: Game Characters
print("\n--- EXAMPLE 2: Game Characters ---")

class Character:
    """Base character class"""
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def attack(self):
        return 10
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} died!")
    
    def display_stats(self):
        print(f"{self.name}: Health={self.health}")

class Warrior(Character):
    """Warrior - strong attack"""
    def __init__(self, name, health, armor):
        super().__init__(name, health)
        self.armor = armor
    
    def attack(self):
        return super().attack() + 20  # Stronger attack
    
    def take_damage(self, damage):
        # Armor reduces damage
        actual_damage = max(0, damage - self.armor)
        super().take_damage(actual_damage)

class Mage(Character):
    """Mage - magical attack"""
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana
    
    def attack(self):
        if self.mana >= 10:
            self.mana -= 10
            return super().attack() + 30  # Magical attack
        return super().attack()
    
    def display_stats(self):
        super().display_stats()
        print(f"Mana: {self.mana}")

warrior = Warrior("Conan", 100, 15)
mage = Mage("Merlin", 80, 50)

warrior.display_stats()
mage.display_stats()

print(f"\nWarrior attack: {warrior.attack()}")
print(f"Mage attack: {mage.attack()}")

warrior.take_damage(20)  # Armor reduces damage
mage.take_damage(20)

warrior.display_stats()
mage.display_stats()

print("""
INHERITANCE IN PRACTICE:

1. GUI Framework:
   - Base Widget class with common properties
   - Specialized widgets (Button, TextBox) inherit and extend
   - Each widget has draw() method with specific behavior

2. Game Characters:
   - Base Character with health and basic attack
   - Warrior adds armor, stronger attack
   - Mage adds mana, magical attack
   - Polymorphism: same attack() method, different behaviors
""")

# ================================================================================
# SUMMARY
# ================================================================================

print("\n" + "=" * 80)
print("INHERITANCE SUMMARY")
print("=" * 80)

print("""
WHAT YOU LEARNED:

1. BASIC INHERITANCE:
   - Child classes inherit from parent classes
   - Use super() to call parent methods
   - Add specialized behavior in child classes

2. TYPES OF INHERITANCE:
   - Single: One parent, one child
   - Multi-level: Chain of inheritance
   - Multiple: One child, multiple parents
   - Hierarchical: One parent, multiple children

3. METHOD OVERRIDING:
   - Child provides different implementation
   - Same method name, different behavior
   - Use super() to extend parent behavior

4. METHOD RESOLUTION ORDER (MRO):
   - Order Python searches for methods
   - Critical for multiple inheritance
   - Use __mro__ to check resolution order

5. ADVANCED TECHNIQUES:
   - Cooperative inheritance with super()
   - Mixin classes for functionality
   - Abstract base classes for interfaces

6. BEST PRACTICES:
   - Use IS-A relationships
   - Keep inheritance shallow (2-3 levels max)
   - Prefer composition when unclear
   - Always check MRO for multiple inheritance

KEY TAKEAWAYS:
- Inheritance promotes code reuse
- Use super() for proper initialization
- MRO is crucial for multiple inheritance
- Don't create deep inheritance hierarchies
- Choose inheritance or composition wisely

NEXT: Learn about Polymorphism (file 06)
""")
