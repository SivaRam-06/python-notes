# RECURSION - Functions Calling Themselves

# =============================================================================
# 1. WHAT IS RECURSION?
# =============================================================================

"""
RECURSION = Function calling itself

Requirements for recursion:
1. BASE CASE - Condition to STOP (prevent infinite loop)
2. RECURSIVE CASE - Function calling itself with different arguments
3. Progress toward base case - Get closer to base case each call

Simple Analogy:
- Russian nesting dolls
- Each doll contains a smaller doll
- Until you reach the smallest doll (base case)
"""


# =============================================================================
# 2. SIMPLE COUNTDOWN EXAMPLE
# =============================================================================

def countdown(n):
    """Count down from n to 0"""
    
    # BASE CASE - Stop condition
    if n < 0:
        print("Blastoff!")
        return
    
    # Do something
    print(n)
    
    # RECURSIVE CASE - Call itself with smaller value
    countdown(n - 1)

countdown(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# 0
# Blastoff!


# =============================================================================
# 3. FACTORIAL - CLASSIC RECURSION EXAMPLE
# =============================================================================

"""
Factorial: 5! = 5 × 4 × 3 × 2 × 1 = 120

Recursive definition:
- 0! = 1 (base case)
- n! = n × (n-1)! (recursive case)
"""

def factorial(n):
    """Calculate factorial using recursion"""
    
    # BASE CASE
    if n == 0 or n == 1:
        return 1
    
    # RECURSIVE CASE
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")   # Output: 120
print(f"10! = {factorial(10)}")  # Output: 3628800

# Trace of factorial(5):
# factorial(5) = 5 * factorial(4)
# factorial(4) = 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)
# factorial(1) = 1 (BASE CASE)
# Result: 5 * 4 * 3 * 2 * 1 = 120


# =============================================================================
# 4. FIBONACCI SEQUENCE
# =============================================================================

"""
Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21...

Rule: Each number is sum of previous two
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2)
"""

def fibonacci(n):
    """Get nth Fibonacci number"""
    
    # BASE CASES
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # RECURSIVE CASE
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci sequence:")
for i in range(8):
    print(f"F({i}) = {fibonacci(i)}", end=" ")
print()


# =============================================================================
# 5. POWER CALCULATION
# =============================================================================

def power(base, exponent):
    """Calculate base^exponent using recursion"""
    
    # BASE CASE
    if exponent == 0:
        return 1
    
    # RECURSIVE CASE
    return base * power(base, exponent - 1)

print(power(2, 3))   # Output: 8
print(power(3, 4))   # Output: 81


# =============================================================================
# 6. SUM OF DIGITS
# =============================================================================

def sum_digits(n):
    """Sum all digits in a number"""
    
    # BASE CASE
    if n < 10:
        return n
    
    # RECURSIVE CASE - Last digit + sum of rest
    return (n % 10) + sum_digits(n // 10)

print(f"Sum of 12345: {sum_digits(12345)}")  # Output: 15 (1+2+3+4+5)


# =============================================================================
# 7. STRING REVERSAL
# =============================================================================

def reverse_string(s):
    """Reverse a string using recursion"""
    
    # BASE CASE
    if len(s) == 0:
        return s
    
    # RECURSIVE CASE - Last char + reversed rest
    return reverse_string(s[1:]) + s[0]

print(f"Hello reversed: {reverse_string('Hello')}")  # Output: olleH


# =============================================================================
# 8. PALINDROME CHECK
# =============================================================================

def is_palindrome(s):
    """Check if string is palindrome"""
    
    # BASE CASE
    if len(s) <= 1:
        return True
    
    # Check first and last char, then check rest
    if s[0] != s[-1]:
        return False
    
    # RECURSIVE CASE
    return is_palindrome(s[1:-1])

print(f"racecar is palindrome: {is_palindrome('racecar')}")  # True
print(f"hello is palindrome: {is_palindrome('hello')}")      # False


# =============================================================================
# 9. BINARY SEARCH
# =============================================================================

def binary_search(arr, target, left, right):
    """Search for target in sorted array using binary search"""
    
    # BASE CASE - Not found
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    # Found it
    if arr[mid] == target:
        return mid
    
    # Search left half
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    
    # Search right half
    else:
        return binary_search(arr, target, mid + 1, right)

numbers = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"Index of 7: {binary_search(numbers, 7, 0, len(numbers)-1)}")  # Output: 3
print(f"Index of 10: {binary_search(numbers, 10, 0, len(numbers)-1)}")  # Output: -1


# =============================================================================
# 10. TREE TRAVERSAL - RECURSIVE DIRECTORY STRUCTURE
# =============================================================================

def print_tree(indent, label):
    """Simulate tree structure traversal"""
    
    # BASE CASE - Leaf node
    if not label:
        return
    
    # Print current node
    print(indent + label)
    
    # RECURSIVE CASE - Print children with more indent
    children = {
        "Root": ["Child1", "Child2", "Child3"],
        "Child1": ["SubChild1A", "SubChild1B"],
        "Child2": ["SubChild2A"],
        "Child3": []
    }
    
    if label in children:
        for child in children[label]:
            print_tree(indent + "  ", child)

print("Tree structure:")
print_tree("", "Root")


# =============================================================================
# 11. COMMON MISTAKE - INFINITE RECURSION
# =============================================================================

# ❌ MISTAKE: No base case or unreachable base case
def bad_recursion(n):
    return bad_recursion(n - 1)  # No base case! Stack overflow!

# This would cause: RecursionError: maximum recursion depth exceeded
# Uncomment to crash: bad_recursion(5)


# ✅ Correct: Always have a reachable base case
def good_recursion(n):
    # BASE CASE - prevents infinite recursion
    if n <= 0:
        return "Done"
    
    # RECURSIVE CASE - moves toward base case
    return good_recursion(n - 1)

print(good_recursion(3))  # Output: Done


# =============================================================================
# 12. RECURSION vs ITERATION
# =============================================================================

# Recursive version
def sum_recursive(*args):
    if len(args) == 0:
        return 0
    return args[0] + sum_recursive(*args[1:])

# Iterative version
def sum_iterative(*args):
    total = 0
    for num in args:
        total += num
    return total

print(f"Recursive sum: {sum_recursive(1, 2, 3, 4, 5)}")   # Output: 15
print(f"Iterative sum: {sum_iterative(1, 2, 3, 4, 5)}")   # Output: 15

# Key differences:
# - Recursion: Elegant, shorter code, but uses more memory (call stack)
# - Iteration: More efficient, faster for large inputs, easier to understand


# =============================================================================
# 13. MUTUAL RECURSION
# =============================================================================

"""
Two functions calling each other (advanced)
"""

def is_even(n):
    """Check if n is even"""
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    """Check if n is odd"""
    if n == 0:
        return False
    return is_even(n - 1)

print(f"4 is even: {is_even(4)}")  # True
print(f"5 is odd: {is_odd(5)}")    # True


# =============================================================================
# 14. RECURSION WITH LIST
# =============================================================================

def flatten_list(nested_list):
    """Flatten a nested list"""
    result = []
    
    for item in nested_list:
        # If item is a list, recursively flatten it
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    
    return result

nested = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
flattened = flatten_list(nested)
print(f"Nested: {nested}")
print(f"Flattened: {flattened}")  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


# =============================================================================
# 15. RECURSION WITH MEMOIZATION (OPTIMIZATION)
# =============================================================================

# Problem: fibonacci(n) recalculates same values many times
# Solution: Remember (memoize) results

cache = {}  # Store computed results

def fibonacci_memo(n):
    """Fibonacci with memoization"""
    
    # Check if already computed
    if n in cache:
        return cache[n]
    
    # BASE CASE
    if n <= 1:
        return n
    
    # RECURSIVE CASE
    result = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    
    # Store in cache before returning
    cache[n] = result
    return result

print(f"F(30) with memoization: {fibonacci_memo(30)}")  # Fast!
print(f"Cache: {cache}")


# =============================================================================
# BEST PRACTICES
# =============================================================================

"""
✅ DO:
   - Always have a base case
   - Make sure base case is reachable
   - Move toward base case each recursion
   - Use recursion for naturally recursive problems
   - Document your base and recursive cases

❌ DON'T:
   - Forget the base case
   - Create infinite recursion
   - Use recursion for simple loops
   - Recurse too deeply (stack overflow)

Good use cases for recursion:
- Tree traversal
- Graph traversal
- Factorial, fibonacci
- Divide and conquer algorithms
- Backtracking problems
"""


# =============================================================================
# KEY POINTS SUMMARY
# =============================================================================

"""
✅ RECURSION = Function calling itself
✅ BASE CASE = Stop condition (must exist!)
✅ RECURSIVE CASE = Function calls itself
✅ PROGRESS = Must move toward base case

Recursion parameters:
-> setrecursionlimit(2000)
-> getrecursionlimit()

Common examples:
- Factorial
- Fibonacci
- Tree traversal
- Binary search
- String reversal

Recursion vs Iteration:
- Recursion: Elegant but uses more memory
- Iteration: More efficient, faster

Always remember: Recursion must have a BASE CASE!
"""
