"""
╔════════════════════════════════════════════════════════════════════════════╗
║         PYTHON DICTIONARIES - LEARN WITH SIMPLE PROGRAMS                   ║
║           Run each program to understand Dictionaries                       ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 1: What is a Dictionary? (Key-Value Pairs)
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 1: What is a Dictionary?")
print("="*70)

# Creating a dictionary
student = {'name': 'Alice', 'age': 20, 'grade': 'A'}
print(f"Dictionary: {student}")
print(f"Type: {type(student)}")
print(f"Value of 'name' key: {student['name']}")
print(f"Number of key-value pairs: {len(student)}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 2: Create Dictionaries in Different Ways
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 2: Create Dictionaries in Different Ways")
print("="*70)

# Way 1: Direct creation
dict1 = {'name': 'Bob', 'age': 25}
print(f"Way 1 - Direct: {dict1}")

# Way 2: Using dict() constructor
dict2 = dict(name='Carol', age=22)
print(f"Way 2 - dict() constructor: {dict2}")

# Way 3: From list of tuples
dict3 = dict([('x', 10), ('y', 20), ('z', 30)])
print(f"Way 3 - From list of tuples: {dict3}")

# Way 4: From two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict4 = dict(zip(keys, values))
print(f"Way 4 - From two lists: {dict4}")

# Way 5: Mixed data types as values
dict5 = {'integer': 42, 'string': 'hello', 'float': 3.14, 'list': [1,2,3]}
print(f"Way 5 - Mixed types: {dict5}")

# Way 6: Empty dictionary
dict6 = {}
print(f"Way 6 - Empty: {dict6}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 3: Access Dictionary Values
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 3: Access Dictionary Values")
print("="*70)

person = {'name': 'David', 'age': 30, 'city': 'Delhi', 'email': 'david@mail.com'}
print(f"Dictionary: {person}")

# Using square bracket
print(f"\nUsing dict['key']:")
print(f"person['name']: {person['name']}")
print(f"person['age']: {person['age']}")

# Using get() method (safer)
print(f"\nUsing dict.get('key'):")
print(f"person.get('city'): {person.get('city')}")
print(f"person.get('phone', 'Not found'): {person.get('phone', 'Not found')}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 4: Add and Modify Dictionary Elements
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 4: Add and Modify Dictionary Elements")
print("="*70)

user = {'name': 'Eve', 'age': 25}
print(f"Original: {user}")

# Add new key-value pair
user['email'] = 'eve@mail.com'
print(f"After adding email: {user}")

# Modify existing value
user['age'] = 26
print(f"After updating age: {user}")

# Add multiple key-value pairs
user.update({'city': 'Mumbai', 'phone': '9876543210'})
print(f"After update(): {user}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 5: Remove Dictionary Elements
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 5: Remove Dictionary Elements")
print("="*70)

data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(f"Original: {data}")

# del - delete specific key
del data['b']
print(f"After del data['b']: {data}")

# pop() - remove and return value
removed = data.pop('a')
print(f"After pop('a') - returned {removed}: {data}")

# popitem() - remove last item
removed_item = data.popitem()
print(f"After popitem() - removed {removed_item}: {data}")

# clear() - remove all
data.clear()
print(f"After clear(): {data}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 6: Get Dictionary Keys, Values, and Items
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 6: Get Keys, Values, and Items")
print("="*70)

product = {'name': 'Laptop', 'price': 50000, 'brand': 'Dell', 'color': 'Silver'}
print(f"Dictionary: {product}")

print(f"\nkeys(): {product.keys()}")
print(f"values(): {product.values()}")
print(f"items(): {product.items()}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 7: Loop Through Dictionary
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 7: Loop Through Dictionary")
print("="*70)

scores = {'Alice': 85, 'Bob': 90, 'Carol': 78}
print(f"Dictionary: {scores}\n")

# Loop through keys only
print("Loop through keys:")
for key in scores:
    print(f"  {key}: {scores[key]}")

# Loop through key-value pairs
print("\nLoop through items (key-value):")
for key, value in scores.items():
    print(f"  {key}: {value}")

# Loop through values only
print("\nLoop through values:")
for value in scores.values():
    print(f"  {value}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 8: Check if Key or Value Exists
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 8: Check if Key or Value Exists")
print("="*70)

contacts = {'Alice': '9876543210', 'Bob': '9876543211', 'Carol': '9876543212'}
print(f"Dictionary: {contacts}")

print(f"\n'Alice' in contacts: {'Alice' in contacts}")
print(f"'David' in contacts: {'David' in contacts}")
print(f"'9876543210' in contacts.values(): {'9876543210' in contacts.values()}")
print(f"'9876543215' in contacts.values(): {'9876543215' in contacts.values()}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 9: Nested Dictionaries
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 9: Nested Dictionaries")
print("="*70)

students = {
    'S001': {'name': 'Alice', 'age': 20, 'grade': 'A'},
    'S002': {'name': 'Bob', 'age': 21, 'grade': 'B'},
    'S003': {'name': 'Carol', 'age': 19, 'grade': 'A+'}
}

print("Nested Dictionary:")
for student_id, info in students.items():
    print(f"  {student_id}: {info}")

# Access nested values
print(f"\nstudents['S001']['name']: {students['S001']['name']}")
print(f"students['S002']['grade']: {students['S002']['grade']}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 10: Dictionary Methods
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 10: Useful Dictionary Methods")
print("="*70)

config = {'host': 'localhost', 'port': 8000, 'debug': True}
print(f"Original: {config}")

# copy() - create a copy
config_copy = config.copy()
config_copy['debug'] = False
print(f"\nAfter copy() and modification:")
print(f"  Original: {config}")
print(f"  Copy: {config_copy}")

# setdefault() - get value or set if not exists
value = config.setdefault('timeout', 30)
print(f"\nsetdefault('timeout', 30): {value}")
print(f"After setdefault: {config}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 11: Real-World Example - User Profile
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 11: Real-World Example - User Profile")
print("="*70)

user_profile = {
    'username': 'john_doe',
    'email': 'john@mail.com',
    'age': 28,
    'location': 'New York',
    'interests': ['coding', 'gaming', 'reading'],
    'social_media': {
        'twitter': '@john_doe',
        'instagram': 'john.doe'
    }
}

print("User Profile:")
print(f"Username: {user_profile['username']}")
print(f"Email: {user_profile['email']}")
print(f"Interests: {', '.join(user_profile['interests'])}")
print(f"Twitter: {user_profile['social_media']['twitter']}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 12: Real-World Example - Inventory System
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 12: Real-World Example - Inventory System")
print("="*70)

inventory = {
    'laptop': {'quantity': 5, 'price': 50000},
    'mouse': {'quantity': 20, 'price': 500},
    'keyboard': {'quantity': 15, 'price': 2000}
}

print("Inventory System:")
total_value = 0
for product, details in inventory.items():
    value = details['quantity'] * details['price']
    total_value += value
    print(f"{product}: {details['quantity']} units × ₹{details['price']} = ₹{value}")

print(f"Total inventory value: ₹{total_value}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 13: Real-World Example - Configuration Settings
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 13: Real-World Example - Configuration Settings")
print("="*70)

app_config = {
    'app_name': 'MyApp',
    'version': '1.0.0',
    'database': {
        'host': 'localhost',
        'port': 5432,
        'name': 'mydb'
    },
    'features': {
        'authentication': True,
        'notifications': True,
        'analytics': False
    }
}

print("App Configuration:")
print(f"App: {app_config['app_name']} v{app_config['version']}")
print(f"Database: {app_config['database']['host']}:{app_config['database']['port']}")
print(f"Features enabled: {sum(1 for v in app_config['features'].values() if v)}/3\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 14: When to Use Dictionaries?
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 14: When to Use Dictionaries?")
print("="*70)

print("""
USE DICTIONARIES WHEN YOU NEED:
  ✓ Key-value relationships
  ✓ Fast lookup by key (O(1) time)
  ✓ Labels/names for data (not just order)
  ✓ Mutable collection (can add/modify)
  ✓ Represent real-world objects (people, configs)
  ✓ Mapping between two sets of data

EXAMPLES:
  • User profiles
  • Configuration settings
  • Inventory system
  • Phone directory/contacts
  • Database records
  • API responses (JSON)
  • Student grades by name
  • Cache/lookup tables

DON'T USE DICTIONARIES WHEN YOU NEED:
  ❌ Ordered collection without keys → Use List
  ❌ Unique elements only → Use Set
  ❌ Immutable structure → Use Tuple
  ❌ Need to preserve insertion order strictly → (Python 3.7+ preserves it anyway)

COMPARISON: DICT vs LIST
┌──────────────┬────────────────┬──────────────────┐
│ Operation    │ List           │ Dictionary       │
├──────────────┼────────────────┼──────────────────┤
│ Access       │ O(n) by value  │ O(1) by key ✓    │
│ Insert       │ O(1) end       │ O(1) ✓           │
│ Remove       │ O(n)           │ O(1) ✓           │
│ Memory       │ Less           │ More             │
│ Order        │ Preserved ✓    │ Preserved (3.7+) │
│ Duplicates   │ Allowed ✓      │ Keys unique ✓    │
│ Named access │ ❌ indices     │ ✓ by key         │
└──────────────┴────────────────┴──────────────────┘
""")

print("="*70)

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 15: Important Points to Remember
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("IMPORTANT POINTS TO REMEMBER")
print("="*70)

print("""
1. KEY-VALUE PAIRS
   dict = {'key': value, 'key2': value2}
   Access: dict['key']
   Keys must be unique

2. KEYS MUST BE IMMUTABLE
   ✓  'string', 123, (1,2), True
   ❌  [1,2], {1,2}, {'a':1}
   Keys cannot be lists, sets, or other dicts

3. VALUES CAN BE ANYTHING
   ✓  'string', 123, [1,2], (1,2), True, None
   ✓  {'nested': 'dict'}, function, class
   Any type is allowed as value

4. ORDERED (Python 3.7+)
   Dictionaries maintain insertion order
   First in = First out in iteration

5. MUTABLE - Can be changed after creation
   ✓  dict['key'] = new_value      - Change value
   ✓  dict['new_key'] = value      - Add key-value
   ✓  del dict['key']              - Remove key
   ✓  dict.update({...})           - Merge dicts

6. COMMON METHODS
   keys()             - Get all keys
   values()           - Get all values
   items()            - Get key-value pairs
   get(key, default)  - Get value safely
   pop(key)           - Remove and return value
   update(dict)       - Merge another dict
   clear()            - Remove all items
   copy()             - Create shallow copy

7. ACCESSING VALUES SAFELY
   dict['key']              - Raises KeyError if not exists
   dict.get('key')          - Returns None if not exists
   dict.get('key', default) - Returns default if not exists

8. LOOPING
   for key in dict:              - Loop through keys
   for value in dict.values():   - Loop through values
   for k, v in dict.items():     - Loop through key-value pairs

9. CHECKING EXISTENCE
   'key' in dict              - Check if key exists
   'key' not in dict          - Check if key doesn't exist
   value in dict.values()     - Check if value exists

10. PERFORMANCE ADVANTAGE
    Lists: Find by value = O(n) - slow for large lists
    Dicts: Find by key = O(1) - fast always!
    For lookup tasks, dicts are much faster

11. REAL-WORLD ANALOGY
    Dictionary = Real-world dictionary
    'cat' → 'a small furry animal'
    
    Similarly:
    student_id → student_details
    'S001' → {'name': 'Alice', 'age': 20}
    
    Fast lookup without reading every entry!

12. NESTED STRUCTURES
    Dicts can contain lists, tuples, other dicts
    users[user_id][profile_field]
    locations[city][street][building_number]
""")

print("="*70)
# print(details)

# # Memebership operator works on the keys only 
# personal_details = {'name':'bob','age':30}
# print(30 in personal_details) # output : False
# print('age' in personal_details) #output : True

# #2 Built-in functions:
# #These finctions only touch or use only keys not the values
# personal_details = {'name':'bob','age':30}
# #Length
# print(len(personal_details))
# #Minimum
# print(min(personal_details))
# #Maximum
# print(max(personal_details))
# #sorted
# sorted(personal_details)
# print(personal_details)

# #3 Indexing on dictionaries:
# '''
# -Dictionaries follow key based indexing
# -Values in dictionaries are stored using keys. so to access a value corresponding to any key,
#  we can use that key and access it
# '''
# personal_details = {'name':'bob','age':30}
# print(personal_details['name'])
# print(personal_details['age'])

# #we can reassign values corresponding to a key using indexing
# personal_details['age'] = 35 #reassignment of the age
# print(personal_details['age'])

# #4.Dictionary methods - dictionary class functions
# #syntax to use : dict_obj.fun()

# #Functions for adding new key-value pairs:
# # - update() = used to add new key:value pairs at the end
# personal_details = {'name':'bob','age':30}
# proff_details = {'job':'Dev','company':'x'}
# personal_details.update(proff_details)
# print(personal_details)

#Functions for removing key:value pairs:
# -popitem() = # It will remove the last added pair in dictionary
#personal_details = {'name':'bob','age':30}
#proff_details = {'job':'Dev','company':'x'}
#personal_details.popitem() #output : {'name': 'bob'}

# -pop() = It will remove the provided key-value pair
#proff_details.pop('company') # output : {'job': 'Dev'}
#print(personal_details)
#print(proff_details)

# -clear() = It remove all the key:value pairs

#functions for accessing values using keys:
# get() - it returns the value of a given key


'''
write a program to calculate the average marks for the marks given as dictionary
marks = {'science':90
        'maths':100
        'english':80}
ouput: the average of<no of subjects>subjects is<avg>
'''
#marks = eval(input())
#sub_marks = marks.values()
#no_of_average = sum(sub_marks)// len(marks)
#print(f"The average of {len(marks)} subjects {no_of_average}")
#print('the average of{} subjects is{}'.format(len(marks),no_of_average))

'''
A person's weekly log of practice duration is given as input.
find the day no of the week where he spent more on practice
input: single line have space separated 7 numbers representing the durations for a week in minutes
output: Day - <day no>
example: 15 90 300 60 35 20 40
op: Day - 3

'''
inp = list(map(int,input().split()))
n = max(inp)
m = inp.index(n) + 1
print(f"Day - {m}")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 16: UNPACKING DICTIONARIES - Assign Keys and Values
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 16: UNPACKING DICTIONARIES")
print("="*70)

# Method 1: Unpack keys directly
person = {'name': 'Alice', 'age': 25, 'city': 'Delhi'}
keys = person.keys()
print(f"Dictionary: {person}")
print(f"Keys: {list(keys)}\n")

# Method 2: Unpack key-value pairs
print("Unpack items():")
for key, value in person.items():
    print(f"  {key} = {value}")

# Method 3: Dictionary comprehension unpacking
scores = {'Alice': 85, 'Bob': 90, 'Carol': 78}
print(f"\nOriginal: {scores}")
doubled = {name: score*2 for name, score in scores.items()}
print(f"Comprehension (doubled): {doubled}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 17: CONVERT DICTIONARY TO OTHER DATA TYPES
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 17: CONVERT DICT → LIST / TUPLE / SET / STRING")
print("="*70)

original_dict = {'name': 'Alice', 'age': 25, 'city': 'Delhi'}
print(f"Original Dictionary: {original_dict}")

# Convert to LIST (keys)
keys_list = list(original_dict)
print(f"\n✓ To List (keys): {keys_list}")
print(f"  Type: {type(keys_list)}")
print(f"  Use when: Need list of keys")

# Convert to LIST (values)
values_list = list(original_dict.values())
print(f"\n✓ To List (values): {values_list}")
print(f"  Type: {type(values_list)}")
print(f"  Use when: Need list of values")

# Convert to LIST (items)
items_list = list(original_dict.items())
print(f"\n✓ To List (items): {items_list}")
print(f"  Type: {type(items_list)}")
print(f"  Use when: Need list of key-value pairs")

# Convert to TUPLE
items_tuple = tuple(original_dict.items())
print(f"\n✓ To Tuple (items): {items_tuple}")
print(f"  Type: {type(items_tuple)}")
print(f"  Use when: Need immutable pairs")

# Convert to SET (keys)
keys_set = set(original_dict)
print(f"\n✓ To Set (keys): {keys_set}")
print(f"  Type: {type(keys_set)}")
print(f"  Use when: Need unique keys, fast lookup")

# Convert to STRING
dict_string = str(original_dict)
print(f"\n✓ To String: {dict_string}")
print(f"  Type: {type(dict_string)}")
print(f"  Use when: Need text representation\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 18: CONVERT OTHER TYPES TO DICTIONARY
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 18: CONVERT LIST / TUPLE / STRING → DICT")
print("="*70)

# From LIST of pairs
list_pairs = [('x', 1), ('y', 2), ('z', 3)]
dict_from_list = dict(list_pairs)
print(f"From List (pairs): {list_pairs}")
print(f"To Dictionary: {dict_from_list}")
print(f"Use when: Have key-value pairs as list")

# From TUPLE of pairs
tuple_pairs = (('id', 101), ('name', 'Alice'))
dict_from_tuple = dict(tuple_pairs)
print(f"\nFrom Tuple (pairs): {tuple_pairs}")
print(f"To Dictionary: {dict_from_tuple}")
print(f"Use when: Have key-value pairs as tuple")

# From TWO LISTS (keys and values)
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict_from_lists = dict(zip(keys, values))
print(f"\nFrom Two Lists:")
print(f"  Keys: {keys}")
print(f"  Values: {values}")
print(f"To Dictionary: {dict_from_lists}")
print(f"Use when: Have keys and values separately")

# From STRING (via split)
data_string = "name=Alice;age=25;city=Delhi"
dict_from_string = dict(item.split('=') for item in data_string.split(';'))
print(f"\nFrom String: '{data_string}'")
print(f"To Dictionary: {dict_from_string}")
print(f"Use when: Parse structured text data\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 19: WHEN TO CONVERT - DECISION GUIDE
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 19: WHEN TO CONVERT - DECISION GUIDE")
print("="*70)

print("""
CONVERSION SCENARIOS:

1. DICT → LIST (When to convert)
   ✓ Need ordered collection
   ✓ Need indexing by position
   ✓ Need list operations
   Example:
   data = {'a': 1, 'b': 2}
   keys = list(data.keys())        # ['a', 'b']
   values = list(data.values())    # [1, 2]
   items = list(data.items())      # [('a', 1), ('b', 2)]


2. DICT → TUPLE (When to convert)
   ✓ Need immutable pairs
   ✓ Use as set element
   ✓ Use as another dict value
   Example:
   config = {'host': 'localhost', 'port': 8000}
   immutable = tuple(config.items())


3. DICT → SET (When to convert)
   ✓ Need unique keys only
   ✓ Need set operations
   Example:
   data = {'x': 1, 'y': 2, 'z': 3}
   keys_only = set(data)


4. DICT → STRING (When to convert)
   ✓ Need text display
   ✓ Printing to console
   ✓ Saving to file
   Example:
   settings = {'theme': 'dark', 'lang': 'en'}
   text = str(settings)


5. LIST/TUPLE → DICT (When to convert)
   ✓ Have key-value pairs
   ✓ Need fast lookup by key
   ✓ Building configuration
   Example:
   pairs = [('a', 1), ('b', 2)]
   mapping = dict(pairs)


6. TWO LISTS → DICT (When to convert)
   ✓ Keys and values separate
   ✓ Need to combine them
   Example:
   names = ['Alice', 'Bob']
   scores = [85, 90]
   results = dict(zip(names, scores))
   # {'Alice': 85, 'Bob': 90}
""")

print("="*70)

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 20: REAL EXAMPLE - Config Conversion Pipeline
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 20: REAL EXAMPLE - Config Conversion Pipeline")
print("="*70)

# Step 1: Parse string to dict
config_string = "host=localhost;port=5432;debug=true"
config_dict = dict(item.split('=') for item in config_string.split(';'))
print(f"Step 1 - Parse (DICT): {config_dict}")

# Step 2: Extract keys to list
keys = list(config_dict.keys())
print(f"Step 2 - Keys (LIST): {keys}")

# Step 3: Extract values to list
values = list(config_dict.values())
print(f"Step 3 - Values (LIST): {values}")

# Step 4: Convert to items tuple
items = tuple(config_dict.items())
print(f"Step 4 - Items (TUPLE): {items}")

# Step 5: Convert string for display
display = str(config_dict)
print(f"Step 5 - Display (STRING): {display}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 21: CONVERSION QUICK REFERENCE
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 21: CONVERSION QUICK REFERENCE")
print("="*70)

print("""
DICTIONARY CONVERSIONS:

DICT → LIST (keys)      list(dict)              → ['a', 'b', 'c']
        ✓ Get keys only
        
DICT → LIST (values)    list(dict.values())    → [1, 2, 3]
        ✓ Get values only
        
DICT → LIST (items)     list(dict.items())     → [('a',1), ('b',2)]
        ✓ Get key-value pairs
        
DICT → TUPLE (items)    tuple(dict.items())    → (('a',1), ('b',2))
        ✓ Immutable pairs
        
DICT → SET (keys)       set(dict)              → {'a', 'b', 'c'}
        ✓ Unique keys
        
DICT → STRING           str(dict)              → "{'a': 1, 'b': 2}"
        ✓ Text display

LIST → DICT (pairs)     dict([('a',1), ('b',2)])  → {'a': 1, 'b': 2}
        ✓ From key-value pairs
        
TWO LISTS → DICT        dict(zip(keys, vals))    → {'a': 1, 'b': 2}
        ✓ Combine keys & values
        
TUPLE → DICT (pairs)    dict((('a',1), ('b',2)))  → {'a': 1, 'b': 2}
        ✓ From pair tuples


UNPACKING EXAMPLES:
═════════════════════════════════════════════════════════════════

# Keys only
for key in dict:
    print(key)

# Values only
for value in dict.values():
    print(value)

# Both (recommended)
for key, value in dict.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squared = {k: v**2 for k, v in dict.items()}

# Extract to lists
keys = list(dict)
values = list(dict.values())
pairs = list(dict.items())
""")

print("="*70)