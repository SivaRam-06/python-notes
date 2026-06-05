"""
================================================================================
                    ABSTRACTION - ADVANCED 1
================================================================================

CONCEPT:
  Abstraction = Hiding complex implementation details
                Showing only essential features to user

MOTTO: "Hide complexity, show simplicity"

ANALOGY:
  Car:
  - You see: Drive, Stop, Turn
  - You don't see: Engine, Transmission, Brakes mechanism
  - You interact only through steering wheel, pedals, buttons

================================================================================
                        WHEN TO USE?
================================================================================
Use Abstraction when:
1. Need to simplify complex operations
2. Want users to interact with interface, not implementation
3. Need to enforce specific method implementation in child classes
4. Want to hide internal details

================================================================================
                        HOW TO USE?
================================================================================
TOOLS FOR ABSTRACTION:

1. ABSTRACT CLASSES (Using ABC module)
2. ABSTRACT METHODS (Methods that must be implemented by children)
3. INTERFACE (Define what methods must exist)

================================================================================
"""

from abc import ABC, abstractmethod
from math import pi

# ================================================================================
# SECTION 1: ABSTRACT CLASSES AND METHODS
# ================================================================================

print("=" * 80)
print("SECTION 1: ABSTRACT CLASSES")
print("=" * 80)

print("""
ABSTRACT CLASS:
- Cannot be instantiated directly
- Children MUST implement abstract methods
- Defines interface/contract that children must follow

WHY?
- Enforce consistent implementation
- Prevent incomplete classes
- Define "what" not "how"
""")

# ABSTRACT CLASS
class Animal(ABC):
    """
    Abstract class - cannot create Animal() directly
    Children must implement abstract methods
    """
    
    @abstractmethod
    def speak(self):
        """Abstract method - children must implement this"""
        pass
    
    @abstractmethod
    def move(self):
        """Abstract method - children must implement this"""
        pass
    
    def sleep(self):
        """Concrete method - children inherit this"""
        print("Zzzzz... sleeping")


# Try to create abstract class - WILL FAIL
print("Trying to create abstract Animal()... ")
try:
    animal = Animal()
except TypeError as e:
    print(f"ERROR: {e}")
    print("Cannot create instance of abstract class!\n")


# CONCRETE CLASSES (Must implement all abstract methods)
class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")
    
    def move(self):
        print("Running on four legs")


class Bird(Animal):
    def speak(self):
        print("Tweet! Tweet!")
    
    def move(self):
        print("Flying with wings")


# Now we can create concrete classes
dog = Dog()
dog.speak()
dog.move()
dog.sleep()

bird = Bird()
bird.speak()
bird.move()
bird.sleep()

print("\nKEY POINT:")
print("- Animal is abstract - cannot create Animal() directly")
print("- Dog and Bird must implement speak() and move()")
print("- Works with sleep() without implementing it")


# ================================================================================
# SECTION 2: ENFORCING CONTRACT
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 2: ABSTRACT METHODS ENFORCE CONTRACT")
print("=" * 80)

class Shape(ABC):
    """Abstract shape - defines shape contract"""
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass


# Try to create incomplete child - WILL FAIL
class IncompleteCircle(Shape):
    """Forgot to implement area()"""
    def perimeter(self):
        pass


print("Trying to create IncompleteCircle()...")
try:
    shape = IncompleteCircle()
except TypeError as e:
    print(f"ERROR: {e}")
    print("Must implement ALL abstract methods!\n")


# Correct implementation
class Circle(Shape):
    """Correct - implements all abstract methods"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * pi * self.radius


circle = Circle(5)
print(f"Circle area: {circle.area():.2f}")
print(f"Circle perimeter: {circle.perimeter():.2f}")

print("\nABSTRACT METHOD CONTRACT:")
print("- Abstract class defines which methods MUST be implemented")
print("- Children MUST implement all abstract methods")
print("- Incomplete implementation = TypeError")


# ================================================================================
# SECTION 3: REAL WORLD - DATABASE
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 3: REAL WORLD - DATABASE ABSTRACTION")
print("=" * 80)

class Database(ABC):
    """
    Abstract Database class
    Defines interface all databases must follow
    """
    
    @abstractmethod
    def connect(self, host, user, password):
        """Connect to database"""
        pass
    
    @abstractmethod
    def execute_query(self, query):
        """Execute SQL query"""
        pass
    
    @abstractmethod
    def disconnect(self):
        """Disconnect from database"""
        pass
    
    def is_connected(self):
        """Common method"""
        return hasattr(self, '_connected') and self._connected


class MySQLDatabase(Database):
    """MySQL implementation"""
    
    def connect(self, host, user, password):
        print(f"Connecting to MySQL: {host} as {user}")
        self._connected = True
    
    def execute_query(self, query):
        if self.is_connected():
            print(f"MySQL: Executing {query}")
        else:
            print("Not connected!")
    
    def disconnect(self):
        print("Disconnecting from MySQL")
        self._connected = False


class PostgresDatabase(Database):
    """PostgreSQL implementation"""
    
    def connect(self, host, user, password):
        print(f"Connecting to PostgreSQL: {host} as {user}")
        self._connected = True
    
    def execute_query(self, query):
        if self.is_connected():
            print(f"PostgreSQL: Executing {query}")
        else:
            print("Not connected!")
    
    def disconnect(self):
        print("Disconnecting from PostgreSQL")
        self._connected = False


class MongoDBDatabase(Database):
    """MongoDB implementation"""
    
    def connect(self, host, user, password):
        print(f"Connecting to MongoDB: {host} as {user}")
        self._connected = True
    
    def execute_query(self, query):
        if self.is_connected():
            print(f"MongoDB: Executing {query}")
        else:
            print("Not connected!")
    
    def disconnect(self):
        print("Disconnecting from MongoDB")
        self._connected = False


# Use with abstraction - works with any database!
def run_application(database):
    """Application works with ANY database"""
    database.connect("localhost", "admin", "password")
    database.execute_query("SELECT * FROM users")
    database.execute_query("INSERT INTO logs VALUES ('event')")
    database.disconnect()


print("\n--- Using with MySQL ---")
mysql_db = MySQLDatabase()
run_application(mysql_db)

print("\n--- Using with PostgreSQL ---")
postgres_db = PostgresDatabase()
run_application(postgres_db)

print("\n--- Using with MongoDB ---")
mongo_db = MongoDBDatabase()
run_application(mongo_db)

print("""
ABSTRACTION BENEFIT:
- Application doesn't care which database
- All databases follow same interface
- Easy to swap implementations
- Add new database type without changing application
""")


# ================================================================================
# SECTION 4: PARTIAL ABSTRACTION
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 4: MIX ABSTRACT AND CONCRETE METHODS")
print("=" * 80)

class PaymentProcessor(ABC):
    """Mix of abstract and concrete methods"""
    
    def __init__(self, amount):
        self.amount = amount
        self.status = "Pending"
    
    @abstractmethod
    def validate(self):
        """Abstract - children implement"""
        pass
    
    @abstractmethod
    def process(self):
        """Abstract - children implement"""
        pass
    
    def finalize(self):
        """Concrete - shared implementation"""
        if self.status == "Completed":
            print("Payment completed and recorded")
        else:
            print("Payment failed")


class CreditCardProcessor(PaymentProcessor):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number
    
    def validate(self):
        print(f"Validating card: {self.card_number}")
        return len(self.card_number) == 16
    
    def process(self):
        if self.validate():
            print(f"Processing credit card payment: {self.amount}")
            self.status = "Completed"


processor = CreditCardProcessor(5000, "1234567890123456")
processor.process()
processor.finalize()

print("""
PARTIAL ABSTRACTION:
- Abstract: Methods that MUST be custom (validate, process)
- Concrete: Common implementation (finalize)
- Efficient - avoid repeating common code
""")


# ================================================================================
# SECTION 5: MULTIPLE ABSTRACT CLASSES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 5: INHERITING FROM MULTIPLE ABSTRACT CLASSES")
print("=" * 80)

class Drawable(ABC):
    """Abstract interface for drawing"""
    @abstractmethod
    def draw(self):
        pass


class Movable(ABC):
    """Abstract interface for movement"""
    @abstractmethod
    def move(self):
        pass


class Player(Drawable, Movable):
    """Player is both drawable and movable"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"Drawing player at ({self.x}, {self.y})")
    
    def move(self):
        self.x += 1
        self.y += 1
        print(f"Player moved to ({self.x}, {self.y})")


player = Player(0, 0)
player.draw()
player.move()
player.draw()

print("""
MULTIPLE ABSTRACT CLASSES:
- Class can inherit from multiple abstract classes
- Must implement methods from all abstract parents
- Useful for adding multiple behaviors
""")


# ================================================================================
# SECTION 6: REAL WORLD - MEDIA PLAYER
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 6: REAL WORLD - MEDIA PLAYER ABSTRACTION")
print("=" * 80)

class MediaPlayer(ABC):
    """Abstract media player"""
    
    @abstractmethod
    def play(self):
        pass
    
    @abstractmethod
    def pause(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    def display_info(self):
        """Common implementation"""
        print(f"Type: {self.__class__.__name__}")


class AudioPlayer(MediaPlayer):
    def play(self):
        print("🔊 Playing audio")
    
    def pause(self):
        print("⏸️  Audio paused")
    
    def stop(self):
        print("⏹️  Audio stopped")


class VideoPlayer(MediaPlayer):
    def play(self):
        print("🎬 Playing video in HD")
    
    def pause(self):
        print("⏸️  Video paused")
    
    def stop(self):
        print("⏹️  Video stopped")


# Polymorphic function using abstraction
def operate_player(player):
    """Works with ANY MediaPlayer"""
    player.display_info()
    player.play()
    player.pause()
    player.stop()


print("Playing audio:")
audio = AudioPlayer()
operate_player(audio)

print("\nPlaying video:")
video = VideoPlayer()
operate_player(video)


# ================================================================================
# SECTION 7: BEST PRACTICES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 7: BEST PRACTICES FOR ABSTRACTION")
print("=" * 80)

print("""
BEST PRACTICES:

1. WHEN TO USE ABSTRACT CLASSES:
   ✓ Multiple classes share same interface
   ✓ Need to enforce implementation
   ✓ Want to provide common functionality
   ✓ Creating framework or library

2. NAMING CONVENTIONS:
   ✓ Abstract classes often end with: Base, Abstract, Interface
   ✓ Example: DatabaseBase, PaymentProcessor, DrawableInterface

3. ABSTRACT vs CONCRETE:
   ✓ Keep abstract classes focused
   ✓ Define "contract" - what must be implemented
   ✓ Don't over-abstract

4. USE @abstractmethod FOR:
   ✓ Methods that MUST be customized
   ✓ Core functionality of class

5. USE REGULAR METHODS FOR:
   ✓ Common implementations
   ✓ Helper functions
   ✓ Shared logic

ANTI-PATTERNS TO AVOID:

✗ Too many abstract classes
✗ Abstract classes with too many abstract methods
✗ Forcing inheritance when composition is better
✗ Making everything abstract

WHEN NOT TO USE:
- Simple utility classes
- Small, focused classes
- When inheritance isn't natural
""")
