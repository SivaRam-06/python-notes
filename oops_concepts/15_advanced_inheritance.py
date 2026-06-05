"""
================================================================================
                    ADVANCED INHERITANCE CONCEPTS
================================================================================

This file covers advanced inheritance topics including:
- Method Resolution Order (MRO) in depth
- Complex multiple inheritance scenarios
- Diamond problem solutions
- Cooperative inheritance patterns
- Advanced super() usage
- Mixin patterns and composition

================================================================================
"""

# ================================================================================
# SECTION 1: METHOD RESOLUTION ORDER (MRO) - IN DEPTH
# ================================================================================

print("=" * 80)
print("SECTION 1: METHOD RESOLUTION ORDER (MRO) - IN DEPTH")
print("=" * 80)

print("""
WHAT IS MRO?
- Method Resolution Order = Order Python searches for methods/attributes
- Critical for multiple inheritance
- Uses C3 Linearization algorithm (mathematically proven)
- Ensures consistent, predictable resolution
- Prevents ambiguity in complex inheritance hierarchies

WHY MRO MATTERS:
- Multiple inheritance creates 'diamond problem'
- Wrong MRO can call wrong method
- super() depends on MRO
- Debugging inheritance issues requires MRO knowledge
""")

# EXAMPLE 1: Simple Diamond Problem
print("\n--- EXAMPLE 1: Diamond Problem ---")

class A:
    def method(self):
        print("Method from A")
        return "A"

class B(A):
    def method(self):
        print("Method from B")
        return "B"

class C(A):
    def method(self):
        print("Method from C")
        return "C"

class D(B, C):  # Multiple inheritance
    pass

print("Diamond inheritance: D(B, C) where B and C inherit from A")
print(f"MRO for D: {D.__mro__}")

d = D()
print("Calling d.method():")
result = d.method()
print(f"Result: {result}")

print("""
DIAMOND PROBLEM ANALYSIS:
- D inherits from B and C
- B and C both inherit from A
- Which method() gets called?
- MRO ensures: D → B → C → A → object
- B's method() is called (first in inheritance list)
""")

# EXAMPLE 2: Complex MRO with super() Chain
print("\n--- EXAMPLE 2: super() Chain Following MRO ---")

class A:
    def __init__(self):
        print("A.__init__")
        super().__init__()

class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()

class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D.__init__")
        super().__init__()

print("Complex inheritance: D(B, C), B(A), C(A)")
print(f"MRO: {D.__mro__}")
print("Creating D() - super() follows MRO:")
d = D()

# EXAMPLE 3: MRO with Method Calls
print("\n--- EXAMPLE 3: MRO with Method Calls ---")

class Logger:
    def log(self, message):
        print(f"Logger: {message}")

class FileHandler(Logger):
    def log(self, message):
        print(f"FileHandler: Writing to file - {message}")
        super().log(message)

class ConsoleHandler(Logger):
    def log(self, message):
        print(f"ConsoleHandler: Writing to console - {message}")
        super().log(message)

class MultiHandler(FileHandler, ConsoleHandler):
    def log(self, message):
        print(f"MultiHandler: Starting multi-log - {message}")
        super().log(message)

print("Multi-inheritance logging system")
print(f"MRO: {MultiHandler.__mro__}")
print("Calling multi_handler.log():")
multi = MultiHandler()
multi.log("Test message")

# EXAMPLE 4: MRO Inspection and Debugging
print("\n--- EXAMPLE 4: MRO Inspection ---")

class Base:
    def show_info(self):
        return f"Base class"

class Mixin1:
    def show_info(self):
        return f"Mixin1: {super().show_info()}"

class Mixin2:
    def show_info(self):
        return f"Mixin2: {super().show_info()}"

class Derived(Mixin1, Mixin2, Base):
    def show_info(self):
        return f"Derived: {super().show_info()}"

print("Mixin pattern with MRO")
print(f"MRO: {Derived.__mro__}")
derived = Derived()
print(f"Result: {derived.show_info()}")

# MRO Debugging
print("\nMRO Analysis:")
for i, cls in enumerate(Derived.__mro__):
    print(f"{i}: {cls.__name__}")

print("""
MRO INSPECTION TOOLS:
- ClassName.__mro__ (tuple of classes)
- ClassName.mro() (same as __mro__)
- super() follows MRO automatically
- Check MRO when debugging inheritance
""")

# ================================================================================
# SECTION 2: COOPERATIVE INHERITANCE PATTERNS
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 2: COOPERATIVE INHERITANCE PATTERNS")
print("=" * 80)

# PATTERN 1: Template Method with super()
print("\n--- PATTERN 1: Template Method Pattern ---")

class DataProcessor:
    """Template method pattern using cooperative inheritance"""

    def process(self):
        """Template method - defines algorithm structure"""
        self.validate_input()
        data = self.load_data()
        processed = self.transform_data(data)
        self.save_data(processed)
        self.cleanup()

    def validate_input(self):
        """Hook method - can be overridden"""
        print("Default validation")

    def load_data(self):
        """Abstract method - must be overridden"""
        raise NotImplementedError

    def transform_data(self, data):
        """Hook method - can be overridden"""
        return data.upper()

    def save_data(self, data):
        """Abstract method - must be overridden"""
        raise NotImplementedError

    def cleanup(self):
        """Hook method - can be overridden"""
        print("Default cleanup")

class CSVProcessor(DataProcessor):
    def load_data(self):
        return "name,age\nAli,25\nSara,30"

    def transform_data(self, data):
        # Extend parent's transformation
        data = super().transform_data(data)
        return data.replace(',', ' | ')

    def save_data(self, data):
        print(f"Saving CSV: {data}")

    def cleanup(self):
        super().cleanup()
        print("CSV cleanup complete")

class JSONProcessor(DataProcessor):
    def validate_input(self):
        super().validate_input()
        print("JSON-specific validation")

    def load_data(self):
        return '{"users": [{"name": "Ali", "age": 25}]}'

    def transform_data(self, data):
        data = super().transform_data(data)
        return f"JSON: {data}"

    def save_data(self, data):
        print(f"Saving JSON: {data}")

print("Template Method with cooperative inheritance:")
csv_proc = CSVProcessor()
csv_proc.process()

print("\nJSON processor:")
json_proc = JSONProcessor()
json_proc.process()

# PATTERN 2: Chain of Responsibility
print("\n--- PATTERN 2: Chain of Responsibility ---")

class Handler:
    """Base handler in chain of responsibility"""

    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        """Handle request or pass to successor"""
        if self.can_handle(request):
            return self.process_request(request)
        elif self.successor:
            return self.successor.handle_request(request)
        else:
            return f"No handler found for: {request}"

    def can_handle(self, request):
        """Check if this handler can process the request"""
        return False

    def process_request(self, request):
        """Process the request"""
        return f"Processed by {self.__class__.__name__}"

class AuthenticationHandler(Handler):
    def can_handle(self, request):
        return request.get('action') == 'login'

    def process_request(self, request):
        return f"Authentication: User {request.get('user')} logged in"

class AuthorizationHandler(Handler):
    def can_handle(self, request):
        return request.get('action') == 'access'

    def process_request(self, request):
        return f"Authorization: Access granted to {request.get('resource')}"

class LoggingHandler(Handler):
    def can_handle(self, request):
        return True  # Can handle any request

    def process_request(self, request):
        result = super().process_request(request)
        print(f"LOG: {result}")
        return result

# Create chain: Logging -> Auth -> Authorization
chain = LoggingHandler(AuthenticationHandler(AuthorizationHandler()))

requests = [
    {'action': 'login', 'user': 'admin'},
    {'action': 'access', 'resource': 'admin_panel'},
    {'action': 'unknown', 'data': 'test'}
]

print("Chain of Responsibility:")
for req in requests:
    result = chain.handle_request(req)
    print(f"Result: {result}\n")

# ================================================================================
# SECTION 3: MIXIN PATTERNS AND MULTIPLE INHERITANCE
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 3: MIXIN PATTERNS AND MULTIPLE INHERITANCE")
print("=" * 80)

# MIXIN PATTERN 1: Functionality Mixins
print("\n--- MIXIN PATTERN 1: Functionality Mixins ---")

class LoggerMixin:
    """Mixin for logging functionality"""
    def log(self, message, level="INFO"):
        print(f"[{level}] {self.__class__.__name__}: {message}")

class SerializerMixin:
    """Mixin for serialization"""
    def to_dict(self):
        return {k: v for k, v in self.__dict__.items()
                if not k.startswith('_')}

    def to_json(self):
        import json
        return json.dumps(self.to_dict())

class ValidatorMixin:
    """Mixin for validation"""
    def validate(self):
        """Validate object state"""
        errors = []
        for attr, value in self.__dict__.items():
            if attr.startswith('_'):
                continue
            error = self._validate_field(attr, value)
            if error:
                errors.append(error)
        return errors

    def _validate_field(self, attr, value):
        """Override in subclasses for custom validation"""
        return None

class User(LoggerMixin, SerializerMixin, ValidatorMixin):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def _validate_field(self, attr, value):
        if attr == 'email' and '@' not in str(value):
            return f"Invalid email: {value}"
        if attr == 'age' and not isinstance(value, int):
            return f"Age must be integer: {value}"
        return None

class Product(LoggerMixin, SerializerMixin, ValidatorMixin):
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def _validate_field(self, attr, value):
        if attr == 'price' and value < 0:
            return f"Price cannot be negative: {value}"
        if attr == 'stock' and value < 0:
            return f"Stock cannot be negative: {value}"
        return None

print("Mixin pattern examples:")
user = User("Ali", "ali@example.com", 25)
product = Product("Laptop", 999.99, 10)

# Test mixins
user.log("User created")
print(f"User JSON: {user.to_json()}")
print(f"User validation: {user.validate()}")

product.log("Product created", "DEBUG")
print(f"Product dict: {product.to_dict()}")
print(f"Product validation: {product.validate()}")

# MIXIN PATTERN 2: Ordered Mixins
print("\n--- MIXIN PATTERN 2: Ordered Mixins ---")

class BeforeMixin:
    def process(self):
        print("BeforeMixin: Pre-processing")
        super().process()
        print("BeforeMixin: Post-processing")

class AfterMixin:
    def process(self):
        print("AfterMixin: Pre-processing")
        super().process()
        print("AfterMixin: Post-processing")

class CoreProcessor:
    def process(self):
        print("CoreProcessor: Main processing")

# Different mixin orders create different behaviors
class Processor1(BeforeMixin, AfterMixin, CoreProcessor):
    pass

class Processor2(AfterMixin, BeforeMixin, CoreProcessor):
    pass

print("Ordered mixins - different orders:")
print("Processor1 (BeforeMixin, AfterMixin, CoreProcessor):")
print(f"MRO: {[cls.__name__ for cls in Processor1.__mro__]}")
p1 = Processor1()
p1.process()

print("\nProcessor2 (AfterMixin, BeforeMixin, CoreProcessor):")
print(f"MRO: {[cls.__name__ for cls in Processor2.__mro__]}")
p2 = Processor2()
p2.process()

# ================================================================================
# SECTION 4: ADVANCED super() TECHNIQUES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 4: ADVANCED super() TECHNIQUES")
print("=" * 80)

# TECHNIQUE 1: super() with Arguments
print("\n--- TECHNIQUE 1: super() with Specific Class ---")

class A:
    def __init__(self, x):
        self.x = x
        print(f"A.__init__({x})")

class B(A):
    def __init__(self, x, y):
        self.y = y
        # Call specific parent method, not following MRO
        super(B, self).__init__(x)  # Explicitly call A.__init__
        print(f"B.__init__({x}, {y})")

class C(A):
    def __init__(self, x, z):
        self.z = z
        super().__init__(x)
        print(f"C.__init__({x}, {z})")

class D(B, C):
    def __init__(self, x, y, z):
        # Complex initialization order
        super(D, self).__init__(x, y)  # Call B.__init__
        C.__init__(self, x, z)  # Directly call C.__init__
        print(f"D.__init__({x}, {y}, {z})")

print("super() with specific class calls:")
print(f"MRO: {D.__mro__}")
d = D(1, 2, 3)

# TECHNIQUE 2: super() in Class Methods
print("\n--- TECHNIQUE 2: super() in Class Methods ---")

class Base:
    @classmethod
    def create(cls, *args, **kwargs):
        print(f"{cls.__name__}.create called")
        return cls(*args, **kwargs)

    @staticmethod
    def get_info():
        return "Base info"

class Derived(Base):
    @classmethod
    def create(cls, *args, **kwargs):
        print(f"{cls.__name__}.create calling parent")
        # super() works in class methods too
        instance = super().create(*args, **kwargs)
        instance.initialized = True
        return instance

    @staticmethod
    def get_info():
        return f"Derived: {super(Derived, Derived).get_info()}"

print("super() in class methods:")
obj = Derived.create("test")
print(f"Object initialized: {obj.initialized}")
print(f"Info: {Derived.get_info()}")

# TECHNIQUE 3: Dynamic super() Resolution
print("\n--- TECHNIQUE 3: Dynamic super() Resolution ---")

class DynamicBase:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

class DynamicDerived(DynamicBase):
    def __init__(self, value, extra):
        super().__init__(value)  # Dynamic resolution
        self.extra = extra

    def get_value(self):
        base_value = super().get_value()
        return f"{base_value} + {self.extra}"

# Runtime inheritance change (advanced)
class NewBase:
    def get_value(self):
        return "New base value"

# Monkey patch for demonstration
def dynamic_super_demo():
    obj = DynamicDerived("original", "extra")
    print(f"Normal: {obj.get_value()}")

    # Simulate dynamic inheritance change
    DynamicDerived.__bases__ = (NewBase,)
    obj2 = DynamicDerived("changed", "extra")
    print(f"After base change: {obj2.get_value()}")

print("Dynamic super() resolution:")
dynamic_super_demo()

# ================================================================================
# SECTION 5: COMPLEX MULTIPLE INHERITANCE SCENARIOS
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 5: COMPLEX MULTIPLE INHERITANCE SCENARIOS")
print("=" * 80)

# SCENARIO 1: Complex Diamond with Cross-Calling
print("\n--- SCENARIO 1: Complex Diamond ---")

class Root:
    def __init__(self, name):
        self.name = name
        print(f"Root.__init__({name})")

    def method(self):
        return f"Root: {self.name}"

class Left(Root):
    def __init__(self, name, left_data):
        super().__init__(name)
        self.left_data = left_data
        print(f"Left.__init__({name}, {left_data})")

    def method(self):
        return f"Left({super().method()}, {self.left_data})"

class Right(Root):
    def __init__(self, name, right_data):
        super().__init__(name)
        self.right_data = right_data
        print(f"Right.__init__({name}, {right_data})")

    def method(self):
        return f"Right({super().method()}, {self.right_data})"

class Bottom(Left, Right):
    def __init__(self, name, left_data, right_data, bottom_data):
        # Complex initialization - call both parents
        Left.__init__(self, name, left_data)
        Right.__init__(self, name, right_data)
        self.bottom_data = bottom_data
        print(f"Bottom.__init__({name}, {left_data}, {right_data}, {bottom_data})")

    def method(self):
        left_result = Left.method(self)
        right_result = Right.method(self)
        return f"Bottom({left_result}, {right_result}, {self.bottom_data})"

print("Complex diamond inheritance:")
print(f"MRO: {Bottom.__mro__}")
bottom = Bottom("test", "L", "R", "B")
print(f"Method result: {bottom.method()}")

# SCENARIO 2: Mixin Composition
print("\n--- SCENARIO 2: Mixin Composition ---")

class EventEmitter:
    """Mixin for event handling"""
    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        if event not in self._listeners:
            self._listeners[event] = []
        self._listeners[event].append(callback)

    def emit(self, event, *args, **kwargs):
        if event in self._listeners:
            for callback in self._listeners[event]:
                callback(*args, **kwargs)

class PersistenceMixin:
    """Mixin for data persistence"""
    def __init__(self):
        self._data = {}

    def save(self, key, value):
        self._data[key] = value
        self.emit('saved', key, value)  # Emit event

    def load(self, key):
        return self._data.get(key)

class ValidationMixin:
    """Mixin for data validation"""
    def validate(self, data):
        """Basic validation - override for custom logic"""
        return len(str(data)) > 0

    def save_with_validation(self, key, value):
        if self.validate(value):
            self.save(key, value)
            return True
        return False

class DataManager(EventEmitter, PersistenceMixin, ValidationMixin):
    """Combines multiple mixins"""
    def __init__(self):
        EventEmitter.__init__(self)
        PersistenceMixin.__init__(self)

    def validate(self, data):
        # Custom validation
        return isinstance(data, (str, int, float)) and len(str(data)) > 2

# Usage
manager = DataManager()
manager.on('saved', lambda k, v: print(f"Saved: {k} = {v}"))

print("Mixin composition:")
print(f"Save 'test': {manager.save_with_validation('key1', 'test')}")
print(f"Save 'x': {manager.save_with_validation('key2', 'x')}")  # Too short
print(f"Load 'key1': {manager.load('key1')}")

# ================================================================================
# SECTION 6: INHERITANCE ANTI-PATTERNS AND SOLUTIONS
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 6: INHERITANCE ANTI-PATTERNS AND SOLUTIONS")
print("=" * 80)

print("""
ANTI-PATTERN 1: Deep Inheritance Chains
❌ Problem: Too many inheritance levels
class A: pass
class B(A): pass
class C(B): pass
class D(C): pass  # Too deep!

✅ Solution: Use composition or limit to 2-3 levels
class Component: pass
class Composite:
    def __init__(self):
        self.component = Component()
""")

# ANTI-PATTERN 2: Multiple Inheritance Abuse
print("""
ANTI-PATTERN 2: Multiple Inheritance Abuse
❌ Problem: Too many parents, confusing MRO
class Monster(Dragon, Wolf, Vampire, Ghost): pass

✅ Solution: Use mixins or composition
class Monster(Dragon, AttackMixin, DefenseMixin): pass
""")

# ANTI-PATTERN 3: God Classes
print("""
ANTI-PATTERN 3: God Classes
❌ Problem: Parent class does everything
class GameObject:  # Does rendering, physics, AI, sound...
    pass

✅ Solution: Split into focused classes
class Renderable: pass
class Physical: pass
class Intelligent: pass
class GameObject(Renderable, Physical, Intelligent): pass
""")

# ANTI-PATTERN 4: Inheritance for Code Reuse Only
print("""
ANTI-PATTERN 4: Inheritance for Code Reuse Only
❌ Problem: Inheriting just to reuse code
class Car(Vehicle):  # Only need Vehicle.drive()
    pass

✅ Solution: Use composition
class Car:
    def __init__(self):
        self.engine = Engine()
    def drive(self):
        return self.engine.drive()
""")

# ANTI-PATTERN 5: Breaking Liskov Substitution Principle
print("""
ANTI-PATTERN 5: Breaking LSP
❌ Problem: Subclass doesn't behave like parent
class Rectangle:
    def set_width(self, w): self.width = w
    def set_height(self, h): self.height = h

class Square(Rectangle):  # Wrong!
    def set_width(self, w):
        self.width = w
        self.height = w  # Square constraint

✅ Solution: Don't inherit if behavior changes
class Square:
    def __init__(self, side):
        self.side = side
""")

# ================================================================================
# SECTION 7: PRACTICAL ADVANCED INHERITANCE EXAMPLES
# ================================================================================

print("\n" + "=" * 80)
print("SECTION 7: PRACTICAL ADVANCED INHERITANCE EXAMPLES")
print("=" * 80)

# EXAMPLE 1: Plugin Architecture
print("\n--- EXAMPLE 1: Plugin Architecture ---")

class Plugin:
    """Base plugin class"""
    def __init__(self, name):
        self.name = name

    def initialize(self, app):
        """Called when plugin loads"""
        pass

    def process_request(self, request):
        """Process request - return None to pass to next plugin"""
        return None

    def shutdown(self):
        """Called when plugin unloads"""
        pass

class LoggingPlugin(Plugin):
    def process_request(self, request):
        print(f"LOG: {request}")
        return None  # Continue to next plugin

class AuthenticationPlugin(Plugin):
    def __init__(self, name):
        super().__init__(name)
        self.users = {'admin': 'pass123'}

    def process_request(self, request):
        if request.get('action') == 'login':
            user = request.get('user')
            password = request.get('password')
            if self.users.get(user) == password:
                request['authenticated'] = True
                print(f"AUTH: {user} logged in")
            else:
                request['error'] = 'Invalid credentials'
                return request  # Stop processing
        return None

class AuthorizationPlugin(Plugin):
    def process_request(self, request):
        if request.get('authenticated') and request.get('action') == 'admin':
            if request.get('user') == 'admin':
                print("AUTHZ: Admin access granted")
            else:
                request['error'] = 'Access denied'
                return request
        return None

class PluginManager:
    """Manages plugins using inheritance and MRO"""
    def __init__(self):
        self.plugins = []

    def add_plugin(self, plugin):
        self.plugins.append(plugin)

    def process_request(self, request):
        """Process through plugin chain"""
        for plugin in self.plugins:
            result = plugin.process_request(request)
            if result is not None:  # Plugin handled request
                return result
        return request

# Usage
manager = PluginManager()
manager.add_plugin(LoggingPlugin("logger"))
manager.add_plugin(AuthenticationPlugin("auth"))
manager.add_plugin(AuthorizationPlugin("authz"))

requests = [
    {'action': 'login', 'user': 'admin', 'password': 'pass123'},
    {'action': 'admin', 'user': 'admin'},
    {'action': 'login', 'user': 'admin', 'password': 'wrong'}
]

print("Plugin architecture:")
for req in requests:
    result = manager.process_request(req.copy())
    print(f"Result: {result}\n")

# EXAMPLE 2: State Pattern with Inheritance
print("\n--- EXAMPLE 2: State Pattern ---")

class TCPState:
    """Base state class"""
    def __init__(self, connection):
        self.connection = connection

    def connect(self):
        raise NotImplementedError

    def send(self, data):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

class ClosedState(TCPState):
    def connect(self):
        print("Connecting...")
        self.connection.state = ListeningState(self.connection)

    def send(self, data):
        print("Cannot send: connection closed")

    def close(self):
        print("Already closed")

class ListeningState(TCPState):
    def connect(self):
        print("Already listening")

    def send(self, data):
        print(f"Sending: {data}")
        self.connection.state = EstablishedState(self.connection)

    def close(self):
        print("Closing connection")
        self.connection.state = ClosedState(self.connection)

class EstablishedState(TCPState):
    def connect(self):
        print("Already connected")

    def send(self, data):
        print(f"Sending: {data}")

    def close(self):
        print("Closing established connection")
        self.connection.state = ClosedState(self.connection)

class TCPConnection:
    """State pattern using inheritance"""
    def __init__(self):
        self.state = ClosedState(self)

    def connect(self):
        self.state.connect()

    def send(self, data):
        self.state.send(data)

    def close(self):
        self.state.close()

# Usage
conn = TCPConnection()
print("TCP State Pattern:")
conn.send("hello")  # Should fail
conn.connect()
conn.send("hello")  # Should work
conn.close()

# ================================================================================
# SUMMARY
# ================================================================================

print("\n" + "=" * 80)
print("ADVANCED INHERITANCE CONCEPTS SUMMARY")
print("=" * 80)

print("""
WHAT YOU LEARNED:

1. METHOD RESOLUTION ORDER (MRO):
   - Order Python searches for methods
   - C3 Linearization algorithm
   - Critical for multiple inheritance
   - Check with __mro__

2. COOPERATIVE INHERITANCE:
   - super() chains following MRO
   - Template Method pattern
   - Chain of Responsibility pattern

3. MIXIN PATTERNS:
   - Multiple inheritance for functionality
   - Ordered mixins for different behaviors
   - Composition over inheritance

4. ADVANCED super() TECHNIQUES:
   - super() with specific class arguments
   - super() in class methods
   - Dynamic resolution

5. COMPLEX SCENARIOS:
   - Diamond problem solutions
   - Cross-calling in multiple inheritance
   - Plugin architectures

6. ANTI-PATTERNS:
   - Deep inheritance chains
   - Multiple inheritance abuse
   - God classes
   - Inheritance for code reuse only
   - Breaking LSP

KEY TAKEAWAYS:
- MRO is crucial for understanding inheritance
- Use super() for cooperative inheritance
- Prefer mixins over deep inheritance
- Check MRO when debugging
- Avoid inheritance anti-patterns

This file provides advanced inheritance concepts beyond the basic file 05.
Use this for complex inheritance scenarios and MRO debugging.
""")