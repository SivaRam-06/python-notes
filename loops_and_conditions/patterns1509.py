"""
* 
* *
* * * 
* * * *
* * * * *
"""
x="*"
for i in range(5):  #range(0,5,+1)
    for j in range(i+1): #range(0,i+1,1)
        print(x,end=" ")
    
    print()

"""
1 
2 3
4 5 6 
7 8 9 10
11 12 13 14 15
"""
x=1
for i in range(5):
    for j in range(i+1):
     print(x,end=" ")
     x+=1
    print()

"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""
x=1
for i in range(5):
   for j in range(i+1):
      print(x,end=" ")
   x+=1
   print()


"""
a
b b
c c c
d d d d
e e e e e 

"""
x=97
for i in range(5):
   for j in range(i+1):
      print(chr(x),end=" ")
   x+=1
   print()

"""
a 
b c 
d e f
g h i j
k l m n o
"""
x=97
for i in range(5):
   for j in range(i+1):
      print(chr(x),end=" ")
      x+=1
   print()

"""
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""


for i in range(5):
   x=1
   for j in range(i+1):
      print(x,end=" ")
      x+=1
   print()

'''
a
ab
abc
abcd
abcde
'''
for i in range(5):
   x=97
   for j in range(i+1):
      print(chr(x),end="")
      x+=1
   print()

'''
*  i=0
* * *  i=1
* * * * *  i=2
* * * * * * * i=3
* * * * * * * * * i=4
'''
x="*"
for i in range(5):
   for j in range(2*i+1):
      print(x,end=" ")

   print()

'''
**
****
******
********
**********
'''


