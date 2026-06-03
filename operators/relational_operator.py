# Relational operators:
'''
-These operators are used for comparision of two values.
-They return boolean True or False based on the comparisions we do.

- Symbol            - Operation

    >                 Greater than
    >=                Greater than or equal to
    <                 Less than
    <=                Less than or equal to
    ==                Is equal to
    !=                Not equal to
'''
#example:
'''
a = 30
b = 40
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)
'''
#You are given the details about the workout of the two persons.
#The input is given in the hours calculate the total time spent.
#On workout by both in minutes.
#Check if person A has worked out more than person B
'''
person_a = int(input("Workout of the person A : "))
person_b = int(input("Workout of the person B : "))
total = person_a+person_b
total_min = total*60
print("Total time spent: ",total_min)
print(person_a>person_b)
'''

#You will be given dimensions of two squares as two lines of input.
#check if the first square can fit in the second square.
#Output should be True or False
s1 = int(input())
s2 = int(input())
print(s1 < s2)

#where to use relational operators in the programs?
'''
> used to compare two values and make decisions based on their relationship
'''
#how to identify relational operators are usedin the programs?
'''
> by looking for the presence of symbols like >, >=, <, <=, ==, != in the code
'''