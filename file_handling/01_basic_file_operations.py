# file_handling/01_basic_file_operations.py
"""
BASIC FILE OPERATIONS
=====================

What is it?
-----------
Basic file operations include opening, reading, writing, and closing files.

When to use it?
---------------
Use these operations when you need to:
1. Read data from files
2. Write data to files
3. Store or retrieve information

How to identify it?
-------------------
Look for situations where you need persistent storage of data.
"""

# Example 1: Opening and closing files
print("=== OPENING AND CLOSING FILES ===")

# Method 1: Traditional approach (must close manually)
file = open("example.txt", "w")  # Open file for writing
file.write("Hello, World!")      # Write to file
file.close()                     # Close the file

# Method 2: Using with statement (automatically closes)
with open("example.txt", "w") as file:
    file.write("Hello, World!")  # File automatically closes after this block

# Example 2: Reading from files
print("\n=== READING FROM FILES ===")

# Write some content first
with open("example.txt", "w") as file:
    file.write("Line 1\nLine 2\nLine 3")

# Read the entire file
with open("example.txt", "r") as file:
    content = file.read()
    print("Full content:")
    print(content)

# Read line by line
with open("example.txt", "r") as file:
    print("\nLine by line:")
    for line in file:
        print(line.strip())  # strip() removes newline characters

# Example 3: Different reading methods
print("\n=== DIFFERENT READING METHODS ===")

with open("example.txt", "r") as file:
    # Read first 5 characters
    first_chars = file.read(5)
    print(f"First 5 characters: {first_chars}")
    
    # Read the next line
    next_line = file.readline()
    print(f"Next line: {next_line.strip()}")
    
    # Read all remaining lines
    remaining_lines = file.readlines()
    print(f"Remaining lines: {remaining_lines}")

"""
Key Points:
- Always close files after use to free resources
- Use 'with' statement for automatic closing
- read() reads the entire file
- readline() reads one line at a time
- readlines() reads all lines into a list
"""
