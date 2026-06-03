# """
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# """

# x="*"
# for i in range(5):
#     print(" "*(5-i-1)*2,end="")
#     for j in range(i+1):
#          print(x,end=" ")

#     print()


# # for i in range(5):
# #     print(" "*(5-i-1)*2,end="")
# #     print("* "*(i+1))


# """
# * * * * * 
#   * * * *
#     * * *
#       * *
#         *
# """

# for i in range(5,0,-1):
#      print(" "*(5-i+1)*2,end="")
#      print("* "*(i-1))



# x=1
# for i in range(5,0,-1):
#      print(" "*(5-i+1)*2,end="")
#      for j in range(i):
#           print("*",end=" ")
#      print()
     

# '''
#         * 
#       * * 
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
# '''

# """
# 1 2 3 4 5
# 2 3 4 5 1
# 3 4 5 1 2 
# 4 5 1 2 3
# 5 1 2 3 4

# """


for i in range(1,6):
     
     for j in range(i,i+5):
          if j<=5:
               print(j,end="*")
          elif j>5:   
               print(j-5,end="*")
      
     print()

"""
1*2*3*4*5*
1*2*3*4*5*
1*2*3*4*5*
1*2*3*4*5*
1*2*3*4*5*
"""
x=1
for i in range(5):
     for j in range(5):
          print(x,end="*")
          x+=1
     print()
     x=1

"""
1*2*3*4*5
1*2*3*4*5
1*2*3*4*5
1*2*3*4*5
1*2*3*4*5
"""
for i in range(5):
     x=1
     a=""
     for j in range(5):
          a+=str(x)+"*"
          
          x+=1
     print(a.rstrip("*"))


x=1
rows=int(input("enter no of rows "))
columns= int(input("enter no-of cols "))
for i in range(rows):
     for j in range(columns):
          print(x,end=" ")
          x+=1
     print()
