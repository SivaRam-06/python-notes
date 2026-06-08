# file_handling/02_file_modes.py
"""
FILE MODES
==========

What is it?
-----------
File modes determine how a file is opened and what operations are allowed.

When to use it?
---------------
Use different modes based on whether you want to:
1. Read from a file
2. Write to a file
3. Append to a file
4. Work with binary data

How to identify it?
-------------------
Look at the second parameter in the open() function.
"""

# Example 1: Common file modes
print("=== COMMON FILE MODES ===")

# 'r' - Read mode (default)
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print("Read mode: File opened for reading")
except FileNotFoundError:
    print("Read mode: File not found")

# 'w' - Write mode (creates new file or overwrites existing)
with open("example.txt", "w") as file:
    file.write("This is new content")
    print("Write mode: File opened for writing")

# 'a' - Append mode (adds to end of file)
with open("example.txt", "a") as file:
    file.write("\nThis is appended content")
    print("Append mode: Content added to end of file")

# Example 2: Reading the results
print("\n=== READING THE RESULTS ===")
with open("example.txt", "r") as file:
    content = file.read()
    print("Final content:")
    print(content)

# Example 3: Binary modes
print("\n=== BINARY MODES ===")

# Write binary data
with open("binary_example.bin", "wb") as file:
    file.write(b"Binary data here")
    print("Binary write mode: Binary file created")

# Read binary data
with open("binary_example.bin", "rb") as file:
    binary_content = file.read()
    print(f"Binary read mode: Read {len(binary_content)} bytes")

# Example 4: Read/Write modes
print("\n=== READ/WRITE MODES ===")

# 'r+' - Read and write (file must exist)
with open("example.txt", "r+") as file:
    content = file.read()
    print(f"Current content: {content}")
    file.write("\nAdded with r+ mode")

# 'w+' - Write and read (creates new file or overwrites existing)
with open("example2.txt", "w+") as file:
    file.write("Initial content")
    file.seek(0)  # Move to beginning of file
    content = file.read()
    print(f"Content after w+ mode: {content}")

# 'a+' - Append and read (creates file if doesn't exist)
with open("example3.txt", "a+") as file:
    file.write("Appended content")
    file.seek(0)  # Move to beginning of file
    content = file.read()
    print(f"Content after a+ mode: {content}")

"""
Key Points:
- 'r' - Read mode (file must exist)
- 'w' - Write mode (creates/overwrites file)
- 'a' - Append mode (creates/appends to file)
- 'b' - Binary mode (use with r, w, a)
- '+' - Read/Write mode (use with r, w, a)
"""
