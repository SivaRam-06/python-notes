"""
╔════════════════════════════════════════════════════════════════════════════╗
║               IF, ELIF, ELSE STATEMENTS - COMPLETE GUIDE                  ║
║          Learn Conditional Statements with Detailed Examples              ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

# ═════════════════════════════════════════════════════════════════════════════
# 1. WHAT ARE CONDITIONAL STATEMENTS?
# ═════════════════════════════════════════════════════════════════════════════
"""
CONDITIONAL STATEMENTS are used to make decisions in your code:
    • IF: Execute code only if a condition is TRUE
    • ELIF: Execute code if previous condition was FALSE but this condition is TRUE
    • ELSE: Execute code if all previous conditions were FALSE
    
WHY USE THEM?
    • Make different decisions based on different situations
    • Control which code runs
    • Create programs that respond to different inputs
    
FLOW:
    IF condition is TRUE? 
        → Run this code
    ELIF another condition is TRUE? 
        → Run this code instead
    ELSE (all above are FALSE)
        → Run this code
"""

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                    SECTION 1: IF STATEMENT                            ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

# ═════════════════════════════════════════════════════════════════════════════
# 1. SIMPLE IF STATEMENT
# ═════════════════════════════════════════════════════════════════════════════
"""
SIMPLE IF:
    Syntax:
        if condition:
            # Code to run if condition is TRUE
    
    • Indentation (spaces) is IMPORTANT!
    • Only run code if condition is TRUE
    • If condition is FALSE, code is skipped
"""

print("1. SIMPLE IF STATEMENT")
print("-" * 60)

# Example 1: Check if age is adult
age = 20
if age >= 18:
    print(f"Age is {age}. You are an adult!")

print()

# Example 2: Check if number is positive
number = 50
if number > 0:
    print(f"{number} is a positive number")

print()

# Example 3: Check if password is long enough
password = "mypassword123"
if len(password) >= 8:
    print(f"Password '{password}' is strong (length: {len(password)})")

print()

# Example 4: Check if student passed
marks = 75
if marks >= 60:
    print(f"Passed! Your marks: {marks}")

print("\n")
