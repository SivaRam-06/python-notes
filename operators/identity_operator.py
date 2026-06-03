# Identity operators
'''
These are used to check whether two variables refer to the same object in memory.

The identity operators are:
    -is - returns True if both variables refer to the same object
    -is not - returns True if both variables do not refer to the same object
'''
#Working of 'is' operator:
'''
If both variables point to the same object in memory, 'is' returns True otherwise False.

example:
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a is b)  # Output: False
    id(a)  # Output: Memory address of a
    id(b)  # Output: Memory address of b (same as a)
    print(id(a))
    print(id(b))
example 2:
    a = 10
    b = 10
    print(a is b)  # Output: True
    id(a)  # Output: Memory address of a
    id(b)  # Output: Memory address of b (same as a)
    print(id(a))
    print(id(b))
'''
#working of 'is not' operator:
'''
If both variables point to different objects in memory, 'is not' returns True otherwise False.

example:
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a is not b)  # Output: True
    id(a)  # Output: Memory address of a
    id(b)  # Output: Memory address of b (different from a)
    print(id(a))
    print(id(b))
example 2:
    a = 10
    b = 10
    print(a is not b)  # Output: False
    id(a)  # Output: Memory address of a
    id(b)  # Output: Memory address of b (same as a)
    print(id(a))
    print(id(b))
'''
#where to use identity operators in the programs?
'''
> used to compare memory locations of two objects
'''
#how to identify identity operators are usedin the programs?
'''
> by looking for the presence of keywords 'is' and 'is not' in the code
'''