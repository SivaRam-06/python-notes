"""
╔════════════════════════════════════════════════════════════════════════════╗
║                         PYTHON SETS - COMPLETE GUIDE                       ║
║                 Learn Sets with Detailed Examples & Explanations            ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

# ═════════════════════════════════════════════════════════════════════════════
# 1. WHAT IS A SET?
# ═════════════════════════════════════════════════════════════════════════════
"""
A SET is:
    • Mutable (can be changed after creation)
    • Unordered (no index, no fixed order)
    • Contains ONLY UNIQUE elements (duplicates are automatically removed)
    • Enclosed in curly braces {}
    • Elements must be immutable (int, float, string, tuple) - NOT lists or dicts
    
WHY USE SETS?
    • Remove duplicates from a collection
    • Perform mathematical set operations (union, intersection, etc.)
    • Check membership quickly
    • Store unique data efficiently
"""

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                     SECTION 1: CREATING SETS                           ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

# ═════════════════════════════════════════════════════════════════════════════
# Creating Sets - Different Ways
# ═════════════════════════════════════════════════════════════════════════════

# Method 1: Using curly braces with elements
print("Method 1: Creating sets with curly braces")
s1 = {1, 2, 3, 4, 5}
print(f"Set of numbers: {s1}")

# Method 2: Mixed data types (strings, numbers, floats, booleans)
s2 = {1, 2.34, True, 'hello', 'world'}
print(f"Mixed data types set: {s2}")

# Method 3: Using set() constructor
s3 = set()  # Empty set
print(f"Empty set: {s3}")
print(f"Type of empty set: {type(s3)}")

# Method 4: Converting from string
s4 = set('hello')  # Each character becomes separate element
print(f"Set from string 'hello': {s4}")

# Method 5: Converting from list
s5 = set([1, 2, 2, 3, 3, 4])  # Duplicates are removed
print(f"Set from list [1,2,2,3,3,4]: {s5}")

# Method 6: Converting from tuple
s6 = set((10, 20, 30, 20))  # Duplicates removed
print(f"Set from tuple (10,20,30,20): {s6}")

print("\n")

# ═════════════════════════════════════════════════════════════════════════════
# IMPORTANT: Duplicate elements are automatically removed
# ═════════════════════════════════════════════════════════════════════════════
print("Important: Duplicates are automatically removed in sets")
s7 = {1, 1, 2, 2, 3, 3, 3, 'a', 'a', 'b'}
print(f"Set with duplicates {1, 1, 2, 2, 3, 3, 3, 'a', 'a', 'b'}: {s7}")

print("\n")

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                 SECTION 2: SET OPERATORS                              ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

# ═════════════════════════════════════════════════════════════════════════════
# 1. UNION OPERATOR (|)
# ═════════════════════════════════════════════════════════════════════════════
"""
UNION (|):
    • Combines all elements from both sets
    • Removes duplicates automatically
    • A | B = all elements in A OR B or both
    
Example:
    A = {1, 2, 3}
    B = {3, 4, 5}
    A | B = {1, 2, 3, 4, 5}
"""

print("1. UNION OPERATOR (|)")
print("-" * 60)
a = {1, 2, 3}
b = {3, 4, 5}
union = a | b
print(f"Set A: {a}")
print(f"Set B: {b}")
print(f"A | B (Union): {union}")
print(f"All elements from A and B combined\n")

# Another example with different data types
fruits1 = {'apple', 'banana', 'orange'}
fruits2 = {'orange', 'mango', 'grape'}
all_fruits = fruits1 | fruits2
print(f"Fruits1: {fruits1}")
print(f"Fruits2: {fruits2}")
print(f"Union of fruits: {all_fruits}\n")

# ═════════════════════════════════════════════════════════════════════════════
# 2. INTERSECTION OPERATOR (&)
# ═════════════════════════════════════════════════════════════════════════════
"""
INTERSECTION (&):
    • Finds common elements in both sets
    • Only includes elements that exist in BOTH A and B
    • A & B = elements in A AND B
    
Example:
    A = {1, 2, 3}
    B = {2, 3, 4}
    A & B = {2, 3}
"""

print("2. INTERSECTION OPERATOR (&)")
print("-" * 60)
a = {1, 2, 3, 4}
b = {2, 3, 5, 6}
intersection = a & b
print(f"Set A: {a}")
print(f"Set B: {b}")
print(f"A & B (Intersection): {intersection}")
print(f"Only elements common to both sets\n")

# Another example
set1 = {'cat', 'dog', 'bird', 'fish'}
set2 = {'dog', 'fish', 'lion', 'tiger'}
common = set1 & set2
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Common animals: {common}\n")

# ═════════════════════════════════════════════════════════════════════════════
# 3. DIFFERENCE OPERATOR (-)
# ═════════════════════════════════════════════════════════════════════════════
"""
DIFFERENCE (-):
    • Finds elements in first set but NOT in second set
    • A - B = elements in A but not in B
    • Order matters! A - B is different from B - A
    
Example:
    A = {1, 2, 3, 4}
    B = {2, 3, 5, 6}
    A - B = {1, 4}
    B - A = {5, 6}
"""

print("3. DIFFERENCE OPERATOR (-)")
print("-" * 60)
a = {1, 2, 3, 4}
b = {2, 3, 5, 6}
difference_a_minus_b = a - b
difference_b_minus_a = b - a
print(f"Set A: {a}")
print(f"Set B: {b}")
print(f"A - B (Elements in A but not in B): {difference_a_minus_b}")
print(f"B - A (Elements in B but not in A): {difference_b_minus_a}\n")

# Another example
students_section_A = {'Amit', 'Bhavna', 'Chirag', 'Deepa'}
students_section_B = {'Bhavna', 'Deepa', 'Eshaan', 'Fiona'}
only_in_A = students_section_A - students_section_B
only_in_B = students_section_B - students_section_A
print(f"Section A students: {students_section_A}")
print(f"Section B students: {students_section_B}")
print(f"Only in Section A: {only_in_A}")
print(f"Only in Section B: {only_in_B}\n")

# ═════════════════════════════════════════════════════════════════════════════
# 4. SYMMETRIC DIFFERENCE OPERATOR (^)
# ═════════════════════════════════════════════════════════════════════════════
"""
SYMMETRIC DIFFERENCE (^):
    • Finds elements in either set but NOT in both
    • A ^ B = (A - B) ∪ (B - A)
    • Elements that are unique to each set
    
Example:
    A = {1, 2, 3, 4}
    B = {2, 3, 5, 6}
    A ^ B = {1, 4, 5, 6}
"""

print("4. SYMMETRIC DIFFERENCE OPERATOR (^)")
print("-" * 60)
a = {1, 2, 3, 4}
b = {2, 3, 5, 6}
symmetric_diff = a ^ b
print(f"Set A: {a}")
print(f"Set B: {b}")
print(f"A ^ B (Elements in either A or B, but not both): {symmetric_diff}")
print(f"This is (A-B) ∪ (B-A)\n")

# Another example
languages_I_know = {'Python', 'Java', 'C++', 'JavaScript'}
languages_friend_knows = {'Python', 'Ruby', 'JavaScript', 'Go'}
different_languages = languages_I_know ^ languages_friend_knows
print(f"I know: {languages_I_know}")
print(f"Friend knows: {languages_friend_knows}")
print(f"Languages we know differently: {different_languages}\n")

print("\n")

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                  SECTION 3: COMPARISON OPERATORS                      ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

# ═════════════════════════════════════════════════════════════════════════════
# Subset (<=, <) and Superset (>=, >)
# ═════════════════════════════════════════════════════════════════════════════

# ============================================================
# SUBSET AND SUPERSET OPERATORS IN PYTHON SETS
# ============================================================

print("5. SUBSET and SUPERSET OPERATORS")
print("-" * 60)

# ------------------------------------------------------------
# 1. SUBSET (<=)
# ------------------------------------------------------------
# A subset means:
# Every element of Set A must be present in Set B.

a = {1, 2}              # Set A
b = {1, 2, 3, 4}        # Set B

print(f"Set A: {a}")
print(f"Set B: {b}")

# Check if A is subset of B
# <= operator checks whether all elements of A are inside B
print(f"A <= B (Is A a subset of B?): {a <= b}")   # True

# Explanation:
# A = {1,2}
# B = {1,2,3,4}
# All elements of A exist in B
print(f"Is every element of A in B? Yes!\n")


# ------------------------------------------------------------
# 2. PROPER SUBSET (<)
# ------------------------------------------------------------
# Proper subset means:
# A is inside B AND A is not equal to B.

print(f"A < B (Is A a proper subset of B?): {a < b}\n")

# Explanation:
# A = {1,2}
# B = {1,2,3,4}
# A is inside B and both sets are not equal
# So it is a proper subset


# ------------------------------------------------------------
# 3. SUPERSET (>=)
# ------------------------------------------------------------
# Superset means:
# Set B contains all elements of Set A.

print(f"B >= A (Is B a superset of A?): {b >= a}")

# Explanation:
# B = {1,2,3,4}
# A = {1,2}
# B contains all elements of A
print(f"B contains all elements of A? Yes!\n")


# ------------------------------------------------------------
# 4. PROPER SUPERSET (>)
# ------------------------------------------------------------
# Proper superset means:
# B contains all elements of A AND B ≠ A

print(f"B > A (Is B a proper superset of A?): {b > a}\n")


# ------------------------------------------------------------
# 5. EQUAL SETS
# ------------------------------------------------------------
# Sets are unordered.
# If two sets contain the same elements, they are equal
# even if the order is different.

set_x = {1, 2, 3}
set_y = {3, 1, 2}   # Same elements, different order

print(f"Set X: {set_x}")
print(f"Set Y: {set_y}")

# Check equality
print(f"X == Y (Are they equal?): {set_x == set_y}\n")

# Explanation:
# Order does not matter in sets
# {1,2,3} = {3,1,2}


# ------------------------------------------------------------
# 6. DISJOINT SETS
# ------------------------------------------------------------
# Disjoint sets means:
# Two sets have NO common elements.

set_p = {1, 2, 3}
set_q = {4, 5, 6}

print(f"Set P: {set_p}")
print(f"Set Q: {set_q}")

# isdisjoint() checks whether two sets share elements
print(f"P.isdisjoint(Q) (No common elements?): {set_p.isdisjoint(set_q)}\n")

# Explanation:
# P = {1,2,3}
# Q = {4,5,6}
# No elements are common
# So they are disjoint sets


print("\n")
print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                    SECTION 4: BUILT-IN FUNCTIONS                      ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

# ═════════════════════════════════════════════════════════════════════════════
# len() - Get number of elements in a set
# ═════════════════════════════════════════════════════════════════════════════
print("1. len() - Get the number of elements")
print("-" * 60)
my_set = {10, 20, 30, 40, 50}
print(f"Set: {my_set}")
print(f"len(set): {len(my_set)}")
print(f"The set has {len(my_set)} elements\n")

# ═════════════════════════════════════════════════════════════════════════════
# min() and max() - Get smallest and largest element
# ═════════════════════════════════════════════════════════════════════════════
print("2. min() and max() - Get smallest and largest elements")
print("-" * 60)
num_set = {15, 5, 25, 10, 30}
print(f"Set: {num_set}")
print(f"min(set): {min(num_set)}")
print(f"max(set): {max(num_set)}")
print(f"Smallest element: {min(num_set)}, Largest element: {max(num_set)}\n")

# ═════════════════════════════════════════════════════════════════════════════
# sum() - Add all elements
# ═════════════════════════════════════════════════════════════════════════════
print("3. sum() - Add all elements")
print("-" * 60)
scores = {10, 20, 15, 25}
print(f"Set: {scores}")
print(f"sum(set): {sum(scores)}")
print(f"Total of all elements: {sum(scores)}\n")

# ═════════════════════════════════════════════════════════════════════════════
# sorted() - Convert set to sorted list
# ═════════════════════════════════════════════════════════════════════════════
print("4. sorted() - Convert to sorted list")
print("-" * 60)
random_set = {5, 2, 8, 1, 9, 3}
print(f"Set (unordered): {random_set}")
sorted_list = sorted(random_set)
print(f"sorted(set): {sorted_list}")
print(f"Returns a LIST in sorted order\n")

# ═════════════════════════════════════════════════════════════════════════════
# any() and all() - Check conditions
# ═════════════════════════════════════════════════════════════════════════════
print("5. any() and all() - Check conditions")
print("-" * 60)
test_set1 = {0, 0, 0}
test_set2 = {1, 2, 3}
test_set3 = {0, 1, 2}
print(f"Set1: {test_set1}")
print(f"Set2: {test_set2}")
print(f"Set3: {test_set3}")
print(f"any({test_set1}) - At least one True? {any(test_set1)}")
print(f"any({test_set2}) - At least one True? {any(test_set2)}")
print(f"all({test_set2}) - All elements True? {all(test_set2)}")
print(f"all({test_set3}) - All elements True? {all(test_set3)}\n")

print("\n")

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                     SECTION 5: SET METHODS                            ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

# ═════════════════════════════════════════════════════════════════════════════
# 1. add() - Add a single element
# ═════════════════════════════════════════════════════════════════════════════
print("1. add() - Add a single element")
print("-" * 60)
fruits = {'apple', 'banana'}
print(f"Original set: {fruits}")
fruits.add('orange')
print(f"After add('orange'): {fruits}")
fruits.add('banana')  # Adding duplicate doesn't change the set
print(f"After add('banana'): {fruits}")
print(f"Adding duplicate elements has no effect\n")

# ═════════════════════════════════════════════════════════════════════════════
# 2. update() - Add multiple elements
# ═════════════════════════════════════════════════════════════════════════════
print("2. update() - Add multiple elements (from list, set, etc.)")
print("-" * 60)
colors = {'red', 'blue'}
print(f"Original set: {colors}")
colors.update(['green', 'yellow'])  # Add from list
print(f"After update(['green', 'yellow']): {colors}")
colors.update({'purple', 'black'})  # Add from another set
print(f"After update({{'purple', 'black'}}): {colors}\n")

# ═════════════════════════════════════════════════════════════════════════════
# 3. remove() - Remove an element (raises error if not found)
# ═════════════════════════════════════════════════════════════════════════════
print("3. remove() - Remove an element (error if not found)")
print("-" * 60)
numbers = {1, 2, 3, 4, 5}
print(f"Original set: {numbers}")
numbers.remove(3)
print(f"After remove(3): {numbers}")
print(f"Element 3 has been removed")
# numbers.remove(10)  # This would cause an error because 10 is not in the set
print(f"Note: remove() raises KeyError if element doesn't exist\n")

# ═════════════════════════════════════════════════════════════════════════════
# 4. discard() - Remove an element (NO error if not found)
# ═════════════════════════════════════════════════════════════════════════════
print("4. discard() - Remove an element (no error if not found)")
print("-" * 60)
numbers = {1, 2, 3, 4, 5}
print(f"Original set: {numbers}")
numbers.discard(4)
print(f"After discard(4): {numbers}")
numbers.discard(10)  # No error! This element doesn't exist
print(f"After discard(10): {numbers}")
print(f"discard() doesn't raise error if element not found\n")

# ═════════════════════════════════════════════════════════════════════════════
# 5. pop() - Remove and return an arbitrary element
# ═════════════════════════════════════════════════════════════════════════════
print("5. pop() - Remove and return an arbitrary element")
print("-" * 60)
items = {10, 20, 30, 40}
print(f"Original set: {items}")
removed = items.pop()  # Removes and returns an element
print(f"Removed element: {removed}")
print(f"Set after pop(): {items}")
print(f"pop() removes one random element (sets are unordered)\n")

# ═════════════════════════════════════════════════════════════════════════════
# 6. clear() - Remove all elements
# ═════════════════════════════════════════════════════════════════════════════
print("6. clear() - Remove all elements")
print("-" * 60)
my_set = {1, 2, 3, 4}
print(f"Original set: {my_set}")
my_set.clear()
print(f"After clear(): {my_set}")
print(f"The set is now empty\n")

# ═════════════════════════════════════════════════════════════════════════════
# 7. copy() - Create a shallow copy
# ═════════════════════════════════════════════════════════════════════════════
print("7. copy() - Create a shallow copy")
print("-" * 60)
original = {1, 2, 3}
copied = original.copy()
print(f"Original set: {original}")
print(f"Copied set: {copied}")
copied.add(4)
print(f"After adding 4 to copy: {copied}")
print(f"Original is unchanged: {original}")
print(f"copy() creates an independent set\n")

# ═════════════════════════════════════════════════════════════════════════════
# 8. union() - Combine two sets (same as |)
# ═════════════════════════════════════════════════════════════════════════════
print("8. union() - Combine two sets")
print("-" * 60)
set_a = {1, 2, 3}
set_b = {3, 4, 5}
result = set_a.union(set_b)
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"set_a.union(set_b): {result}")
print(f"Same as: set_a | set_b\n")

# ═════════════════════════════════════════════════════════════════════════════
# 9. intersection() - Find common elements (same as &)
# ═════════════════════════════════════════════════════════════════════════════
print("9. intersection() - Find common elements")
print("-" * 60)
set_x = {1, 2, 3, 4}
set_y = {2, 3, 5, 6}
result = set_x.intersection(set_y)
print(f"Set X: {set_x}")
print(f"Set Y: {set_y}")
print(f"set_x.intersection(set_y): {result}")
print(f"Same as: set_x & set_y\n")

# ═════════════════════════════════════════════════════════════════════════════
# 10. difference() - Find elements in first set but not second (same as -)
# ═════════════════════════════════════════════════════════════════════════════
print("10. difference() - Find unique elements")
print("-" * 60)
set_p = {1, 2, 3, 4}
set_q = {2, 3, 5, 6}
result = set_p.difference(set_q)
print(f"Set P: {set_p}")
print(f"Set Q: {set_q}")
print(f"set_p.difference(set_q): {result}")
print(f"Same as: set_p - set_q\n")

# ═════════════════════════════════════════════════════════════════════════════
# 11. symmetric_difference() - Find elements in either but not both
# ═════════════════════════════════════════════════════════════════════════════
print("11. symmetric_difference() - Find unique elements in both")
print("-" * 60)
set_m = {1, 2, 3, 4}
set_n = {2, 3, 5, 6}
result = set_m.symmetric_difference(set_n)
print(f"Set M: {set_m}")
print(f"Set N: {set_n}")
print(f"set_m.symmetric_difference(set_n): {result}")
print(f"Same as: set_m ^ set_n\n")

# ═════════════════════════════════════════════════════════════════════════════
# 12. issubset() - Check if one set is subset of another
# ═════════════════════════════════════════════════════════════════════════════
print("12. issubset() - Check if this is a subset")
print("-" * 60)
set_small = {1, 2}
set_large = {1, 2, 3, 4}
print(f"Small set: {set_small}")
print(f"Large set: {set_large}")
print(f"set_small.issubset(set_large): {set_small.issubset(set_large)}")
print(f"Same as: set_small <= set_large\n")

# ═════════════════════════════════════════════════════════════════════════════
# 13. issuperset() - Check if one set is superset of another
# ═════════════════════════════════════════════════════════════════════════════
print("13. issuperset() - Check if this is a superset")
print("-" * 60)
set_big = {1, 2, 3, 4}
set_tiny = {1, 2}
print(f"Big set: {set_big}")
print(f"Tiny set: {set_tiny}")
print(f"set_big.issuperset(set_tiny): {set_big.issuperset(set_tiny)}")
print(f"Same as: set_big >= set_tiny\n")

# ═════════════════════════════════════════════════════════════════════════════
# 14. isdisjoint() - Check if sets have no common elements
# ═════════════════════════════════════════════════════════════════════════════
print("14. isdisjoint() - Check if sets have no common elements")
print("-" * 60)
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Set 3: {set3}")
print(f"set1.isdisjoint(set2): {set1.isdisjoint(set2)} - No common elements")
print(f"set1.isdisjoint(set3): {set1.isdisjoint(set3)} - Have common element 3\n")

print("\n")

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                   SECTION 6: PRACTICAL EXAMPLES                       ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

# ═════════════════════════════════════════════════════════════════════════════
# Example 1: Remove duplicates from a list
# ═════════════════════════════════════════════════════════════════════════════
print("Example 1: Remove duplicates from a list")
print("-" * 60)
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5]
print(f"List with duplicates: {numbers_with_duplicates}")
unique_numbers = set(numbers_with_duplicates)
print(f"After converting to set: {unique_numbers}")
print(f"Back to list: {sorted(list(unique_numbers))}\n")

# ═════════════════════════════════════════════════════════════════════════════
# Example 2: Find common elements between two lists
# ═════════════════════════════════════════════════════════════════════════════
print("Example 2: Find common elements between two lists")
print("-" * 60)
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = set(list1) & set(list2)
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Common elements: {common}\n")

# ═════════════════════════════════════════════════════════════════════════════
# Example 3: Find unique characters in a string
# ═════════════════════════════════════════════════════════════════════════════
print("Example 3: Find unique characters in a string")
print("-" * 60)
word = "programming"
unique_chars = set(word)
print(f"Word: {word}")
print(f"Unique characters: {sorted(unique_chars)}")
print(f"Number of unique characters: {len(unique_chars)}\n")

# ═════════════════════════════════════════════════════════════════════════════
# Example 4: Find students in both sections
# ═════════════════════════════════════════════════════════════════════════════
print("Example 4: Find students in both sections")
print("-" * 60)
section_A = {'Amit', 'Bhavna', 'Chirag', 'Deepa', 'Eshaan'}
section_B = {'Bhavna', 'Deepa', 'Fiona', 'Girish', 'Eshaan'}
students_in_both = section_A & section_B
students_only_in_A = section_A - section_B
students_only_in_B = section_B - section_A
print(f"Section A: {section_A}")
print(f"Section B: {section_B}")
print(f"In both sections: {students_in_both}")
print(f"Only in A: {students_only_in_A}")
print(f"Only in B: {students_only_in_B}\n")

# ═════════════════════════════════════════════════════════════════════════════
# Example 5: Check membership (in operator)
# ═════════════════════════════════════════════════════════════════════════════
print("Example 5: Check membership in a set")
print("-" * 60)
colors = {'red', 'green', 'blue', 'yellow'}
print(f"Set: {colors}")
print(f"'red' in colors: {'red' in colors}")
print(f"'purple' in colors: {'purple' in colors}")
print(f"'pink' not in colors: {'pink' not in colors}\n")

print("\n")

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                   SECTION 7: IMPORTANT NOTES                          ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

print("""
KEY POINTS ABOUT SETS:

1. UNORDERED - Sets don't maintain order, so you can't access elements by index
   ❌ my_set[0]  - This won't work!
   ✓  for element in my_set  - This works

2. UNIQUE ELEMENTS - Duplicates are automatically removed
   {1, 1, 2, 2} becomes {1, 2}

3. MUTABLE - You can add/remove elements after creation
   ✓  add(), remove(), update(), clear()

4. IMMUTABLE ELEMENTS - Elements must be immutable
   ✓  Can contain: int, float, string, tuple, bool
   ❌ Cannot contain: list, dictionary, set

5. EMPTY SET - Use set(), NOT {}
   ❌ empty = {}  - This creates an empty DICTIONARY
   ✓  empty = set()  - This creates an empty SET

6. OPERATIONS - Use operators for set operations
   | → Union
   & → Intersection
   - → Difference
   ^ → Symmetric Difference

7. PERFORMANCE - Sets are fast for:
   • Checking membership (x in set)
   • Removing duplicates
   • Performing set operations

8. FROZENSET - An immutable version of set
   ✓  Can be used as dictionary key
   ✓  Can be element of another set
   
Example of frozenset:
"""
)

fs = frozenset([1, 2, 3])
print(f"Frozen set: {fs}")
print(f"frozensets are immutable and hashable\n")


python_batch = set(input().split(','))
sql_batch = set(input().split(','))
common = python_batch & sql_batch
n = len(common)
s_n = sorted(common)
s_p = s_n[1]
print(common)
print(s_p)

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 17: UNPACKING SETS - Extract Elements
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 17: UNPACKING SETS")
print("="*70)

# Basic unpacking (order not guaranteed)
my_set = {1, 2, 3}
a, b, c = sorted(my_set)  # Sort first for predictable order
print(f"Set: {my_set}")
print(f"Unpacked (sorted): a={a}, b={b}, c={c}")

# Unpacking with rest
data_set = {10, 20, 30, 40, 50}
first, *rest = sorted(data_set)
print(f"\nSet: {data_set}")
print(f"first={first}, rest={rest}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 18: CONVERT SET TO OTHER DATA TYPES
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 18: CONVERT SET → LIST / TUPLE / STRING")
print("="*70)

original_set = {1, 2, 3, 4, 5}
print(f"Original Set: {original_set}")

# Convert to LIST
my_list = list(original_set)
print(f"\n✓ To List: {my_list}")
print(f"  Type: {type(my_list)}")
print(f"  Use when: Need ordering/indexing")

# Convert to TUPLE
my_tuple = tuple(original_set)
print(f"\n✓ To Tuple: {my_tuple}")
print(f"  Type: {type(my_tuple)}")
print(f"  Use when: Need immutable collection")

# Convert to STRING
my_string = str(original_set)
print(f"\n✓ To String: {my_string}")
print(f"  Type: {type(my_string)}")
print(f"  Use when: Need text representation\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 19: CONVERT OTHER TYPES TO SET
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 19: CONVERT LIST / TUPLE / STRING → SET")
print("="*70)

# From LIST
my_list = [1, 2, 2, 3, 3, 3]
set_from_list = set(my_list)
print(f"From List: {my_list}")
print(f"To Set: {set_from_list}")
print(f"Use when: Remove duplicates from list")

# From TUPLE
my_tuple = (10, 20, 10, 30)
set_from_tuple = set(my_tuple)
print(f"\nFrom Tuple: {my_tuple}")
print(f"To Set: {set_from_tuple}")
print(f"Use when: Get unique elements from tuple")

# From STRING
my_string = "hello"
set_from_string = set(my_string)
print(f"\nFrom String: '{my_string}'")
print(f"To Set: {set_from_string}")
print(f"Use when: Find unique characters\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 20: WHEN TO CONVERT - DECISION GUIDE
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 20: WHEN TO CONVERT - DECISION GUIDE")
print("="*70)

print("""
CONVERSION SCENARIOS:

1. SET → LIST (When to convert)
   ✓ Need ordering
   ✓ Need indexing (access by position)
   ✓ Need list operations
   Example:
   numbers = {3, 1, 2}
   ordered = sorted(numbers)  # [1, 2, 3]


2. SET → TUPLE (When to convert)
   ✓ Need immutable collection
   ✓ Use as dictionary key
   ✓ Use as set element
   Example:
   coords_set = {(1,2), (3,4)}
   coords_tuple = tuple((1,2))


3. SET → STRING (When to convert)
   ✓ Need text representation
   ✓ Display/print
   Example:
   items = {1, 2, 3}
   text = str(items)


4. LIST → SET (When to convert)
   ✓ Remove duplicates
   ✓ Fast membership checking (O(1))
   ✓ Set operations (union, intersection, difference)
   Example:
   items = [1, 2, 2, 3]
   unique = set(items)


5. TUPLE → SET (When to convert)
   ✓ Remove duplicates
   ✓ Need set operations
   Example:
   data = (10, 20, 10, 30)
   unique = set(data)


6. STRING → SET (When to convert)
   ✓ Find unique characters
   ✓ Character analysis
   Example:
   word = "hello"
   unique_chars = set(word)
""")

print("="*70)

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 21: REAL EXAMPLE - Data Deduplication Pipeline
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 21: REAL EXAMPLE - Duplicate Removal Pipeline")
print("="*70)

# Step 1: Raw list with duplicates
raw_data = [5, 2, 8, 2, 5, 1, 8, 3]
print(f"Step 1 - Raw (LIST): {raw_data}")

# Step 2: Convert to set to remove duplicates
unique_data = set(raw_data)
print(f"Step 2 - Deduplicate (SET): {unique_data}")

# Step 3: Convert to list and sort
sorted_data = sorted(list(unique_data))
print(f"Step 3 - Sort (LIST): {sorted_data}")

# Step 4: Convert to tuple (immutable final result)
final_data = tuple(sorted_data)
print(f"Step 4 - Immutable (TUPLE): {final_data}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 22: CONVERSION QUICK REFERENCE
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 22: CONVERSION QUICK REFERENCE")
print("="*70)

print("""
SET CONVERSIONS:

SET → LIST             list(set)               → [1, 2, 3] (unordered)
       ✓ Indexing
       
       sorted(set)             → [1, 2, 3] (ordered)
       ✓ Sorted order
       
SET → TUPLE            tuple(set)              → (1, 2, 3) (unordered)
       ✓ Immutable
       
SET → STRING           str(set)                → "{1, 2, 3}"
       ✓ Display

LIST → SET             set(list)               → {1, 2, 3}
       ✓ Remove duplicates
       [1, 2, 2, 3] → {1, 2, 3}
       
TUPLE → SET            set(tuple)              → {1, 2, 3}
       ✓ Remove duplicates
       (1, 2, 2) → {1, 2}
       
STRING → SET           set(string)             → {'h', 'e', 'l', 'o'}
       ✓ Unique chars
       "hello" → {'h', 'e', 'l', 'o'}


SET OPERATIONS (No conversion needed):
═════════════════════════════════════════════════════════════════

Union:          set1 | set2
Intersection:   set1 & set2
Difference:     set1 - set2
Symmetric Diff: set1 ^ set2

Example:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
common = set1 & set2  # {3}
all_items = set1 | set2  # {1, 2, 3, 4, 5}
""")

# Advanced Set Methods - In-place operations and specialized methods

# Creating sample sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {3, 4, 5}

# 1. difference_update() - Removes all elements of another set from this set
# Modifies the set in-place (doesn't return a new set)
print("Original set1:", set1)
set1.difference_update(set2)
print("After difference_update(set2):", set1)

# Reset set1
set1 = {1, 2, 3, 4, 5}

# 2. intersection_update() - Updates the set with the intersection of itself and another set
# Keeps only elements found in both sets
print("\nOriginal set1:", set1)
set1.intersection_update(set2)
print("After intersection_update(set2):", set1)

# Reset set1
set1 = {1, 2, 3, 4, 5}

# 3. symmetric_difference_update() - Updates the set with the symmetric difference
# Keeps elements that are in either set but not in both
print("\nOriginal set1:", set1)
set1.symmetric_difference_update(set2)
print("After symmetric_difference_update(set2):", set1)

# 4. Set comprehension with conditions
print("\nSet comprehension with condition:")
even_squares = {x**2 for x in range(10) if x**2 % 2 == 0}
print("Even squares:", even_squares)

# 5. Set operations with multiple sets
print("\nOperations with multiple sets:")
set4 = {5, 6, 7}
# Union of multiple sets
multi_union = set1.union(set2, set3, set4)
print("Union of multiple sets:", multi_union)
# Intersection of multiple sets
multi_intersection = set1.intersection(set2, set3)
print("Intersection of multiple sets:", multi_intersection)