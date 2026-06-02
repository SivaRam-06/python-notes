# 📚 Python Data Types: Unpacking & Conversion Complete Guide

## Overview
This guide explains how to **unpack** and **convert** between all Python data types with practical examples.

---

## 🎯 QUICK REFERENCE TABLE

### Unpacking Methods by Data Type

| Data Type | Unpacking | Example |
|-----------|-----------|---------|
| **LIST** | Basic: `a,b,c = [1,2,3]` | `x, *rest, y = [1,2,3,4,5]` |
| **TUPLE** | Basic: `a,b,c = (1,2,3)` | `x, *rest, y = (1,2,3,4,5)` |
| **STRING** | Basic: `a,b,c = "ABC"` | `x, *rest, y = "ABCDE"` |
| **DICT** | Via items: `for k,v in dict.items()` | dict_comp: `{k:v*2 for k,v in d.items()}` |
| **SET** | Via sort: `a,b,c = sorted({1,2,3})` | `x, *rest = sorted(set_data)` |
| **FROZENSET** | Via sort: `a,b,c = sorted(fs)` | `x, *rest = sorted(frozenset_data)` |

---

## 1️⃣ LIST UNPACKING & CONVERSION

### Unpacking Lists
```python
# Basic unpacking
numbers = [1, 2, 3]
a, b, c = numbers

# With rest (*rest)
data = [10, 20, 30, 40, 50]
first, *middle, last = data
# first = 10, middle = [20, 30, 40], last = 50

# Ignoring values
scores = [85, 90, 78, 92]
high, low, _, _ = scores
```

### Converting FROM List
```python
list_data = [1, 2, 3, 4]

# → TUPLE
my_tuple = tuple(list_data)
✓ Use when: Need immutable, use as dict key

# → SET
my_set = set(list_data)
✓ Use when: Remove duplicates, fast lookup

# → STRING
my_string = str(list_data)
✓ Use when: Display, print, save to file

# → DICT (from pairs)
pairs = [('name', 'Alice'), ('age', 25)]
my_dict = dict(pairs)
✓ Use when: Have key-value pairs
```

### Converting TO List
```python
# FROM TUPLE
tuple_data = (1, 2, 3)
my_list = list(tuple_data)
✓ Use when: Need to add/modify elements

# FROM SET
set_data = {3, 1, 2}
my_list = list(set_data)
✓ Use when: Need ordering or indexing

# FROM STRING
string_data = "hello"
my_list = list(string_data)
✓ Use when: Work with individual characters

# FROM DICT
dict_data = {'name': 'Alice', 'age': 25}
keys = list(dict_data.keys())
values = list(dict_data.values())
items = list(dict_data.items())
```

---

## 2️⃣ TUPLE UNPACKING & CONVERSION

### Unpacking Tuples
```python
# Basic unpacking
coords = (10, 20)
x, y = coords

# Multiple values
person = ('Alice', 25, 'Engineer')
name, age, job = person

# With rest
data = (1, 2, 3, 4, 5)
first, *middle, last = data

# Swapping
a, b = (100, 200)
a, b = b, a  # a = 200, b = 100
```

### Converting FROM Tuple
```python
tuple_data = (1, 2, 3, 4)

# → LIST
my_list = list(tuple_data)
✓ Use when: Need to add/remove/modify

# → SET
my_set = set(tuple_data)
✓ Use when: Remove duplicates, unique elements

# → STRING
my_string = str(tuple_data)
✓ Use when: Display, print

# → FROZENSET
my_fs = frozenset(tuple_data)
✓ Use when: Need immutable hashable set
```

### Converting TO Tuple
```python
# FROM LIST
list_data = [1, 2, 3]
my_tuple = tuple(list_data)
✓ Use when: Immutability, dict key, set element

# FROM SET
set_data = {5, 2, 8}
my_tuple = tuple(set_data)
✓ Use when: Ordered immutable collection

# FROM STRING
string_data = "hello"
my_tuple = tuple(string_data)
✓ Use when: Immutable character sequence

# FROM DICT
dict_data = {'a': 1, 'b': 2}
items_tuple = tuple(dict_data.items())
✓ Use when: Preserve key-value pairs
```

---

## 3️⃣ DICTIONARY UNPACKING & CONVERSION

### Unpacking Dictionaries
```python
# Loop through key-value pairs
person = {'name': 'Alice', 'age': 25}
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary comprehension
scores = {'Alice': 85, 'Bob': 90}
doubled = {name: score*2 for name, score in scores.items()}

# Extract to variables
name, age, *_ = person.keys()
```

### Converting FROM Dictionary
```python
dict_data = {'name': 'Alice', 'age': 25, 'city': 'Delhi'}

# → LIST (keys)
keys_list = list(dict_data)
✓ Use when: Need list of keys

# → LIST (values)
values_list = list(dict_data.values())
✓ Use when: Need list of values

# → LIST (items)
items_list = list(dict_data.items())
✓ Use when: Need key-value pairs as list

# → TUPLE (items)
items_tuple = tuple(dict_data.items())
✓ Use when: Need immutable pairs

# → SET (keys)
keys_set = set(dict_data)
✓ Use when: Unique keys, fast lookup

# → STRING
dict_string = str(dict_data)
✓ Use when: Display, text representation
```

### Converting TO Dictionary
```python
# FROM LIST of pairs
pairs = [('x', 1), ('y', 2)]
my_dict = dict(pairs)
✓ Use when: Have key-value pairs

# FROM TWO LISTS
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
✓ Use when: Separate keys and values

# FROM TUPLE of pairs
tuple_pairs = (('id', 101), ('name', 'Alice'))
my_dict = dict(tuple_pairs)
✓ Use when: Pairs as tuples

# FROM STRING (parsing)
data_string = "name=Alice;age=25"
my_dict = dict(item.split('=') for item in data_string.split(';'))
✓ Use when: Parse structured text
```

---

## 4️⃣ STRING UNPACKING & CONVERSION

### Unpacking Strings
```python
# Basic character unpacking
word = "ABC"
a, b, c = word

# With rest
text = "Hello"
first, *middle, last = text
# first = 'H', middle = ['e','l','l'], last = 'o'

# Via split
date_str = "2024-01-15"
year, month, day = date_str.split('-')
```

### Converting FROM String
```python
string_data = "hello"

# → LIST (characters)
my_list = list(string_data)  # ['h', 'e', 'l', 'l', 'o']
✓ Use when: Character-by-character processing

# → TUPLE (characters)
my_tuple = tuple(string_data)  # ('h', 'e', 'l', 'l', 'o')
✓ Use when: Immutable characters

# → SET (unique characters)
my_set = set(string_data)  # {'h', 'e', 'l', 'o'}
✓ Use when: Unique characters only

# → INT (numeric string)
int_value = int("42")
✓ Use when: String contains number

# → FLOAT (decimal string)
float_value = float("3.14")
✓ Use when: String contains decimal

# → LIST (split into words)
words = "Python is amazing".split()
✓ Use when: Break into words/parts
```

### Converting TO String
```python
# FROM LIST
list_data = [1, 2, 3]
str_simple = str(list_data)  # "[1, 2, 3]"
str_csv = ','.join(map(str, list_data))  # "1,2,3"
✓ Use when: Display or custom format

# FROM INT
int_data = 42
str_data = str(int_data)
✓ Use when: Text version of number

# FROM FLOAT
float_data = 3.14
str_data = str(float_data)
✓ Use when: Text version of decimal

# FROM TUPLE
tuple_data = (1, 2, 3)
str_data = str(tuple_data)
✓ Use when: Display tuple

# FROM DICT
dict_data = {'name': 'Alice'}
str_data = str(dict_data)
✓ Use when: Display dictionary
```

---

## 5️⃣ SET UNPACKING & CONVERSION

### Unpacking Sets
```python
# Note: Need to sort first (sets are unordered)
my_set = {1, 2, 3}
a, b, c = sorted(my_set)

# With rest
data_set = {10, 20, 30, 40, 50}
first, *rest = sorted(data_set)
```

### Converting FROM Set
```python
set_data = {1, 2, 3, 4, 5}

# → LIST
my_list = list(set_data)
✓ Use when: Need ordering or indexing
ordered_list = sorted(list(set_data))

# → TUPLE
my_tuple = tuple(set_data)
✓ Use when: Need immutable collection

# → STRING
my_string = str(set_data)
✓ Use when: Display, print

# → FROZENSET
my_fs = frozenset(set_data)
✓ Use when: Need hashable set
```

### Converting TO Set
```python
# FROM LIST
list_data = [1, 2, 2, 3, 3, 3]
my_set = set(list_data)  # {1, 2, 3}
✓ Use when: Remove duplicates

# FROM TUPLE
tuple_data = (10, 20, 10, 30)
my_set = set(tuple_data)  # {10, 20, 30}
✓ Use when: Get unique elements

# FROM STRING
string_data = "hello"
my_set = set(string_data)  # {'h', 'e', 'l', 'o'}
✓ Use when: Find unique characters
```

---

## 6️⃣ FROZENSET UNPACKING & CONVERSION

### Unpacking Frozensets
```python
# Sort first (frozensets are unordered)
my_fs = frozenset({1, 2, 3})
a, b, c = sorted(my_fs)

# With rest
data_fs = frozenset({10, 20, 30, 40, 50})
first, *rest = sorted(data_fs)
```

### Converting FROM Frozenset
```python
fs_data = frozenset({1, 2, 3, 4, 5})

# → SET
my_set = set(fs_data)
✓ Use when: Need mutable set

# → LIST
my_list = list(fs_data)
sorted_list = sorted(list(fs_data))
✓ Use when: Need ordering/indexing

# → TUPLE
my_tuple = tuple(fs_data)
✓ Use when: Ordered immutable

# → STRING
my_string = str(fs_data)
✓ Use when: Display
```

### Converting TO Frozenset
```python
# FROM SET
set_data = {1, 2, 3}
my_fs = frozenset(set_data)
✓ Use when: Need immutable, dict key, set element

# FROM LIST
list_data = [1, 2, 2, 3]
my_fs = frozenset(list_data)  # frozenset({1, 2, 3})
✓ Use when: Unique + immutable

# FROM TUPLE
tuple_data = (5, 5, 10, 15)
my_fs = frozenset(tuple_data)
✓ Use when: Convert to immutable set

# FROM STRING
string_data = "hello"
my_fs = frozenset(string_data)
✓ Use when: Immutable unique chars
```

---

## 🔄 CONVERSION DECISION MATRIX

### When to Convert: Quick Lookup

| Current | Goal | Reason | Code |
|---------|------|--------|------|
| List | Tuple | Need immutable | `tuple(list)` |
| List | Set | Remove duplicates | `set(list)` |
| List | String | Display | `str(list)` |
| Set | List | Need indexing | `list(set)` |
| Set | Tuple | Need ordered immutable | `tuple(set)` |
| String | List | Character processing | `list(string)` |
| String | Int | Parse number | `int(string)` |
| Dict | List | Extract keys/values | `list(dict.keys())` |
| Tuple | List | Need to modify | `list(tuple)` |
| Any | String | Display/print | `str(any)` |

---

## 📊 REAL-WORLD CONVERSION PIPELINES

### Pipeline 1: Data Deduplication
```python
# Raw data with duplicates
raw_data = [5, 2, 8, 2, 5, 1, 8, 3]

# Step 1: Convert to set to remove duplicates
unique_data = set(raw_data)

# Step 2: Convert to list and sort
sorted_data = sorted(list(unique_data))

# Step 3: Convert to tuple (final immutable result)
final_data = tuple(sorted_data)

print(final_data)  # (1, 2, 3, 5, 8)
```

### Pipeline 2: CSV Parsing
```python
# Raw CSV data
csv_line = "John,25,Engineer,50000"

# Step 1: Split into list
fields = csv_line.split(',')

# Step 2: Convert to appropriate types
name = fields[0]
age = int(fields[1])
job = fields[2]
salary = float(fields[3])

# Step 3: Build dictionary
record = {'name': name, 'age': age, 'job': job, 'salary': salary}

print(record)  # {'name': 'John', 'age': 25, 'job': 'Engineer', 'salary': 50000.0}
```

### Pipeline 3: Immutable Cache Keys
```python
# Step 1: Create mutable set
tags = {'python', 'coding', 'tutorial'}

# Step 2: Convert to frozenset (immutable)
locked_tags = frozenset(tags)

# Step 3: Use as dictionary key
cache = {
    locked_tags: 'Python coding tutorials content',
    frozenset({'java', 'coding'}): 'Java coding content'
}

# Step 4: Lookup from cache
content = cache[locked_tags]
```

### Pipeline 4: Data Transformation
```python
# Data with multiple types
data_string = "1,2,3,4,5"

# Step 1: Split string to list
numbers_list = data_string.split(',')

# Step 2: Convert to integers
int_list = [int(x) for x in numbers_list]

# Step 3: Convert to set (unique)
unique_set = set(int_list)

# Step 4: Convert to sorted list
sorted_list = sorted(list(unique_set))

# Step 5: Convert to tuple (final)
final_tuple = tuple(sorted_list)

print(final_tuple)  # (1, 2, 3, 4, 5)
```

---

## ✅ IMPORTANT RULES

### Unpacking Rules
- ✓ Number of variables must match (or use `*rest`)
- ✓ Works left-to-right assignment
- ✓ `*variable` captures remaining values
- ✓ Use `_` to ignore values

### Conversion Rules
- ✓ Can only convert between compatible types
- ✓ Order not preserved: set/dict → list needs sort
- ✓ String conversion: use `str(data)`
- ✓ Numeric string conversion: use `int()` or `float()`
- ✓ Immutable types: tuple, frozenset, str
- ✓ Mutable types: list, set, dict

### When NOT to Convert
- ❌ Don't convert immutable to mutable for temporary use (performance loss)
- ❌ Don't use list as dict key (use tuple)
- ❌ Don't use mutable in set (use tuple/frozenset)
- ❌ Don't convert large datasets unnecessarily (memory waste)

---

## 🎓 SUMMARY: Each File Has

Each data type file in the folder now includes:

1. **Unpacking Programs** - How to extract values
2. **Conversion FROM** - Convert this type to others
3. **Conversion TO** - Convert other types to this type
4. **Decision Guide** - When and why to convert
5. **Real-World Examples** - Practical conversion pipelines
6. **Quick Reference Table** - Fast lookup guide

**Run each program to see output and understand better!**

---

## 📝 FILE LOCATIONS

- `list_datatype.py` - Programs 19-24
- `tuple_datatype.py` - Programs 18-23
- `dictionary_datatype.py` - Programs 16-21
- `string_datatype.py` - Programs 18-23
- `set_datatype.py` - Programs 17-22
- `frozenset_datatype.py` - Programs 17-22

---

## 🚀 NEXT STEPS

1. Run each program to see output
2. Modify examples with your own data
3. Practice unpacking and conversions
4. Build your own conversion pipelines
5. Understand when to use each conversion

Happy Learning! 🎉
