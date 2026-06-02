"""
╔════════════════════════════════════════════════════════════════════════════╗
║           PYTHON STRINGS - LEARN WITH SIMPLE PROGRAMS                      ║
║        Run each program to understand Strings & String Operations          ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 1: What is a String? (Immutable Sequence of Characters)
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 1: What is a String?")
print("="*70)

# Creating strings
single_quote = 'hello'
double_quote = "world"
triple_quote = '''This is a
multi-line string'''

print(f"Single quote: {single_quote}")
print(f"Double quote: {double_quote}")
print(f"Type: {type(single_quote)}")
print(f"Length: {len(single_quote)} characters\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 2: Create Strings in Different Ways
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 2: Create Strings in Different Ways")
print("="*70)

# Way 1: Single quotes
str1 = 'Python'
print(f"Way 1 - Single quotes: {str1}")

# Way 2: Double quotes
str2 = "Java"
print(f"Way 2 - Double quotes: {str2}")

# Way 3: Triple quotes (multi-line)
str3 = '''This is a
multi-line
string'''
print(f"Way 3 - Triple quotes (multi-line):\n{str3}")

# Way 4: Using str() constructor
str4 = str(42)
print(f"\nWay 4 - From number: {str4}")

# Way 5: Escape sequences
str5 = "Hello\nWorld\tTabbed"
print(f"Way 5 - With escapes:\n{str5}")

# Way 6: Empty string
str6 = ""
print(f"Way 6 - Empty: '{str6}' (length = {len(str6)})\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 3: Access String Characters by Index
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 3: Access Characters by Index")
print("="*70)

text = "PYTHON"
print(f"String: {text}")

print(f"\nPositive indexing:")
print(f"Index 0: {text[0]}")
print(f"Index 2: {text[2]}")
print(f"Index 5: {text[5]}")

print(f"\nNegative indexing (from end):")
print(f"Index -1 (last): {text[-1]}")
print(f"Index -2 (second last): {text[-2]}")
print(f"Index -6 (first): {text[-6]}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 4: Slice Strings (Get Portions)
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 4: Slicing - Get Portions of String")
print("="*70)

word = "ABCDEFGH"
print(f"Original string: {word}")

print(f"word[1:4]: {word[1:4]} (index 1 to 3)")
print(f"word[:3]: {word[:3]} (first 3 characters)")
print(f"word[3:]: {word[3:]} (from index 3 to end)")
print(f"word[::2]: {word[::2]} (every 2nd character)")
print(f"word[::-1]: {word[::-1]} (reversed)\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 5: Immutability - Strings Cannot Be Modified
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 5: Immutability - Strings Cannot Be Modified")
print("="*70)

my_string = "Hello"
print(f"Original: {my_string}")

print("\nTrying to change character (will cause error):")
try:
    my_string[0] = 'J'
except TypeError as e:
    print(f"❌ Error: {e}")

print("\nTrying to append (will cause error):")
try:
    my_string.append('!')
except AttributeError as e:
    print(f"❌ Error: {e}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 6: String Concatenation and Repetition
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 6: Concatenation and Repetition")
print("="*70)

str1 = "Hello"
str2 = "World"

# Concatenation
greeting = str1 + " " + str2
print(f"Concatenation: {greeting}")

# Repetition
repeated = str1 * 3
print(f"Repetition: {repeated}")

# Using f-strings (modern way)
name = "Alice"
age = 25
formatted = f"My name is {name} and I am {age} years old"
print(f"F-string: {formatted}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 7: String Methods - Case Conversion
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 7: String Methods - Case Conversion")
print("="*70)

text = "Hello World"
print(f"Original: {text}")

print(f"upper(): {text.upper()}")
print(f"lower(): {text.lower()}")
print(f"capitalize(): {text.capitalize()}")
print(f"title(): {text.title()}")
print(f"swapcase(): {text.swapcase()}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 8: String Methods - Finding and Replacing
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 8: String Methods - Finding and Replacing")
print("="*70)

text = "Hello World Hello"
print(f"String: {text}")

# find() - returns index or -1
index = text.find("World")
print(f"find('World'): {index}")

# count() - count occurrences
count = text.count("Hello")
print(f"count('Hello'): {count}")

# replace() - replace substrings
replaced = text.replace("Hello", "Hi")
print(f"replace('Hello', 'Hi'): {replaced}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 9: String Methods - Splitting and Joining
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 9: String Methods - Splitting and Joining")
print("="*70)

# split() - split string into list
sentence = "Python is awesome"
words = sentence.split()
print(f"Original: {sentence}")
print(f"split(): {words}")

# split with delimiter
csv_data = "apple,banana,orange,mango"
fruits = csv_data.split(',')
print(f"split(','): {fruits}")

# join() - join list into string
words_list = ['I', 'love', 'Python']
sentence = " ".join(words_list)
print(f"join(): {sentence}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 10: String Methods - Stripping Whitespace
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 10: String Methods - Stripping Whitespace")
print("="*70)

text = "  Hello World  "
print(f"Original: '{text}'")

print(f"strip(): '{text.strip()}'")
print(f"lstrip(): '{text.lstrip()}'")
print(f"rstrip(): '{text.rstrip()}'")

# Remove specific characters
text2 = "###Python###"
print(f"\nRemove '#' from '{text2}':")
print(f"strip('#'): '{text2.strip('#')}'\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 11: Check if String Contains Substrings
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 11: Check if String Contains Substrings")
print("="*70)

text = "Python is amazing"
print(f"String: {text}")

print(f"'Python' in text: {'Python' in text}")
print(f"'Java' in text: {'Java' in text}")
print(f"'amazing' in text: {'amazing' in text}")
print(f"'is' not in text: {'is' not in text}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 12: String Methods - Checking String Type
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 12: String Methods - Checking String Type")
print("="*70)

# isalpha() - all alphabets
print(f"'hello'.isalpha(): {'hello'.isalpha()}")
print(f"'hello123'.isalpha(): {'hello123'.isalpha()}")

# isdigit() - all digits
print(f"'12345'.isdigit(): {'12345'.isdigit()}")
print(f"'12a45'.isdigit(): {'12a45'.isdigit()}")

# isalnum() - alphabets and digits
print(f"'hello123'.isalnum(): {'hello123'.isalnum()}")

# isspace() - all whitespace
print(f"'   '.isspace(): {'   '.isspace()}")
print(f"'hello'.isspace(): {'hello'.isspace()}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 13: String Formatting
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 13: String Formatting")
print("="*70)

name = "Alice"
age = 25
salary = 50000.75

# Old style %
print("Old style: 'Hello %s, you are %d years old' % (name, age)")
print("Hello %s, you are %d years old" % (name, age))

# format() method
print("\nformat() method:")
print("Hello {}, you are {} years old".format(name, age))
print("Salary: ${:.2f}".format(salary))

# f-strings (modern, recommended)
print("\nf-strings (modern):")
print(f"Hello {name}, you are {age} years old")
print(f"Salary: ${salary:,.2f}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 14: Real-World Example - User Input Processing
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 14: Real-World Example - User Input Processing")
print("="*70)

# Simulating user input
user_input = "  jOHN dOE  "
print(f"Raw input: '{user_input}'")

# Clean and process
cleaned = user_input.strip().title()
print(f"Cleaned: '{cleaned}'")

# Extract information
email = "john.doe@company.com"
username = email.split('@')[0]
domain = email.split('@')[1]
print(f"\nEmail: {email}")
print(f"Username: {username}")
print(f"Domain: {domain}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 15: Real-World Example - Log Parser
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 15: Real-World Example - Log Parser")
print("="*70)

log = "ERROR: Database connection failed at 2024-01-15 10:30:45"
print(f"Log entry: {log}")

# Extract log level
if log.startswith("ERROR"):
    level = "ERROR"
print(f"Log level: {level}")

# Extract timestamp
timestamp = log.split(" at ")[-1]
print(f"Timestamp: {timestamp}")

# Replace sensitive info
masked_log = log.replace("Database", "***")
print(f"Masked: {masked_log}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 16: When to Use Strings?
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 16: When to Use Strings?")
print("="*70)

print("""
STRINGS ARE USED FOR:
  ✓ Text data (names, messages, content)
  ✓ Immutable sequences (safe, unchangeable)
  ✓ Messages and display output
  ✓ File names and paths
  ✓ Data parsing and processing
  ✓ Regular expressions pattern matching
  ✓ JSON data handling
  ✓ User input processing

REAL-WORLD EXAMPLES:
  • User names and passwords
  • Email addresses
  • Messages and comments
  • Log entries
  • File names and paths
  • Configuration settings
  • API keys and tokens
  • Chat messages
  • Document content
  • Error messages

WHY STRINGS ARE IMMUTABLE:
  ✓ Safety: Cannot be accidentally modified
  ✓ Hashable: Can be used as dictionary keys
  ✓ Thread-safe: No concurrency issues
  ✓ Performance: Can be cached and optimized
  ✓ Intent: Shows data should not change

STRING METHODS CHEAT SHEET:
  Case:        upper(), lower(), capitalize(), title()
  Search:      find(), count(), startswith(), endswith()
  Replace:     replace(), strip(), lstrip(), rstrip()
  Split/Join:  split(), join(), partition()
  Check:       isalpha(), isdigit(), isalnum(), isspace()
  Format:      format(), f-strings, %, format_map()
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
   ❌ string[0] = 'x'        - ERROR
   ❌ string.append('x')     - ERROR (no append method)
   ✓  string = 'new string' - Create new string

2. ORDERED - Characters have specific positions
   string[0] is always first character
   Order is preserved forever

3. INDEXED - Access by position (0, 1, 2, ...)
   ✓  string[0]    - First character
   ✓  string[-1]   - Last character
   ✓  string[1:4]  - Characters 1-3

4. QUOTED - Must be enclosed in quotes
   ✓  'hello'      - Single quotes
   ✓  "hello"      - Double quotes
   ✓  '''hello'''  - Triple quotes (multi-line)
   ✗  hello        - ERROR (no quotes)

5. ESCAPE SEQUENCES
   \\n    - Newline
   \\t    - Tab
   \\\\    - Backslash
   \\'    - Single quote
   \\"    - Double quote
   \\r    - Carriage return

6. SLICING SYNTAX
   string[start:end:step]
   string[1:4]      - Characters 1,2,3
   string[:3]       - First 3 characters
   string[2:]       - From character 2 to end
   string[::2]      - Every 2nd character
   string[::-1]     - Reversed

7. CONCATENATION
   'Hello' + ' ' + 'World'     - Concatenate
   'Ha' * 3                     - Repeat ('HaHaHa')
   f'Hello {name}'              - F-string formatting

8. IMPORTANT METHODS (Don't modify, return new strings)
   upper()         - All uppercase
   lower()         - All lowercase
   strip()         - Remove whitespace
   replace(old, new) - Replace substring
   split()         - Convert to list
   join()          - Convert list to string
   find(sub)       - Find position
   count(sub)      - Count occurrences
   startswith(x)   - Check if starts with
   endswith(x)     - Check if ends with

9. CHECKING CONTENT
   'sub' in string           - Check substring
   string.isalpha()          - All letters?
   string.isdigit()          - All digits?
   string.isalnum()          - Letters and digits?
   string.isspace()          - All whitespace?

10. FORMATTING OPTIONS
    Old: 'Hello %s' % name
    Method: 'Hello {}'.format(name)
    Modern: f'Hello {name}'  ← RECOMMENDED
    
    Formatting:
    f'{value:10}'    - Width 10
    f'{value:.2f}'   - 2 decimal places
    f'{value:>10}'   - Right align
    f'{value:<10}'   - Left align
    f'{value:^10}'   - Center

11. IMMUTABILITY MEANS
    ✓ Safe to use as dict keys
    ✓ Safe in multi-threaded code
    ✓ Can be cached safely
    ✓ Performance optimizations possible
    ❌ Cannot modify in place
    ❌ Must create new strings for changes

12. COMMON OPERATIONS
    Combine strings:
    text = ' '.join(['Hello', 'World'])
    
    Split into parts:
    words = 'Hello World'.split()
    
    Extract substring:
    domain = 'user@domain.com'.split('@')[1]
    
    Clean input:
    name = input().strip().title()
""")

print("="*70)

#Properties of a string:
'''
1)Immutable:
-Changes in an existing object is not possible.
2)Ordered:
-Order of insertion of characters is preserved through out its existence in memory.
3)Indexable:
-Elements can be accessed by using indexing.

String input()
-input() function considers every input by user as string object only by default
#example:
name = input('Enter the name: ')
print(type(name))
'''
#Uses of backslash in strings:
'''
1) It can be used as escape character
2) It can be used to introduce new line, tabspace character,etc
3) It can be used for line continuation in paragraphs to improve readability
'''
'''
s = 'It\'s python class' #'\' is used escape the next character or that character can be included in the string 
print(s)

s = "This is \t python class"
print(s)

s = "This is \n python class"
print(s)
'''
text = 'This is codegnan. It has it\'s locations in hyderabad,'\
    'vijaywada,banglore'
#Operations on strings:
#1)String concatenation:
'''
-Joining two or more string together is called string concatenation.
    ' + 'is the operator is used for string concatenation.
'''
#write a program to take first name and last name as two lines of input and print full name.
'''
first_name = input("Enter your first name: ")
last_name = input("Enter your last_name: ")
full_name = first_name + " " +  last_name
print(full_name)
'''
#2)string repeatition:
'''
-Repeates the characters in a string given no of times.
    ' * ' operator is used for string repetition.
'''
#write a program to print following pattern
'''
******
******
******
'''
'''
s = "*"
b = s*6
print(b)
print(b)
print(b)
'''
#3) Relational operator
#-work by comparing ASCII values

#4)Logical operators
#-Try to convert strings to boolean internal for a non empty string boolean value will be True and for empty string, False.

#5) Arithmetic operators
#-these do not work connot be used as compound assignment operators for updating values

#6) Identity and membership operators can be used.

#7) unsupported operators will give typeError.


# Built-in functions on strings:
'''
- built-in functions are predefined functions that are available in python without importing any module.
'''
'''
#1) len(): returns length of the string:
s = "python"
print(len(s))
#2) max(): returns the character with highest ASCII value
s1 = "python"
print(max(s1))
#3) min(): returns the character with lowest ASCII value
s2 = "python"
print(min(s2))
#4) ord(): returns ASCII value of a character
ch = 'a'
print(ord(ch))
#5) chr(): returns character for a given ASCII value
val = 97
print(chr(val))
#6) sorted(): returns sorted list of characters in ascending order
s3 = "python"
print(sorted(s3, reverse=True))
'''
#String Indexing:
'''
-Each character in a string is assigned a unique index value based on its position.
#There are two types of indexing:
-Positive indexing or zero-based: 
    -starts from 0 to n-1(where n is length of string)
    -it runs from left to right(starting from first character to last character)
-Negative indexing:
    -starts from -1 to -n(where n is length of string)
    -it runs from right to left(starting from last character to first character)
'''
'''
s = "python"
print(s[2])  #t
print(s[-4]) #t
#write a program to print first and last character of a string using indexing and output should be True or False based on condition.
s = input("Enter any string: ")
first_char = s[0]
last_char = s[-1]
print(first_char == last_char)
#write a program to check if the middle character of the given string is vowel or not.Always an odd length string is granted.
s = input("Enter any odd length string: ")
mid_index = len(s)//2
mid_char = s[mid_index]
print(mid_char in 'aeiouAEIOU')
if mid_char in 'aeiouAEIOU':
    print("Middle character is vowel")
#write a program to check if the second character from the end is consonant or not.
s = input("Enter any string: ")
second_last_char = s[-2] #[len(s)-2]
print(second_last_char not in 'aeiouAEIOU')
'''
'''
To access single element, we follow the syntax:
    string_variable[index_value]
To access a substring from a string, we follow the syntax:
    string_variable[start_index:end_index:step_size]
     -These three values are optional.
     -The default values for these are:
        start_index=0 #start from first character
        end_index=length of string #goes up to last character
        step_size=1 #access every character
'''

#String Slicing:
'''
s = "pythonprogramming"
print(s[0:6]) #python
print(s[6:])  #programming
print(s[:6])  #python
print(s[:])   #pythonprogramming
print(s[::2]) #ptopormig
print(s[1::2])#yhnpammng
print(s[::-1])#gnimmargorpnohtyp
print(s[-1::-1])#gnimmargorpnohtyp
print(s[-3:-7:-1])#marg
print(s[-1:-len(s)-1:-1])#gnimmargorpnohtyp
print(s[-len(s):-1])#pythonprogramming
print(s[-len(s):]) #pythonprogramming
print(s[len(s)-1:len(s)-len(s)-1:-1])#gnimmargorpnohtyp
'''
'''
#wirte a program to check whether the given string is palindrome or not.output should be True or False.
s = input("Enter any string: ")
print(s == s[::-1])
#write a program to check if the first half of the string is equal to the second half of the string.it is guaranteed that the length of the string is even.
s = input("Enter any even length string: ")
print(s[:len(s)//2] == s[len(s)//2:])
'''
#String class Methods:
'''
-functions defined in a particular class work only on those data types for which they are defined.
 these functions are called as methods.

#-Syntax to call a method:
    string_variable.method_name(arguments)
-If there are no arguments, empty parenthesis has to be provided.
-There are various string methods available in python to perform different operations on string datatype.
'''

# Case conversion and searching methods:

#1) capitalize(): converts first character of string to uppercase and rest to lowercase
s = "python programming"
print(s.capitalize())
#2) casefold(): converts all characters of string to lowercase
s1 = "PYTHON PROGRAMMING"
print(s1.casefold())
#3) upper(): converts all characters of string to uppercase
s2 = "python programming"
print(s2.upper())
#4) lower(): converts all characters of string to lowercase
s3 = "PYTHON PROGRAMMING"
print(s3.lower())
#5) title(): converts first character of each word to uppercase and rest to lowercase
s4 = "python programming language"
print(s4.title())
#6) swapcase(): converts uppercase characters to lowercase and lowercase characters to uppercase
s5 = "Python Programming Language"
print(s5.swapcase())
#7) find(): returns the lowest index of substring if found else returns -1
s6 = "python programming"
print(s6.find('gram'))
#8) rfind(): returns the highest index of substring if found else returns -1
s7 = "python programming python"
print(s7.rfind('python'))
#9) index(): returns the lowest index of substring if found else raises ValueError
s8 = "python programming"
print(s8.index('pro'))
#10) rindex(): returns the highest index of substring if found else raises ValueError
s9 = "python programming python"
print(s9.rindex('python'))
#11) count(): returns the number of occurrences of substring in string
s10 = "python programming python"
print(s10.count('python'))
#12) strip(): removes leading and trailing characters(space by default)
s11 = "   python programming   "
print(s11.strip())
#13) lstrip(): removes leading characters(space by default)
s12 = "   python programming   "
print(s12.lstrip())
#14) rstrip(): removes trailing characters(space by default)
s13 = "   python programming   "
print(s13.rstrip())
#15) replace(): replaces all occurrences of old substring with new substring
s14 = "python programming"
print(s14.replace('python', 'java'))
#16) split(): splits the string into list of substrings based on the given separator(space by default)
s15 = "python programming language"
print(s15.split())
#17) join(): joins the elements of iterable with the given string as separator
s16 = "-".join(['python', 'programming', 'language'])
print(s16)
#18) isalpha(): returns True if all characters in string are alphabets else returns False
s17 = "python"
print(s17.isalpha())
#19) isdigit(): returns True if all characters in string are digits else returns False
s18 = "12345"
print(s18.isdigit())
#20) isalnum(): returns True if all characters in string are alphanumeric else returns False
s19 = "python123"
print(s19.isalnum())
#21) islower(): returns True if all characters in string are lowercase else returns False
s20 = "python"
print(s20.islower())
#22) isupper(): returns True if all characters in string are uppercase else returns False
s21 = "PYTHON"
print(s21.isupper())
#23) istitle(): returns True if string is in title case else returns False
s22 = "Python Programming"
print(s22.istitle())
#24) startswith(): returns True if string starts with the given substring else returns False
s23 = "python programming"
print(s23.startswith('python'))
#25) endswith(): returns True if string ends with the given substring else returns False
s24 = "python programming"
print(s24.endswith('programming'))
#26) format(): formats the string by replacing the placeholders with the given values
s25 = "My name is {} and I am {} years old."
print(s25.format('Siva Ram', 25))
#27) zfill(): pads the string with leading zeros to make its length equal to the given width
s26 = "python"
print(s26.zfill(10))

# Check if given password is valid
# conditions:
# 1) length should have minimum of 5 characters and maximum 8 characters
# 2) should contain at least one digit
# 3) should contain at least one special character from [@,#,$,%,&,*]
# 4) not start with a digit
password = input("Enter a new password: ")
special_characters = '@#$%&*'
con1 = len(password) >=5 and len(password) <=8
con2 = not password.isalnum()
con3 = not password[0].isdigit()
print(con1 and con2 and con3)

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 18: UNPACKING STRINGS - Extract Characters and Parts
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 18: UNPACKING STRINGS")
print("="*70)

# Unpack individual characters
word = "ABC"
a, b, c = word
print(f"String: {word}")
print(f"Unpacked: a={a}, b={b}, c={c}")

# Unpack with rest
text = "Hello"
first, *middle, last = text
print(f"\nString: {text}")
print(f"first={first}, middle={list(middle)}, last={last}")

# Split and unpack
date_str = "2024-01-15"
year, month, day = date_str.split('-')
print(f"\nString: {date_str}")
print(f"year={year}, month={month}, day={day}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 19: CONVERT STRING TO OTHER DATA TYPES
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 19: CONVERT STRING → LIST / TUPLE / SET / INT / FLOAT")
print("="*70)

original_string = "hello"
print(f"Original String: '{original_string}'")

# Convert to LIST
my_list = list(original_string)
print(f"\n✓ To List: {my_list}")
print(f"  Type: {type(my_list)}")
print(f"  Use when: Need character-by-character processing")

# Convert to TUPLE
my_tuple = tuple(original_string)
print(f"\n✓ To Tuple: {my_tuple}")
print(f"  Type: {type(my_tuple)}")
print(f"  Use when: Need immutable character sequence")

# Convert to SET
my_set = set(original_string)
print(f"\n✓ To Set: {my_set}")
print(f"  Type: {type(my_set)}")
print(f"  Use when: Need unique characters")

# Convert STRING with numbers to INT/FLOAT
number_str = "12345"
my_int = int(number_str)
print(f"\n✓ To Integer: {my_int}")
print(f"  Type: {type(my_int)}")
print(f"  Use when: String contains number")

float_str = "3.14"
my_float = float(float_str)
print(f"\n✓ To Float: {my_float}")
print(f"  Type: {type(my_float)}")
print(f"  Use when: String contains decimal number")

# Split string to list
sentence = "Python is amazing"
words = sentence.split()
print(f"\n✓ To List (split): {words}")
print(f"  Type: {type(words)}")
print(f"  Use when: Break string into words/parts\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 20: CONVERT OTHER TYPES TO STRING
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 20: CONVERT LIST / INT / FLOAT / TUPLE / DICT → STRING")
print("="*70)

# From LIST
my_list = [1, 2, 3, 4, 5]
string_from_list = str(my_list)
print(f"From List: {my_list}")
print(f"To String: {string_from_list}")
print(f"Use when: Need text display of list")

# From INT
my_int = 42
string_from_int = str(my_int)
print(f"\nFrom Int: {my_int}")
print(f"To String: '{string_from_int}'")
print(f"Use when: Need text version of number")

# From FLOAT
my_float = 3.14159
string_from_float = str(my_float)
print(f"\nFrom Float: {my_float}")
print(f"To String: '{string_from_float}'")
print(f"Use when: Need text version of decimal")

# From TUPLE
my_tuple = (1, 2, 3)
string_from_tuple = str(my_tuple)
print(f"\nFrom Tuple: {my_tuple}")
print(f"To String: {string_from_tuple}")
print(f"Use when: Need text display of tuple")

# From DICTIONARY
my_dict = {'name': 'Alice', 'age': 25}
string_from_dict = str(my_dict)
print(f"\nFrom Dict: {my_dict}")
print(f"To String: {string_from_dict}")
print(f"Use when: Need text display of dict\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 21: WHEN TO CONVERT - DECISION GUIDE
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 21: WHEN TO CONVERT - DECISION GUIDE")
print("="*70)

print("""
CONVERSION SCENARIOS:

1. STRING → LIST (When to convert)
   ✓ Need character-by-character processing
   ✓ Need to modify characters
   ✓ Need list operations
   Example:
   text = "hello"
   chars = list(text)        # ['h', 'e', 'l', 'l', 'o']


2. STRING → TUPLE (When to convert)
   ✓ Need immutable character sequence
   ✓ Use as dictionary key
   ✓ Use in set
   Example:
   text = "abc"
   immutable = tuple(text)   # ('a', 'b', 'c')


3. STRING → SET (When to convert)
   ✓ Need unique characters only
   ✓ Find different characters
   Example:
   text = "hello"
   unique = set(text)        # {'h', 'e', 'l', 'o'}


4. STRING → INT/FLOAT (When to convert)
   ✓ String contains numeric value
   ✓ Need mathematical operations
   Example:
   text = "42"
   number = int(text)
   total = number + 10


5. STRING → DICTIONARY (When to convert)
   ✓ Parse structured text
   ✓ Build key-value mapping
   Example:
   data = "name=Alice;age=25"
   parsed = dict(item.split('=') for item in data.split(';'))


6. LIST → STRING (When to convert)
   ✓ Display/print
   ✓ Save to file
   ✓ Send over network
   Example:
   items = [1, 2, 3]
   text = str(items)
   or
   text = ','.join(map(str, items))


7. INT/FLOAT → STRING (When to convert)
   ✓ Concatenate with text
   ✓ Format output
   Example:
   count = 42
   message = f"Total: {count}"  # Auto-converts


8. TUPLE/DICT → STRING (When to convert)
   ✓ Display/print
   ✓ Save to file
   Example:
   coords = (10, 20)
   text = str(coords)
""")

print("="*70)

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 22: REAL EXAMPLE - Data Parsing Pipeline
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 22: REAL EXAMPLE - CSV Data Parsing Pipeline")
print("="*70)

# Step 1: Raw CSV string
csv_line = "John,25,Engineer,50000"
print(f"Step 1 - Raw (STRING): '{csv_line}'")

# Step 2: Split to list
fields = csv_line.split(',')
print(f"Step 2 - Split (LIST): {fields}")

# Step 3: Convert specific fields
name = fields[0]
age = int(fields[1])
job = fields[2]
salary = float(fields[3])
print(f"Step 3 - Converted:")
print(f"  name (STRING): {name}")
print(f"  age (INT): {age}")
print(f"  job (STRING): {job}")
print(f"  salary (FLOAT): {salary}")

# Step 4: Build dictionary
record = {'name': name, 'age': age, 'job': job, 'salary': salary}
print(f"Step 4 - Dictionary: {record}")

# Step 5: Convert back to string for display
output = str(record)
print(f"Step 5 - Display (STRING): {output}\n")

# ═════════════════════════════════════════════════════════════════════════════
# PROGRAM 23: CONVERSION QUICK REFERENCE
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("PROGRAM 23: CONVERSION QUICK REFERENCE")
print("="*70)

print("""
STRING CONVERSIONS:

STRING → LIST          list(string)            → ['h','e','l','l','o']
         ✓ Chars
         
         string.split()               → ['Python', 'is', 'great']
         ✓ Words
         
STRING → TUPLE         tuple(string)           → ('h','e','l','l','o')
         ✓ Immutable chars
         
STRING → SET           set(string)             → {'h', 'e', 'l', 'o'}
         ✓ Unique chars
         
STRING → INT           int(string)             → 42
         ✓ Numeric string
         
STRING → FLOAT         float(string)           → 3.14
         ✓ Decimal string

LIST → STRING          str(list)               → "[1, 2, 3]"
         ✓ Display
         
         ','.join(map(str, list))    → "1,2,3"
         ✓ Custom format
         
INT → STRING           str(int)                → "42"
         ✓ Concatenation
         
         f"Value: {int}"             → "Value: 42"
         ✓ Formatting

FLOAT → STRING         str(float)              → "3.14"
         ✓ Display
         
DICT → STRING          str(dict)               → "{'a': 1}"
         ✓ Display

TUPLE → STRING         str(tuple)              → "(1, 2, 3)"
         ✓ Display


PARSING EXAMPLES:
═════════════════════════════════════════════════════════════════

# CSV to dictionary
csv = "id,name,age"
values = csv.split(',')

# Space-separated to list
data = "1 2 3 4 5"
nums = [int(x) for x in data.split()]

# Comma-separated to list
items = "apple,banana,orange"
fruits = items.split(',')

# JSON-like string to dict
text = "name=Alice;age=25"
data = dict(item.split('=') for item in text.split(';'))

# Number string to int
count = int("123")
total = count + 10

# String unpacking
a, b, c = "ABC"

# Join list to CSV string
items = [1, 2, 3]
csv = ','.join(map(str, items))
""")

print("="*70)