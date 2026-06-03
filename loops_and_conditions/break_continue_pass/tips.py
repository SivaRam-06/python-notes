# ═════════════════════════════════════════════════════════════════════════════
# 7. IMPORTANT NOTES
# ═════════════════════════════════════════════════════════════════════════════

print("""
KEY POINTS:

1. BREAK - Exits the loop completely
   for i in range(10):
       if i == 5:
           break  ← Stops here, jumps out
   print("After loop")  ← This executes

2. CONTINUE - Skips rest of iteration, goes to next iteration
   for i in range(5):
       if i == 2:
           continue  ← Skips i=2, jumps to i=3
       print(i)  ← This line skipped for i=2

3. NESTED LOOPS - BREAK only exits immediate loop
   for outer in range(3):
       for inner in range(3):
           if inner == 2:
               break  ← Exits INNER loop only
                     ← Outer loop continues
   
   To exit both loops, use a flag variable:
   exit_outer = False
   for outer in range(3):
       for inner in range(3):
           if condition:
               exit_outer = True
               break
       if exit_outer:
           break

4. PASS - Perfect for placeholders
   def my_function():
       pass  ← Placeholder, will add code later
   
   if condition:
       pass  ← Do nothing for now

5. Common Patterns

   PATTERN 1: Search and stop
   for item in list:
       if item == target:
           print("Found!")
           break

   PATTERN 2: Skip certain items
   for item in list:
       if item is invalid:
           continue
       process(item)

   PATTERN 3: Process valid data
   total = 0
   for value in values:
       if value < 0:
           continue
       total = total + value

6. Performance Note
   - BREAK is useful to stop early (saves time)
   - CONTINUE can be slower than break (still loops)
   - Use break when you find what you need
   - Use continue to filter data

7. Order matters
   ✓ break before code you want to skip
   ✓ continue skips code after it
   
   for num in range(10):
       print(f"Checking {num}")  ← Always prints
       if num == 5:
           continue  ← Skips print below
       print(f"Processing {num}")  ← Skips when num=5
""")

print("\n")