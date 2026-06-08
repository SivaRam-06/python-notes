# file_handling/06_working_with_csv.py
"""
WORKING WITH CSV FILES
======================

What is it?
-----------
CSV (Comma-Separated Values) files store tabular data in plain text.

When to use it?
---------------
Use CSV files when you need to:
1. Store table-like data
2. Exchange data between applications
3. Work with spreadsheet data

How to identify it?
-------------------
Look for csv module and .csv file extensions.
"""

import csv

# Example 1: Writing CSV files
print("=== WRITING CSV FILES ===")

# Data to write
data = [
    ["Name", "Age", "City"],
    ["John Doe", 30, "New York"],
    ["Jane Smith", 25, "London"],
    ["Bob Johnson", 35, "Paris"]
]

# Write to CSV file
with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
    print("CSV file created")

# Example 2: Reading CSV files
print("\n=== READING CSV FILES ===")

# Read from CSV file
with open("people.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Example 3: Working with dictionaries
print("\n=== WORKING WITH DICTIONARIES ===")

# Write using DictWriter
with open("people_dict.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({"Name": "John Doe", "Age": 30, "City": "New York"})
    writer.writerow({"Name": "Jane Smith", "Age": 25, "City": "London"})
    writer.writerow({"Name": "Bob Johnson", "Age": 35, "City": "Paris"})
    print("CSV file with headers created")

# Read using DictReader
with open("people_dict.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old and lives in {row['City']}")

# Example 4: Different delimiters
print("\n=== DIFFERENT DELIMITERS ===")

# Create TSV (Tab-Separated Values) file
with open("people.tsv", "w", newline="") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerows(data)
    print("TSV file created")

# Read TSV file
with open("people.tsv", "r") as file:
    reader = csv.reader(file, delimiter="\t")
    for row in reader:
        print(row)

# Example 5: Practical example - processing CSV data
print("\n=== PRACTICAL EXAMPLE ===")

# Calculate average age from CSV
total_age = 0
count = 0

with open("people.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        if row:  # Skip empty rows
            total_age += int(row[1])
            count += 1

if count > 0:
    average_age = total_age / count
    print(f"Average age: {average_age:.2f}")

"""
Key Points:
- csv.writer() writes data to CSV files
- csv.reader() reads data from CSV files
- csv.DictWriter() writes dictionaries to CSV files
- csv.DictReader() reads CSV files into dictionaries
- Use newline="" when writing to avoid extra blank lines
- You can specify different delimiters for TSV files
"""
