# file_handling/05_file_operations.py
"""
FILE OPERATIONS
===============

What is it?
-----------
File operations include copying, moving, renaming, and deleting files.

When to use it?
---------------
Use these operations when you need to:
1. Copy files to another location
2. Move or rename files
3. Delete files or directories
4. Manage your file system

How to identify it?
-------------------
Look for shutil and os module functions.
"""

import os
import shutil

# Example 1: Copying files
print("=== COPYING FILES ===")

# Create a source file
with open("source.txt", "w") as f:
    f.write("This is the source file content")

# Copy file
shutil.copy("source.txt", "copy.txt")
print("File copied successfully")

# Copy with metadata
shutil.copy2("source.txt", "copy_with_metadata.txt")
print("File copied with metadata")

# Copy to a directory
if not os.path.exists("backup"):
    os.mkdir("backup")
shutil.copy("source.txt", "backup/")
print("File copied to backup directory")

# Example 2: Moving and renaming files
print("\n=== MOVING AND RENAMING FILES ===")

# Rename a file
os.rename("copy.txt", "renamed.txt")
print("File renamed")

# Move a file
if not os.path.exists("storage"):
    os.mkdir("storage")
shutil.move("renamed.txt", "storage/")
print("File moved to storage directory")

# Example 3: Deleting files
print("\n=== DELETING FILES ===")

# Delete a file
if os.path.exists("copy_with_metadata.txt"):
    os.remove("copy_with_metadata.txt")
    print("File deleted")

# Delete empty directory
if os.path.exists("empty_dir"):
    os.mkdir("empty_dir")  # Create it first
    os.rmdir("empty_dir")
    print("Empty directory deleted")

# Example 4: Working with directories
print("\n=== WORKING WITH DIRECTORIES ===")

# Create a directory with files
if not os.path.exists("test_dir"):
    os.mkdir("test_dir")
with open("test_dir/file1.txt", "w") as f:
    f.write("content")
with open("test_dir/file2.txt", "w") as f:
    f.write("content")

# Copy entire directory
shutil.copytree("test_dir", "test_dir_backup")
print("Directory copied")

# Remove entire directory (with contents)
shutil.rmtree("test_dir_backup")
print("Directory removed")

# Example 5: Practical example - backup system
print("\n=== PRACTICAL EXAMPLE - BACKUP SYSTEM ===")

# Create some files to backup
if not os.path.exists("documents"):
    os.mkdir("documents")
with open("documents/report.txt", "w") as f:
    f.write("Important report content")
with open("documents/data.xlsx", "w") as f:
    f.write("Fake Excel content")

# Create backup
if not os.path.exists("backups"):
    os.mkdir("backups")
    
# Create backup with timestamp
import datetime
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_name = f"backup_{timestamp}"
shutil.copytree("documents", f"backups/{backup_name}")
print(f"Backup created: {backup_name}")

# List all backups
print("Available backups:")
for item in os.listdir("backups"):
    if os.path.isdir(os.path.join("backups", item)):
        print(f"  {item}")

"""
Key Points:
- shutil.copy() copies files
- shutil.copy2() copies files with metadata
- os.rename() renames or moves files
- shutil.move() moves files or directories
- os.remove() deletes files
- os.rmdir() deletes empty directories
- shutil.rmtree() deletes directories with contents
- shutil.copytree() copies entire directories
"""
