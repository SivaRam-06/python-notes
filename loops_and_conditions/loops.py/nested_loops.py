# # ═════════════════════════════════════════════════════════════════════════════
# # 6. NESTED LOOPS - Complete Learning Guide with Sample Input/Output
# # ═════════════════════════════════════════════════════════════════════════════
# """
# NESTED LOOPS:
#     • A loop inside another loop (outer loop contains inner loop)
#     • Inner loop repeats completely for each outer loop iteration
#     • Perfect for processing 2D data (matrices, tables, grids)
#     • Each example shows: Input → Iterations → Output
# """

# print("╔════════════════════════════════════════════════════════════════════════╗")
# print("║         NESTED LOOPS - COMPLETE GUIDE WITH ITERATION TRACKING        ║")
# print("╚════════════════════════════════════════════════════════════════════════╝\n")


# # ═════════════════════════════════════════════════════════════════════════════
# # EXAMPLE 1: MULTIPLICATION TABLE
# # ═════════════════════════════════════════════════════════════════════════════
# print("\n" + "="*60)
# print("EXAMPLE 1️⃣  - MULTIPLICATION TABLE")
# print("="*60)

# print("\n📝 SAMPLE INPUT:")
# print("   Create multiplication table for 1-3")

# print("\n💻 CODE WITH ITERATION TRACKING:")
# print("""
# for row in range(1, 4):          # row: 1, 2, 3 (3 iterations)
#     for col in range(1, 4):      # col: 1, 2, 3 (3 iterations per row)
#         result = row * col
#         print(f"{result:3d}", end=" ")
#     print()
# """)

# print("📊 OUTPUT (Actual Execution):")
# print("Iteration breakdown:")
# print("  Row 1: 1×1=1  | 1×2=2  | 1×3=3")
# print("  Row 2: 2×1=2  | 2×2=4  | 2×3=6")
# print("  Row 3: 3×1=3  | 3×2=6  | 3×3=9")
# print("\nResult:")
# for row in range(1, 4):
#     for col in range(1, 4):
#         result = row * col
#         print(f"{result:3d}", end=" ")
#     print()


# # ═════════════════════════════════════════════════════════════════════════════
# # EXAMPLE 2: PRINT SQUARE PATTERN
# # ═════════════════════════════════════════════════════════════════════════════
# print("\n" + "="*60)
# print("EXAMPLE 2️⃣  - PRINT SQUARE PATTERN WITH STARS")
# print("="*60)

# print("\n📝 SAMPLE INPUT:")
# print("   Create 4×4 square pattern")

# print("\n💻 CODE WITH ITERATION TRACKING:")
# print("""
# for row in range(1, 5):          # row: 1, 2, 3, 4 (4 rows)
#     for col in range(1, 5):      # col: 1, 2, 3, 4 (4 columns per row)
#         print("*", end=" ")      # print star
#     print()                        # new line after each row
# """)

# print("📊 OUTPUT (Actual Execution):")
# print("Iteration breakdown:")
# print("  Row 1: * in columns 1,2,3,4")
# print("  Row 2: * in columns 1,2,3,4")
# print("  Row 3: * in columns 1,2,3,4")
# print("  Row 4: * in columns 1,2,3,4")
# print("\nResult:")
# for row in range(1, 5):
#     for col in range(1, 5):
#         print("*", end=" ")
#     print()


# # ═════════════════════════════════════════════════════════════════════════════
# # EXAMPLE 3: TRIANGLE PATTERN
# # ═════════════════════════════════════════════════════════════════════════════
# print("\n" + "="*60)
# print("EXAMPLE 3️⃣  - PRINT TRIANGLE PATTERN")
# print("="*60)

# print("\n📝 SAMPLE INPUT:")
# print("   Create 5-row triangle (row n has n stars)")

# print("\n💻 CODE WITH ITERATION TRACKING:")
# print("""
# for row in range(1, 6):          # row: 1, 2, 3, 4, 5 (5 rows)
#     for col in range(1, row+1):  # col: 1 to row (increases with each row)
#         print("*", end=" ")
#     print()
# """)

# print("📊 OUTPUT (Actual Execution):")
# print("Iteration breakdown:")
# print("  Row 1: 1 star   (col 1 to 1)")
# print("  Row 2: 2 stars  (col 1 to 2)")
# print("  Row 3: 3 stars  (col 1 to 3)")
# print("  Row 4: 4 stars  (col 1 to 4)")
# print("  Row 5: 5 stars  (col 1 to 5)")
# print("\nResult:")
# for row in range(1, 6):
#     for col in range(1, row+1):
#         print("*", end=" ")
#     print()


# # ═════════════════════════════════════════════════════════════════════════════
# # EXAMPLE 4: PRINT 2D LIST (MATRIX)
# # ═════════════════════════════════════════════════════════════════════════════
# print("\n" + "="*60)
# print("EXAMPLE 4️⃣  - PRINT 2D LIST (MATRIX)")
# print("="*60)

# print("\n📝 SAMPLE INPUT:")
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print("   matrix =", matrix)

# print("\n💻 CODE WITH ITERATION TRACKING:")
# print("""
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in range(len(matrix)):         # i: 0, 1, 2 (3 rows)
#     for j in range(len(matrix[i])):  # j: 0, 1, 2 (3 columns per row)
#         print(f"{matrix[i][j]:4d}", end=" ")
#     print()
# """)

# print("📊 OUTPUT (Actual Execution):")
# print("Iteration breakdown:")
# print("  i=0: Access matrix[0][0]=1, matrix[0][1]=2, matrix[0][2]=3")
# print("  i=1: Access matrix[1][0]=4, matrix[1][1]=5, matrix[1][2]=6")
# print("  i=2: Access matrix[2][0]=7, matrix[2][1]=8, matrix[2][2]=9")
# print("\nResult:")
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(f"{matrix[i][j]:4d}", end=" ")
#     print()


# # ═════════════════════════════════════════════════════════════════════════════
# # EXAMPLE 5: SUM ALL ELEMENTS IN MATRIX
# # ═════════════════════════════════════════════════════════════════════════════
# print("\n" + "="*60)
# print("EXAMPLE 5️⃣  - CALCULATE SUM OF ALL MATRIX ELEMENTS")
# print("="*60)

# print("\n📝 SAMPLE INPUT:")
# matrix = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]
# print("   matrix =", matrix)

# print("\n💻 CODE WITH ITERATION TRACKING:")
# print("""
# matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# total = 0

# for i in range(len(matrix)):         # i: 0, 1, 2
#     for j in range(len(matrix[i])):  # j: 0, 1, 2
#         total += matrix[i][j]
#         # Print each iteration
#         print(f"Add {matrix[i][j]} → Total = {total}")

# print(f"Final sum: {total}")
# """)

# print("📊 OUTPUT (Actual Execution):")
# total = 0
# iteration = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         iteration += 1
#         total += matrix[i][j]
#         print(f"  Iteration {iteration}: Add {matrix[i][j]:2d} → Total = {total:3d}")

# print(f"\nFinal sum: {total}")


# # ═════════════════════════════════════════════════════════════════════════════
# # EXAMPLE 6: SUM EACH ROW
# # ═════════════════════════════════════════════════════════════════════════════
# print("\n" + "="*60)
# print("EXAMPLE 6️⃣  - CALCULATE SUM OF EACH ROW")
# print("="*60)

# print("\n📝 SAMPLE INPUT:")
# matrix = [
#     [5, 10, 15],
#     [20, 25, 30],
#     [35, 40, 45]
# ]
# print("   matrix =", matrix)

# print("\n💻 CODE WITH ITERATION TRACKING:")
# print("""
# matrix = [[5, 10, 15], [20, 25, 30], [35, 40, 45]]

# for row_idx in range(len(matrix)):              # row_idx: 0, 1, 2
#     row_sum = 0
#     print(f"Row {row_idx}: ", end="")
#     for col_idx in range(len(matrix[row_idx])): # col_idx: 0, 1, 2
#         row_sum += matrix[row_idx][col_idx]
#         print(f"{matrix[row_idx][col_idx]}", end=" ")
#         if col_idx < len(matrix[row_idx]) - 1:
#             print("+", end=" ")
#     print(f" = {row_sum}")
# """)

# print("📊 OUTPUT (Actual Execution):")
# for row_idx in range(len(matrix)):
#     row_sum = 0
#     print(f"Row {row_idx}: ", end="")
#     for col_idx in range(len(matrix[row_idx])):
#         row_sum += matrix[row_idx][col_idx]
#         print(f"{matrix[row_idx][col_idx]}", end=" ")
#         if col_idx < len(matrix[row_idx]) - 1:
#             print("+", end=" ")
#     print(f" = {row_sum}")


# # ═════════════════════════════════════════════════════════════════════════════
# # EXAMPLE 7: SUM EACH COLUMN
# # ═════════════════════════════════════════════════════════════════════════════
# print("\n" + "="*60)
# print("EXAMPLE 7️⃣  - CALCULATE SUM OF EACH COLUMN")
# print("="*60)

# print("\n📝 SAMPLE INPUT:")
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print("   matrix =", matrix)

# print("\n💻 CODE WITH ITERATION TRACKING:")
# print("""
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # Number of columns = len(matrix[0])
# for col_idx in range(len(matrix[0])):        # col_idx: 0, 1, 2
#     col_sum = 0
#     print(f"Column {col_idx}: ", end="")
#     for row_idx in range(len(matrix)):       # row_idx: 0, 1, 2
#         element = matrix[row_idx][col_idx]
#         col_sum += element
#         print(f"{element}", end=" ")
#         if row_idx < len(matrix) - 1:
#             print("+", end=" ")
#     print(f" = {col_sum}")
# """)

# print("📊 OUTPUT (Actual Execution):")
# for col_idx in range(len(matrix[0])):
#     col_sum = 0
#     print(f"Column {col_idx}: ", end="")
#     for row_idx in range(len(matrix)):
#         element = matrix[row_idx][col_idx]
#         col_sum += element
#         print(f"{element}", end=" ")
#         if row_idx < len(matrix) - 1:
#             print("+", end=" ")
#     print(f" = {col_sum}")


# # ═════════════════════════════════════════════════════════════════════════════
# # EXAMPLE 8: FIND MAXIMUM ELEMENT
# # ═════════════════════════════════════════════════════════════════════════════
# print("\n" + "="*60)
# print("EXAMPLE 8️⃣  - FIND MAXIMUM ELEMENT IN MATRIX")
# print("="*60)

# print("\n📝 SAMPLE INPUT:")
# matrix = [
#     [15, 30, 20],
#     [50, 10, 45],
#     [25, 60, 35]
# ]
# print("   matrix =", matrix)

# print("\n💻 CODE WITH ITERATION TRACKING:")
# print("""
# matrix = [[15, 30, 20], [50, 10, 45], [25, 60, 35]]
# max_element = matrix[0][0]

# for i in range(len(matrix)):         # i: 0, 1, 2
#     for j in range(len(matrix[i])):  # j: 0, 1, 2
#         if matrix[i][j] > max_element:
#             print(f"Found {matrix[i][j]} > {max_element}")
#             max_element = matrix[i][j]

# print(f"Maximum: {max_element}")
# """)

# print("📊 OUTPUT (Actual Execution):")
# max_element = matrix[0][0]
# print(f"Starting max: {max_element}\n")
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] > max_element:
#             print(f"  [Iteration {i},{j}] Found {matrix[i][j]} > {max_element}")
#             max_element = matrix[i][j]

# print(f"\nMaximum element: {max_element}")


# # ═════════════════════════════════════════════════════════════════════════════
# # EXAMPLE 9: SEARCH FOR ELEMENT
# # ═════════════════════════════════════════════════════════════════════════════
# print("\n" + "="*60)
# print("EXAMPLE 9️⃣  - SEARCH FOR ELEMENT IN MATRIX")
# print("="*60)

# print("\n📝 SAMPLE INPUT:")
# matrix = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]
# search_value = 50
# print("   matrix =", matrix)
# print(f"   search_value = {search_value}")

# print("\n💻 CODE WITH ITERATION TRACKING:")
# print("""
# matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# search_value = 50
# found = False

# for i in range(len(matrix)):         # i: 0, 1, 2
#     for j in range(len(matrix[i])):  # j: 0, 1, 2
#         print(f"Checking [{i}][{j}] = {matrix[i][j]}", end="")
#         if matrix[i][j] == search_value:
#             print(" ✓ FOUND!")
#             found = True
#             break
#         else:
#             print()
#     if found:
#         break
# """)

# print("📊 OUTPUT (Actual Execution):")
# found = False
# iteration = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         iteration += 1
#         print(f"  Iteration {iteration}: Checking [{i}][{j}] = {matrix[i][j]}", end="")
#         if matrix[i][j] == search_value:
#             print(" ✓ FOUND!")
#             found = True
#             break
#         else:
#             print()
#     if found:
#         break

# if not found:
#     print(f"  Element {search_value} not found")


# # ═════════════════════════════════════════════════════════════════════════════
# # EXAMPLE 10: TRANSPOSE A MATRIX
# # ═════════════════════════════════════════════════════════════════════════════
# print("\n" + "="*60)
# print("EXAMPLE 🔟  - TRANSPOSE A MATRIX (SWAP ROWS AND COLUMNS)")
# print("="*60)

# print("\n📝 SAMPLE INPUT:")
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# print("   Original matrix (2×3):")
# for row in matrix:
#     print(f"      {row}")

# print("\n💻 CODE WITH ITERATION TRACKING:")
# print("""
# matrix = [[1, 2, 3], [4, 5, 6]]
# transpose = []

# for col_idx in range(len(matrix[0])):        # col_idx: 0, 1, 2
#     new_row = []
#     print(f"Column {col_idx} becomes Row {col_idx}: ", end="")
#     for row_idx in range(len(matrix)):       # row_idx: 0, 1
#         element = matrix[row_idx][col_idx]
#         new_row.append(element)
#         print(f"{element} ", end="")
#     transpose.append(new_row)
#     print()
# """)

# print("📊 OUTPUT (Actual Execution):")
# transpose = []
# for col_idx in range(len(matrix[0])):
#     new_row = []
#     print(f"  Column {col_idx} becomes Row {col_idx}: ", end="")
#     for row_idx in range(len(matrix)):
#         element = matrix[row_idx][col_idx]
#         new_row.append(element)
#         print(f"{element} ", end="")
#     transpose.append(new_row)
#     print()

# print("\nTransposed matrix (3×2):")
# for row in transpose:
#     print(f"      {row}")


# # ═════════════════════════════════════════════════════════════════════════════
# # EXAMPLE 11: NESTED LOOP WITH DICTIONARY
# # ═════════════════════════════════════════════════════════════════════════════
# print("\n" + "="*60)
# print("EXAMPLE 1️⃣1️⃣  - NESTED LOOP WITH DICTIONARY AND LIST")
# print("="*60)

# print("\n📝 SAMPLE INPUT:")
# students = {
#     "Ali": [85, 90, 88],
#     "Bob": [92, 88, 95]
# }
# print("   students =", students)

# print("\n💻 CODE WITH ITERATION TRACKING:")
# print("""
# students = {"Ali": [85, 90, 88], "Bob": [92, 88, 95]}

# for name, marks in students.items():        # Outer loop: each student
#     total = 0
#     print(f"{name}: ", end="")
#     for mark in marks:                      # Inner loop: each mark
#         total += mark
#         print(f"{mark} ", end="")
#     average = total / len(marks)
#     print(f"→ Avg = {average:.1f}")
# """)

# print("📊 OUTPUT (Actual Execution):")
# for name, marks in students.items():
#     total = 0
#     print(f"  {name}: ", end="")
#     iteration = 0
#     for mark in marks:
#         iteration += 1
#         total += mark
#         print(f"{mark} ", end="")
#     average = total / len(marks)
#     print(f"→ Avg = {average:.1f}")


# # ═════════════════════════════════════════════════════════════════════════════
# # EXAMPLE 12: COUNT ELEMENTS MATCHING CONDITION
# # ═════════════════════════════════════════════════════════════════════════════
# print("\n" + "="*60)
# print("EXAMPLE 1️⃣2️⃣  - COUNT ELEMENTS MATCHING CONDITION")
# print("="*60)

# print("\n📝 SAMPLE INPUT:")
# matrix = [
#     [5, 15, 25],
#     [10, 30, 20],
#     [45, 35, 50]
# ]
# threshold = 20
# print("   matrix =", matrix)
# print(f"   threshold = {threshold} (count elements > 20)")

# print("\n💻 CODE WITH ITERATION TRACKING:")
# print("""
# matrix = [[5, 15, 25], [10, 30, 20], [45, 35, 50]]
# threshold = 20
# count = 0

# print("Elements > 20:")
# for i in range(len(matrix)):         # i: 0, 1, 2
#     for j in range(len(matrix[i])):  # j: 0, 1, 2
#         if matrix[i][j] > threshold:
#             print(f"[{i}][{j}] = {matrix[i][j]} ✓")
#             count += 1

# print(f"Total count: {count}")
# """)

# print("📊 OUTPUT (Actual Execution):")
# count = 0
# print("Elements > 20:")
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] > threshold:
#             print(f"  [{i}][{j}] = {matrix[i][j]} ✓")
#             count += 1

# print(f"Total count: {count}")


# # ═════════════════════════════════════════════════════════════════════════════
# # EXAMPLE 13: CALCULATE AVERAGE OF ALL ELEMENTS
# # ═════════════════════════════════════════════════════════════════════════════
# print("\n" + "="*60)
# print("EXAMPLE 1️⃣3️⃣  - CALCULATE AVERAGE OF ALL ELEMENTS")
# print("="*60)

# print("\n📝 SAMPLE INPUT:")
# matrix = [
#     [10, 20, 30],
#     [40, 50, 60]
# ]
# print("   matrix =", matrix)

# print("\n💻 CODE WITH ITERATION TRACKING:")
# print("""
# matrix = [[10, 20, 30], [40, 50, 60]]
# total = 0
# count = 0

# for i in range(len(matrix)):         # i: 0, 1
#     for j in range(len(matrix[i])):  # j: 0, 1, 2
#         total += matrix[i][j]
#         count += 1
#         print(f"[{i}][{j}]={matrix[i][j]} → count={count}, total={total}")

# average = total / count
# print(f"Average = {total} ÷ {count} = {average}")
# """)

# print("📊 OUTPUT (Actual Execution):")
# total = 0
# count = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         total += matrix[i][j]
#         count += 1
#         print(f"  [{i}][{j}]={matrix[i][j]} → count={count}, total={total}")

# average = total / count
# print(f"\nAverage = {total} ÷ {count} = {average}")


# # ═════════════════════════════════════════════════════════════════════════════
# # EXAMPLE 14: MULTIPLY EACH ELEMENT BY A VALUE
# # ═════════════════════════════════════════════════════════════════════════════
# print("\n" + "="*60)
# print("EXAMPLE 1️⃣4️⃣  - MULTIPLY ALL ELEMENTS BY A VALUE")
# print("="*60)

# print("\n📝 SAMPLE INPUT:")
# matrix = [
#     [1, 2],
#     [3, 4]
# ]
# multiplier = 5
# print("   Original matrix =", matrix)
# print(f"   Multiplier = {multiplier}")

# print("\n💻 CODE WITH ITERATION TRACKING:")
# print("""
# matrix = [[1, 2], [3, 4]]
# multiplier = 5

# for i in range(len(matrix)):         # i: 0, 1
#     for j in range(len(matrix[i])):  # j: 0, 1
#         old = matrix[i][j]
#         matrix[i][j] *= multiplier
#         print(f"[{i}][{j}]: {old} × {multiplier} = {matrix[i][j]}")
# """)

# print("📊 OUTPUT (Actual Execution):")
# matrix = [
#     [1, 2],
#     [3, 4]
# ]
# multiplier = 5

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         old = matrix[i][j]
#         matrix[i][j] *= multiplier
#         print(f"  [{i}][{j}]: {old} × {multiplier} = {matrix[i][j]}")

# print(f"\nUpdated matrix = {matrix}")


# # ═════════════════════════════════════════════════════════════════════════════
# # EXAMPLE 15: NESTED LOOP WITH TUPLES (COORDINATES & DISTANCE)
# # ═════════════════════════════════════════════════════════════════════════════
# print("\n" + "="*60)
# print("EXAMPLE 1️⃣5️⃣  - NESTED LOOP WITH LIST OF TUPLES")
# print("="*60)

# print("\n📝 SAMPLE INPUT:")
# coordinates = [
#     (1, 2),
#     (3, 4),
#     (5, 6)
# ]
# print("   coordinates =", coordinates)

# print("\n💻 CODE WITH ITERATION TRACKING:")
# print("""
# import math

# coordinates = [(1, 2), (3, 4), (5, 6)]

# for idx, (x, y) in enumerate(coordinates):   # Unpack tuple
#     distance = math.sqrt(x**2 + y**2)
#     print(f"Point {idx}: ({x}, {y}) → Distance = {distance:.2f}")
# """)

# print("📊 OUTPUT (Actual Execution):")
# import math

# for idx, (x, y) in enumerate(coordinates):
#     distance = math.sqrt(x**2 + y**2)
#     print(f"  Point {idx}: ({x}, {y}) → Distance = {distance:.2f}")


# print("\n" + "="*60)
# print("✅ END OF ALL NESTED LOOP EXAMPLES - ALL ITERATIONS EXPLAINED")
# print("="*60)
# a = 5 /2
# print(a)

# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end = " ")
#     print()
# for k in range(n-1,0,-1):
#     for j in range(1,k+1):
#         print("*",end = " ")
#     print()

# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(end=" ")
#     for k in range(1,i+1):
#         print("*",end = " ")
#     print()

# for x in range(n-1,0,-1):
#     for y in range(1,n-x+1):
#         print(end = " ")
#     for z in range(1,x+1):
#         print("*",end=" ")
#     print()

# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end = " ")
#     print()
# for x in range(n-1,0,-1):
#     for y in range(1,n-x+1):
#         print(" ",end = " ")
#     for z in range(1,x+1):
#         print("*",end = " ")
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()

# l = int(input())
# b = int(input())
# for i in range(b):
#     for j in range(l):
#         print("*",end = " ")
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()

# l = int(input())
# b = int(input())
# for i in range(b):
#     for j in range(l):
#         if i==0 or i == b-1 or j == 0 or j == l-1:
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()
#write a program to print H pattern
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         if j == 0 or j == n-1 or i == n//2:
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()

# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end = " ")
#     print()

# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end = " ")
#     print()

# n = int(input())
# for i in range(1,n+1):
#     row = ""
#     for j in range(1,i+1):
#         row += str(j) + " "
#     print(row)

# n = int(input())
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end = " ")
#     print()

# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(end=" ")
#     for k in range(1,i+1):
#         print("*",end = " ")
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1 or i < j or i > j:
#             print("*",end = " ")
#         else:
#             print(" ",end= " ")
#     print()

# n = int(input())
# for x in range(n-1,0,-1):
#     for y in range(1,n-x+1):
#         print(end = " ")
#     for z in range(1,x+1):
#         print("*",end=" ")
#     print()

# n = int(input())
# arr = list(map(int,input().split()))
# k = int(input())
# c = 0
# for i in range(n):
#     for j in range(i+1,n):
#         if (arr[i]+arr[j])%k == 0:
#             c += 1
# print(c)

# n = int(input())
# r = 0
# while n > 0:
#     d = n % 10
#     r = r * 10 + d
#     n //= 10
# print(r)

# a = input()
# b = ""
# for i in a:
#     if i.isalpha():
#         b = i + b
#     else:
#         b += i
# c = ""
# for i in range(len(b)//2):
#     c = c+b[i]+b[i+3]
# print(c)

i = 0
while i < 5:
    x = 1
    m = ""
    while i+1 <= i:
        m += (str(x) + "*")
        x += 1
    print(m.rstrip("*"))
    i += 1