#output formatting:
'''
-There are multiple ways for printing the output in a formatted way
-we can give multiple odjects to print function, it generatesba new string by adding spaces between
 those objects by default
'''
# 1) comma based formatting
# a = 10
# b = 'python'
# print(str(a)+b)

# Area of the square : <ans>
# a = int(input())
# b = a*a
# print(f"Area of the square: {b}")
# print("Area of the square: {}".format(b))
# print("Area of the square:",b)

#2) % - operator based formatting
# %d - int
# %f - float
# %.nf - rounded float to n digits after decimal point
#1.23456
# %s - string

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# string = 'This is %s. They are %d years old.' %(name, age)
# print(f"This is {name}. They are {age} years old.")
# print("This is {}. They are {} years old.".format(name,age))
# print(string)

# d = 12.3468
# print("%.2f"%(d)) #12.35

# r = float(input())
# pi = 3.14
# area = pi*r**2
# print("Area: %.3f"%(area))

# # 3) formatted string literals
'''
-We mention f at the beginning of the string and placeholders with variables or simple expressions
 inside the string. The f at the beginning indicates that it is not a direct string literal and the
 curly brackets should be considered as place holder'''
# name = input()
# age = int(input())
# print(f"This is {name}. They are {age} years old.")

# a = 56
# b = 10
# print(f"sum of a and b is {a+b}")

#4) format method in string class
'''
This is method present in the string class
We call this function on a string object which has place holders
We pass the values that have to be embedded inside the string to the function as arguments in proper order
'''
# name = input()
# age = int(input())
# print("This is {}. They are {} years old.".format(name, age))