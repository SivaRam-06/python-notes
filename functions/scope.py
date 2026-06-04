# SCOPE - Understanding Variable Access

# =============================================================================
# 1. SCOPE CONCEPT
# =============================================================================

"""
SCOPE = Region of code where a variable can be accessed

Types of Scope:
1. LOCAL - inside a function
2. GLOBAL - outside all functions (module level)
3. BUILT-IN - Python's built-in variables and functions
4. ENCLOSING - in nested functions (advanced)
"""


# =============================================================================
# 2. LOCAL SCOPE - VARIABLES INSIDE FUNCTIONS
# =============================================================================

def my_function():
    """Variables inside functions are LOCAL"""
    x = 10  # Local variable
    y = 20  # Local variable
    print(f"Inside function: x = {x}, y = {y}")
    return x + y

my_function()
print()

# ❌ Can't access local variables outside function
# print(x)  # NameError: name 'x' is not defined
# print(y)  # NameError: name 'y' is not defined


# =============================================================================
# 3. GLOBAL SCOPE - VARIABLES OUTSIDE FUNCTIONS
# =============================================================================

# Global variable (defined outside function)
global_x = 100
global_y = 200

def access_global():
    """Can READ global variables"""
    print(f"Accessing global: global_x = {global_x}")
    print(f"Accessing global: global_y = {global_y}")

access_global()


# =============================================================================
# 4. LOCAL vs GLOBAL WITH SAME NAME
# =============================================================================

name = "Global Name"  # Global scope

def show_name():
    """Local scope takes priority over global"""
    name = "Local Name"  # Local scope
    print(f"Inside function: {name}")  # Uses LOCAL name

show_name()                           # Output: Inside function: Local Name
print(f"Outside function: {name}")    # Output: Outside function: Global Name


# =============================================================================
# 5. READING GLOBAL VARIABLES
# =============================================================================

counter = 0  # Global variable

def increment_counter_read():
    """Can READ global variable"""
    print(f"Counter is: {counter}")  # Can read global

increment_counter_read()  # Output: Counter is: 0


# =============================================================================
# 6. MODIFYING GLOBAL VARIABLES - THE global KEYWORD
# =============================================================================

counter = 0  # Global variable

def increment_counter_modify():
    """Use 'global' keyword to MODIFY global variable"""
    global counter  # Tell Python we want to modify the GLOBAL counter
    counter += 1    # Now this modifies the global variable
    print(f"Counter inside: {counter}")

print(f"Before: {counter}")     # Output: Before: 0
increment_counter_modify()      # Output: Counter inside: 1
print(f"After: {counter}")      # Output: After: 1

# Without the 'global' keyword, it would create a LOCAL variable instead


# =============================================================================
# 7. COMMON MISTAKE - FORGETTING 'global' KEYWORD
# =============================================================================

score = 0  # Global

def update_score_wrong():
    """Without 'global', creates a LOCAL variable"""
    score = 10  # This creates LOCAL score, not global!
    print(f"Inside: {score}")

def update_score_right():
    """With 'global', modifies the actual global"""
    global score
    score = 10
    print(f"Inside: {score}")

print(f"Original: {score}")     # Output: Original: 0
update_score_wrong()             # Output: Inside: 10
print(f"After wrong: {score}")   # Output: After wrong: 0 (unchanged!)

update_score_right()             # Output: Inside: 10
print(f"After right: {score}")   # Output: After right: 10 (changed!)


# =============================================================================
# 8. FUNCTION PARAMETERS - LOCAL SCOPE
# =============================================================================

name = "Global Name"  # Global

def greet(name):  # Parameter 'name' is LOCAL
    """Parameter creates local variable"""
    print(f"Inside function: {name}")  # Uses LOCAL parameter

greet("Local Name")             # Output: Inside function: Local Name
print(f"Outside: {name}")        # Output: Outside: Global Name


# =============================================================================
# 9. NESTED FUNCTIONS AND SCOPE
# =============================================================================

x = "Global X"  # Global scope

def outer():
    x = "Outer X"  # Outer function scope
    
    def inner():
        x = "Inner X"  # Inner function scope
        print(f"Inner: {x}")
    
    print(f"Outer: {x}")
    inner()

print(f"Global: {x}")
outer()

"""
Output:
Global: Global X
Outer: Outer X
Inner: Inner X

Each scope has its own 'x' variable!
"""


# =============================================================================
# 10. NESTED FUNCTIONS - THE 'nonlocal' KEYWORD
# =============================================================================

def make_multiplier(n):
    """Create a multiplier function"""
    
    def multiplier(x):
        nonlocal n  # Access the 'n' from outer function scope
        n += 1      # Modify the outer function's variable
        return x * n
    
    return multiplier

times3 = make_multiplier(3)
print(times3(10))  # Output: 40 (10 * 4, because n was incremented)
print(times3(10))  # Output: 50 (10 * 5, because n was incremented again)


# =============================================================================
# 11. PRACTICAL EXAMPLE - CONFIGURATION SETTINGS
# =============================================================================

# Global configuration
DEBUG_MODE = True
MAX_RETRIES = 3
API_KEY = "secret123"

def connect_to_api():
    """Read global configuration"""
    if DEBUG_MODE:
        print("Debug mode is ON")
    print(f"Retries: {MAX_RETRIES}")
    print(f"Using key: {API_KEY}")

connect_to_api()
print()

# Change global setting and see effect
def set_debug_mode(enabled):
    """Change debug setting"""
    global DEBUG_MODE
    DEBUG_MODE = enabled
    print(f"Debug mode set to: {DEBUG_MODE}")

set_debug_mode(False)
connect_to_api()


# =============================================================================
# 12. SCOPE CHAIN - LOOKUP ORDER
# =============================================================================

"""
Python looks for variables in this order:

1. LOCAL - inside the function
2. ENCLOSING - in outer functions (for nested functions)
3. GLOBAL - module level (outside functions)
4. BUILT-IN - Python's built-in names (print, len, etc.)

This is called LEGB rule (Local, Enclosing, Global, Built-in)
"""

name = "Built-in"  # Global

def outer_func():
    name = "Enclosing"
    
    def inner_func():
        name = "Local"
        print(name)  # Which 'name' will it use?
        # Python uses LOCAL first!
    
    inner_func()

outer_func()  # Output: Local (uses local scope first)


# =============================================================================
# 13. ACCESSING BUILT-INS
# =============================================================================

# Even if you override a name, you can still access built-ins
list = [1, 2, 3]  # We shadow the built-in 'list' type

print(type(list))      # Output: <class 'list'> (our list)
print(type([1, 2, 3])) # Output: <class 'list'> (built-in still works)

# But list() constructor might not work as expected
# my_list = list("ABC")  # Creates a list from string


# =============================================================================
# 14. BEST PRACTICES FOR SCOPE
# =============================================================================

# ✅ GOOD: Keep variables local when possible
def calculate_total(price, tax_rate=0.1):
    """Use local variables for calculations"""
    tax = price * tax_rate
    total = price + tax
    return total

total = calculate_total(100)
print(f"Total: {total}")


# ❌ AVOID: Relying on global variables
global_data = 100

def process_global():
    """Modifying global variables makes code hard to understand"""
    global global_data
    global_data += 50

# ✅ BETTER: Return values instead of using globals
def process_data(data):
    """Pass data as parameter, return result"""
    return data + 50

result = process_data(100)


# =============================================================================
# 15. COMMON MISTAKES
# =============================================================================

# ❌ MISTAKE 1: Trying to modify global without 'global' keyword
attempts = 0

def count_attempts_wrong():
    attempts = 0  # Creates LOCAL variable
    attempts += 1
    return attempts

print(count_attempts_wrong())  # Output: 1
print(attempts)                # Output: 0 (global unchanged!)


# ✅ Correct
attempts = 0

def count_attempts_right():
    global attempts
    attempts += 1
    return attempts

print(count_attempts_right())   # Output: 1
print(attempts)                 # Output: 1 (global changed!)


# ❌ MISTAKE 2: Confusing scope with visibility
def function1():
    local_var = "Function 1"
    print(local_var)

def function2():
    # print(local_var)  # ERROR: Can't access from function1
    local_var = "Function 2"
    print(local_var)


# ❌ MISTAKE 3: Modifying mutable global objects
shared_list = [1, 2, 3]  # Global list

def modify_list():
    shared_list.append(4)  # Modifies the global list (no 'global' needed!)

# This works because list is mutable, but it's confusing!
# Better to make it explicit with 'global'


# =============================================================================
# KEY POINTS SUMMARY
# =============================================================================

"""
✅ LOCAL SCOPE - inside functions
✅ GLOBAL SCOPE - outside functions
✅ BUILTIN SCOPE - Python's built-ins

✅ LOCAL takes priority over GLOBAL
✅ Use 'global' to MODIFY global variables
✅ Use 'nonlocal' for nested function scopes

✅ LEGB Rule - order Python looks for variables:
   Local → Enclosing → Global → Built-in

✅ BEST PRACTICE:
   - Keep variables local when possible
   - Pass parameters instead of using globals
   - Avoid global variables for complex logic
   - Use globals only for Constants

Clean scope = readable and maintainable code!
"""
