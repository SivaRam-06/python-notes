# ============================================================
# PYTHON LIST COMPREHENSION - COMPLETE DETAILED GUIDE
# ============================================================

# This file contains a complete explanation of List Comprehension

# in Python with detailed comments, examples, syntax, use cases,

# nested comprehensions, conditions, performance notes, and more.

#

# Everything is explained step-by-step using comments.

# ============================================================

# ============================================================
# 1. WHAT IS LIST COMPREHENSION?
# ============================================================

# List Comprehension is a short and elegant way to create lists

# in Python.

#

# Instead of writing multiple lines using loops, we can create

# lists in a single line.

#

# It makes code:

# - Shorter

# - Cleaner

# - Faster

# - Easier to read (when used properly)

#

# ------------------------------------------------------------

# BASIC IDEA:

# ------------------------------------------------------------

# Traditional way:

#

# result = []

# for i in range(5):

# result.append(i)

#

# List comprehension way:

#

# result = [i for i in range(5)]

#

# Both produce:

# [0, 1, 2, 3, 4]

# ============================================================

# ============================================================

# 2. BASIC SYNTAX OF LIST COMPREHENSION

# ============================================================

# Syntax:

#

# [expression for item in iterable]

#

# ------------------------------------------------------------

# PARTS EXPLANATION:

# ------------------------------------------------------------

# expression:

# The value to store in the list.

#

# item:

# Variable used during iteration.

#

# iterable:

# Any iterable object like:

# - list

# - tuple

# - string

# - range()

# - set

# - dictionary

#

# ------------------------------------------------------------

# EXAMPLE:

# ------------------------------------------------------------

numbers = [x for x in range(5)]
print(numbers)

# Output: [0, 1, 2, 3, 4]

# ============================================================

# ============================================================

# 3. TRADITIONAL LOOP VS LIST COMPREHENSION

# ============================================================

# ------------------------------------------------------------

# USING NORMAL LOOP

# ------------------------------------------------------------

squares = []

for num in range(1, 6):
# Append square of each number
squares.append(num ** 2)

print(squares)

# Output: [1, 4, 9, 16, 25]

# ------------------------------------------------------------

# USING LIST COMPREHENSION

# ------------------------------------------------------------

squares2 = [num ** 2 for num in range(1, 6)]

print(squares2)

# Output: [1, 4, 9, 16, 25]

# List comprehension reduces multiple lines into one clean line.

# ============================================================

# ============================================================

# 4. CREATING LISTS FROM RANGE()

# ============================================================

# Create list from 0 to 9

nums = [x for x in range(10)]
print(nums)

# Create even numbers

even_nums = [x for x in range(20) if x % 2 == 0]
print(even_nums)

# Create odd numbers

odd_nums = [x for x in range(20) if x % 2 != 0]
print(odd_nums)

# ============================================================

# ============================================================

# 5. USING EXPRESSIONS IN LIST COMPREHENSION

# ============================================================

# The expression part can contain:

# - Mathematical operations

# - Function calls

# - String operations

# - Conditions

# - Any valid Python expression

# ============================================================

# Multiply numbers by 10

result = [x * 10 for x in range(5)]
print(result)

# Output: [0, 10, 20, 30, 40]

# Cube of numbers

cubes = [x ** 3 for x in range(1, 6)]
print(cubes)

# Output: [1, 8, 27, 64, 125]

# Convert numbers to strings

str_nums = [str(x) for x in range(5)]
print(str_nums)

# Output: ['0', '1', '2', '3', '4']

# ============================================================

# ============================================================

# 6. LIST COMPREHENSION WITH CONDITIONS

# ============================================================

# Syntax:

#

# [expression for item in iterable if condition]

#

# The condition filters elements.

# Only elements satisfying the condition are included.

# ============================================================

# Get only even numbers

even = [x for x in range(10) if x % 2 == 0]
print(even)

# Output: [0, 2, 4, 6, 8]

# Get numbers greater than 5

greater = [x for x in range(10) if x > 5]
print(greater)

# Output: [6, 7, 8, 9]

# Get words with length greater than 4

words = ["apple", "bat", "banana", "dog", "elephant"]

long_words = [word for word in words if len(word) > 4]
print(long_words)

# Output: ['apple', 'banana', 'elephant']

# ============================================================

# ============================================================

# 7. IF-ELSE IN LIST COMPREHENSION

# ============================================================

# Syntax:

#

# [value_if_true if condition else value_if_false

# for item in iterable]

#

# IMPORTANT:

# ------------------------------------------------------------

# if-else expression comes BEFORE the for loop.

# ============================================================

# Mark numbers as Even or Odd

labels = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]

print(labels)

# Output:

# ['Even', 'Odd', 'Even', 'Odd', ...]

# Positive and Negative classification

numbers = [-2, -1, 0, 1, 2]

status = ["Positive" if n > 0 else "Negative or Zero" for n in numbers]

print(status)

# ============================================================

# ============================================================

# 8. USING FUNCTIONS INSIDE LIST COMPREHENSION

# ============================================================

def square(n):
return n * n

# Apply function to every element

result = [square(x) for x in range(5)]
print(result)

# Output: [0, 1, 4, 9, 16]

# Using built-in functions

names = ["john", "alice", "bob"]

capitalized = [name.upper() for name in names]
print(capitalized)

# Output: ['JOHN', 'ALICE', 'BOB']

# ============================================================

# ============================================================

# 9. LIST COMPREHENSION WITH STRINGS

# ============================================================

# Convert characters to uppercase

chars = [char.upper() for char in "python"]
print(chars)

# Output: ['P', 'Y', 'T', 'H', 'O', 'N']

# Extract vowels from a string

vowels = [ch for ch in "programming" if ch in "aeiou"]
print(vowels)

# Output: ['o', 'a', 'i']

# ============================================================

# ============================================================

# 10. LIST COMPREHENSION WITH LISTS

# ============================================================

numbers = [1, 2, 3, 4, 5]

# Double every number

doubled = [x * 2 for x in numbers]
print(doubled)

# Output: [2, 4, 6, 8, 10]

# Filter numbers greater than 2

filtered = [x for x in numbers if x > 2]
print(filtered)

# Output: [3, 4, 5]

# ============================================================

# ============================================================

# 11. NESTED LIST COMPREHENSION

# ============================================================

# Nested list comprehension means using one comprehension

# inside another.

#

# Syntax:

# [expression for item1 in iterable1 for item2 in iterable2]

# ============================================================

# Create pairs

pairs = [(x, y) for x in [1, 2, 3] for y in [10, 20, 30]]

print(pairs)

# Output:

# [(1, 10), (1, 20), (1, 30),

# (2, 10), (2, 20), (2, 30),

# (3, 10), (3, 20), (3, 30)]

# Matrix flattening

matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

# Convert 2D list into 1D list

flattened = [num for row in matrix for num in row]

print(flattened)

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ============================================================

# ============================================================

# 12. NESTED CONDITIONS IN LIST COMPREHENSION

# ============================================================

numbers = range(20)

# Numbers divisible by both 2 and 3

result = [x for x in numbers if x % 2 == 0 if x % 3 == 0]

print(result)

# Output: [0, 6, 12, 18]

# ============================================================

# ============================================================

# 13. LIST COMPREHENSION FOR MATRIX CREATION

# ============================================================

# Create a 3x3 matrix filled with zeros

matrix = [[0 for col in range(3)] for row in range(3)]

print(matrix)

# Output:

# [[0, 0, 0],

# [0, 0, 0],

# [0, 0, 0]]

# Create multiplication table

multiplication_table = [[row * col for col in range(1, 6)]
for row in range(1, 6)]

print(multiplication_table)

# ============================================================

# ============================================================

# 14. USING MULTIPLE CONDITIONS

# ============================================================

# Numbers divisible by 2 and 5

result = [x for x in range(100) if x % 2 == 0 and x % 5 == 0]

print(result)

# Words starting with 'a'

words = ["apple", "banana", "ant", "cat", "animal"]

filtered = [w for w in words if w.startswith("a")]

print(filtered)

# Output: ['apple', 'ant', 'animal']

# ============================================================

# ============================================================

# 15. USING ELSE WITH MULTIPLE CONDITIONS

# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

result = [
"Divisible by 2" if x % 2 == 0 else "Not Divisible by 2"
for x in numbers
]

print(result)

# ============================================================

# ============================================================

# 16. PERFORMANCE OF LIST COMPREHENSION

# ============================================================

# List comprehensions are generally faster than normal loops.

#

# Why?

# ------------------------------------------------------------

# Because Python optimizes comprehensions internally.

#

# Advantages:

# - Less code

# - Faster execution

# - Better readability

#

# But avoid very complex comprehensions because they become

# difficult to understand.

# ============================================================

# ============================================================

# 17. MEMORY USAGE

# ============================================================

# List comprehensions create the entire list in memory.

#

# For huge datasets, generator expressions are better.

# ============================================================

# List comprehension creates full list

nums = [x for x in range(1000)]

# Generator expression (memory efficient)

generator = (x for x in range(1000))

print(generator)

# Output: generator object

# ============================================================

# ============================================================

# 18. COMMON REAL-WORLD EXAMPLES

# ============================================================

# ------------------------------------------------------------

# Example 1: Remove spaces from strings

# ------------------------------------------------------------

text = "Python List Comprehension"

chars = [ch for ch in text if ch != " "]
print(chars)

# ------------------------------------------------------------

# Example 2: Get lengths of words

# ------------------------------------------------------------

words = ["apple", "banana", "cat"]

lengths = [len(word) for word in words]
print(lengths)

# Output: [5, 6, 3]

# ------------------------------------------------------------

# Example 3: Convert temperatures

# ------------------------------------------------------------

celsius = [0, 10, 20, 30]

fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

print(fahrenheit)

# Output: [32.0, 50.0, 68.0, 86.0]

# ============================================================

# ============================================================

# 19. LIST COMPREHENSION WITH FILES

# ============================================================

# Example:

#

# lines = [line.strip() for line in open("file.txt")]

#

# This reads all lines from a file and removes spaces/newlines.

# ============================================================

# ============================================================

# 20. LIST COMPREHENSION WITH DICTIONARIES

# ============================================================

student_marks = {
"John": 90,
"Alice": 75,
"Bob": 60,
"David": 85
}

# Get students with marks greater than 80

high_scorers = [name for name, marks in student_marks.items() if marks > 80]

print(high_scorers)

# Output: ['John', 'David']

# ============================================================

# ============================================================

# 21. LIST COMPREHENSION WITH SETS

# ============================================================

numbers = {1, 2, 3, 4, 5}

squares = [x ** 2 for x in numbers]
print(squares)

# ============================================================

# ============================================================

# 22. COMMON MISTAKES

# ============================================================

# ------------------------------------------------------------

# Mistake 1: Forgetting brackets

# ------------------------------------------------------------

# WRONG:

# x for x in range(5)

#

# CORRECT:

# [x for x in range(5)]

# ------------------------------------------------------------

# Mistake 2: Wrong if-else position

# ------------------------------------------------------------

# WRONG:

# [x for x in range(5) if x % 2 == 0 else 0]

#

# CORRECT:

# [x if x % 2 == 0 else 0 for x in range(5)]

# ------------------------------------------------------------

# Mistake 3: Overcomplicated comprehensions

# ------------------------------------------------------------

# Avoid writing extremely complex one-liners.

# Readability is important.

# ============================================================

# ============================================================

# 23. WHEN TO USE LIST COMPREHENSION

# ============================================================

# Use list comprehension when:

# - You want to transform data

# - You want filtering

# - Logic is simple

# - You want shorter code

#

# Avoid when:

# - Logic becomes too complex

# - Multiple nested conditions reduce readability

# ============================================================

# ============================================================

# 24. ADVANTAGES OF LIST COMPREHENSION

# ============================================================

# 1. Cleaner code

# 2. Shorter syntax

# 3. Faster execution

# 4. Easy filtering

# 5. Easy transformations

# 6. Better readability (simple cases)

# ============================================================

# ============================================================

# 25. DISADVANTAGES OF LIST COMPREHENSION

# ============================================================

# 1. Complex comprehensions are hard to read

# 2. Uses more memory than generators

# 3. Debugging can become difficult

# ============================================================

# ============================================================

# 26. DIFFERENCE BETWEEN LIST COMPREHENSION

# AND GENERATOR EXPRESSION

# ============================================================

# LIST COMPREHENSION:

# Uses [] brackets

# Creates complete list in memory

#

# GENERATOR EXPRESSION:

# Uses () brackets

# Generates values one by one

# ============================================================

list_comp = [x for x in range(5)]
generator_exp = (x for x in range(5))

print(list_comp)
print(generator_exp)

# ============================================================

# ============================================================

# 27. ADVANCED EXAMPLES

# ============================================================

# ------------------------------------------------------------

# Example 1: Flatten nested lists

# ------------------------------------------------------------

nested = [[1, 2], [3, 4], [5, 6]]

flat = [item for sublist in nested for item in sublist]

print(flat)

# Output: [1, 2, 3, 4, 5, 6]

# ------------------------------------------------------------

# Example 2: Create coordinate pairs

# ------------------------------------------------------------

coordinates = [(x, y) for x in range(3) for y in range(3)]

print(coordinates)

# ------------------------------------------------------------

# Example 3: Remove vowels

# ------------------------------------------------------------

text = "programming"

result = [ch for ch in text if ch not in "aeiou"]

print(result)

# Output: ['p', 'r', 'g', 'r', 'm', 'm', 'n', 'g']

# ============================================================

# ============================================================

# 28. INTERVIEW QUESTIONS ON LIST COMPREHENSION

# ============================================================

# Q1: What is list comprehension?

# ------------------------------------------------------------

# A concise way to create lists in Python.

#

# Q2: Why use list comprehension?

# ------------------------------------------------------------

# Cleaner, shorter, and faster code.

#

# Q3: Difference between list comprehension and generator?

# ------------------------------------------------------------

# List comprehension stores all values in memory.

# Generator produces values one by one.

#

# Q4: Can we use conditions?

# ------------------------------------------------------------

# Yes, using if and if-else.

# ============================================================

# ============================================================

# 29. PRACTICE PROBLEMS

# ============================================================

# Try solving these using list comprehension:

#

# 1. Create squares of numbers from 1 to 20

# 2. Extract vowels from a sentence

# 3. Create list of even numbers

# 4. Convert words to uppercase

# 5. Flatten a nested list

# 6. Remove negative numbers from list

# 7. Create multiplication table

# 8. Replace odd numbers with 0

# ============================================================

# ============================================================

# 30. QUICK REVISION

# ============================================================

# BASIC:

# [x for x in iterable]

#

# WITH CONDITION:

# [x for x in iterable if condition]

#

# WITH IF-ELSE:

# [a if condition else b for x in iterable]

#

# NESTED:

# [x for row in matrix for x in row]

# ============================================================

# ============================================================

# 31. COMPLETE EXAMPLE PROGRAMS

# ============================================================

# This section contains separate example programs for practice.

# Each program is explained clearly using comments.

# ============================================================

# ============================================================

# PROGRAM 1: CREATE A LIST OF SQUARES

# ============================================================

# Traditional way

squares = []

for i in range(1, 6):
# Store square of each number
squares.append(i * i)

print("Squares using loop:", squares)

# Using list comprehension

squares2 = [i * i for i in range(1, 6)]

print("Squares using list comprehension:", squares2)

# ============================================================

# PROGRAM 2: FIND EVEN NUMBERS

# ============================================================

# Generate even numbers from 1 to 20

even_numbers = [num for num in range(1, 21) if num % 2 == 0]

print("Even Numbers:")
print(even_numbers)

# ============================================================

# PROGRAM 3: FIND ODD NUMBERS

# ============================================================

odd_numbers = [num for num in range(1, 21) if num % 2 != 0]

print("Odd Numbers:")
print(odd_numbers)

# ============================================================

# PROGRAM 4: CONVERT STRINGS TO UPPERCASE

# ============================================================

names = ["john", "alice", "bob"]

# Convert each name into uppercase

upper_names = [name.upper() for name in names]

print("Uppercase Names:")
print(upper_names)

# ============================================================

# PROGRAM 5: FIND LENGTH OF EACH WORD

# ============================================================

words = ["apple", "banana", "cat", "elephant"]

# Store length of every word

lengths = [len(word) for word in words]

print("Length of each word:")
print(lengths)

# ============================================================

# PROGRAM 6: CREATE LIST OF CUBES

# ============================================================

cubes = [x ** 3 for x in range(1, 11)]

print("Cubes:")
print(cubes)

# ============================================================

# PROGRAM 7: FILTER POSITIVE NUMBERS

# ============================================================

numbers = [-10, -5, 0, 5, 10, 15]

# Keep only positive numbers

positive = [num for num in numbers if num > 0]

print("Positive Numbers:")
print(positive)

# ============================================================

# PROGRAM 8: REPLACE EVEN AND ODD LABELS

# ============================================================

result = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]

print("Even/Odd Labels:")
print(result)

# ============================================================

# PROGRAM 9: EXTRACT VOWELS FROM STRING

# ============================================================

text = "list comprehension"

# Extract only vowels

vowels = [ch for ch in text if ch in "aeiou"]

print("Vowels:")
print(vowels)

# ============================================================

# PROGRAM 10: REMOVE SPACES FROM STRING

# ============================================================

sentence = "Python is powerful"

# Remove spaces

characters = [ch for ch in sentence if ch != " "]

print("Characters without spaces:")
print(characters)

# ============================================================

# PROGRAM 11: FLATTEN A NESTED LIST

# ============================================================

nested = [[1, 2], [3, 4], [5, 6]]

# Convert 2D list into 1D list

flat = [item for sublist in nested for item in sublist]

print("Flattened List:")
print(flat)

# ============================================================

# PROGRAM 12: CREATE MATRIX

# ============================================================

# Create 3x3 matrix filled with zeros

matrix = [[0 for col in range(3)] for row in range(3)]

print("3x3 Matrix:")
print(matrix)

# ============================================================

# PROGRAM 13: MULTIPLICATION TABLE

# ============================================================

# Create multiplication table from 1 to 5

multiplication_table = [
[row * col for col in range(1, 6)]
for row in range(1, 6)
]

print("Multiplication Table:")
print(multiplication_table)

# ============================================================

# PROGRAM 14: CREATE COORDINATE PAIRS

# ============================================================

coordinates = [(x, y) for x in range(3) for y in range(3)]

print("Coordinate Pairs:")
print(coordinates)

# ============================================================

# PROGRAM 15: FILTER LONG WORDS

# ============================================================

words = ["apple", "hi", "banana", "dog", "elephant"]

# Keep words with length greater than 4

long_words = [word for word in words if len(word) > 4]

print("Long Words:")
print(long_words)

# ============================================================

# PROGRAM 16: CONVERT CELSIUS TO FAHRENHEIT

# ============================================================

celsius = [0, 10, 20, 30, 40]

fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

print("Fahrenheit Values:")
print(fahrenheit)

# ============================================================

# PROGRAM 17: GET FIRST LETTER OF EACH WORD

# ============================================================

words = ["Python", "Java", "C", "JavaScript"]

first_letters = [word[0] for word in words]

print("First Letters:")
print(first_letters)

# ============================================================

# PROGRAM 18: REMOVE NEGATIVE NUMBERS

# ============================================================

numbers = [-5, 10, -15, 20, 25]

non_negative = [num for num in numbers if num >= 0]

print("Non Negative Numbers:")
print(non_negative)

# ============================================================

# PROGRAM 19: CREATE LIST OF BOOLEAN VALUES

# ============================================================

numbers = [1, 2, 3, 4, 5]

# Check whether numbers are even

boolean_result = [num % 2 == 0 for num in numbers]

print("Boolean Results:")
print(boolean_result)

# ============================================================

# PROGRAM 20: LIST COMPREHENSION USING FUNCTIONS

# ============================================================

def square(num):
return num * num

# Apply function to each number

result = [square(x) for x in range(1, 6)]

print("Squares using function:")
print(result)

# ============================================================

# 32. FINAL SUMMARY

# ============================================================

# List comprehension is one of the most powerful and commonly

# used features in Python.

#

# It helps write concise and readable code.

#

# Important concepts covered:

# ------------------------------------------------------------

# ✔ Basic syntax

# ✔ Conditions

# ✔ If-else

# ✔ Nested comprehensions

# ✔ Matrix operations

# ✔ String operations

# ✔ Dictionary usage

# ✔ Performance

# ✔ Memory usage

# ✔ Real-world examples

# ✔ Common mistakes

# ✔ Interview ques
