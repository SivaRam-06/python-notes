# ═════════════════════════════════════════════════════════════════════════════
# 9. IMPORTANT NOTES AND TIPS
# ═════════════════════════════════════════════════════════════════════════════

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                    IMPORTANT NOTES & TIPS                             ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

print("""
KEY POINTS:

1. INDENTATION
   The code INSIDE the loop must be indented (4 spaces or 1 tab)
   
   ✓ Correct:
       for number in range(5):
           print(number)  ← Indented
   
   ✗ Wrong:
       for number in range(5):
       print(number)  ← Not indented (ERROR!)

2. range() FUNCTION
   • range(10): 0, 1, 2, ..., 9 (NOT 10!)
   • range(1, 10): 1, 2, 3, ..., 9 (NOT 10!)
   • range(0, 10, 2): 0, 2, 4, 6, 8 (step by 2)
   • range(10, 0, -1): 10, 9, 8, ..., 1 (counting down)

3. LOOP VARIABLE
   for item in list:  ← 'item' gets one element each iteration
   
   The variable name can be anything:
   for x in list:
   for fruit in list:
   for number in list:

4. INFINITE LOOP - DANGER!
   ❌ while True:
       print("This never stops!")  ← No way to exit!
   
   ✓ while condition:
       print("Do something")
       condition = False  ← Change condition to exit

5. MODIFYING LISTS WHILE LOOPING (Tricky!)
   ❌ AVOID:
       for item in list:
           list.remove(item)  ← Can cause problems!
   
   ✓ BETTER:
       for item in list[:]:  ← Loop through copy
           list.remove(item)

6. LOOP COUNTER
   for i in range(n):
       # i starts at 0, goes up to n-1
   
   If you want 1-10:
       for i in range(1, 11):  ← 1 to 10
       for i in range(10):     ← 0 to 9

7. BREAK vs CONTINUE
   - break: Exit the loop immediately
   - continue: Skip rest of current iteration, go to next one

8. NESTED LOOP - Count iterations
   for i in range(3):  ← Outer loop: 3 times
       for j in range(2):  ← Inner loop: 2 times each
           print()  ← Prints: 3 × 2 = 6 times
""")

print("\n")