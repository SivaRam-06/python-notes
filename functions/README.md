# Functions in Python - Complete Guide

## What is a Function?
A function is a block of reusable code that performs a specific task. Instead of writing the same code multiple times, you define it once and call it whenever needed.

---

## Why Use Functions?
✅ **Reusability** - Write once, use many times
✅ **Modularity** - Organize code into logical parts
✅ **Maintainability** - Easier to update and fix
✅ **Readability** - Code becomes cleaner and easier to understand

---

## Files in This Folder

### 1. **function_basics.py**
   - How to define a function
   - How to call a function
   - Function structure and syntax

### 2. **parameters_and_arguments.py**
   - Positional parameters
   - Keyword parameters
   - Difference between parameters and arguments

### 3. **return_values.py**
   - Returning single values
   - Returning multiple values
   - Return vs Print

### 4. **default_parameters.py**
   - Setting default values for parameters
   - When to use default parameters
   - Overriding defaults

### 5. **variable_length_arguments.py**
   - *args (non-keyword variable length arguments)
   - **kwargs (keyword variable length arguments)
   - Using both together

### 6. **scope.py**
   - Local scope
   - Global scope
   - function scope vs global scope conflicts

### 7. **types_of_functions.py**
   - Different categories of functions
   - Built-in vs user-defined functions
   - Lambda, recursive, nested functions
   - Higher-order functions and generators
   - Closures and decorators
   - When to use each type

### 8. **lambda_functions.py**
   - Anonymous functions
   - When to use lambda
   - Lambda with map, filter, sort

### 9. **built_in_functions.py**
   - Common Python built-in functions
   - How and when to use them
   - Examples and practical use cases

### 10. **function_recursion.py**
   - Recursive functions
   - Base case and recursive case
   - Examples: factorial, fibonacci

### 11. **tips_and_best_practices.py**
   - Tips for writing good functions
   - Common mistakes and how to fix them
   - Debugging techniques
   - Performance optimization
   - Function design principles

---

## Basic Function Syntax

```python
def function_name(parameters):
    """Docstring explaining what the function does"""
    # Function body
    code_here
    return result
```

---

## Quick Example

```python
# Define
def greet(name):
    return f"Hello, {name}!"

# Call
print(greet("Alex"))  # Output: Hello, Alex!
```

---

## Key Concepts to Master
1. Define and call functions
2. Work with parameters
3. Return values
4. Handle multiple arguments (*args, **kwargs)
5. Understand scope
6. Use lambda functions
7. Know built-in functions
8. Write recursive functions

---

**Start with function_basics.py and go through each file in order!**
