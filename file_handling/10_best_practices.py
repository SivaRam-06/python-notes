# file_handling/10_best_practices.py
"""
FILE HANDLING BEST PRACTICES
============================

What is it?
-----------
Best practices for working with files in Python.

When to use it?
---------------
Always follow these practices when working with files.

How to identify it?
-------------------
Look for these patterns in well-written Python code.
"""

import os

# Practice 1: Use with statement for automatic closing
print("=== USE WITH STATEMENT ===")

# Bad practice: Manual closing (might forget to close)
file = open("example.txt", "w")
file.write("content")
file.close()

# Good practice: Automatic closing
with open("example.txt", "w") as file:
    file.write("content")
# File automatically closed here

# Practice 2: Handle file paths properly
print("\n=== HANDLE FILE PATHS PROPERLY ===")

# Bad practice: Hardcoded paths
file_path = "C:/Users/Name/Documents/file.txt"  # Platform-specific

# Good practice: Use os.path.join for cross-platform compatibility
file_path = os.path.join("data", "files", "document.txt")
print(f"File path: {file_path}")

# Good practice: Use pathlib (Python 3.4+)
from pathlib import Path
file_path = Path("data") / "files" / "document.txt"
print(f"File path with pathlib: {file_path}")

# Practice 3: Check if files exist before operations
print("\n=== CHECK IF FILES EXIST ===")

filename = "example.txt"

# Bad practice: Assume file exists
# with open(filename, "r") as file:
#     content = file.read()

# Good practice: Check first
if os.path.exists(filename):
    with open(filename, "r") as file:
        content = file.read()
    print("File read successfully")
else:
    print(f"File '{filename}' does not exist")

# Practice 4: Use appropriate file modes
print("\n=== USE APPROPRIATE FILE MODES ===")

# For reading text
with open("example.txt", "r") as file:
    content = file.read()

# For writing text (overwrites)
with open("example.txt", "w") as file:
    file.write("new content")

# For appending text
with open("example.txt", "a") as file:
    file.write("appended content")

# For reading binary
with open("image.jpg", "rb") as file:
    binary_data = file.read()

# For writing binary
with open("image.jpg", "wb") as file:
    file.write(binary_data)

# Practice 5: Handle exceptions properly
print("\n=== HANDLE EXCEPTIONS PROPERLY ===")

filename = "example.txt"

try:
    with open(filename, "r") as file:
        content = file.read()
        # Process content
        numbers = [int(line) for line in content.split()]
        print(f"Numbers: {numbers}")
except FileNotFoundError:
    print(f"File '{filename}' not found")
except ValueError:
    print("File contains non-numeric data")
except Exception as e:
    print(f"Unexpected error: {e}")

# Practice 6: Use context managers for complex operations
print("\n=== USE CONTEXT MANAGERS FOR COMPLEX OPERATIONS ===")

from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    """Custom context manager for file operations"""
    file = None
    try:
        file = open(filename, mode)
        yield file
    except Exception as e:
        print(f"Error working with {filename}: {e}")
        raise
    finally:
        if file and not file.closed:
            file.close()

# Use the custom context manager
try:
    with open_file("example.txt", "r") as file:
        content = file.read()
        print("File content:", content)
except Exception:
    print("Failed to read file")

# Practice 7: Practical example - backup system
print("\n=== PRACTICAL EXAMPLE - BACKUP SYSTEM ===")

import shutil
import datetime

def create_backup(source_dir, backup_dir):
    """Create a backup of a directory"""
    try:
        # Create backup directory if it doesn't exist
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        # Create timestamped backup
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"backup_{timestamp}"
        backup_path = os.path.join(backup_dir, backup_name)
        
        # Copy directory
        shutil.copytree(source_dir, backup_path)
        print(f"Backup created: {backup_path}")
        return True
        
    except Exception as e:
        print(f"Backup failed: {e}")
        return False

# Test the backup function
create_backup("data", "backups")

"""
Key Points:
- Always use with statement for automatic closing
- Use os.path.join or pathlib for cross-platform paths
- Check if files exist before operations
- Use appropriate file modes for your needs
- Handle exceptions properly in file operations
- Create custom context managers for complex operations
- Always follow best practices for reliable code
"""
