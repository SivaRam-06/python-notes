"""
CALL BY REFERENCE – BEGINNER FRIENDLY GUIDE
-------------------------------------------

Call by reference means:
The FUNCTION receives the ORIGINAL variable,
so any changes made inside the function
WILL affect the original value.

⚠️ In Python:
We do NOT have true call by reference.

Instead Python uses:
✅ Call by object reference (call by sharing)

But mutable objects (like lists) behave
LIKE call by reference.

This file explains everything step by step.
"""


# ---------------------------------------------------------
# 1️⃣ REAL CALL BY REFERENCE (CONCEPT DEMO USING LIST)
# ---------------------------------------------------------

def modify_list(data):
    print("Inside function before change:", data)

    data.append(4)   # modifying original object

    print("Inside function after change:", data)


print("CALL BY REFERENCE BEHAVIOUR USING LIST")

my_list = [1, 2, 3]

print("Before function call:", my_list)

modify_list(my_list)

print("After function call:", my_list)

"""
The original list is changed.

Why?
Because both variable and function
refer to the SAME object in memory.
"""


# ---------------------------------------------------------
# 2️⃣ MEMORY ADDRESS CHECK USING id()
# ---------------------------------------------------------

def check_reference(lst):
    print("Inside function id:", id(lst))


print("\nMEMORY ADDRESS CHECK")

numbers = [10, 20, 30]

print("Outside id:", id(numbers))

check_reference(numbers)

"""
Same id → same object → reference is shared
"""


# ---------------------------------------------------------
# 3️⃣ MODIFYING ELEMENTS USING INDEX
# ---------------------------------------------------------

def update_element(values):
    values[0] = 100


print("\nMODIFYING ELEMENT USING INDEX")

data = [5, 6, 7]

print("Before function call:", data)

update_element(data)

print("After function call:", data)


# ---------------------------------------------------------
# 4️⃣ USING DICTIONARY (MUTABLE)
# ---------------------------------------------------------

def update_student(student):
    student["marks"] = 95


print("\nCALL BY REFERENCE WITH DICTIONARY")

student_info = {"name": "Ram", "marks": 80}

print("Before function call:", student_info)

update_student(student_info)

print("After function call:", student_info)


# ---------------------------------------------------------
# 5️⃣ REASSIGNMENT DOES NOT CHANGE ORIGINAL
# ---------------------------------------------------------

def reassign_list(lst):
    lst = [100, 200]   # new object created
    print("Inside function:", lst)


print("\nREASSIGNMENT EXAMPLE")

sample = [1, 2, 3]

print("Before function call:", sample)

reassign_list(sample)

print("After function call:", sample)

"""
Here original list is NOT changed.

Because:
We created a NEW object inside the function.
"""


# ---------------------------------------------------------
# 6️⃣ TRUE CALL BY REFERENCE STYLE (RETURNING VALUE)
# ---------------------------------------------------------

def modify_value(x):
    x += 10
    return x


print("\nRETURN AND UPDATE METHOD")

num = 5

print("Before function call:", num)

num = modify_value(num)

print("After function call:", num)

"""
This is the Python way to achieve
true call by reference behaviour.
"""


# ---------------------------------------------------------
# 7️⃣ HOW TO PREVENT ORIGINAL DATA FROM CHANGING
# ---------------------------------------------------------

def safe_modify(lst):
    lst = lst.copy()
    lst.append(999)
    print("Inside function:", lst)


print("\nPROTECT ORIGINAL DATA")

original_list = [1, 2, 3]

safe_modify(original_list)

print("After function call:", original_list)


# ---------------------------------------------------------
# 🎯 FINAL SUMMARY
# ---------------------------------------------------------

"""
DOES PYTHON HAVE CALL BY REFERENCE?

❌ No (not true call by reference)

BUT

✅ Mutable objects behave like call by reference

MUTABLE TYPES:
list, dict, set

IMMUTABLE TYPES:
int, float, str, tuple

REAL PYTHON TERM:
⭐ Call by object reference (call by sharing)
"""