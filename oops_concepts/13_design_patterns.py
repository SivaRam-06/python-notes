"""
================================================================================
        DESIGN PATTERNS - MASTERY 1
================================================================================

CONCEPT:
  Design Patterns = Proven solutions to common programming problems
  Reusable templates for solving recurring design issues

WHY?
  - Solve problems in clean, tested ways
  - Better code organization
  - Improve communication (developers know pattern names)
  - Increased maintainability

================================================================================
                    COMMON DESIGN PATTERNS
================================================================================

1. SINGLETON     - Only one instance of class exists
2. FACTORY       - Create objects without specifying exact classes
3. OBSERVER      - Notify multiple objects when state changes
4. DECORATOR     - Add behavior to objects dynamically
5. STRATEGY      - Switch between different algorithms
6. ADAPTER       - Make incompatible classes work together

================================================================================
"""

# ===============================================================================
# SECTION 1: SINGLETON PATTERN
# ===============================================================================

print("=" * 80)
print("SECTION 1: SINGLETON PATTERN - Only One Instance")
print("=" * 80)

print("""
SINGLETON PATTERN:
- Ensures only one instance of a class exists
- Provides global access point
- Common for: Database connections, logging, configuration

WHY USEFUL?
- Database connection - expensive to create multiple
- Logger - want single point of logging
- Configuration - one source of truth
""")

# WRONG - Multiple instances
class Database_Wrong:
    """Without singleton - can create multiple"""
    def __init__(self, host):
        self.host = host
    
    def connect(self):
        print(f"Connecting to {self.host}")


db1 = Database_Wrong("localhost")
db2 = Database_Wrong("localhost")
print(f"Two different instances (WRONG):")
print(f"db1 is db2: {db1 is db2}")  # False


# RIGHT - Singleton pattern
print("\n--- SINGLETON PATTERN ---\n")

class Database:
    """Singleton - only one instance"""
    __instance = None
    
    def __new__(cls, host):
        # Create instance only once
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.host = host
            print(f"Creating new database instance: {host}")
        else:
            print("Using existing database instance")
        return cls.__instance
    
    def connect(self):
        print(f"Connected to {self.host}")


db1 = Database("localhost")
db2 = Database("localhost")
print(f"\nTwo variables reference SAME instance:")
print(f"db1 is db2: {db1 is db2}")  # True!

db1.connect()
db2.connect()


# ===============================================================================
# SECTION 2: FACTORY PATTERN
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 2: FACTORY PATTERN - Creating Objects")
print("=" * 80)

print("""
FACTORY PATTERN:
- Create objects without specifying exact classes
- Object type depends on parameters
- Centralizes object creation

WHY USEFUL?
- Reduces coupling (don't know exact classes)
- Easy to add new types
- Flexible object creation
""")

# Without Factory - Tight coupling
print("\n--- WITHOUT FACTORY (WRONG) ---")

def create_payment_wrong(method_type, amount):
    """Not using factory"""
    if method_type == "credit":
        return "CreditCardPayment"
    elif method_type == "paypal":
        return "PayPalPayment"
    elif method_type == "upi":
        return "UPIPayment"
    # If you add new type, must modify this function!


# With Factory Pattern
print("\n--- WITH FACTORY PATTERN (RIGHT) ---")

class CreditCard:
    def process(self, amount):
        return f"Processing credit card: {amount}"


class PayPal:
    def process(self, amount):
        return f"Processing PayPal: {amount}"


class UPI:
    def process(self, amount):
        return f"Processing UPI: {amount}"


class PaymentFactory:
    """Factory - creates payment objects"""
    
    payment_methods = {
        "credit": CreditCard,
        "paypal": PayPal,
        "upi": UPI
    }
    
    @staticmethod
    def create_payment(method_type):
        """Create appropriate payment object"""
        if method_type not in PaymentFactory.payment_methods:
            raise ValueError(f"Unknown payment method: {method_type}")
        return PaymentFactory.payment_methods[method_type]()
    
    @staticmethod
    def register_payment(name, payment_class):
        """Add new payment type without changing factory"""
        PaymentFactory.payment_methods[name] = payment_class


# Use factory
credit_payment = PaymentFactory.create_payment("credit")
print(credit_payment.process(1000))

paypal_payment = PaymentFactory.create_payment("paypal")
print(paypal_payment.process(1000))

# Add new type dynamically!
class Bitcoin:
    def process(self, amount):
        return f"Processing Bitcoin: {amount}"

PaymentFactory.register_payment("bitcoin", Bitcoin)
bitcoin_payment = PaymentFactory.create_payment("bitcoin")
print(bitcoin_payment.process(1000))

print("""
FACTORY BENEFITS:
- Create objects without knowing exact classes
- Easy to add new types
- Centralized creation logic
- Reduces if-else chains
""")


# ===============================================================================
# SECTION 3: OBSERVER PATTERN
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 3: OBSERVER PATTERN - Event Notification")
print("=" * 80)

print("""
OBSERVER PATTERN:
- Subject (Observable) notifies observers when state changes
- Observers react to changes
- One-to-many relationship

WHY USEFUL?
- Event handling systems
- Real-time notifications
- Decoupled architecture
""")

class Stock:
    """Subject - observable"""
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._observers = []
    
    def attach(self, observer):
        """Add observer"""
        self._observers.append(observer)
    
    def detach(self, observer):
        """Remove observer"""
        self._observers.remove(observer)
    
    def notify(self):
        """Notify all observers"""
        for observer in self._observers:
            observer.update(self)
    
    def set_price(self, new_price):
        """Change price and notify observers"""
        print(f"\nChanging {self.name} price: {self.price} → {new_price}")
        self.price = new_price
        self.notify()


class Investor:
    """Observer"""
    
    def __init__(self, name):
        self.name = name
    
    def update(self, stock):
        """React to stock price change"""
        print(f"  Investor {self.name}: {stock.name} price is now {stock.price}")


class TradingBot:
    """Another observer"""
    
    def update(self, stock):
        """Auto-trade based on price"""
        if stock.price > 1000:
            print(f"  Bot: SELL alert for {stock.name}")
        else:
            print(f"  Bot: BUY alert for {stock.name}")


# Use observer pattern
stock = Stock("APPLE", 1100)

investor1 = Investor("Ahmed")
investor2 = Investor("Fatima")
bot = TradingBot()

stock.attach(investor1)
stock.attach(investor2)
stock.attach(bot)

stock.set_price(1050)
stock.set_price(950)

print("""
OBSERVER BENEFITS:
- Loosely coupled components
- Multiple observers for one subject
- Easy to add/remove observers
- Event-driven architecture
""")


# ===============================================================================
# SECTION 4: STRATEGY PATTERN
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 4: STRATEGY PATTERN - Algorithm Selection")
print("=" * 80)

print("""
STRATEGY PATTERN:
- Define multiple algorithms
- Select algorithm at runtime
- Encapsulate each algorithm

WHY USEFUL?
- Multiple ways to do same thing
- Switch algorithms dynamically
- Cleaner than multiple if-else
""")

class PaymentStrategy:
    """Base strategy"""
    def pay(self, amount):
        pass


class CreditCardStrategy(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} via credit card"


class UPIStrategy(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} via UPI"


class CashStrategy(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} in cash"


class ShoppingCart:
    """Context - uses strategy"""
    
    def __init__(self, total):
        self.total = total
        self.strategy = None
    
    def set_payment_strategy(self, strategy):
        """Select payment strategy"""
        self.strategy = strategy
    
    def checkout(self):
        """Use selected strategy"""
        if self.strategy is None:
            raise ValueError("Payment strategy not set!")
        return self.strategy.pay(self.total)


# Use strategy
cart = ShoppingCart(1000)

# Different strategies
cart.set_payment_strategy(CreditCardStrategy())
print(cart.checkout())

cart.set_payment_strategy(UPIStrategy())
print(cart.checkout())

cart.set_payment_strategy(CashStrategy())
print(cart.checkout())

print("""
STRATEGY BENEFITS:
- Avoid long if-else chains
- Easy to add new strategies
- Switch strategies at runtime
- Clean and maintainable
""")


# ===============================================================================
# SECTION 5: DECORATOR PATTERN
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 5: DECORATOR PATTERN - Add Behavior Dynamically")
print("=" * 80)

print("""
DECORATOR PATTERN:
- Add new functionality to objects dynamically
- Alternative to subclassing
- Wrap objects with behavior

WHY USEFUL?
- Add features without modifying original
- Combine multiple decorators
- More flexible than inheritance
""")

class Coffee:
    """Base component"""
    def cost(self):
        return 100
    
    def description(self):
        return "Coffee"


class CoffeeDecorator(Coffee):
    """Base decorator"""
    def __init__(self, coffee):
        self.coffee = coffee
    
    def cost(self):
        return self.coffee.cost()
    
    def description(self):
        return self.coffee.description()


class MilkDecorator(CoffeeDecorator):
    """Add milk"""
    def cost(self):
        return self.coffee.cost() + 20
    
    def description(self):
        return self.coffee.description() + " + Milk"


class SugarDecorator(CoffeeDecorator):
    """Add sugar"""
    def cost(self):
        return self.coffee.cost() + 10
    
    def description(self):
        return self.coffee.description() + " + Sugar"


class WhippedCreamDecorator(CoffeeDecorator):
    """Add whipped cream"""
    def cost(self):
        return self.coffee.cost() + 30
    
    def description(self):
        return self.coffee.description() + " + Whipped Cream"


# Combine decorators
coffee = Coffee()
coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)
coffee = WhippedCreamDecorator(coffee)

print(f"Description: {coffee.description()}")
print(f"Cost: {coffee.cost()}")

print("""
DECORATOR BENEFITS:
- Add behavior dynamically
- Combine multiple decorators
- Flexible combinations
- Avoid complex inheritance
""")


# ===============================================================================
# SECTION 6: ADAPTER PATTERN
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 6: ADAPTER PATTERN - Make Incompatible Interfaces Compatible")
print("=" * 80)

print("""
ADAPTER PATTERN:
- Convert interface of a class into another interface clients expect
- Make incompatible classes work together
- Like a real adapter (USB to HDMI, etc.)

WHY USEFUL?
- Integrate legacy code with new systems
- Use third-party libraries with different interfaces
- Make classes work together without changing their code
""")

# Target interface that client expects
class MediaPlayer:
    """Target interface"""
    def play(self, audio_type, file_name):
        pass


class AdvancedMediaPlayer:
    """Adaptee interface - more advanced but incompatible"""
    def play_vlc(self, file_name):
        pass
    
    def play_mp4(self, file_name):
        pass


class VlcPlayer(AdvancedMediaPlayer):
    """Concrete adaptee for VLC"""
    def play_vlc(self, file_name):
        print(f"Playing VLC file: {file_name}")
    
    def play_mp4(self, file_name):
        # VLC can play MP4 too
        print(f"Playing MP4 file with VLC: {file_name}")


class Mp4Player(AdvancedMediaPlayer):
    """Concrete adaptee for MP4"""
    def play_vlc(self, file_name):
        # MP4 player can't play VLC
        pass
    
    def play_mp4(self, file_name):
        print(f"Playing MP4 file: {file_name}")


class MediaAdapter(MediaPlayer):
    """Adapter class"""
    def __init__(self, audio_type):
        if audio_type.lower() == "vlc":
            self.advanced_player = VlcPlayer()
        elif audio_type.lower() == "mp4":
            self.advanced_player = Mp4Player()
    
    def play(self, audio_type, file_name):
        if audio_type.lower() == "vlc":
            self.advanced_player.play_vlc(file_name)
        elif audio_type.lower() == "mp4":
            self.advanced_player.play_mp4(file_name)


class AudioPlayer(MediaPlayer):
    """Client that uses target interface"""
    def __init__(self):
        self.adapter = None
    
    def play(self, audio_type, file_name):
        # Built-in support for MP3
        if audio_type.lower() == "mp3":
            print(f"Playing MP3 file: {file_name}")
        # Use adapter for other formats
        elif audio_type.lower() in ["vlc", "mp4"]:
            self.adapter = MediaAdapter(audio_type)
            self.adapter.play(audio_type, file_name)
        else:
            print(f"Invalid media type: {audio_type}")


# Test the adapter pattern
audio_player = AudioPlayer()
audio_player.play("mp3", "song.mp3")      # Built-in support
audio_player.play("mp4", "movie.mp4")     # Uses adapter
audio_player.play("vlc", "video.vlc")     # Uses adapter
audio_player.play("avi", "movie.avi")     # Unsupported

print("""
ADAPTER PATTERN BENEFITS:
- Makes incompatible interfaces work together
- Promotes reusability of existing code
- Doesn't modify existing code
- Follows Single Responsibility Principle
- Easy to add new adapters
""")

print("""
WHEN TO USE ADAPTER PATTERN:
- Integrate legacy code with new systems
- Use third-party libraries with different interfaces
- Make classes work together without changing them
- Bridge different APIs or protocols
- Database migration scenarios
""")


# ===============================================================================
# SECTION 7: BEST PRACTICES
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 7: WHEN TO USE WHICH PATTERN")
print("=" * 80)

print("""
PATTERN SELECTION GUIDE:

SINGLETON:
- Use when: Only one instance should exist globally
- Examples: Database connection, Logger, Configuration
- Pro: Guaranteed single instance, global access
- Con: Not testable, hides dependencies

FACTORY:
- Use when: Creating different object types
- Examples: Payment methods, Database drivers
- Pro: Decoupled creation, easy to add types
- Con: Added complexity for simple cases

OBSERVER:
- Use when: Objects need to react to changes
- Examples: Event systems, notifications
- Pro: Loose coupling, one-to-many relationship
- Con: Hard to track flow, memory leaks if not careful

STRATEGY:
- Use when: Multiple algorithms for same task
- Examples: Sorting, Payment, Compression
- Pro: Switch algorithms at runtime, clean code
- Con: More classes to manage

DECORATOR:
- Use when: Add features to objects dynamically
- Examples: Coffee orders, UI components
- Pro: Flexible combinations, don't modify original
- Con: More complex, many small classes

ADAPTER:
- Use when: Make incompatible interfaces work together
- Examples: Legacy code integration, API bridging, third-party libraries
- Pro: Reuse existing code, no modification needed
- Con: Sometimes just needs refactoring, added complexity

GOLDEN RULES:
1. Don't use patterns prematurely
2. Use patterns only when they solve a real problem
3. Keep it simple - choose simplest solution first
4. Learn from existing code
5. Patterns are guides, not rules
""")
