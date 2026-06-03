# """
# ╔════════════════════════════════════════════════════════════════════════════╗
# ║                        LOOPS - COMPLETE GUIDE                             ║
# ║            Learn For and While Loops with Detailed Examples               ║
# ╚════════════════════════════════════════════════════════════════════════════╝
# """

# # ═════════════════════════════════════════════════════════════════════════════
# # 1. WHAT ARE LOOPS?
# # ═════════════════════════════════════════════════════════════════════════════
# """
# LOOPS are used to repeat code multiple times:
#     • FOR LOOP: Used when you KNOW how many times to repeat
#     • WHILE LOOP: Used when you repeat UNTIL a condition becomes FALSE
    
# WHY USE LOOPS?
#     • Avoid repeating the same code many times
#     • Process each item in a list
#     • Keep asking for input until user provides correct answer
#     • Count or calculate multiple values
    
# TYPES OF LOOPS:
#     1. FOR LOOP: "Repeat this 10 times" or "For each item in list"
#     2. WHILE LOOP: "Keep repeating while this is TRUE"
# """

# print("╔════════════════════════════════════════════════════════════════════════╗")
# print("║                    SECTION 1: FOR LOOPS                                ║")
# print("╚════════════════════════════════════════════════════════════════════════╝\n")

# # ═════════════════════════════════════════════════════════════════════════════
# # 1. FOR LOOP - Looping a Fixed Number of Times
# # ═════════════════════════════════════════════════════════════════════════════
# """
# FOR LOOP with RANGE:
#     Syntax:
#         for variable in range(start, end, step):
#             # Code to repeat
    
#     • range(10): Numbers 0 to 9 (10 times)
#     • range(1, 11): Numbers 1 to 10
#     • range(0, 10, 2): Numbers 0, 2, 4, 6, 8 (step by 2)
    
#     WHY?
#     • Know exactly how many times to repeat
#     • Count from one number to another
# """

# print("1. FOR LOOP WITH RANGE - Repeat a Fixed Number of Times")
# print("-" * 60)

# # Example 1: Print numbers 0 to 9
# print("Print numbers 0 to 9:")
# for number in range(10):
#     print(number, end=" ")
# print("\n")

# # Example 2: Print numbers 1 to 5
# print("Print numbers 1 to 5:")
# for number in range(1, 6):
#     print(number, end=" ")
# print("\n")

# # Example 3: Count by 2 (0, 2, 4, 6, 8)
# print("Count by 2s (0 to 8):")
# for number in range(0, 10, 2):
#     print(number, end=" ")
# print("\n")

# # Example 4: Countdown from 5 to 1
# print("Countdown from 5 to 1:")
# for number in range(5, 0, -1):
#     print(number, end=" ")
# print("\n")
# print()

# # Example 5: Print a multiplication table
# print("Multiplication Table of 5:")
# for number in range(1, 11):
#     result = 5 * number
#     print(f"5 × {number} = {result}")

# print("\n")

# # Example 6: Print a pattern
# print("Print a star pattern:")
# for row in range(1, 6):
#     stars = "*" * row
#     print(stars)

# print("\n")

# # ═════════════════════════════════════════════════════════════════════════════
# # 2. FOR LOOP - Looping Through a List
# # ═════════════════════════════════════════════════════════════════════════════
# """
# FOR LOOP WITH LIST:
#     Syntax:
#         for item in list:
#             # Code to process each item
    
#     • Visit each element one by one
#     • item gets the current element
#     • Good for processing collections
# """

# print("╔════════════════════════════════════════════════════════════════════════╗")
# print("║           SECTION 2: FOR LOOP - LOOPING THROUGH LISTS                 ║")
# print("╚════════════════════════════════════════════════════════════════════════╝\n")

# print("2. FOR LOOP WITH LISTS")
# print("-" * 60)

# # Example 1: Loop through fruits
# print("Loop through a list of fruits:")
# fruits = ["apple", "banana", "orange", "mango"]
# for fruit in fruits:
#     print(f"I like {fruit}")

# print()

# # Example 2: Loop through numbers and do something
# print("Loop through numbers and multiply by 2:")
# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     doubled = number * 2
#     print(f"{number} × 2 = {doubled}")

# print()

# # Example 3: Loop through students and print roll numbers
# print("Student Roll Numbers:")
# students = ["Ali", "Bhavna", "Chirag", "Deepa", "Eshaan"]
# for index in range(len(students)):
#     roll_number = index + 1
#     student_name = students[index]
#     print(f"Roll {roll_number}: {student_name}")

# print()

# # Example 4: Loop through and find total sum
# print("Calculate total sum of prices:")
# prices = [100, 250, 150, 300, 200]
# total = 0
# for price in prices:
#     total = total + price
#     print(f"Added ${price}, Running total: ${total}")
# print(f"Final total: ${total}")

# print()

# # Example 5: Loop through strings (each character)
# print("Loop through word characters:")
# word = "HELLO"
# for letter in word:
#     print(f"Letter: {letter}")

# print("\n")

# # ═════════════════════════════════════════════════════════════════════════════
# # 3. FOR LOOP - Using enumerate() to get index and item
# # ═════════════════════════════════════════════════════════════════════════════
# """
# ENUMERATE:
#     Gives both the index (position) AND the item
    
#     Syntax:
#         for index, item in enumerate(list):
#             # index = position (0, 1, 2...)
#             # item = the actual element
# """

# print("╔════════════════════════════════════════════════════════════════════════╗")
# print("║        SECTION 3: FOR LOOP - Using enumerate()                         ║")
# print("╚════════════════════════════════════════════════════════════════════════╝\n")

# print("3. USING enumerate() - Get Both Index and Item")
# print("-" * 60)

# # Example 1: Get both index and fruit
# print("Get index and fruit:")
# fruits = ["apple", "banana", "orange", "mango"]
# for index, fruit in enumerate(fruits):
#     print(f"Position {index}: {fruit}")

# print()

# Example 2: Create a menu with numbers
# print("Menu with numbers:")
# menu_items = ["Pizza", "Burger", "Fries", "Shake", "Salad"]
# for position, item in enumerate(menu_items, start=1):  # start=1 starts counting from 1
#     print(f"{position}. {item}")

# print()

# # Example 3: Check if item is at the end
# print("Mark the last item:")
# colors = ["Red", "Green", "Blue", "Yellow"]
# for index, color in enumerate(colors):
#     if index == len(colors) - 1:
#         print(f"• {color} (This is the last one!)")
#     else:
#         print(f"• {color}")

# print("\n")

# # ═════════════════════════════════════════════════════════════════════════════
# # 4. FOR LOOP WITH DICTIONARIES
# # ═════════════════════════════════════════════════════════════════════════════
# """
# LOOP THROUGH DICTIONARIES:
    
#     for key in dictionary:          # Gets only keys
#     for value in dictionary.values(): # Gets only values
#     for key, value in dictionary.items(): # Gets both
# """

# print("╔════════════════════════════════════════════════════════════════════════╗")
# print("║           SECTION 4: FOR LOOP - LOOPING THROUGH DICTIONARIES           ║")
# print("╚════════════════════════════════════════════════════════════════════════╝\n")

# print("4. FOR LOOP WITH DICTIONARIES")
# print("-" * 60)

# # Example 1: Loop through dictionary keys
# print("Loop through dictionary keys only:")
#student_marks = {"Ali": 85, "Bhavna": 90, "Chirag": 78}
# for name in student_marks:
#     print(f"Name: {name}")

# print()

# # Example 2: Loop through values only
# print("Loop through values only:")
# for marks in student_marks.values():
#     print(f"Marks: {marks}")

# print()

# # Example 3: Loop through both keys and values
# print("Loop through both keys and values:")
# for name, marks in student_marks.items():
#     print(f"{name} scored {marks} marks")

# print()

# # Example 4: Dictionary of items and prices
# print("Store inventory:")
# inventory = {"apples": 50, "bananas": 30, "oranges": 45, "mangoes": 20}
# total_items = 0
# for item, quantity in inventory.items():
#     total_items = total_items + quantity
#     print(f"{item}: {quantity} units")
# print(f"Total items in stock: {total_items}")

# print("\n")
# a = list(map(int,input().split()))
# p = 0
# for i in a:
#     p += i
# print(p)

# nums = list(map(int, input().split()))
# even = []
# odd = []
# for i in nums:
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even numbers:",len(even))
# print("Odd numbers:",len(odd))

# a = eval(input())
# for i in a:
#     print(i, a[i])
# for i in d.values():#d.keys()#d.items()

# a = eval(input())
# b = 0
# for i in a.values():
#     b += i
# print(b)

# a = eval(input())[1,2,3,4]
# b = 0
# c = 0
# for i in a:
#     b += a[i]
# c += 1
# if b//c > 90:
#     print("A")
# elif b//c > 70:
#     print("B")
# elif b//c > 50:
#     print("C")
# else:
#     print("D")

