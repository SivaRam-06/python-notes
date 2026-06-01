#Single line comment

"""
Multiline comment.
"""

'''
This is also a multiline comment.
'''

'''
1.Numeric category:
    a)int = 3,-9,45
    b)float = 38.5,-9.54321
    c)complex = 2+5j,-9+52j
    
2.Sequence category:
    a)str = "abc12&"
    b)list = [2,"python",4.54]
    c)tuple = (1,2,3)

3.Unordered category:
    a)set = {1,2,3}

4.Mapping category:
    a)dict = {'name':'siva_ram',
              'email':'siva@gmail.com'}

5.Boolean: True, False
'''

# Variable: variables are like a containers for the storing values
'''
-Rules for naming variables in python:
    1)Name should contain either an alphabet or a digit or an underscore.
    2)The first character can never be a digit.
    3)keywords or reserved words cannot be used as variable names.

-Note:Python is case-sensitive . while accessing variable, we need to use
      proper case that was used when we have defined the variable.

-Common mistakes made in the declaration of the variable.
    1)var name
    2)2var1
    3)siva$@!ram
    4)for


#Re-assignment of the variable.
v = 50
print(v)

v = "python"
print(v)

#Multiple assignments in a single line.
a = 5
b = 10

a,b,c= 5,10,15
print(a+b+c)

#Swapping of the variables(inter-changing of the values).
a = 5
b = 10
print("Before swapping:",a,b)

a,b = b,a
print("After swapping:",a,b)

#Deleting a variable.
a = "python"
del a
print(a) '''

#swapping without using third variable
x=5
y=6
x=x+y # x=11
y=x-y # y=5
x=x-y # x=6
print(x,y)