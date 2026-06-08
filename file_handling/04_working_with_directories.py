# file_handling/04_working_with_directories.py
"""
WORKING WITH DIRECTORIES
========================

What is it?
-----------
Working with directories involves creating, listing, and managing folders.

When to use it?
---------------
Use directory operations when you need to:
1. Create new folders
2. List files in a directory
3. Check if a path exists
4. Navigate through directory structures

How to identify it?
-------------------
Look for os and os.path module functions.
"""

import os

# Example 1: Checking if a path exists
print("=== CHECKING PATH EXISTENCE ===")

# Check if a file exists
file_exists = os.path.exists("example.txt")
print(f"example.txt exists: {file_exists}")

# Check if a directory exists
dir_exists = os.path.exists("my_folder")
print(f"my_folder exists: {dir_exists}")

# Example 2: Creating directories
print("\n=== CREATING DIRECTORIES ===")

# Create a single directory
if not os.path.exists("my_folder"):
    os.mkdir("my_folder")
    print("Created my_folder")

# Create nested directories
if not os.path.exists("parent/child/grandchild"):
    os.makedirs("parent/child/grandchild")
    print("Created nested directories")

# Example 3: Listing directory contents
print("\n=== LISTING DIRECTORY CONTENTS ===")

# List files and folders in current directory
contents = os.listdir(".")
print("Current directory contents:")
for item in contents:
    print(f"  {item}")

# List with full path
print("\nContents with full path:")
for item in os.listdir("."):
    full_path = os.path.join(".", item)
    print(f"  {full_path}")

# Example 4: Directory information
print("\n=== DIRECTORY INFORMATION ===")

# Check if a path is a file or directory
for item in os.listdir("."):
    full_path = os.path.join(".", item)
    if os.path.isfile(full_path):
        print(f"{item} is a file")
    elif os.path.isdir(full_path):
        print(f"{item} is a directory")

# Get file size
if os.path.exists("example.txt"):
    size = os.path.getsize("example.txt")
    print(f"example.txt size: {size} bytes")

# Example 5: Navigating directories
print("\n=== NAVIGATING DIRECTORIES ===")

# Get current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# Change directory
os.chdir("my_folder")
print(f"After chdir: {os.getcwd()}")

# Change back
os.chdir("..")
print(f"Back to parent: {os.getcwd()}")

# Example 6: Practical example - list all files of a type
print("\n=== PRACTICAL EXAMPLE ===")

# Create some test files
with open("document.txt", "w") as f:
    f.write("text content")
with open("image.jpg", "w") as f:
    f.write("fake image content")
with open("data.csv", "w") as f:
    f.write("csv,content")

# List all text files
print("Text files in current directory:")
for item in os.listdir("."):
    if os.path.isfile(item) and item.endswith(".txt"):
        print(f"  {item}")

"""
Key Points:
- os.path.exists() checks if a path exists
- os.mkdir() creates a single directory
- os.makedirs() creates nested directories
- os.listdir() lists directory contents
- os.path.isfile() and os.path.isdir() check path types
- os.getcwd() gets current directory
- os.chdir() changes directory
"""
