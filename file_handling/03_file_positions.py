# file_handling/03_file_positions.py
"""
FILE POSITIONS
==============

What is it?
-----------
File positions track where the next read or write operation will occur.

When to use it?
---------------
Use file positions when you need to:
1. Move to a specific location in a file
2. Know your current position in a file
3. Read from or write to specific parts of a file

How to identify it?
-------------------
Look for seek() and tell() methods in file operations.
"""

# Example 1: Using tell() to get current position
print("=== USING TELL() ===")

with open("example.txt", "w") as file:
    file.write("Hello, World!")  # Write some content

with open("example.txt", "r") as file:
    position = file.tell()
    print(f"Initial position: {position}")
    
    # Read first 5 characters
    content = file.read(5)
    position = file.tell()
    print(f"After reading 5 characters: {position}")
    print(f"Content: {content}")

# Example 2: Using seek() to change position
print("\n=== USING SEEK() ===")

with open("example.txt", "r") as file:
    # Move to position 7
    file.seek(7)
    position = file.tell()
    print(f"Position after seek(7): {position}")
    
    # Read from position 7
    content = file.read()
    print(f"Content from position 7: {content}")

# Example 3: seek() with different arguments
print("\n=== SEEK() WITH DIFFERENT ARGUMENTS ===")

with open("example.txt", "r") as file:
    # seek(offset, whence)
    # whence: 0 = start, 1 = current, 2 = end
    
    # Move to beginning
    file.seek(0)
    print(f"Position after seek(0): {file.tell()}")
    
    # Move 5 bytes from current position
    file.seek(5, 1)
    print(f"Position after seek(5, 1): {file.tell()}")
    
    # Move to 2 bytes before end
    file.seek(-2, 2)
    print(f"Position after seek(-2, 2): {file.tell()}")
    content = file.read()
    print(f"Content from near end: {content}")

# Example 4: Practical use case - reading specific parts
print("\n=== PRACTICAL USE CASE ===")

# Create a file with structured data
with open("data.txt", "w") as file:
    file.write("Name: John Doe\nAge: 30\nCity: New York")

# Read only the age value
with open("data.txt", "r") as file:
    # Find the position of "Age: "
    content = file.read()
    age_pos = content.find("Age: ")
    
    if age_pos != -1:
        # Move to the age position
        file.seek(age_pos)
        # Skip "Age: "
        file.seek(5, 1)
        # Read the age value
        age = file.readline().strip()
        print(f"Age: {age}")

"""
Key Points:
- tell() returns the current file position
- seek(offset) moves to a specific position
- seek(offset, whence) moves relative to a reference point
- Use positions to read/write specific parts of files
"""
