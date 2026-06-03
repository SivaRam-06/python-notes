# Logical operators
'''
These are special keywords working with boolean operands and they work
according to their respective logic gates.
'''
#AND operator(and):
'''
 - operand1      operand2        result

   True          True            True
   True          False           False
   False         True            False
   False         False           False
'''
#OR operator(or):
'''
- operand1      operand2        result

   True          True            True
   True          False           True
   False         True            True
   False         False           False
'''
#NOT operator(not):
'''
- operand       result

   True          False
   False         True
'''
#check weather the given number is in the range of 100 to 200 both inclusive.
#Output should be True or False.
num = int(input("Enter the number: "))
print(num>=100 and num<=200)
#where to use logical operators in the programs?
'''
> used to combine multiple boolean expressions and make decisions based on their truth values
'''
#how to identify logical operators are usedin the programs?
'''
> by looking for the presence of keywords 'and', 'or', and 'not' in the code
'''