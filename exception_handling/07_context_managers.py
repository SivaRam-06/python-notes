# exception_handling/07_context_managers.py
"""
CONTEXT MANAGERS
================

What is it?
-----------
A way to manage resources (like files) that need to be cleaned up
after use, using the with statement.

When to use it?
---------------
Use context managers when:
1. Working with files
2. Working with network connections
3. Working with database connections
4. Any resource that needs cleanup

How to identify it?
-------------------
Look for operations that require cleanup (closing, releasing, etc.).
"""

# Example 1: Basic with statement
print("=== BASIC WITH STATEMENT ===")

# Without context manager (manual cleanup)
file = open("test.txt", "w")
try:
    file.write("Hello, World!")
finally:
    file.close()

# With context manager (automatic cleanup)
with open("test.txt", "w") as file:
    file.write("Hello, World!")
# File is automatically closed here

# Example 2: Creating custom context managers
print("\n=== CUSTOM CONTEXT MANAGERS ===")

from contextlib import contextmanager

@contextmanager
def timer():
    """A context manager that measures execution time"""
    import time
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")

# Using the custom context manager
with timer():
    # This code will be timed
    total = 0
    for i in range(1000000):
        total += i

# Example 3: Class-based context manager
print("\n=== CLASS-BASED CONTEXT MANAGER ===")

class DatabaseConnection:
    """A simple database connection context manager"""
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False
    
    def __enter__(self):
        """Called when entering the with block"""
        print(f"Connecting to database: {self.db_name}")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting the with block"""
        print("Closing database connection")
        self.connected = False
        # Return False to propagate exceptions, True to suppress them
        return False
    
    def execute(self, query):
        """Execute a database query"""
        if not self.connected:
            raise Exception("Not connected to database")
        print(f"Executing query: {query}")
        # In real code, this would execute the query

# Using the class-based context manager
with DatabaseConnection("my_database") as db:
    db.execute("SELECT * FROM users")
    db.execute("INSERT INTO users VALUES (1, 'John')")

"""
Key Points:
- Context managers automatically handle resource cleanup
- Use the with statement for context managers
- You can create custom context managers with @contextmanager
- Class-based context managers use __enter__ and __exit__ methods
- Essential for proper resource management
"""
