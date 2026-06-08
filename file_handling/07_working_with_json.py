# file_handling/07_working_with_json.py
"""
WORKING WITH JSON FILES
=======================

What is it?
-----------
JSON (JavaScript Object Notation) is a lightweight data format for storing
and exchanging data.

When to use it?
---------------
Use JSON files when you need to:
1. Store structured data
2. Exchange data between applications
3. Save configuration settings
4. Work with web APIs

How to identify it?
-------------------
Look for json module and .json file extensions.
"""

import json

# Example 1: Writing JSON files
print("=== WRITING JSON FILES ===")

# Data to write (Python dictionary)
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "photography"],
    "is_student": False
}

# Write to JSON file
with open("person.json", "w") as file:
    json.dump(data, file, indent=4)  # indent for pretty formatting
    print("JSON file created")

# Example 2: Reading JSON files
print("\n=== READING JSON FILES ===")

# Read from JSON file
with open("person.json", "r") as file:
    loaded_data = json.load(file)
    print("Loaded data:")
    print(json.dumps(loaded_data, indent=2))  # Pretty print

# Example 3: Working with complex data
print("\n=== WORKING WITH COMPLEX DATA ===")

# List of dictionaries
people = [
    {"name": "John Doe", "age": 30, "city": "New York"},
    {"name": "Jane Smith", "age": 25, "city": "London"},
    {"name": "Bob Johnson", "age": 35, "city": "Paris"}
]

# Write list to JSON
with open("people.json", "w") as file:
    json.dump(people, file, indent=4)
    print("JSON file with array created")

# Read list from JSON
with open("people.json", "r") as file:
    loaded_people = json.load(file)
    for person in loaded_people:
        print(f"{person['name']} from {person['city']}")

# Example 4: JSON strings and Python objects
print("\n=== JSON STRINGS AND PYTHON OBJECTS ===")

# Convert Python object to JSON string
json_string = json.dumps(data, indent=2)
print("JSON string:")
print(json_string)

# Convert JSON string to Python object
python_object = json.loads(json_string)
print("Python object:")
print(python_object)

# Example 5: Practical example - configuration file
print("\n=== PRACTICAL EXAMPLE - CONFIGURATION FILE ===")

# Create configuration
config = {
    "app_name": "My Application",
    "version": "1.0.0",
    "settings": {
        "theme": "dark",
        "language": "en",
        "notifications": True
    },
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb"
    }
}

# Save configuration
with open("config.json", "w") as file:
    json.dump(config, file, indent=4)
    print("Configuration file saved")

# Load configuration
with open("config.json", "r") as file:
    loaded_config = json.load(file)
    print(f"App: {loaded_config['app_name']} v{loaded_config['version']}")
    print(f"Database: {loaded_config['database']['host']}:{loaded_config['database']['port']}")

"""
Key Points:
- json.dump() writes Python objects to JSON files
- json.load() reads JSON files into Python objects
- json.dumps() converts Python objects to JSON strings
- json.loads() converts JSON strings to Python objects
- Use indent parameter for pretty formatting
- JSON supports strings, numbers, booleans, arrays, and objects
"""
