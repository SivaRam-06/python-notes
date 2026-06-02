# check whether mutable or immutable.
'''
In Python, data types can be classified into two categories: mutable and immutable.
Mutable data types can be changed after their creation, while immutable data types cannot be changed once they are created.
Here are some common mutable and immutable data types in Python:
'''
#Mutable Data Types:
'''
1. List: Lists are ordered collections of items that can be modified after their creation. You
    can add, remove, or change elements in a list.
    Example: 
    my_list = [1, 2, 3]
    my_list[0] = 10  # Modifying the first element
    print(my_list)  # Output: [10, 2, 3]
2. Dictionary: Dictionaries are collections of key-value pairs that can be modified. You can add,
    remove, or change key-value pairs in a dictionary.
    Example:
    my_dict = {'a': 1, 'b': 2}
    my_dict['a'] = 10  # Modifying the value for key 'a'
    print(my_dict)  # Output: {'a': 10, 'b': 2}
3. Set: Sets are unordered collections of unique items that can be modified. You can add or remove
    elements from a set.
    Example:
    my_set = {1, 2, 3}
    my_set.add(4)  # Adding an element to the set
    print(my_set)  # Output: {1, 2, 3, 4}
'''
#Immutable Data Types:
'''
1. Tuple: Tuples are ordered collections of items that cannot be modified after their creation.
    Example:
    my_tuple = (1, 2, 3)
    # my_tuple[0] = 10  # This will raise a TypeError
    print(my_tuple)  # Output: (1, 2, 3)
2. String: Strings are sequences of characters that cannot be modified after their creation.
    Example:
    my_string = "Hello"
    # my_string[0] = 'h'  # This will raise a TypeError
    print(my_string)  # Output: "Hello"
3. Frozenset: Frozensets are immutable versions of sets. Once created, you cannot add or remove
    elements from a frozenset.
    Example:
    my_frozenset = frozenset([1, 2, 3])
    # my_frozenset.add(4)  # This will raise an AttributeError
    print(my_frozenset)  # Output: frozenset({1, 2, 3})
Understanding the difference between mutable and immutable data types is important for effective programming in Python, as it affects how data is managed and manipulated in your code.
'''
# Example to demonstrate mutable and immutable data types
# Mutable example with list
my_list = [1, 2, 3]
a = 8  # Binary: 010100
result = a >> 3  # Binary: 000101 (Decimal: 5)
print(result) 