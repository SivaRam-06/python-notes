"""
CALL BY VALUE – BEGINNER FRIENDLY GUIDE
---------------------------------------

Call by value means:
A COPY of the variable is passed to the function,
so the original value is NOT changed.

⚠️ BUT in Python:
We do NOT have pure call by value or call by reference.

Python uses:
✅ Call by object reference  (also called call by sharing)

This means:
- Immutable objects → behave like call by value
- Mutable objects → behave like call by reference

We will understand this step by step.
"""


# ---------------------------------------------------------
# 1️⃣ IMMUTABLE EXAMPLE – INTEGER
# ---------------------------------------------------------

def change_number(x):
    print("Inside function before change:", x)

    x = 20   # new object is created

    print("Inside function after change:", x)


print("IMMUTABLE EXAMPLE – INTEGER")

num = 10
print("Before function call:", num)

change_number(num)

print("After function call:", num)

"""
Explanation:
Original value does NOT change.

Why?
Because integers are IMMUTABLE.
So it behaves like CALL BY VALUE.
"""


# ---------------------------------------------------------
# 2️⃣ IMMUTABLE EXAMPLE – STRING
# ---------------------------------------------------------

def change_text(text):
    print("Inside function before change:", text)

    text = "Python"

    print("Inside function after change:", text)


print("\nIMMUTABLE EXAMPLE – STRING")

name = "Java"
print("Before function call:", name)

change_text(name)

print("After function call:", name)


# ---------------------------------------------------------
# 3️⃣ MUTABLE EXAMPLE – LIST
# ---------------------------------------------------------

def change_list(my_list):
    print("Inside function before change:", my_list)

    my_list.append(4)

    print("Inside function after change:", my_list)


print("\nMUTABLE EXAMPLE – LIST")

numbers = [1, 2, 3]
print("Before function call:", numbers)

change_list(numbers)

print("After function call:", numbers)

"""
Explanation:
Original list IS changed.

Why?
Because lists are MUTABLE.
So both function and original variable
refer to the SAME object.
"""


# ---------------------------------------------------------
# 4️⃣ REASSIGNING A LIST (IMPORTANT INTERVIEW QUESTION)
# ---------------------------------------------------------

def reassign_list(lst):
    lst = [100, 200]   # new object created
    print("Inside function:", lst)


print("\nREASSIGNING A LIST")

my_data = [10, 20]
print("Before function call:", my_data)

reassign_list(my_data)

print("After function call:", my_data)

"""
Here original list is NOT changed.

Because:
We created a NEW list inside the function.
"""


# ---------------------------------------------------------
# 5️⃣ CHECKING MEMORY ADDRESS USING id()
# ---------------------------------------------------------

def check_id(value):
    print("Inside function id:", id(value))


print("\nCHECKING OBJECT ID")

a = 50
print("Outside id:", id(a))

check_id(a)


# ---------------------------------------------------------
# 6️⃣ HOW TO AVOID CHANGING ORIGINAL LIST
# ---------------------------------------------------------

def safe_change(lst):
    lst = lst.copy()   # create copy
    lst.append(99)
    print("Inside function:", lst)


print("\nAVOID CHANGING ORIGINAL LIST")

original = [1, 2, 3]

safe_change(original)

print("After function call:", original)


# ---------------------------------------------------------
# 🎯 SUMMARY
# ---------------------------------------------------------

"""
PYTHON PARAMETER PASSING:

IMMUTABLE (int, float, str, tuple)
➡ behaves like CALL BY VALUE
➡ original value NOT changed

MUTABLE (list, set, dict)
➡ behaves like CALL BY REFERENCE
➡ original value CAN change

ACTUAL TERM:
✅ Call by object reference (Call by sharing)
"""