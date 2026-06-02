# ================== INPUT FORMATTING ==================

'''
- In Python, input is taken using the input() function
- By default, input() returns data as a string
- We need to convert it into required data types like int, float, etc.
'''

# 1) Basic input (string input)
# name = input()
# print(name)

# 2) Taking integer input
# a = int(input())
# print(a)

# 3) Taking float input
# x = float(input())
# print(x)

# 4) Taking multiple inputs in one line
'''
- split() is used to separate input values (default separator is space)
- map() is used to apply a function (like int/float) to all elements
'''

# a, b = map(int, input().split())
# print(a, b)

# 5) Taking list input
'''
- Convert input into list using split()
- Use map() if elements need to be integers
'''

# arr = list(map(int, input().split()))
# print(arr)

# 6) Taking string list
# words = input().split()
# print(words)

# 7) Taking multiple lines input
'''
- Use loop to take multiple inputs
'''

# n = int(input())
# arr = []
# for i in range(n):
#     x = int(input())
#     arr.append(x)
# print(arr)

# 8) Taking matrix input
'''
- Nested list using loops
'''

# rows = int(input())
# cols = int(input())
# matrix = []
# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)
# print(matrix)

# 9) Taking input with prompt message
# name = input("Enter your name: ")
# print(name)

# 10) Reading full line (including spaces)
'''
- input() already reads full line as string
'''

# sentence = input()
# print(sentence)

# ================== IMPORTANT NOTES ==================

'''
- input() always returns string → convert when needed
- Use int(), float() for conversion
- Use split() for multiple inputs
- Use map() for applying type conversion efficiently
'''
# input function
# > It helps to take input from the user 
# we can give a prompt to this function if necessary and the prompt 
# should be given as a string.
# inp=input(" type here:")
# print(inp)

#type function:

# input fuction always considers the given input as string data type only
#  To use that as a value belonging to some other data type, we need to convert that 
#  Type converision/Type casting:
#  It is coverting  from one data type to other
#  To do type conversion we use the functions with same names as their respective class names
#  Not all conversions are possible,only compatible values can be converted and remaining 
#  conversions throw arrow 

print(type("q"))
print(type(2))
print(type(4.56))
print(type(True))
print(type([43,"srt",3.44,False,"45"]))
print(type((23,"2323","lokesh")))
print(type({"hello",23}))
print(type({"name":"lokesh","rollno":2323}))