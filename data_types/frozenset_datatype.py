"""
╔════════════════════════════════════════════════════════════════════════════╗
║            PYTHON FROZENSETS - LEARN WITH SIMPLE PROGRAMS                  ║
║                 Run each program to understand Frozensets                   ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 1: What is a Frozenset? (Immutable version of set)
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 1: What is a Frozenset?")
print("="*70)

# Regular set (mutable - can be changed)
regular_set = {1, 2, 3}
print(f"Regular set: {regular_set}")
print(f"Type: {type(regular_set)}")

# Frozenset (immutable - cannot be changed)
frozen_set = frozenset({1, 2, 3})
print(f"\nFrozen set: {frozen_set}")
print(f"Type: {type(frozen_set)}")

print("\nKey difference: Frozenset is IMMUTABLE (cannot be modified)\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 2: Create Frozensets in Different Ways
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 2: Create Frozensets in Different Ways")
print("="*70)

# Way 1: From a set
fs1 = frozenset({10, 20, 30})
print(f"Way 1 - From set: {fs1}")

# Way 2: From a list
fs2 = frozenset([1, 2, 2, 3, 3])
print(f"Way 2 - From list [1,2,2,3,3]: {fs2}")
print(f"Notice: Duplicates removed!")

# Way 3: From a string
fs3 = frozenset('hello')
print(f"Way 3 - From string 'hello': {fs3}")

# Way 4: From a tuple
fs4 = frozenset((5, 10, 15))
print(f"Way 4 - From tuple (5,10,15): {fs4}")

# Way 5: Empty frozenset
fs5 = frozenset()
print(f"Way 5 - Empty frozenset: {fs5}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 3: Why Frozensets? (Can be used as dictionary keys)
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 3: Frozensets as Dictionary Keys (Regular sets CANNOT!)")
print("="*70)

# ❌ Regular set as key - ERROR!
print("Trying regular set as dictionary key:")
try:
    my_dict = {{1, 2}: 'value'}
    print("Success!")
except TypeError as e:
    print(f"❌ ERROR: {e}")

# ✓ Frozenset as key - WORKS!
print("\nUsing frozenset as dictionary key:")
my_dict = {frozenset({1, 2}): 'value1', frozenset({3, 4}): 'value2'}
print(f"✓ Success! Dictionary: {my_dict}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 4: Why Frozensets? (Can be element of another set)
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 4: Frozensets as Elements of Another Set (Regular sets CANNOT!)")
print("="*70)

# ❌ Regular set inside another set - ERROR!
print("Trying regular set inside another set:")
try:
    my_set = {{1, 2}, {3, 4}}
    print("Success!")
except TypeError as e:
    print(f"❌ ERROR: {e}")

# ✓ Frozenset inside another set - WORKS!
print("\nUsing frozenset inside another set:")
my_set = {frozenset({1, 2}), frozenset({3, 4}), frozenset({5, 6})}
print(f"✓ Success! Set of frozensets: {my_set}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 5: Frozenset is IMMUTABLE (Cannot add/remove/modify)
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 5: Frozensets are IMMUTABLE (Cannot be modified)")
print("="*70)

fs = frozenset({10, 20, 30})
print(f"Frozenset: {fs}")

# Try to add - ERROR!
print("\nTrying to add element:")
try:
    fs.add(40)
except AttributeError as e:
    print(f"❌ ERROR: {e}")

# Try to remove - ERROR!
print("\nTrying to remove element:")
try:
    fs.remove(10)
except AttributeError as e:
    print(f"❌ ERROR: {e}")

print("\n✓ Frozensets cannot be modified! They are frozen/immutable!\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 6: Frozenset Set Operations (Union, Intersection, Difference)
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 6: Frozenset Operations (Union, Intersection, Difference)")
print("="*70)

fs1 = frozenset({1, 2, 3, 4})
fs2 = frozenset({3, 4, 5, 6})

print(f"Frozenset 1: {fs1}")
print(f"Frozenset 2: {fs2}")

# Union
union = fs1 | fs2
print(f"\nUnion (|): {union}")

# Intersection
intersection = fs1 & fs2
print(f"Intersection (&): {intersection}")

# Difference
difference = fs1 - fs2
print(f"Difference (-): {difference}")

# Symmetric Difference
sym_diff = fs1 ^ fs2
print(f"Symmetric Difference (^): {sym_diff}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 7: Frozenset Built-in Functions
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 7: Built-in Functions (len, min, max, sum)")
print("="*70)

fs = frozenset({5, 2, 8, 1, 9})
print(f"Frozenset: {fs}")

print(f"len(fs): {len(fs)} - How many elements?")
print(f"min(fs): {min(fs)} - Smallest element")
print(f"max(fs): {max(fs)} - Largest element")
print(f"sum(fs): {sum(fs)} - Sum of all elements")
print(f"sorted(fs): {sorted(fs)} - Convert to sorted list\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 8: Check if Element Exists (in operator)
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 8: Check if Element Exists")
print("="*70)

colors = frozenset({'red', 'green', 'blue', 'yellow'})
print(f"Frozenset: {colors}")

print(f"'red' in colors: {'red' in colors}")
print(f"'purple' in colors: {'purple' in colors}")
print(f"'blue' not in colors: {'blue' not in colors}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 9: Loop Through Frozenset
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 9: Loop Through Frozenset")
print("="*70)

animals = frozenset({'dog', 'cat', 'bird', 'fish'})
print(f"Frozenset: {animals}")
print("Loop through frozenset:")

for animal in animals:
    print(f"  - {animal}")

print()

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 10: Frozenset Comparison (subset, superset, equal)
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 10: Frozenset Comparison")
print("="*70)

fs1 = frozenset({1, 2})
fs2 = frozenset({1, 2, 3, 4})

print(f"fs1: {fs1}")
print(f"fs2: {fs2}")

print(f"\nfs1 <= fs2 (is fs1 a subset?): {fs1 <= fs2}")
print(f"fs2 >= fs1 (is fs2 a superset?): {fs2 >= fs1}")
print(f"fs1 == fs1 (are they equal?): {fs1 == fs1}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 11: Frozenset Methods (only read operations allowed)
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 11: Frozenset Methods (only for reading, not modifying)")
print("="*70)

fs1 = frozenset({1, 2, 3, 4})
fs2 = frozenset({3, 4, 5, 6})

# copy() method
copied = fs1.copy()
print(f"copy(): {copied}")

# union() method
union = fs1.union(fs2)
print(f"union(): {union}")

# intersection() method
intersection = fs1.intersection(fs2)
print(f"intersection(): {intersection}")

# difference() method
difference = fs1.difference(fs2)
print(f"difference(): {difference}")

# symmetric_difference() method
sym_diff = fs1.symmetric_difference(fs2)
print(f"symmetric_difference(): {sym_diff}")

# issubset() method
is_subset = fs1.issubset(fs2)
print(f"issubset(): {is_subset}")

# issuperset() method
is_superset = fs1.issuperset(fs2)
print(f"issuperset(): {is_superset}")

# isdisjoint() method
fs3 = frozenset({7, 8, 9})
is_disjoint = fs1.isdisjoint(fs3)
print(f"isdisjoint(): {is_disjoint}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 12: Real-World Example - Unique Colors in Images
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 12: Real-World Example - Find Unique Colors in Two Images")
print("="*70)

image1_colors = frozenset(['red', 'blue', 'green', 'yellow'])
image2_colors = frozenset(['blue', 'green', 'purple', 'white'])

print(f"Image 1 colors: {image1_colors}")
print(f"Image 2 colors: {image2_colors}")

common = image1_colors & image2_colors
print(f"Colors in both images: {common}")

only_in_1 = image1_colors - image2_colors
print(f"Colors only in image 1: {only_in_1}")

only_in_2 = image2_colors - image1_colors
print(f"Colors only in image 2: {only_in_2}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 13: Real-World Example - Product Features
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 13: Real-World Example - Product Features Comparison")
print("="*70)

phone_A_features = frozenset({'camera', 'battery', 'display', 'processor', 'RAM'})
phone_B_features = frozenset({'camera', 'battery', 'display', 'GPU', '5G'})

print(f"Phone A features: {phone_A_features}")
print(f"Phone B features: {phone_B_features}")

both_have = phone_A_features & phone_B_features
print(f"Both phones have: {both_have}")

only_A = phone_A_features - phone_B_features
print(f"Only phone A has: {only_A}")

only_B = phone_B_features - phone_A_features
print(f"Only phone B has: {only_B}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 14: Using Frozenset as Dictionary Key - Practical Example
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 14: Using Frozenset as Dictionary Key (Practical)")
print("="*70)

# Store inventory by product features
inventory = {
    frozenset({'color:red', 'size:large'}): 45,
    frozenset({'color:blue', 'size:small'}): 30,
    frozenset({'color:green', 'size:medium'}): 60,
}

print("Inventory by features:")
for features, quantity in inventory.items():
    print(f"  Features {features}: {quantity} units")

# Look up inventory by features
key = frozenset({'color:red', 'size:large'})
print(f"\nQuantity for {key}: {inventory[key]} units\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 15: Key Differences - Set vs Frozenset
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 15: Key Differences - Set vs Frozenset")
print("="*70)

print("""
REGULAR SET                          FROZENSET
──────────────────────────────────────────────────────────────
✓ Mutable (can modify)               ✓ Immutable (cannot modify)
❌ Cannot be dict key                ✓ Can be dict key
❌ Cannot be set element             ✓ Can be set element
✓ add(), remove(), pop()             ❌ No add/remove methods
✓ copy(), update()                   ✓ copy()
✓ union(), intersection()            ✓ union(), intersection()
✓ Operations: |, &, -, ^            ✓ Operations: |, &, -, ^
✓ Subset/superset checks             ✓ Subset/superset checks

WHEN TO USE SET?
  • When you need to modify data
  • Quick additions/removals
  • General purpose collection

WHEN TO USE FROZENSET?
  • When you need immutability
  • Using as dictionary key
  • Using as set element
  • Thread-safe operations
  • Create hash-based collections
""")

print("="*70)

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 16: Important Points to Remember
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("IMPORTANT POINTS TO REMEMBER")
print("="*70)

print("""
1. IMMUTABLE - Cannot be changed after creation
   ❌ frozenset.add(x)    - This won't work!
   ❌ frozenset.remove(x) - This won't work!
   ✓  frozenset | set     - Operations work!

2. HASHABLE - Can be used as dict key or set element
   ✓  {frozenset({1,2}): 'value'}
   ✓  {frozenset({1,2}), frozenset({3,4})}
   ❌ {{1,2}: 'value'}     - Regular set error!

3. DUPLICATE REMOVAL - Still removes duplicates
   frozenset([1,1,2,2,3]) becomes frozenset({1,2,3})

4. OPERATIONS WORK - Union, intersection, difference
   fs1 | fs2  →  Union
   fs1 & fs2  →  Intersection
   fs1 - fs2  →  Difference
   fs1 ^ fs2  →  Symmetric difference

5. READ OPERATIONS ONLY - Methods available
   ✓  len(), min(), max(), sum()
   ✓  union(), intersection(), difference()
   ✓  issubset(), issuperset(), isdisjoint()
   ✓  copy()
   ❌ add(), remove(), discard(), clear()

6. USE CASES
   • Dictionary keys
   • Set elements
   • Constants that shouldn't change
   • Cache keys
   • Thread-safe collections

7. CREATION METHODS
   frozenset()                    → Empty frozenset
   frozenset({1, 2, 3})          → From set
   frozenset([1, 2, 3])          → From list
   frozenset('hello')            → From string
   frozenset((1, 2, 3))          → From tuple
""")

print("="*70)

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 17: UNPACKING FROZENSETS - Extract Elements
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 17: UNPACKING FROZENSETS")
print("="*70)

# Basic unpacking (order not guaranteed)
my_frozenset = frozenset({1, 2, 3})
a, b, c = sorted(my_frozenset)
print(f"Frozenset: {my_frozenset}")
print(f"Unpacked (sorted): a={a}, b={b}, c={c}")

# Unpacking with rest
data_fs = frozenset({10, 20, 30, 40, 50})
first, *rest = sorted(data_fs)
print(f"\nFrozenset: {data_fs}")
print(f"first={first}, rest={rest}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 18: CONVERT FROZENSET TO OTHER DATA TYPES
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 18: CONVERT FROZENSET → SET / LIST / TUPLE / STRING")
print("="*70)

original_fs = frozenset({1, 2, 3, 4, 5})
print(f"Original Frozenset: {original_fs}")

# Convert to SET
my_set = set(original_fs)
print(f"\n✓ To Set: {my_set}")
print(f"  Type: {type(my_set)}")
print(f"  Use when: Need mutable set operations")

# Convert to LIST
my_list = list(original_fs)
print(f"\n✓ To List: {my_list}")
print(f"  Type: {type(my_list)}")
print(f"  Use when: Need ordering/indexing")

# Convert to TUPLE
my_tuple = tuple(original_fs)
print(f"\n✓ To Tuple: {my_tuple}")
print(f"  Type: {type(my_tuple)}")
print(f"  Use when: Need immutable but ordered")

# Convert to STRING
my_string = str(original_fs)
print(f"\n✓ To String: {my_string}")
print(f"  Type: {type(my_string)}")
print(f"  Use when: Need text representation\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 19: CONVERT OTHER TYPES TO FROZENSET
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 19: CONVERT SET / LIST / TUPLE / STRING → FROZENSET")
print("="*70)

# From SET
my_set = {1, 2, 3, 4}
fs_from_set = frozenset(my_set)
print(f"From Set: {my_set}")
print(f"To Frozenset: {fs_from_set}")
print(f"Use when: Need immutable version of set")

# From LIST
my_list = [10, 20, 10, 30]
fs_from_list = frozenset(my_list)
print(f"\nFrom List: {my_list}")
print(f"To Frozenset: {fs_from_list}")
print(f"Use when: Remove duplicates + immutability")

# From TUPLE
my_tuple = (5, 5, 10, 15)
fs_from_tuple = frozenset(my_tuple)
print(f"\nFrom Tuple: {my_tuple}")
print(f"To Frozenset: {fs_from_tuple}")
print(f"Use when: Convert to immutable set")

# From STRING
my_string = "hello"
fs_from_string = frozenset(my_string)
print(f"\nFrom String: '{my_string}'")
print(f"To Frozenset: {fs_from_string}")
print(f"Use when: Immutable unique characters\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 20: WHEN TO CONVERT - DECISION GUIDE
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 20: WHEN TO CONVERT - DECISION GUIDE")
print("="*70)

print("""
CONVERSION SCENARIOS:

1. FROZENSET → SET (When to convert)
   ✓ Need mutable set
   ✓ Want to add/remove elements
   ✓ Need set modification methods
   Example:
   fixed = frozenset({1, 2, 3})
   mutable = set(fixed)
   mutable.add(4)


2. FROZENSET → LIST (When to convert)
   ✓ Need ordering
   ✓ Need indexing
   ✓ Need list operations
   Example:
   items = frozenset({3, 1, 2})
   ordered = sorted(list(items))


3. FROZENSET → TUPLE (When to convert)
   ✓ Need ordered immutable collection
   ✓ Use as dictionary value
   Example:
   unique = frozenset({5, 2, 8})
   coords_tuple = tuple(sorted(unique))


4. SET → FROZENSET (When to convert)
   ✓ Need immutable set
   ✓ Use as dictionary key
   ✓ Use as set element
   ✓ Thread-safe storage
   Example:
   mutable = {1, 2, 3}
   immutable = frozenset(mutable)


5. LIST/TUPLE → FROZENSET (When to convert)
   ✓ Need unique immutable collection
   ✓ Remove duplicates + immutability
   ✓ Use as dictionary key
   Example:
   data = [1, 2, 2, 3]
   unique_locked = frozenset(data)


6. STRING → FROZENSET (When to convert)
   ✓ Unique immutable characters
   ✓ Fast membership checking
   Example:
   word = "hello"
   unique_chars = frozenset(word)
""")

print("="*70)

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 21: REAL EXAMPLE - Immutable Cache Keys
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 21: REAL EXAMPLE - Immutable Cache with Frozensets")
print("="*70)

# Step 1: Create mutable set
tags = {'python', 'coding', 'tutorial'}
print(f"Step 1 - Mutable (SET): {tags}")

# Step 2: Convert to frozenset (immutable)
locked_tags = frozenset(tags)
print(f"Step 2 - Immutable (FROZENSET): {locked_tags}")

# Step 3: Use as dictionary key (can't use regular set)
cache = {
    locked_tags: 'Content about Python coding tutorials',
    frozenset({'java', 'coding'}): 'Content about Java coding'
}
print(f"Step 3 - Cache dictionary: {cache}")

# Step 4: Access from cache
print(f"Step 4 - Lookup: {cache[locked_tags]}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 22: CONVERSION QUICK REFERENCE
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 22: CONVERSION QUICK REFERENCE")
print("="*70)

print("""
FROZENSET CONVERSIONS:

FROZENSET → SET         set(frozenset)          → {1, 2, 3}
            ✓ Mutable
            
FROZENSET → LIST        list(frozenset)         → [1, 2, 3]
            ✓ Indexing
            
            sorted(list(fs))        → [1, 2, 3] (ordered)
            ✓ Sorted order
            
FROZENSET → TUPLE       tuple(frozenset)        → (1, 2, 3)
            ✓ Ordered immutable
            
FROZENSET → STRING      str(frozenset)          → "frozenset({1, 2})"
            ✓ Display

SET → FROZENSET         frozenset(set)          → frozenset({1, 2, 3})
            ✓ Immutable
            ✓ Dictionary key
            ✓ Set element
            
LIST → FROZENSET        frozenset(list)         → frozenset({1, 2, 3})
            ✓ Unique + immutable
            [1, 2, 2] → frozenset({1, 2})
            
TUPLE → FROZENSET       frozenset(tuple)        → frozenset({1, 2, 3})
            ✓ Unique + immutable
            
STRING → FROZENSET      frozenset(string)       → frozenset({'h','e','l','o'})
            ✓ Unique chars


KEY DIFFERENCE: SET vs FROZENSET
═════════════════════════════════════════════════════════════════

SET                     FROZENSET
─────────────────────────────────────────────
Mutable                 Immutable
❌ Dictionary key       ✓ Dictionary key
❌ Set element          ✓ Set element
Slower                  Faster
add()                   ❌ (no modify methods)
remove()                ❌
clear()                 ❌
✓ High-level ops        ✓ High-level ops


WHEN TO USE FROZENSET:
═════════════════════════════════════════════════════════════════

1. Dictionary keys
   cache = {frozenset({1, 2}): 'result'}

2. Set elements  
   set_of_sets = {frozenset({1, 2}), frozenset({3, 4})}

3. Constants that shouldn't change
   ALLOWED_TAGS = frozenset({'python', 'java', 'c++'})

4. Thread-safe shared data
   # Multiple threads can safely read frozenset

5. Hash-based lookups
   # Fast membership checking without modification
""")

print("="*70)
