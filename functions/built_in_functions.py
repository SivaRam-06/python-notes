# BUILT-IN FUNCTIONS - Common Python Functions

# =============================================================================
# 1. TYPE CHECKING FUNCTIONS
# =============================================================================

# type() - Get the data type
print(type(42))              # <class 'int'>
print(type("hello"))         # <class 'str'>
print(type([1, 2, 3]))       # <class 'list'>
print(type({"a": 1}))      # <class 'dict'>
print(type((1, 2, 3)))       # <class 'tuple'>
print(type({1, 2, 3}))       # <class 'set'>
print()

# isinstance() - Check if object is instance of class
number = 42
is_int = isinstance(number, int)
is_str = isinstance(number, str)
print(f"42 is int: {is_int}")      # True
print(f"42 is str: {is_str}")      # False
print()


# =============================================================================
# 2. LENGTH AND SIZE FUNCTIONS
# =============================================================================

# len() - Get length of sequence
print(len("hello"))         # 5
print(len([1, 2, 3, 4]))    # 4
print(len((1, 2, 3)))       # 3
print(len({"a": 1, "b": 2}))  # 2
print()


# =============================================================================
# 3. NUMERIC FUNCTIONS
# =============================================================================

# abs() - Absolute value
print(abs(-5))              # 5
print(abs(-3.14))           # 3.14
print()

# round() - Round to nearest number
print(round(3.14159))       # 3
print(round(3.14159, 2))    # 3.14
print(round(3.14159, 3))    # 3.142
print()

# min() and max() - Find minimum and maximum
numbers = [10, 5, 20, 3, 15]
print(f"Min: {min(numbers)}")  # 3
print(f"Max: {max(numbers)}")  # 20
print()

# sum() - Sum all elements
print(sum([1, 2, 3, 4, 5]))  # 15
print(sum([1, 2, 3, 4, 5], 10))  # 25 (start with 10)
print()

# pow() - Power (exponentiation)
print(pow(2, 3))            # 8 (2^3)
print(pow(2, 3, 5))         # 3 (2^3 mod 5)
print()


# =============================================================================
# 4. STRING FUNCTIONS
# =============================================================================

# str() - Convert to string
print(str(42))              # "42"
print(str(3.14))            # "3.14"
print(str([1, 2, 3]))       # "[1, 2, 3]"
print()

# len() - String length
print(len("hello world"))   # 11
print()

# ord() and chr() - Character/ASCII conversion
print(ord("A"))              # 65
print(chr(65))              # "A"
print(ord("a"))              # 97
print()


# =============================================================================
# 5. CONVERSION FUNCTIONS
# =============================================================================

# int() - Convert to integer
print(int(3.14))            # 3
print(int("42"))           # 42
print(int("101", 2))       # 5 (binary to decimal)
print()

# float() - Convert to float
print(float("3.14"))       # 3.14
print(float(10))            # 10.0
print()

# bool() - Convert to boolean
print(bool(1))              # True
print(bool(0))              # False
print(bool(" "))             # False (empty string)
print(bool("text"))        # True
print(bool([]))             # False (empty list)
print(bool([1]))            # True
print()


# =============================================================================
# 6. SEQUENCE FUNCTIONS
# =============================================================================

# list() - Create or convert list
print(list("abc"))         # ['a', 'b', 'c']
print(list(range(5)))       # [0, 1, 2, 3, 4]
print()

# tuple() - Create or convert tuple
print(tuple([1, 2, 3]))     # (1, 2, 3)
print(tuple("abc"))        # ('a', 'b', 'c')
print()

# set() - Create set
print(set([1, 2, 2, 3]))    # {1, 2, 3} (removes duplicates)
print(set("aabbcc"))       # {'a', 'b', 'c'}
print()

# dict() - Create dictionary
print(dict([("a", 1), ("b", 2)]))  # {'a': 1, 'b': 2}
print()


# =============================================================================
# 7. SEQUENCE OPERATIONS
# =============================================================================

# sorted() - Sort sequence
print(sorted([3, 1, 4, 1, 5]))           # [1, 1, 3, 4, 5]
print(sorted(["apple", "banana", "cherry"]))  # ['apple', 'banana', 'cherry']
print(sorted([3, 1, 4, 1, 5], reverse=True))  # [5, 4, 3, 1, 1]
print()

# reversed() - Reverse sequence
print(list(reversed([1, 2, 3, 4])))      # [4, 3, 2, 1]
print()

# zip() - Combine sequences
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
print()

# enumerate() - Get index and value
for i, name in enumerate(names):
    print(f"{i}: {name}")
print()


# =============================================================================
# 8. MAPPING FUNCTIONS
# =============================================================================

# map() - Apply function to all elements
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")  # [2, 4, 6, 8, 10]
print()

# filter() - Keep elements matching condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")     # [2, 4]
print()


# =============================================================================
# 9. LOOPING FUNCTIONS
# =============================================================================

# range() - Generate sequence of numbers
print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(2, 5)))        # [2, 3, 4]
print(list(range(0, 10, 2)))    # [0, 2, 4, 6, 8]
print(list(range(5, 0, -1)))    # [5, 4, 3, 2, 1]
print()


# =============================================================================
# 10. INPUT/OUTPUT FUNCTIONS
# =============================================================================

# print() - Output to console
print("Hello", "World")              # With multiple arguments
print("Name:", "Alice", sep="-")    # Custom separator
print("Line1")
print("Line2", end=" ")              # Custom end instead of newline
print("Line3")
print()

# input() - Get user input
# user_input = input("Enter something: ")
# print(f"You entered: {user_input}")


# =============================================================================
# 11. LOGICAL FUNCTIONS
# =============================================================================

# all() - True if all elements are truthy
print(all([True, True, True]))     # True
print(all([True, False, True]))    # False
print(all([1, 2, 3]))             # True
print(all([1, 2, 0]))             # False (0 is falsy)
print()

# any() - True if any element is truthy
print(any([False, False, False]))  # False
print(any([False, True, False]))   # True
print(any([0, 0, 1]))             # True
print()


# =============================================================================
# 12. PRACTICAL EXAMPLES
# =============================================================================

# Example 1: Finding statistics
scores = [85, 90, 78, 92, 88, 95, 81]

average = sum(scores) / len(scores)
highest = max(scores)
lowest = min(scores)
total = sum(scores)

print(f"Scores: {scores}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print()


# Example 2: Data processing
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22},
    {"name": "Diana", "age": 28}
]

# Sort by age
by_age = sorted(data, key=lambda x: x["age"])
print("By age:", [(d["name"], d["age"]) for d in by_age])

# Get oldest
oldest = max(data, key=lambda x: x["age"])
print(f"Oldest: {oldest['name']} ({oldest['age']})")

# Get average age
avg_age = sum(d["age"] for d in data) / len(data)
print(f"Average age: {avg_age:.1f}")
print()


# Example 3: String processing
text = "hello world python".title()
print(f"Title case: {text}")

# Convert to different types
binary = bin(42)  # Convert to binary
hex_val = hex(42)   # Convert to hexadecimal
oct_val = oct(42)   # Convert to octal
print(f"42 in binary: {binary}")
print(f"42 in hex: {hex_val}")
print(f"42 in octal: {oct_val}")
print()


# =============================================================================
# 13. COMPARISON FUNCTIONS
# =============================================================================

# For comparing with default behavior
words = ["apple", "banana", "cherry", "date"]

# Sort by length
by_length = sorted(words, key=len, reverse=True)
print(f"By length: {by_length}")

# Find longest word
longest = max(words, key=len)
print(f"Longest: {longest}")

# Find shortest word
shortest = min(words, key=len)
print(f"Shortest: {shortest}")
print()


# =============================================================================
# 14. USEFUL COMBINATIONS
# =============================================================================

# Get unique elements while preserving order
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(dict.fromkeys(numbers))  # Preserves order
print(f"Unique: {unique}")

# Another way: using set (loses order)
unique_set = list(set(numbers))
print(f"Unique (set): {sorted(unique_set)}")

# Find duplicates
from collections import Counter
counts = Counter(numbers)
duplicates = [num for num, count in counts.items() if count > 1]
print(f"Duplicates: {duplicates}")
print()


# =============================================================================
# KEY POINTS SUMMARY
# =============================================================================

"""
Common Built-in Functions:

TYPE CHECKING:
- type() - Get type
- isinstance() - Check type

NUMERIC:
- abs() - Absolute value
- round() - Round number
- min(), max() - Find min/max
- sum() - Sum elements
- pow() - Power

SEQUENCE:
- len() - Length
- sorted() - Sort
- reversed() - Reverse
- zip() - Combine sequences
- enumerate() - Index and value

CONVERSION:
- int(), float(), str(), bool()
- list(), tuple(), set(), dict()

MAPPING:
- map() - Apply function
- filter() - Filter elements

LOGICAL:
- all() - All true?
- any() - Any true?

These functions save time and make code cleaner!
"""
