# file_handling/09_error_handling.py
"""
ERROR HANDLING IN FILE OPERATIONS
=================================

What is it?
-----------
Error handling in file operations involves catching and handling
exceptions that may occur during file operations.

When to use it?
---------------
Use error handling when you need to:
1. Handle missing files gracefully
2. Deal with permission issues
3. Manage disk space errors
4. Handle corrupt files

How to identify it?
-------------------
Look for try-except blocks around file operations.
"""

# Example 1: Handling file not found errors
print("=== HANDLING FILE NOT FOUND ERRORS ===")

try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the filename.")

# Example 2: Handling permission errors
print("\n=== HANDLING PERMISSION ERRORS ===")

try:
    # Try to open a file we don't have permission to access
    with open("/root/protected_file.txt", "r") as file:
        content = file.read()
        print(content)
except PermissionError:
    print("Permission denied. You don't have access to this file.")

# Example 3: Handling multiple file errors
print("\n=== HANDLING MULTIPLE FILE ERRORS ===")

filename = "example.txt"

try:
    with open(filename, "r") as file:
        content = file.read()
        # Try to convert to integer (might cause ValueError)
        number = int(content)
        print(f"Number: {number}")
except FileNotFoundError:
    print(f"File '{filename}' not found.")
except PermissionError:
    print(f"Permission denied for '{filename}'.")
except ValueError:
    print(f"File '{filename}' does not contain a valid number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Example 4: Using else and finally with files
print("\n=== USING ELSE AND FINALLY WITH FILES ===")

file = None
try:
    file = open("example.txt", "r")
    content = file.read()
    print("File content:")
    print(content)
except FileNotFoundError:
    print("File not found.")
else:
    print("File read successfully.")
finally:
    if file and not file.closed:
        file.close()
        print("File closed in finally block.")

# Example 5: Practical example - robust file processing
print("\n=== PRACTICAL EXAMPLE - ROBUST FILE PROCESSING ===")

def process_file(filename):
    """Process a file with robust error handling"""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            
        # Process each line
        for i, line in enumerate(lines, 1):
            try:
                # Try to convert each line to a number
                number = float(line.strip())
                print(f"Line {i}: {number}")
            except ValueError:
                print(f"Line {i}: Invalid number '{line.strip()}'")
                
        return True
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return False
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'.")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

# Test the function
success = process_file("example.txt")
print(f"Processing {'succeeded' if success else 'failed'}")

# Example 6: Creating missing directories
print("\n=== CREATING MISSING DIRECTORIES ===")

import os

filename = "data/files/important.txt"

try:
    with open(filename, "w") as file:
        file.write("Important content")
except FileNotFoundError:
    # Create the directory if it doesn't exist
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")
        
        # Try again
        with open(filename, "w") as file:
            file.write("Important content")
        print("File created successfully")
except Exception as e:
    print(f"Error: {e}")

"""
Key Points:
- Always handle FileNotFoundError for missing files
- Handle PermissionError for access issues
- Use try-except blocks around file operations
- Use finally to ensure files are closed
- Create missing directories when appropriate
"""
