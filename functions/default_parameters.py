# DEFAULT PARAMETERS - Using Pre-set Values

# =============================================================================
# 1. BASIC DEFAULT PARAMETER
# =============================================================================

def greet(name, greeting="Hello"):
    """Greet with default greeting message"""
    return f"{greeting}, {name}!"

# Using default parameter
print(greet("Alice"))                 # Output: Hello, Alice!
print(greet("Bob", "Hi"))             # Output: Hi, Bob!
print(greet("Charlie", "Hey there"))  # Output: Hey there, Charlie!


# =============================================================================
# 2. MULTIPLE DEFAULT PARAMETERS
# =============================================================================

def create_user(username, email, age=18, country="USA"):
    """Create user with some defaults"""
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Age: {age}")
    print(f"Country: {country}")
    print()

# Using all defaults
create_user("alice@example.com", "alice123")

# Override one default
create_user("alice@example.com", "alice123", 25)

# Override multiple defaults
create_user("alice@example.com", "alice123", 25, "Canada")

# Override specific defaults using keyword
create_user("alice@example.com", "alice123", country="UK")


# =============================================================================
# 3. DEFAULT WITH NONE - MEANING NO VALUE PROVIDED
# =============================================================================

def process_data(data, format_type=None):
    """Process data with optional formatting"""
    if format_type is None:
        return data
    elif format_type == "uppercase":
        return data.upper()
    elif format_type == "lowercase":
        return data.lower()
    elif format_type == "title":
        return data.title()

print(process_data("hello world"))              # Output: hello world
print(process_data("hello world", "uppercase")) # Output: HELLO WORLD
print(process_data("hello world", "title"))    # Output: Hello World


# =============================================================================
# 4. DEFAULT BOOLEAN FOR FLAGS
# =============================================================================

def show_details(name, show_email=False, show_age=False):
    """Show user details based on flags"""
    info = f"Name: {name}"
    
    if show_email:
        info += ", Email: user@email.com"
    
    if show_age:
        info += ", Age: 25"
    
    return info

print(show_details("Alice"))                           # Name: Alice
print(show_details("Bob", show_email=True))            # Name: Bob, Email: user@email.com
print(show_details("Charlie", show_age=True))          # Name: Charlie, Age: 25
print(show_details("Diana", show_email=True, show_age=True))  # All details


# =============================================================================
# 5. DEFAULT NUMERIC VALUES
# =============================================================================

def calculate_discount(price, discount_percent=0):
    """Calculate price after discount"""
    discounted = price * (1 - discount_percent / 100)
    return discounted

print(calculate_discount(100))      # Output: 100.0 (no discount)
print(calculate_discount(100, 10))  # Output: 90.0 (10% off)
print(calculate_discount(100, 50))  # Output: 50.0 (50% off)


# =============================================================================
# 6. DEFAULT CONTAINER VALUES (LIST, DICT)
# =============================================================================

# ❌ DANGEROUS: Mutable default (list/dict)
def add_to_list_bad(item, my_list=[]):
    """Don't use mutable defaults!"""
    my_list.append(item)
    return my_list

result1 = add_to_list_bad(1)
print(f"Result 1: {result1}")  # Output: [1]

result2 = add_to_list_bad(2)
print(f"Result 2: {result2}")  # Output: [1, 2] - SHARED LIST!

result3 = add_to_list_bad(3)
print(f"Result 3: {result3}")  # Output: [1, 2, 3] - SHARED LIST!


# ✅ CORRECT: Use None and create new container
def add_to_list_good(item, my_list=None):
    """Correct way to use mutable default"""
    if my_list is None:
        my_list = []
    
    my_list.append(item)
    return my_list

result1 = add_to_list_good(1)
print(f"Result 1: {result1}")  # Output: [1]

result2 = add_to_list_good(2)
print(f"Result 2: {result2}")  # Output: [2] - Different list!

result3 = add_to_list_good(3)
print(f"Result 3: {result3}")  # Output: [3] - Different list!


# =============================================================================
# 7. DEFAULTS WITH DIFFERENT DATA TYPES
# =============================================================================

def configure_server(host="localhost", port=8000, debug=False, 
                     allowed_hosts=None, timeout=30):
    """Configure server with various default types"""
    
    if allowed_hosts is None:
        allowed_hosts = []
    
    print(f"Host: {host} (type: {type(host).__name__})")
    print(f"Port: {port} (type: {type(port).__name__})")
    print(f"Debug: {debug} (type: {type(debug).__name__})")
    print(f"Allowed Hosts: {allowed_hosts} (type: {type(allowed_hosts).__name__})")
    print(f"Timeout: {timeout} (type: {type(timeout).__name__})")
    print()

configure_server()
configure_server("192.168.1.1", 3000, True, ["localhost", "127.0.0.1"])


# =============================================================================
# 8. PRACTICAL EXAMPLE - FILE OPERATIONS
# =============================================================================

def read_file(filename, encoding="utf-8", skip_empty_lines=True, max_lines=None):
    """
    Simulate reading file with defaults
    - Default encoding: UTF-8
    - Default: skip empty lines
    - Default: read all lines
    """
    print(f"Reading: {filename}")
    print(f"  Encoding: {encoding}")
    print(f"  Skip empty lines: {skip_empty_lines}")
    print(f"  Max lines: {max_lines if max_lines else 'unlimited'}")
    print()

read_file("data.txt")
read_file("data.txt", "latin-1", False)
read_file("data.txt", max_lines=100)


# =============================================================================
# 9. OVERRIDING DEFAULTS
# =============================================================================

def make_pizza(crust="regular", size="medium", toppings=None):
    """Make pizza with various options"""
    if toppings is None:
        toppings = ["cheese"]
    
    print(f"Crust: {crust}")
    print(f"Size: {size}")
    print(f"Toppings: {', '.join(toppings)}")
    print()

# Using all defaults
make_pizza()

# Override size but keep crust default
make_pizza(size="large")

# Override multiple but keep one default
make_pizza(crust="thin", toppings=["cheese", "pepperoni", "mushroom"])


# =============================================================================
# 10. WHEN TO USE DEFAULTS
# =============================================================================

# ✅ Good uses of defaults:
# - Optional configuration
# - Common/standard values
# - Backward compatibility
# - Making function simpler to use

def send_email(recipient, subject, message, cc=None, bcc=None, priority="normal"):
    """Most emails don't need cc/bcc, so they have defaults"""
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print(f"Message: {message}")
    if cc:
        print(f"CC: {cc}")
    if bcc:
        print(f"BCC: {bcc}")
    print(f"Priority: {priority}")
    print()

send_email("user@example.com", "Hello", "This is a test")
send_email("user@example.com", "Urgent", "Please review", priority="high")


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================

# ❌ MISTAKE 1: Using mutable objects as defaults
def bad_append(item, list_param=[]):
    """This creates a shared list!"""
    list_param.append(item)
    return list_param

# ✅ Correct
def good_append(item, list_param=None):
    """Create new list each time"""
    if list_param is None:
        list_param = []
    list_param.append(item)
    return list_param


# ❌ MISTAKE 2: Positional args after defaults
# def wrong_order(a=10, b):  # ERROR: non-default after default
#     pass

# ✅ Correct: required args first, then defaults
def right_order(b, a=10):
    """Required argument first, then default"""
    pass


# ❌ MISTAKE 3: All parameters have defaults (confusing)
def confusing(a=1, b=2, c=3):
    """Can't tell which arguments are important"""
    pass

# ✅ Better: Reserve defaults for optional parameters
def clear(filename, mode="read", encoding="utf-8"):
    """Clear which parameters are required vs optional"""
    pass


# =============================================================================
# KEY POINTS SUMMARY
# =============================================================================

"""
✅ DEFAULT PARAMETERS - provide preset values
✅ Syntax: def function(param=default_value)
✅ Can have multiple defaults

✅ DEFAULTS ARE OPTIONAL - can always override
✅ Required parameters MUST come before defaults
✅ Use keyword arguments to override specific defaults

⚠️  NEVER use mutable objects as defaults (list, dict)
✅ Use None as default, then create new container

Defaults make functions:
- Easier to use (less required arguments)
- More flexible (can override when needed)
- Backward compatible (old code still works)
"""
