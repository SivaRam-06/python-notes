"""
================================================================================
            OPERATOR OVERLOADING - ADVANCED 4
================================================================================

CONCEPT:
  Operator Overloading = Defining custom behavior for operators (+, -, *, etc.)
  Makes objects work naturally with Python operators

MOTTO: "Make objects behave like built-in types"

WHY?
  - More intuitive and readable code
  - Objects work like primitives
  - Better user experience

ANALOGY:
  Without: total = number.add(number2)
  With: total = number + number2  (more natural!)

================================================================================
                    COMMON OPERATOR OVERLOADING METHODS
================================================================================

__add__(self, other)        a + b
__sub__(self, other)        a - b
__mul__(self, other)        a * b
__truediv__(self, other)    a / b
__eq__(self, other)         a == b
__ne__(self, other)         a != b
__lt__(self, other)         a < b
__le__(self, other)         a <= b
__gt__(self, other)         a > b
__ge__(self, other)         a >= b
__len__(self)               len(a)
__str__(self)               str(a), print(a)
__repr__(self)              repr(a)
__getitem__(self, key)      a[key]
__setitem__(self, key, value) a[key] = value
__call__(self)              a()

================================================================================
"""

# ================================================================================
# SECTION 1: STRING REPRESENTATION OPERATORS
# ================================================================================

print("=" * 80)
print("SECTION 1: __str__ and __repr__ OPERATORS")
print("=" * 80)

class Point:
    """Basic Point class without operator overloading"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(3, 4)
print(f"Without __str__: {point}")
print(f"Type: {type(point)}")

print("\n--- NOW WITH __str__ ---\n")

class PointBetter:
    """Point with string representation"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """Called by str() and print()"""
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        """Called by repr() - should be detailed"""
        return f"PointBetter(x={self.x}, y={self.y})"


point2 = PointBetter(3, 4)
print(f"With __str__: {point2}")
print(f"With str(): {str(point2)}")
print(f"With repr(): {repr(point2)}")

print("""
__str__() vs __repr__():
__str__  - Human-readable (for end users)
__repr__ - Detailed representation (for developers)
""")


# ================================================================================
# SECTION 2: ARITHMETIC OPERATORS
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 2: ARITHMETIC OPERATORS (+, -, *, /)")
print("=" * 80)

class Complex_Number:
    """Complex number with arithmetic operators"""
    
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        """Implement a + b"""
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return Complex_Number(new_real, new_imag)
    
    def __sub__(self, other):
        """Implement a - b"""
        new_real = self.real - other.real
        new_imag = self.imag - other.imag
        return Complex_Number(new_real, new_imag)
    
    def __mul__(self, other):
        """Implement a * b"""
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        new_real = (self.real * other.real) - (self.imag * other.imag)
        new_imag = (self.real * other.imag) + (self.imag * other.real)
        return Complex_Number(new_real, new_imag)
    
    def __str__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"


c1 = Complex_Number(3, 4)
c2 = Complex_Number(1, 2)

print(f"c1 = {c1}")
print(f"c2 = {c2}")

result_add = c1 + c2
print(f"\nc1 + c2 = {result_add}")

result_sub = c1 - c2
print(f"c1 - c2 = {result_sub}")

result_mul = c1 * c2
print(f"c1 * c2 = {result_mul}")

print("""
ARITHMETIC OPERATORS:
__add__() for +
__sub__() for -
__mul__() for *
__truediv__() for /
__floordiv__() for //
__mod__() for %
__pow__() for **
""")


# ================================================================================
# SECTION 3: COMPARISON OPERATORS
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 3: COMPARISON OPERATORS (==, <, >, etc.)")
print("=" * 80)

class Student:
    """Student with comparison operators"""
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def __str__(self):
        return f"{self.name}({self.marks})"
    
    def __eq__(self, other):
        """Implement a == b"""
        return self.marks == other.marks
    
    def __lt__(self, other):
        """Implement a < b"""
        return self.marks < other.marks
    
    def __le__(self, other):
        """Implement a <= b"""
        return self.marks <= other.marks
    
    def __gt__(self, other):
        """Implement a > b"""
        return self.marks > other.marks
    
    def __ge__(self, other):
        """Implement a >= b"""
        return self.marks >= other.marks


s1 = Student("Ali", 85)
s2 = Student("Fatima", 92)
s3 = Student("Hassan", 85)

print(f"{s1} == {s3}: {s1 == s3}")
print(f"{s1} < {s2}: {s1 < s2}")
print(f"{s1} > {s2}: {s1 > s2}")
print(f"{s1} <= {s2}: {s1 <= s2}")

# Sort students by marks
students = [s2, s1, s3]
students.sort()
print(f"\nSorted by marks: {[str(s) for s in students]}")

print("""
COMPARISON OPERATORS:
__eq__() for ==
__ne__() for !=
__lt__() for <
__le__() for <=
__gt__() for >
__ge__() for >=
""")


# ===============================================================================
# SECTION 4: CONTAINER OPERATORS
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 4: CONTAINER OPERATORS (len, [], in, etc.)")
print("=" * 80)

class ShoppingCart:
    """Shopping cart with container operators"""
    
    def __init__(self):
        self.items = []
    
    def add_item(self, item, price):
        """Add item to cart"""
        self.items.append((item, price))
    
    def __len__(self):
        """Implement len(cart)"""
        return len(self.items)
    
    def __getitem__(self, index):
        """Implement cart[index]"""
        return self.items[index]
    
    def __setitem__(self, index, value):
        """Implement cart[index] = value"""
        self.items[index] = value
    
    def __contains__(self, item_name):
        """Implement 'item_name' in cart"""
        return any(item_name == item for item, price in self.items)
    
    def __str__(self):
        return f"Cart with {len(self)} items"


cart = ShoppingCart()
cart.add_item("Apple", 50)
cart.add_item("Banana", 30)
cart.add_item("Orange", 40)

print(f"Cart: {cart}")
print(f"Items in cart: {len(cart)}")
print(f"First item: {cart[0]}")
print(f"Second item: {cart[1]}")

print(f"\n'Apple' in cart: {'Apple' in cart}")
print(f"'Mango' in cart: {'Mango' in cart}")

# Modify item
cart[0] = ("Apple (Organic)", 60)
print(f"\nAfter modification - First item: {cart[0]}")

print("""
CONTAINER OPERATORS:
__len__() for len()
__getitem__() for obj[key]
__setitem__() for obj[key] = value
__contains__() for 'item' in obj
__iter__() for iteration
""")


# ===============================================================================
# SECTION 5: CALLABLE OBJECTS
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 5: __call__ - MAKING OBJECTS CALLABLE")
print("=" * 80)

class Multiplier:
    """Object that can be called like a function"""
    
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        """Make object callable using ()"""
        return x * self.factor


double = Multiplier(2)
triple = Multiplier(3)

print(f"double(5) = {double(5)}")
print(f"double(10) = {double(10)}")
print(f"triple(5) = {triple(5)}")

print("""
__call__() USAGE:
- Makes object work like a function
- Can create function-like objects
- Useful for closures and decorators
""")


# ===============================================================================
# SECTION 6: REAL WORLD - VECTOR CLASS
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 6: REAL WORLD - VECTOR CLASS")
print("=" * 80)

import math

class Vector:
    """2D Vector with complete operator overloading"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
    
    # Arithmetic
    def __add__(self, other):
        """Vector addition"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Vector subtraction"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Scalar multiplication"""
        return Vector(self.x * scalar, self.y * scalar)
    
    # Comparison
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # Utility
    def __len__(self):
        """Magnitude of vector"""
        return math.sqrt(self.x**2 + self.y**2)


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")

print(f"\nv1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")

print(f"\nMagnitude of v1: {len(v1):.2f}")
print(f"v1 == v2: {v1 == v2}")


# ===============================================================================
# SECTION 7: MONEY/CURRENCY EXAMPLE
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 7: REAL WORLD - MONEY CLASS")
print("=" * 80)

class Money:
    """Money with operator overloading"""
    
    def __init__(self, amount, currency="PKR"):
        self.amount = amount
        self.currency = currency
    
    def __str__(self):
        return f"{self.currency} {self.amount}"
    
    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"
    
    def __add__(self, other):
        """Add money"""
        if self.currency != other.currency:
            raise ValueError("Different currencies!")
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other):
        """Subtract money"""
        if self.currency != other.currency:
            raise ValueError("Different currencies!")
        return Money(self.amount - other.amount, self.currency)
    
    def __mul__(self, factor):
        """Multiply money"""
        return Money(self.amount * factor, self.currency)
    
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency
    
    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Different currencies!")
        return self.amount < other.amount
    
    def __gt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Different currencies!")
        return self.amount > other.amount


m1 = Money(1000, "PKR")
m2 = Money(500, "PKR")

print(f"m1 = {m1}")
print(f"m2 = {m2}")

print(f"\nm1 + m2 = {m1 + m2}")
print(f"m1 - m2 = {m1 - m2}")
print(f"m1 * 2 = {m1 * 2}")

print(f"\nm1 > m2: {m1 > m2}")
print(f"m1 > Money(2000, 'PKR'): {m1 > Money(2000, 'PKR')}")


# ===============================================================================
# SECTION 8: BEST PRACTICES
# ===============================================================================

print("\n" + "=" * 80)
print("SECTION 8: BEST PRACTICES FOR OPERATOR OVERLOADING")
print("=" * 80)

print("""
BEST PRACTICES:

1. USE SENSIBLE OPERATORS:
   ✓ Use operators that make natural sense
   ✓ + for combining, - for removing
   ✓ * for scaling
   ✗ Don't use + for something that doesn't make sense for combining

2. RETURN APPROPRIATE TYPES:
   - For arithmetic: Return same or compatible type
   - For comparison: Return boolean
   - For container: Return appropriate values

3. MAINTAIN CONSISTENCY:
   ✓ If __eq__() is implemented, implement others
   ✓ If a == b is True, then a <= b and a >= b should be True
   ✓ Operator behavior should be predictable

4. HANDLE EDGE CASES:
   ✓ Check types before operations
   ✓ Raise appropriate exceptions
   ✓ Handle None values

5. DOCUMENT YOUR OPERATORS:
   ✓ Write clear docstrings
   ✓ Explain what each operator does
   ✓ Provide examples

6. DON'T OVERLOAD FOR NO REASON:
   ✗ Only use if it improves readability
   ✗ Avoid confusing implementations
   ✗ Keep operators intuitive

COMMON PATTERNS:

Pattern 1: Numeric Type
class Complex:
    def __add__(self, other):
        # Add two complex numbers
        pass

Pattern 2: Container Type
class CustomList:
    def __getitem__(self, index):
        # Get item by index
        pass

Pattern 3: Comparable Type
class Comparable:
    def __eq__(self, other):
        # Check equality
        pass
    def __lt__(self, other):
        # Check less than
        pass

OPERATORS TO RARELY USE:
- Don't overload bitwise operators (&, |) for non-bitwise operations
- Don't use ** for anything but exponentiation
- Avoid using / for non-division operations
""")
