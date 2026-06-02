"""
╔════════════════════════════════════════════════════════════════════════════╗
║            PYTHON TUPLES - LEARN WITH SIMPLE PROGRAMS                      ║
║            Run each program to understand Tuples & Immutability            ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 1: What is a Tuple? (Ordered, Immutable Collection)
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 1: What is a Tuple?")
print("="*70)

# Creating a tuple
fruits = ('apple', 'banana', 'orange', 'mango')
print(f"Tuple: {fruits}")
print(f"Type: {type(fruits)}")
print(f"First element: {fruits[0]}")
print(f"Last element: {fruits[-1]}")
print(f"Length: {len(fruits)}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 2: Create Tuples in Different Ways
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 2: Create Tuples in Different Ways")
print("="*70)

# Way 1: Direct creation with parentheses
tuple1 = (1, 2, 3, 4, 5)
print(f"Way 1 - With parentheses: {tuple1}")

# Way 2: Without parentheses
tuple2 = 1, 2, 3, 4, 5
print(f"Way 2 - Without parentheses: {tuple2}")

# Way 3: Mixed data types
tuple3 = (1, 'hello', 3.14, True, None)
print(f"Way 3 - Mixed types: {tuple3}")

# Way 4: Nested tuples
tuple4 = ((1, 2), ('a', 'b'), (10, 20))
print(f"Way 4 - Nested: {tuple4}")

# Way 5: Single element tuple (comma is important!)
tuple5 = (42,)
print(f"Way 5 - Single element: {tuple5}")

# Way 6: Empty tuple
tuple6 = ()
print(f"Way 6 - Empty: {tuple6}")

# Way 7: Using tuple() constructor
tuple7 = tuple('hello')
print(f"Way 7 - From string: {tuple7}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 3: Access Tuple Elements by Index
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 3: Access Elements by Index")
print("="*70)

numbers = (10, 20, 30, 40, 50)
print(f"Tuple: {numbers}")

print(f"\nPositive indexing:")
print(f"Index 0: {numbers[0]}")
print(f"Index 2: {numbers[2]}")
print(f"Index 4: {numbers[4]}")

print(f"\nNegative indexing (from end):")
print(f"Index -1 (last): {numbers[-1]}")
print(f"Index -2 (second last): {numbers[-2]}")
print(f"Index -5 (first): {numbers[-5]}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 4: Slice Tuples (Get Portions)
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 4: Slicing - Get Portions of Tuple")
print("="*70)

letters = ('a', 'b', 'c', 'd', 'e', 'f')
print(f"Original tuple: {letters}")

print(f"letters[1:4]: {letters[1:4]} (index 1 to 3)")
print(f"letters[:3]: {letters[:3]} (first 3 elements)")
print(f"letters[2:]: {letters[2:]} (from index 2 to end)")
print(f"letters[::2]: {letters[::2]} (every 2nd element)")
print(f"letters[::-1]: {letters[::-1]} (reversed)\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 5: Immutability - Cannot Modify Tuples
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 5: Immutability - Tuples Cannot Be Modified")
print("="*70)

my_tuple = (1, 2, 3, 4)
print(f"Original: {my_tuple}")

print("\nTrying to modify element (will cause error):")
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"❌ Error: {e}")

print("\nTrying to append (will cause error):")
try:
    my_tuple.append(5)
except AttributeError as e:
    print(f"❌ Error: {e}")

print("\nTrying to remove (will cause error):")
try:
    my_tuple.remove(2)
except AttributeError as e:
    print(f"❌ Error: {e}")

print("\nTrying to delete element (will cause error):")
try:
    del my_tuple[0]
except TypeError as e:
    print(f"❌ Error: {e}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 6: Tuple Unpacking
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 6: Tuple Unpacking - Assign to Multiple Variables")
print("="*70)

# Basic unpacking
coordinates = (10, 20)
x, y = coordinates
print(f"Coordinates: {coordinates}")
print(f"x = {x}, y = {y}")

# Unpacking multiple values
person = ('Alice', 25, 'Engineer')
name, age, job = person
print(f"\nPerson: {person}")
print(f"Name: {name}, Age: {age}, Job: {job}")

# Unpacking with *
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"\nNumbers: {numbers}")
print(f"First: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 7: Tuple Concatenation and Repetition
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 7: Concatenation and Repetition")
print("="*70)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation (+)
combined = tuple1 + tuple2
print(f"Tuple 1: {tuple1}")
print(f"Tuple 2: {tuple2}")
print(f"Concatenation: {combined}")

# Repetition (*)
repeated = tuple1 * 3
print(f"Repetition (×3): {repeated}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 8: Check if Element Exists
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 8: Check if Element Exists")
print("="*70)

colors = ('red', 'blue', 'green', 'yellow')
print(f"Tuple: {colors}")

print(f"'red' in colors: {'red' in colors}")
print(f"'purple' in colors: {'purple' in colors}")
print(f"'blue' not in colors: {'blue' not in colors}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 9: Find Index and Count Elements
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 9: Find Index and Count Elements")
print("="*70)

data = (10, 20, 30, 20, 40, 20)
print(f"Tuple: {data}")

# index() - find position
position = data.index(30)
print(f"Position of 30: {position}")

# count() - count occurrences
count = data.count(20)
print(f"Count of 20: {count}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 10: Loop Through Tuple
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 10: Loop Through Tuple")
print("="*70)

items = ('apple', 'banana', 'orange')
print(f"Tuple: {items}\n")

# Using for loop
print("Simple loop:")
for item in items:
    print(f"  - {item}")

# Using enumerate
print("\nWith index:")
for index, item in enumerate(items):
    print(f"  {index}: {item}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 11: Built-in Functions with Tuples
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 11: Built-in Functions (len, min, max, sum)")
print("="*70)

numbers = (5, 2, 8, 1, 9, 3)
print(f"Tuple: {numbers}")

print(f"len(tuple): {len(numbers)} - How many elements?")
print(f"min(tuple): {min(numbers)} - Smallest element")
print(f"max(tuple): {max(numbers)} - Largest element")
print(f"sum(tuple): {sum(numbers)} - Sum of all elements\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 12: Tuples as Dictionary Keys
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 12: Tuples as Dictionary Keys (Immutability Benefit)")
print("="*70)

# Can use tuple as key (immutable)
locations = {
    (10, 20): 'Point A',
    (30, 40): 'Point B',
    (50, 60): 'Point C'
}

print("Using tuples as dictionary keys:")
for key, value in locations.items():
    print(f"  {key} → {value}")

print(f"\nAccessing value: locations[(30, 40)] = {locations[(30, 40)]}")

# Cannot use list as key (mutable)
print("\nTrying to use list as key (will cause error):")
try:
    bad_dict = {[1, 2]: 'Point'}
except TypeError as e:
    print(f"❌ Error: {e}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 13: Tuples in Sets
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 13: Tuples in Sets (Immutability Benefit)")
print("="*70)

# Can use tuple as set element (immutable)
points = {(0, 0), (1, 1), (2, 2)}
print(f"Set of tuples: {points}")

# Cannot use list as set element (mutable)
print("\nTrying to add list to set (will cause error):")
try:
    bad_set = {[1, 2], [3, 4]}
except TypeError as e:
    print(f"❌ Error: {e}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 14: Real-World Example - GPS Coordinates
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 14: Real-World Example - GPS Coordinates")
print("="*70)

# Store locations as tuples
locations = [
    ('Delhi', (28.7041, 77.1025)),
    ('Mumbai', (19.0760, 72.8777)),
    ('Bangalore', (12.9716, 77.5946))
]

print("City Locations (Latitude, Longitude):")
for city, (lat, lon) in locations:
    print(f"  {city}: {lat}°N, {lon}°E")

# Immutability ensures coordinates can't be accidentally modified
coordinates = (28.7041, 77.1025)
print(f"\nOriginal coordinates: {coordinates}")
print("Coordinates are safe from accidental modification!\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 15: Real-World Example - Function Return Values
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 15: Real-World Example - Function Return Values")
print("="*70)

def get_student_info():
    """Function returns multiple values as tuple"""
    name = 'Alice'
    age = 20
    grade = 'A'
    return name, age, grade  # Returns tuple

# Calling function and unpacking
student_name, student_age, student_grade = get_student_info()
print(f"Function returned: get_student_info()")
print(f"Unpacked as: name={student_name}, age={student_age}, grade={student_grade}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 16: When to Use Tuples?
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 16: When to Use Tuples?")
print("="*70)

print("""
USE TUPLES WHEN YOU NEED:
  ✓ Immutable collection (cannot be modified)
  ✓ Safe from accidental changes
  ✓ Use as dictionary keys
  ✓ Use as set elements
  ✓ Return multiple values from function
  ✓ Create hashable objects
  ✓ Slightly better performance than lists

EXAMPLES:
  • Coordinates (latitude, longitude)
  • RGB colors (255, 128, 0)
  • Dictionary keys - coordinates or dates
  • Set elements - storing unique locations
  • Function return values
  • Database records (rows)
  • Configuration constants

DON'T USE TUPLES WHEN YOU NEED:
  ❌ To modify collection → Use List
  ❌ Add/remove elements → Use List
  ❌ Key-value pairs → Use Dictionary
  ❌ Unique elements only → Use Set

COMPARISON: LIST vs TUPLE
┌─────────────────┬────────────────┬──────────────────┐
│ Feature         │ List           │ Tuple            │
├─────────────────┼────────────────┼──────────────────┤
│ Mutable         │ Yes ✓          │ No ✗             │
│ Ordered         │ Yes ✓          │ Yes ✓            │
│ Dictionary Key  │ No ✗           │ Yes ✓            │
│ Set Element     │ No ✗           │ Yes ✓            │
│ Speed           │ Slower         │ Faster ✓         │
│ Methods         │ Many ✓         │ Few (2) ✗        │
│ Memory          │ More           │ Less ✓           │
└─────────────────┴────────────────┴──────────────────┘
""")

print("="*70)

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 17: Important Points to Remember
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("IMPORTANT POINTS TO REMEMBER")
print("="*70)

print("""
1. IMMUTABLE - Cannot be changed after creation
   ❌ tuple[0] = value       - ERROR
   ❌ tuple.append(value)   - ERROR
   ❌ tuple.remove(value)   - ERROR
   ❌ del tuple[0]          - ERROR

2. ORDERED - Elements have specific order
   tuple[0] is always the first element
   Order is preserved forever

3. INDEXED - Access by position (0, 1, 2, ...)
   ✓  tuple[0]    - First element
   ✓  tuple[-1]   - Last element
   ✓  tuple[1:4]  - Slice elements 1-3

4. SINGLE ELEMENT TUPLE needs comma!
   ✓  (42,)       - Correct tuple
   ❌  (42)       - Just a number in parentheses
   print(type((42,)))   # <class 'tuple'>
   print(type((42)))    # <class 'int'>

5. ONLY 2 METHODS AVAILABLE
   count(x)   - Count occurrences
   index(x)   - Find position

6. HASHABLE - Can be used as dict key or set element
   ✓  {(1,2): 'point'}     - Correct
   ✓  {(1,2)}              - Correct in set
   ❌  {[1,2]: 'point'}    - Error (list not hashable)
   ❌  {[1,2]}             - Error (list not hashable)

7. UNPACKING
   a, b, c = (1, 2, 3)           - Simple unpacking
   first, *rest = (1, 2, 3, 4)   - With *rest
   first, *middle, last = data   - Grab middle

8. OPERATIONS CREATE NEW TUPLE (Immutability)
   new_tuple = tuple1 + tuple2   - Concatenation
   new_tuple = tuple1 * 3        - Repetition
   Original tuples are unchanged!

9. CONVERTING TO OTHER TYPES
   list(tuple)       - Convert to list (mutable)
   set(tuple)        - Convert to set (unique)
   tuple(list)       - Convert to tuple (immutable)
   tuple(string)     - ('h','e','l','l','o')

10. WHY USE TUPLES?
    • Safety: Immutability prevents accidental changes
    • Performance: Slightly faster than lists
    • Dictionary keys: Lists can't be keys, tuples can
    • Set elements: Lists can't be in sets, tuples can
    • Multiple returns: Functions return multiple values
    • Clarity: Shows "don't modify this" intent
""")

print("="*70)
t1 = (1,2)
t2 = (3,4,5)
new = t1+t2
print(new)
print(id(t1))
print(id(t2))
print(id(new))

# Built-in functions - functions that work on iterables
#example - min(), max(), sorted(), etc.

#indexing can be used on tuples also similar to other iterables

#tuple methods - tuple class functions
a = (1,2,3,1,2,3)
print(a.count(1)) #count method
print(a.index(2)) #index method

# immutability behaviour of tuple

t = (1,[2,3])
#t[0] = 10 not supported
t[1][0] = 20 #supported
print(t)
#Tuples  does not support item assignment but if it is having mutable elements as members,
#Then the elements in them can be changed

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 18: UNPACKING TUPLES - Assign to Multiple Variables
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 18: UNPACKING TUPLES - Assign to Multiple Variables")
print("="*70)

# Basic unpacking
coords = (10, 20)
x, y = coords
print(f"Tuple: {coords}")
print(f"Unpacked: x={x}, y={y}")

# Multiple unpacking
person = ('Alice', 25, 'Engineer')
name, age, job = person
print(f"\nTuple: {person}")
print(f"Unpacked: name={name}, age={age}, job={job}")

# Unpacking with rest
data = (1, 2, 3, 4, 5)
first, *middle, last = data
print(f"\nTuple: {data}")
print(f"first={first}, middle={middle}, last={last}")

# Unpacking and swapping
a, b = (100, 200)
a, b = b, a
print(f"\nAfter swap: a={a}, b={b}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 19: CONVERT TUPLE TO OTHER DATA TYPES
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 19: CONVERT TUPLE → LIST / SET / STRING / DICT")
print("="*70)

original_tuple = (1, 2, 3, 4, 5)
print(f"Original Tuple: {original_tuple}")

# Convert to LIST
my_list = list(original_tuple)
print(f"\n✓ To List: {my_list}")
print(f"  Type: {type(my_list)}")
print(f"  Use when: Need to add/remove/modify elements")

# Convert to SET
my_set = set(original_tuple)
print(f"\n✓ To Set: {my_set}")
print(f"  Type: {type(my_set)}")
print(f"  Use when: Need unique elements only")

# Convert to STRING
my_string = str(original_tuple)
print(f"\n✓ To String: {my_string}")
print(f"  Type: {type(my_string)}")
print(f"  Use when: Need text representation")

# Convert to DICTIONARY
tuple_pairs = (('name', 'Alice'), ('age', 25), ('city', 'Delhi'))
my_dict = dict(tuple_pairs)
print(f"\n✓ To Dictionary (from pairs): {my_dict}")
print(f"  Type: {type(my_dict)}")
print(f"  Use when: Need key-value pairs\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 20: CONVERT OTHER TYPES TO TUPLE
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 20: CONVERT LIST / SET / STRING / DICT → TUPLE")
print("="*70)

# From LIST
my_list = [1, 2, 3, 4]
tuple_from_list = tuple(my_list)
print(f"From List: {my_list}")
print(f"To Tuple: {tuple_from_list}")
print(f"Use when: Need immutable version of list")

# From SET
my_set = {5, 2, 8, 1}
tuple_from_set = tuple(my_set)
print(f"\nFrom Set: {my_set}")
print(f"To Tuple: {tuple_from_set}")
print(f"Use when: Need ordered immutable collection")

# From STRING
my_string = "hello"
tuple_from_string = tuple(my_string)
print(f"\nFrom String: '{my_string}'")
print(f"To Tuple: {tuple_from_string}")
print(f"Use when: Need immutable character collection")

# From DICTIONARY
my_dict = {'name': 'Alice', 'age': 25}
tuple_keys = tuple(my_dict.keys())
tuple_values = tuple(my_dict.values())
print(f"\nFrom Dictionary: {my_dict}")
print(f"To Tuple (keys): {tuple_keys}")
print(f"To Tuple (values): {tuple_values}")
print(f"Use when: Need immutable key/value collection\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 21: WHEN TO CONVERT - DECISION GUIDE
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 21: WHEN TO CONVERT - DECISION GUIDE")
print("="*70)

print("""
CONVERSION SCENARIOS:

1. TUPLE → LIST (When to convert)
   ✓ Need to add/remove elements
   ✓ Need to modify elements
   ✓ Need list methods (append, insert, remove)
   Example:
   data = (1, 2, 3)
   data_list = list(data)
   data_list.append(4)


2. TUPLE → SET (When to convert)
   ✓ Need unique elements (remove duplicates)
   ✓ Need fast membership checking
   ✓ Need set operations (union, intersection)
   Example:
   items = (1, 2, 2, 3)
   unique = set(items)  # Output: {1, 2, 3}


3. TUPLE → STRING (When to convert)
   ✓ Need text representation
   ✓ Printing/displaying
   ✓ Saving to file
   Example:
   coords = (10, 20)
   text = str(coords)  # Output: '(10, 20)'


4. LIST → TUPLE (When to convert)
   ✓ Need immutable collection
   ✓ Use as dictionary key
   ✓ Use in set (list elements)
   ✓ Want faster performance
   ✓ Shared data (thread-safe)
   Example:
   tasks = [1, 2, 3]
   tasks_locked = tuple(tasks)


5. TUPLE IN MULTIPLE RETURNS (Already tuple!)
   ✓ Functions returning multiple values
   Example:
   def get_info():
       return 'Alice', 25, 'Engineer'  # Returns tuple


6. DICTIONARY ↔ TUPLE (Key consideration)
   ✓ dict(tuple_pairs) - convert to dict
   ✓ tuple(dict.items()) - convert to tuple
   Example:
   pairs = (('x', 1), ('y', 2))
   mapping = dict(pairs)
""")

print("="*70)

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 22: REAL EXAMPLE - Coordinate System with Conversions
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 22: REAL EXAMPLE - Coordinate Conversions")
print("="*70)

# Start with tuple (immutable coordinates)
point_tuple = (10, 20, 30)
print(f"Step 1 - Immutable point (TUPLE): {point_tuple}")

# Convert to list to modify
point_list = list(point_tuple)
point_list[2] = 35
print(f"Step 2 - Modify point (LIST): {point_list}")

# Convert back to tuple (immutable again)
point_tuple = tuple(point_list)
print(f"Step 3 - Lock point (TUPLE): {point_tuple}")

# Use as dictionary key
locations = {
    point_tuple: 'Laboratory',
    (5, 15, 25): 'Library'
}
print(f"Step 4 - Use as keys: {locations}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 23: CONVERSION QUICK REFERENCE TABLE
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 23: CONVERSION QUICK REFERENCE")
print("="*70)

print("""
TUPLE CONVERSIONS:

TUPLE → LIST           list(tuple)           → [1, 2, 3]
        ✓ Add/modify elements
        ✓ List methods available
        
TUPLE → SET            set(tuple)            → {1, 2, 3}
        ✓ Remove duplicates
        ✓ Fast lookup
        
TUPLE → STRING         str(tuple)            → '(1, 2, 3)'
        ✓ Text display
        ✓ File output
        
TUPLE → DICT           dict(tuple_pairs)     → {'a': 1, 'b': 2}
        ✓ Key-value mapping
        ✓ Fast lookup

LIST → TUPLE           tuple(list)           → (1, 2, 3)
        ✓ Immutability
        ✓ Dictionary key
        ✓ Better performance
        
SET → TUPLE            tuple(set)            → (1, 2, 3)
        ✓ Ordered version
        ✓ Indexed access
        
STRING → TUPLE         tuple(string)         → ('h', 'e', 'l', 'l', 'o')
        ✓ Character unpacking
        
DICT → TUPLE           tuple(dict.items())   → (('a', 1), ('b', 2))
        ✓ Preserve pairs
        ✓ Immutable mapping


UNPACKING EXAMPLES:
═════════════════════════════════════════════════════════════════

# Simple unpacking
x, y = (1, 2)

# With rest
first, *rest, last = (1, 2, 3, 4, 5)

# Nested unpacking
(a, b), (c, d) = ((1, 2), (3, 4))

# Swapping
a, b = b, a

# Function returns
name, age, job = get_person_info()
""")

print("="*70)
