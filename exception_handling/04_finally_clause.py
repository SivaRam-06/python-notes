# exception_handling/04_finally_clause.py
"""
THE FINALLY CLAUSE
==================

What is it?
-----------
The finally clause always runs, whether an error occurred or not.

When to use it?
---------------
Use finally for cleanup code that must run in all circumstances.

How to identify it?
-------------------
Look for code that must execute regardless of success or failure.
"""

# Example 1: Basic finally clause
print("=== BASIC FINALLY CLAUSE ===")

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"10 divided by {num} is {result}")
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero!")
finally:
    # This always runs, error or not
    print("Calculation attempt completed.")

# Example 2: Why use finally?
print("\n=== WHY USE FINALLY? ===")

# Without finally (problematic)
file = None
try:
    file = open("test.txt", "w")
    file.write("Hello, World!")
except IOError as e:
    print(f"Error writing to file: {e}")
if file:
    file.close()
    print("File closed")

# With finally (better)
file = None
try:
    file = open("test.txt", "w")
    file.write("Hello, World!")
except IOError as e:
    print(f"Error writing to file: {e}")
finally:
    # This always runs, ensuring the file is closed
    if file:
        file.close()
        print("File closed in finally block")

# Example 3: Real-world database example
print("\n=== REAL-WORLD DATABASE EXAMPLE ===")

# Simulate database connection
class DatabaseConnection:
    def __init__(self):
        print("Database connected")
    
    def close(self):
        print("Database connection closed")
    
    def execute_query(self, query):
        if "error" in query.lower():
            raise Exception("Query execution error")
        print(f"Query executed: {query}")

# Using finally to ensure cleanup
db = None
try:
    db = DatabaseConnection()
    db.execute_query("SELECT * FROM users")
    db.execute_query("CREATE error")  # This will cause an error
except Exception as e:
    print(f"Database error: {e}")
finally:
    if db:
        db.close()

"""
Key Points:
- Finally clause always runs, error or not
- Use it for cleanup operations (closing files, connections, etc.)
- Ensures resources are properly released
- Essential for robust, reliable code
"""
