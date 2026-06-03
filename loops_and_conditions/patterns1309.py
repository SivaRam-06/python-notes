"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *  rows= 5   columns=5
"""
x="*"
for  i in range(5):
    for j in range(5):
        print(x ,end=" ")
    print()

"""
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25   r=5  c=5
"""
x=1
for i in range(5):
    for j in range(5):
        print(x,end=" ")
        x+=1
    print()

"""
1 1 1 1 1
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4
5 5 5 5 5
"""
x=1
for i in range(5):
    for j in range(5):
        print(x,end=" ")
    x+=1
    print()

"""
A B C D E 
F G H I J 
K L M N O
P Q R S T
U V W X Y
"""
x=65
for i in range(5):
    for j in range(5):
        print(chr(x),end=" ")
    x+=1
    print()