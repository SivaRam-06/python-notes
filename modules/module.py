"""
MODULES IN PYTHON – BEGINNER FRIENDLY GUIDE
------------------------------------------

A module is simply a Python file (.py) that contains:
✔ functions
✔ variables
✔ classes

We use modules to:
✅ organize code
✅ reuse code
✅ make large programs manageable
"""


# ---------------------------------------------------------
# 1️⃣ WHAT IS A MODULE?
# ---------------------------------------------------------

"""
Suppose we have a file:

my_math.py

def add(a, b):
    return a + b

That file itself is called a MODULE.
"""


# ---------------------------------------------------------
# 2️⃣ IMPORTING A MODULE
# ---------------------------------------------------------

print("IMPORTING STANDARD MODULE")

import math

print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)


# ---------------------------------------------------------
# 3️⃣ IMPORT SPECIFIC ITEMS FROM MODULE
# ---------------------------------------------------------

print("\nIMPORTING SPECIFIC FUNCTION")

from math import sqrt, pi

print("Square root of 25:", sqrt(25))
print("Value of pi:", pi)


# ---------------------------------------------------------
# 4️⃣ USING ALIAS NAME
# ---------------------------------------------------------

print("\nUSING ALIAS")

import math as m

print("2 power 3:", m.pow(2, 3))


# ---------------------------------------------------------
# 5️⃣ IMPORT ALL (NOT RECOMMENDED)
# ---------------------------------------------------------

print("\nIMPORT ALL (STAR)")

from math import *

print("ceil value of 4.2:", ceil(4.2))


"""
Why not recommended?

Because:
It imports everything → memory waste
It can create name conflicts
"""


# ---------------------------------------------------------
# 6️⃣ CREATING YOUR OWN MODULE
# ---------------------------------------------------------

"""
Create a file called:

my_module.py

def greet(name):
    return f"Hello, {name}"

value = 100

Then use it like this:

import my_module

print(my_module.greet("Ram"))
print(my_module.value)
"""


# ---------------------------------------------------------
# 7️⃣ __name__ VARIABLE (VERY IMPORTANT)
# ---------------------------------------------------------

print("\nUNDERSTANDING __name__")

print("This file name is:", __name__)

"""
If a file is run directly:
__name__ = "__main__"

If a file is imported as module:
__name__ = module_name
"""


# ---------------------------------------------------------
# 8️⃣ WHY USE  __name__ == "__main__"
# ---------------------------------------------------------

def test_function():
    print("This runs only when file executed directly")


if __name__ == "__main__":
    print("Running directly")
    test_function()


"""
This prevents automatic execution when imported.
"""


# ---------------------------------------------------------
# 9️⃣ BUILT-IN MODULE EXAMPLES
# ---------------------------------------------------------

print("\nBUILT-IN MODULE EXAMPLES")

import random

print("Random number:", random.randint(1, 10))

import datetime

print("Current date and time:", datetime.datetime.now())


# ---------------------------------------------------------
# 🔟 MODULE SEARCH PATH
# ---------------------------------------------------------

import sys

print("\nMODULE SEARCH PATH")

for path in sys.path:
    print(path)


"""
Python searches modules in:

1) Current folder
2) Standard library
3) Installed packages
"""


# ---------------------------------------------------------
# 1️⃣1️⃣ DIR() FUNCTION
# ---------------------------------------------------------

print("\nUSING dir() TO SEE MODULE CONTENT")

print(dir(math))


# ---------------------------------------------------------
# 🎯 FINAL SUMMARY
# ---------------------------------------------------------

"""
MODULE:
A Python file containing code.

IMPORT WAYS:

import module
from module import function
import module as alias
from module import *

IMPORTANT:

__name__ == "__main__"

BUILT-IN MODULES:
math, random, datetime, sys

ADVANTAGES:
Code reuse
Better organization
Easy maintenance
"""
