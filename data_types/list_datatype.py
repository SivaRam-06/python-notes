"""
╔════════════════════════════════════════════════════════════════════════════╗
║              PYTHON LISTS - LEARN WITH SIMPLE PROGRAMS                     ║
║                    Run each program to understand Lists                     ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 1: What is a List? (Ordered, Mutable Collection)
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 1: What is a List?")
print("="*70)

# Creating a list
fruits = ['apple', 'banana', 'orange', 'mango']
print(f"List: {fruits}")
print(f"Type: {type(fruits)}")
print(f"First element (index 0): {fruits[0]}")
print(f"Last element (index -1): {fruits[-1]}")
print(f"Length: {len(fruits)}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 2: Create Lists in Different Ways
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 2: Create Lists in Different Ways")
print("="*70)

# Way 1: Direct creation
list1 = [1, 2, 3, 4, 5]
print(f"Way 1 - Direct: {list1}")

# Way 2: Mixed data types
list2 = [1, 'hello', 3.14, True, None]
print(f"Way 2 - Mixed types: {list2}")

# Way 3: Nested lists
list3 = [[1, 2], ['a', 'b'], [10, 20]]
print(f"Way 3 - Nested: {list3}")

# Way 4: Using list() constructor
list4 = list('hello')
print(f"Way 4 - From string: {list4}")

# Way 5: Using range()
list5 = list(range(1, 6))
print(f"Way 5 - From range: {list5}")

# Way 6: Empty list
list6 = []
print(f"Way 6 - Empty: {list6}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 3: Access List Elements by Index
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 3: Access Elements by Index")
print("="*70)

numbers = [10, 20, 30, 40, 50]
print(f"List: {numbers}")

print(f"\nPositive indexing:")
print(f"Index 0: {numbers[0]}")
print(f"Index 2: {numbers[2]}")
print(f"Index 4: {numbers[4]}")

print(f"\nNegative indexing (from end):")
print(f"Index -1 (last): {numbers[-1]}")
print(f"Index -2 (second last): {numbers[-2]}")
print(f"Index -5 (first): {numbers[-5]}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 4: Slice Lists (Get Portions)
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 4: Slicing - Get Portions of List")
print("="*70)

letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"Original list: {letters}")

print(f"letters[1:4]: {letters[1:4]} (index 1 to 3)")
print(f"letters[:3]: {letters[:3]} (first 3 elements)")
print(f"letters[2:]: {letters[2:]} (from index 2 to end)")
print(f"letters[::2]: {letters[::2]} (every 2nd element)")
print(f"letters[::-1]: {letters[::-1]} (reversed)\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 5: Add Elements to List
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 5: Add Elements to List")
print("="*70)

my_list = [1, 2, 3]
print(f"Original: {my_list}")

# append() - add at end
my_list.append(4)
print(f"After append(4): {my_list}")

# insert() - add at specific position
my_list.insert(1, 10)
print(f"After insert(1, 10): {my_list}")

# extend() - add multiple elements
my_list.extend([5, 6])
print(f"After extend([5, 6]): {my_list}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 6: Remove Elements from List
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 6: Remove Elements from List")
print("="*70)

my_list = [10, 20, 30, 40, 50]
print(f"Original: {my_list}")

# remove() - remove by value
my_list.remove(30)
print(f"After remove(30): {my_list}")

# pop() - remove by index
removed = my_list.pop(1)
print(f"After pop(1) - removed {removed}: {my_list}")

# del - delete by index
del my_list[0]
print(f"After del [0]: {my_list}")

# clear() - remove all
my_list.clear()
print(f"After clear(): {my_list}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 7: Modify List Elements
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 7: Modify List Elements")
print("="*70)

scores = [10, 20, 30, 40]
print(f"Original: {scores}")

# Change single element
scores[1] = 25
print(f"After scores[1] = 25: {scores}")

# Change multiple elements (slice)
scores[0:2] = [15, 22]
print(f"After scores[0:2] = [15, 22]: {scores}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 8: Check if Element Exists
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 8: Check if Element Exists")
print("="*70)

colors = ['red', 'blue', 'green', 'yellow']
print(f"List: {colors}")

print(f"'red' in colors: {'red' in colors}")
print(f"'purple' in colors: {'purple' in colors}")
print(f"'blue' not in colors: {'blue' not in colors}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 9: Find Index and Count Elements
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 9: Find Index and Count Elements")
print("="*70)

data = [10, 20, 30, 20, 40, 20]
print(f"List: {data}")

# index() - find position
position = data.index(30)
print(f"Position of 30: {position}")

# count() - count occurrences
count = data.count(20)
print(f"Count of 20: {count}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 10: Loop Through List
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 10: Loop Through List")
print("="*70)

items = ['apple', 'banana', 'orange']
print(f"List: {items}\n")

# Using for loop
print("For loop:")
for item in items:
    print(f"  - {item}")

# Using enumerate
print("\nFor loop with index:")
for index, item in enumerate(items):
    print(f"  {index}: {item}\n")
# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 11: Sort and Reverse List
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 11: Sort and Reverse List")
print("="*70)

numbers = [5, 2, 8, 1, 9]
print(f"Original: {numbers}")

# sort() - sorts in place
numbers.sort()
print(f"After sort(): {numbers}")

# reverse() - reverses in place
numbers.reverse()
print(f"After reverse(): {numbers}")

# Using sorted() function - returns new list
new_numbers = [5, 2, 8, 1, 9]
sorted_list = sorted(new_numbers)
print(f"Original list: {new_numbers}")
print(f"sorted(list): {sorted_list} (original unchanged)\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 12: Copy Lists
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 12: Copy Lists (Shallow vs Assignment)")
print("="*70)

original = [1, 2, 3]
print(f"Original: {original}")

# Assignment - points to same list
reference = original
reference.append(4)
print(f"After reference.append(4):")
print(f"  Original: {original}")
print(f"  Reference: {reference}")
print(f"  Same object? {original is reference}")

# copy() - creates actual copy
original2 = [10, 20, 30]
copy_list = original2.copy()
copy_list.append(40)
print(f"\nAfter copy_list.append(40):")
print(f"  Original: {original2}")
print(f"  Copy: {copy_list}")
print(f"  Same object? {original2 is copy_list}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 13: Built-in Functions
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 13: Built-in Functions (len, min, max, sum)")
print("="*70)

numbers = [5, 2, 8, 1, 9, 3]
print(f"List: {numbers}")

print(f"len(list): {len(numbers)} - How many elements?")
print(f"min(list): {min(numbers)} - Smallest element")
print(f"max(list): {max(numbers)} - Largest element")
print(f"sum(list): {sum(numbers)} - Sum of all elements\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 14: Real-World Example - Student Grades
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 14: Real-World Example - Student Grades")
print("="*70)

grades = [85, 90, 78, 92, 88]
print(f"Grades: {grades}")
print(f"Total students: {len(grades)}")
print(f"Highest grade: {max(grades)}")
print(f"Lowest grade: {min(grades)}")
print(f"Average: {sum(grades) / len(grades):.2f}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 15: Real-World Example - To-Do List
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 15: Real-World Example - To-Do List Management")
print("="*70)

tasks = ['Buy groceries', 'Finish homework', 'Call mom']
print(f"Tasks: {tasks}\n")

# Add task
tasks.append('Pay bills')
print(f"Added 'Pay bills': {tasks}")

# Remove task
tasks.remove('Finish homework')
print(f"Completed 'Finish homework': {tasks}")

# Check if task exists
if 'Buy groceries' in tasks:
    print(f"'Buy groceries' is still pending")

print(f"Total tasks: {len(tasks)}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 16: Real-World Example - Shopping Cart
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 16: Real-World Example - Shopping Cart")
print("="*70)

cart = [
    {'item': 'Laptop', 'price': 50000},
    {'item': 'Mouse', 'price': 500},
    {'item': 'Keyboard', 'price': 2000}
]

print("Shopping Cart:")
for item in cart:
    print(f"  {item['item']}: ₹{item['price']}")

total = sum(item['price'] for item in cart)
print(f"Total: ₹{total}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 17: Key Differences - List vs Tuple vs Set
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 17: When to Use Lists?")
print("="*70)

print("""
USE LISTS WHEN YOU NEED:
  ✓ Ordered collection (maintains order)
  ✓ Access by index (list[0], list[1])
  ✓ Mutable (can add/remove/modify)
  ✓ Allow duplicates
  ✓ Store multiple different data types

EXAMPLES:
  • Student list
  • To-do list
  • Inventory items
  • Shopping cart
  • Search results
  • Chat messages
  • Game scores

DON'T USE LISTS WHEN YOU NEED:
  ❌ Immutable collection → Use Tuple
  ❌ Unique elements only → Use Set
  ❌ Key-value pairs → Use Dictionary
  ❌ No access by index → Use Set/Dictionary
""")

print("="*70)

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 18: Important Points to Remember
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("IMPORTANT POINTS TO REMEMBER")
print("="*70)

print("""
1. ORDERED - Elements have a specific order
   list[0] is always the first element
   Order is preserved

2. INDEXED - Access by position (0, 1, 2, ...)
   ✓  list[0]    - First element
   ✓  list[-1]   - Last element
   ✓  list[1:4]  - Slice elements 1-3

3. MUTABLE - Can be modified after creation
   ✓  append()   - Add at end
   ✓  insert()   - Add at position
   ✓  remove()   - Remove element
   ✓  pop()      - Remove by index
   ✓  list[0] = value - Change element

4. DUPLICATES ALLOWED
   [1, 1, 2, 2, 3] is valid
   Same element can appear multiple times

5. MIXED TYPES ALLOWED
   [1, 'hello', 3.14, True, None] is valid
   Can store any data type

6. IMPORTANT METHODS
   append(x)    - Add at end
   insert(i, x) - Add at position i
   remove(x)    - Remove first x
   pop(i)       - Remove at index
   index(x)     - Find position
   count(x)     - Count occurrences
   sort()       - Sort in place
   reverse()    - Reverse in place
   copy()       - Create copy
   clear()      - Remove all

7. BUILT-IN FUNCTIONS
   len(list)      - Number of elements
   max(list)      - Largest value
   min(list)      - Smallest value
   sum(list)      - Sum of numbers
   sorted(list)   - Return sorted list

8. SLICING SYNTAX
   list[start:end:step]
   list[1:4]      - Elements 1,2,3
   list[:3]       - First 3 elements
   list[2:]       - From element 2 to end
   list[::2]      - Every 2nd element
   list[::-1]     - Reversed
""")
print("After sort:", my_list)  # Output: [1, 2, 3, 4]

# reverse() : reverses the order of elements in the list.
my_list.reverse()
print("After reverse:", my_list)  # Output: [4, 3, 2, 1]

#copy() - to create a copy of given list

#operations on list 
'''
1. operators working on list:
    - concatenation - the + operator is used to concatenate two lists.
    example:
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    result = list1 + list2
    print(result) #output: [1, 2, 3, 4, 5, 6]
    - repetition - the * operator is used to repeat a list a specified number of times.
    example:
    list1 = [1, 2, 3]
    result = list1 * 3
    print(result) #output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
    - membership - the in operator is used to check if an element is present in a list
    example:
    list1 = [1, 2, 3, 4, 5]
    print(3 in list1) #output: True
    print(6 in list1) #output: False
    - relational - comparison operators (==, !=, <, >, <=, >=) can be used to compare two lists.
    example:
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(list1 == list2) #output: True
    - identity - the is operator is used to check if two lists are the same object in memory.
    example:
    list1 = [1, 2, 3]
    list2 = list1
    print(list1 is list2) #output: True
2. indexing and slicing:
    - indexing and sclicing are similar to that of strings data type as list is mutable,
        elements at a particular position can be changed by reassignment using index.
    a = [1,3,5]
    print(a)
    a[1] = 4
    print(a) #output: [1, 4, 5]
3. built-in functions with list:
    - len(): returns the number of elements in the list.
    - min(): returns the smallest element in the list.
    - max(): returns the largest element in the list.
    - sum(): returns the sum of all elements in the list (only for numeric lists).
    - sorted(): returns a new list containing all elements from the original list in ascending order.
    - list(): converts an iterable (like a string or tuple) into a list.

'''
# list split()
string = "apple,banana,cherry"
fruits = string.split(',')
print("Fruits list:", fruits)  # Output: ['apple', 'banana', 'cherry']
#space separated elements input
l_space = input("Enter elements: ").split()
print("List from space-separated input:", l_space)
# comma separated elements input
l_comma = input("Enter elements: ").split(',')
print("List from comma-separated input:", l_comma)
'''
write a program to check how many words are given as input and input will be single line
with space separated words. output should be number saying how many words are there in the input.
'''
user_input_words = input("Enter words separated by space: ").split()
word_count = len(user_input_words)
print("Number of words entered:", word_count)

#map() function with list
'''
map() in simple terms is a function that takes another function and a iterable as inputs and applies that function to each item in the iterable.
It returns a map object (which is an iterator) that can be converted into other iterables
'''
nums_1 =  input("Enter numbers separated by space: ").split()
print("Before map:", nums_1)  # Output: List of strings
print("After map:", list(map(int, nums_1)))  # Output: List of integers
#directly using map with list
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("List of integers:", nums)
'''
write a program to find the maximum element in given numbers.input will be single line 
with space separated numbers.
'''
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
max_number = max(numbers)
print("Maximum number entered:", max_number)
'''
write a program to sort the given numbers as a list 
input will be single line with space separated numbers.
output should be a list with the elements sorted in ascending order.
'''
numbers_to_sort = list(map(int, input("Enter numbers separated by comma: ").split(',')))
sorted_num = sorted(numbers_to_sort)
print("Sorted numbers using sorted():", sorted_num)
numbers_to_sort.sort()
print("Sorted numbers:", numbers_to_sort)
'''
write a program to find the second greatest element from the given elements.
input will be single line comma separated numbers.
output should be a single number
'''
elements = list(map(int, input("Enter numbers separated by comma: ").split(',')))
second_greatest = sorted(elements)
single_number = second_greatest[-2]
print("Second greatest number is:", single_number)
'''
write a program to find the average of the given numbers.
input will be single line space separated numbers.
output should be average of the numbers.
'''
nums_for_avg = list(map(int, input("Enter numbers separated by space: ").split()))
average = sum(nums_for_avg) / len(nums_for_avg)
print("Average of the numbers is:", average)
print('Average : {}'.format(average))

'''
write a program to find the missing number from the given series
the series starts from 1 and ends at some n.
there will be a total of n-1 numbers as one number goes missing.
find that missing number.
'''
series_numbers = list(map(int, input("Enter numbers separated by space: ").split()))
len = len(series_numbers)+1
expected_sum = len * (len + 1) // 2
actual_sum = sum(series_numbers)
missing_number = expected_sum - actual_sum
print("Missing number is:", missing_number)

nums = list(map(int, input().split()))
n = nums[-1]
correct_nums = (n * (n + 1)) // 2
nums_sum = sum(nums)
missing_num = correct_nums - nums_sum
print(missing_num)

# program to find the missing square number from the given series
nums = list(map(int, input().split()))
last = nums[-1]
n = last**0.5
nums_sum = n * (n + 1) * (2 * n + 1) // 6
given_sum = sum(nums)
missing_square = nums_sum - given_sum
print(missing_square)

nums = list(map(int, input().split()))
n = len(nums) + 1
correct_sum = n*(n + 1)*(2*n + 1)/6
nums_sum = sum(nums)
missing_square_num = correct_sum - nums_sum
print(missing_square_num)

'''
write a program to find the number of characters present at even positions in the given string.
'''
name = input("Enter a string: ")
even_position = name[1::2]
count = len(even_position)
print(count)
'''
write a program to find the sum of even numbers present in the given series of
natural numbers from 1 to n.
input: 1 2 3 4 5 6 7 8
output: 20
'''
nums = list(map(int, input("Enter numbers separated by space: ").split()))
even = nums[1::2]
sum_even = sum(even)
print(sum_even)

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 19: UNPACKING LISTS - Assign to Multiple Variables
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 19: UNPACKING LISTS - Assign to Multiple Variables")
print("="*70)

# Basic unpacking (number of variables must match)
numbers = [1, 2, 3]
a, b, c = numbers
print(f"List: {numbers}")
print(f"Unpacked: a={a}, b={b}, c={c}")

# Unpacking with rest (*rest)
data = [10, 20, 30, 40, 50]
first, *middle, last = data
print(f"\nList: {data}")
print(f"first={first}, middle={middle}, last={last}")

# Unpacking only some values
colors = ['red', 'green', 'blue', 'yellow']
color1, color2, *rest = colors
print(f"\nList: {colors}")
print(f"color1={color1}, color2={color2}, rest={rest}")

# Ignoring values with _
scores = [85, 90, 78, 92]
high, low, _, _ = scores
print(f"\nList: {scores}")
print(f"high={high}, low={low} (other values ignored)\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 20: CONVERT LIST TO OTHER DATA TYPES
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 20: CONVERT LIST → TUPLE / SET / STRING / DICT")
print("="*70)

original_list = [1, 2, 3, 4, 5]
print(f"Original List: {original_list}")

# Convert to TUPLE
my_tuple = tuple(original_list)
print(f"\n✓ To Tuple: {my_tuple}")
print(f"  Type: {type(my_tuple)}")
print(f"  Use when: Need immutable, hashable collection")

# Convert to SET
my_set = set(original_list)
print(f"\n✓ To Set: {my_set}")
print(f"  Type: {type(my_set)}")
print(f"  Use when: Need unique elements only")

# Convert to STRING
my_string = str(original_list)
print(f"\n✓ To String: {my_string}")
print(f"  Type: {type(my_string)}")
print(f"  Use when: Need text representation")

# Convert to DICTIONARY
list_pairs = [('name', 'Alice'), ('age', 25), ('city', 'Delhi')]
my_dict = dict(list_pairs)
print(f"\n✓ To Dictionary (from pairs): {my_dict}")
print(f"  Type: {type(my_dict)}")
print(f"  Use when: Need key-value pairs\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 21: CONVERT OTHER TYPES TO LIST
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 21: CONVERT TUPLE / SET / STRING / DICT → LIST")
print("="*70)

# From TUPLE
my_tuple = (1, 2, 3, 4)
list_from_tuple = list(my_tuple)
print(f"From Tuple: {my_tuple}")
print(f"To List: {list_from_tuple}")
print(f"Use when: Need to add/modify elements in tuple")

# From SET
my_set = {5, 2, 8, 1}
list_from_set = list(my_set)
print(f"\nFrom Set: {my_set}")
print(f"To List: {list_from_set}")
print(f"Use when: Need ordering or indexing of set elements")

# From STRING
my_string = "hello"
list_from_string = list(my_string)
print(f"\nFrom String: '{my_string}'")
print(f"To List: {list_from_string}")
print(f"Use when: Need to work with individual characters")

# From DICTIONARY (keys)
my_dict = {'name': 'Alice', 'age': 25, 'city': 'Delhi'}
list_keys = list(my_dict.keys())
list_values = list(my_dict.values())
print(f"\nFrom Dictionary: {my_dict}")
print(f"To List (keys): {list_keys}")
print(f"To List (values): {list_values}")
print(f"Use when: Need to work with just keys or values\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 22: WHEN TO CONVERT - DECISION GUIDE
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 22: WHEN TO CONVERT - DECISION GUIDE")
print("="*70)

print("""
CONVERSION SCENARIOS:

1. LIST → TUPLE (When to convert)
   ✓ Need immutable collection
   ✓ Use as dictionary key
   ✓ Use in set
   ✓ Want faster performance
   ✓ Thread-safe shared data
   Example:
   tasks = [('complete', 'urgent'), ('review', 'normal')]
   tasks = set(map(tuple, tasks))  # Remove duplicates


2. LIST → SET (When to convert)
   ✓ Need unique elements (remove duplicates)
   ✓ Need fast membership checking
   ✓ Need set operations (union, intersection)
   ✓ Need hashable items
   Example:
   items = [1, 2, 2, 3, 3, 3]
   unique_items = set(items)  # Output: {1, 2, 3}


3. LIST → STRING (When to convert)
   ✓ Need text representation
   ✓ Printing/displaying
   ✓ Saving to file
   ✓ Sending over network
   Example:
   data = [1, 2, 3]
   text = str(data)  # Output: '[1, 2, 3]'


4. LIST → DICTIONARY (When to convert)
   ✓ Have key-value pairs
   ✓ Need fast lookup by key
   ✓ Building configuration
   Example:
   pairs = [('id', 1), ('name', 'Alice')]
   record = dict(pairs)


5. TUPLE → LIST (When to convert)
   ✓ Need to modify (add/remove/change)
   ✓ Need list-only methods
   ✓ Building dynamic collection
   Example:
   fixed = (1, 2, 3)
   mutable = list(fixed)
   mutable.append(4)


6. SET → LIST (When to convert)
   ✓ Need ordering
   ✓ Need indexing
   ✓ Need list methods
   Example:
   unique = {3, 1, 2}
   sorted_list = sorted(set_data)


7. STRING → LIST (When to convert)
   ✓ Need character-by-character processing
   ✓ Need to modify characters
   ✓ Splitting into parts
   Example:
   text = 'hello'
   chars = list(text)  # ['h', 'e', 'l', 'l', 'o']


8. DICTIONARY → LIST (When to convert)
   ✓ Need keys only
   ✓ Need values only
   ✓ Need key-value pairs
   Example:
   config = {'host': 'localhost', 'port': 8000}
   keys = list(config.keys())
""")

print("="*70)

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 23: REAL EXAMPLE - Data Pipeline with Conversions
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 23: REAL EXAMPLE - Data Pipeline with Conversions")
print("="*70)

# Step 1: Start with list (duplicates)
raw_data = [2, 3, 2, 5, 3, 7, 5]
print(f"Step 1 - Raw data (LIST): {raw_data}")

# Step 2: Convert to set to remove duplicates
unique_data = set(raw_data)
print(f"Step 2 - Remove duplicates (SET): {unique_data}")

# Step 3: Convert to list and sort
sorted_data = sorted(list(unique_data))
print(f"Step 3 - Sort (LIST): {sorted_data}")

# Step 4: Convert to tuple for immutability
final_data = tuple(sorted_data)
print(f"Step 4 - Final immutable (TUPLE): {final_data}")

# Step 5: Use as dictionary value
results = {'data': final_data, 'count': len(final_data)}
print(f"Step 5 - Store in dict: {results}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 24: CONVERSION QUICK REFERENCE
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 24: CONVERSION QUICK REFERENCE")
print("="*70)

print("""
FROM\TO     TUPLE          SET            STRING         DICT
════════════════════════════════════════════════════════════════
LIST        tuple(list)    set(list)      str(list)      dict(pairs)
                ✓ Add imm.   ✓ Unique       ✓ Display      ✓ K-V pairs
                
TUPLE       -              set(tuple)     str(tuple)     dict(pairs)
                           ✓ Unique       ✓ Display      ✓ K-V pairs
                
SET         tuple(set)     -              str(set)       dict(pairs)
            ✓ Order lost   (already)      ✓ Display      ✓ K-V pairs
                
STRING      tuple(str)     set(str)       -              dict(pairs)
            ✓ Chars        ✓ Unique       (already)      ✓ K-V pairs
                
DICT        tuple(d.items()) set(d.keys()) str(dict)      -
            ✓ K-V pairs    ✓ Keys only    ✓ Display      (already)


CONVERSION EXAMPLES:
═════════════════════════════════════════════════════════════════

# List operations
numbers = [1, 2, 2, 3]
unique = set(numbers)              # [1,2,2,3] → {1,2,3}
sorted_nums = sorted(unique)       # {1,2,3} → [1,2,3]

# String processing
text = "hello"
chars = list(text)                 # "hello" → ['h','e','l','l','o']
unique_chars = set(text)           # "hello" → {'h','e','l','o'}

# Tuple unpacking
values = [10, 20, 30]
a, b, c = values                   # Unpack directly
x, *rest = values                  # x=10, rest=[20,30]

# Dictionary conversion
pairs = [('x', 1), ('y', 2)]
data = dict(pairs)                 # → {'x': 1, 'y': 2}

# Nested conversion
matrix = [[1,2], [3,4]]
flat_list = [x for row in matrix for x in row]  # [1,2,3,4]
""")

print("="*70)