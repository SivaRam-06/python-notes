# Control Flow Statements - Complete Learning Guide

## 📚 Introduction

Control Flow Statements help your program make decisions and repeat code. They are essential for writing effective Python programs.

### Two Main Types:
1. **Conditional Statements** - Make decisions (IF, ELIF, ELSE)
2. **Loop Statements** - Repeat code (FOR, WHILE)
3. **Loop Control** - Control how loops behave (BREAK, CONTINUE, PASS)

---

## 📖 Files in This Guide

### 1. **CONTROL_FLOW_MASTER_GUIDE.py** (Start here!)
   - Quick reference for all control flow concepts
   - Decision trees to help you choose the right statement
   - Comparison tables
   - Flow diagrams
   - Complete example program

### 2. **if_elif_else_statements.py** (Detailed Guide)
   - Simple IF statements
   - IF-ELSE statements
   - IF-ELIF-ELSE statements  
   - Multiple conditions with AND, OR, NOT
   - Real-world examples (grades, ATM, admission)
   - Common mistakes

### 3. **for_while_loops.py** (Detailed Guide)
   - FOR loops with range()
   - FOR loops with lists and dictionaries
   - Using enumerate() to get index and item
   - WHILE loops
   - Nested loops
   - Real-world examples
   - FOR vs WHILE comparison

### 4. **break_continue_pass.py** (Detailed Guide)
   - BREAK statement (exit loop)
   - CONTINUE statement (skip iteration)
   - PASS statement (placeholder)
   - Using these in nested loops
   - Real-world examples
   - Common mistakes

---

## 🎯 Quick Start - Which Should You Use?

### Making a Decision?
| Situation | Use | Example |
|-----------|-----|---------|
| Yes/No decision | IF or IF-ELSE | `if age >= 18:` |
| Multiple options | IF-ELIF-ELSE | `if marks >= 90: A+ / elif marks >= 80: A` |

### Need to Repeat Code?
| Situation | Use | Example |
|-----------|-----|---------|
| Know how many times | FOR | `for i in range(10):` |
| Until condition is met | WHILE | `while count < 10:` |
| Process each item | FOR | `for item in list:` |

### Control Loop?
| Situation | Use | Example |
|-----------|-----|---------|
| Exit when found | BREAK | `if found: break` |
| Skip this item | CONTINUE | `if invalid: continue` |
| Placeholder | PASS | `if error: pass` |

---

## 📝 Syntax Reference

### IF Statement
```python
if condition:
    # Code runs if condition is TRUE
    print("This runs if true")
```

### IF-ELSE Statement
```python
if condition:
    # Code if TRUE
    print("True path")
else:
    # Code if FALSE
    print("False path")
```

### IF-ELIF-ELSE Statement
```python
if condition1:
    # Code if condition1 is TRUE
elif condition2:
    # Code if condition2 is TRUE (and condition1 is FALSE)
elif condition3:
    # Code if condition3 is TRUE (and above are FALSE)
else:
    # Code if all above are FALSE
```

### FOR Loop with range()
```python
for i in range(10):           # 0 to 9
    print(i)

for i in range(1, 11):        # 1 to 10
    print(i)

for i in range(0, 10, 2):     # 0, 2, 4, 6, 8 (step by 2)
    print(i)

for i in range(5, 0, -1):     # 5, 4, 3, 2, 1 (countdown)
    print(i)
```

### FOR Loop with List
```python
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Get both index and item
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### FOR Loop with Dictionary
```python
student = {"Ali": 85, "Bhavna": 90}
for name in student:            # Keys only
    print(name)

for marks in student.values():  # Values only
    print(marks)

for name, marks in student.items():  # Both
    print(f"{name}: {marks}")
```

### WHILE Loop
```python
count = 0
while count < 10:
    print(count)
    count = count + 1  # IMPORTANT: Change condition!
```

### BREAK Statement
```python
for item in list:
    if item == target:
        break  # Exit loop immediately
```

### CONTINUE Statement
```python
for number in list:
    if number < 0:
        continue  # Skip to next iteration
    print(number)  # This line is skipped for negative numbers
```

### PASS Statement
```python
if error:
    pass  # Do nothing (placeholder)
```

---

## 🔧 Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `if age == 18:` |
| `!=` | Not equal | `if name != "Ali":` |
| `>` | Greater than | `if score > 50:` |
| `<` | Less than | `if age < 18:` |
| `>=` | Greater than or equal | `if height >= 160:` |
| `<=` | Less than or equal | `if weight <= 70:` |

---

## 🔗 Logical Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | Both conditions must be TRUE | `if age >= 18 and has_license:` |
| `or` | At least one condition is TRUE | `if has_money or friend_pays:` |
| `not` | Reverses the condition | `if not is_raining:` |

---

## 🎓 Learning Path

### Beginner Level
1. Start with `if_elif_else_statements.py`
2. Understand how IF and ELSE work
3. Learn IF-ELIF-ELSE for multiple options
4. Practice with simple examples

### Intermediate Level
5. Read `for_while_loops.py`
6. Understand FOR loops with range()
7. Learn to loop through lists
8. Practice nested loops

### Advanced Level
9. Read `break_continue_pass.py`
10. Understand BREAK, CONTINUE, PASS
11. Learn to control loop flow
12. Practice complex programs

### Master Level
13. Review `CONTROL_FLOW_MASTER_GUIDE.py`
14. Understand when to use each statement
15. Practice real-world examples
16. Build your own projects

---

## ⚠️ Common Mistakes

### Mistake 1: Using `=` instead of `==`
```python
# ❌ WRONG - This ASSIGNS value, not compares
if name = "Ali":
    print("Hello Ali")

# ✓ CORRECT - This COMPARES values
if name == "Ali":
    print("Hello Ali")
```

### Mistake 2: Forgetting Indentation
```python
# ❌ WRONG
if age >= 18:
print("Adult")  # Not indented!

# ✓ CORRECT
if age >= 18:
    print("Adult")  # Properly indented
```

### Mistake 3: Forgetting Colon
```python
# ❌ WRONG
if age >= 18
    print("Adult")  # Missing colon!

# ✓ CORRECT
if age >= 18:
    print("Adult")
```

### Mistake 4: range() End Value
```python
# range(10) does NOT include 10!
for i in range(10):
    print(i)  # Prints 0 to 9 (NOT 10!)

# To print 0 to 10:
for i in range(11):  # 11 means up to 10
    print(i)
```

### Mistake 5: Infinite WHILE Loop
```python
# ❌ WRONG - Infinite loop! (never stops)
while True:
    print("This never stops!")

# ✓ CORRECT - Add a way to exit
while True:
    user_input = input("Enter 'stop' to quit: ")
    if user_input == "stop":
        break  # Exit here!
```

### Mistake 6: Not Changing Condition in WHILE
```python
# ❌ WRONG - Infinite loop!
count = 0
while count < 10:
    print(count)
    # Forgot to change count!

# ✓ CORRECT
count = 0
while count < 10:
    print(count)
    count = count + 1  # Change the condition!
```

### Mistake 7: BREAK in Nested Loop
```python
# ❌ WRONG - Only exits inner loop
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # Only breaks inner loop!
    print(i)  # This still runs for all i values

# To exit both, use a flag:
# ✓ CORRECT
exit_flag = False
for i in range(3):
    for j in range(3):
        if j == 1:
            exit_flag = True
            break
    if exit_flag:
        break  # Now breaks outer loop too
```

---

## 🧪 Practice Exercises

### Easy
1. Create a program that checks if a number is positive or negative
2. Write a program that prints numbers 1 to 20
3. Create a program that checks if a year is a leap year

### Medium
4. Write a program that grades students based on marks (A, B, C, F)
5. Create a program that finds a specific word in a list
6. Write a program that calculates the sum of numbers 1 to 100

### Hard
7. Create a simple ATM program with IF-ELIF and WHILE
8. Write a program that processes student data with FOR loop and filtering
9. Create a password validation program with limited attempts

### Expert
10. Build a complete student management system using all control flow concepts
11. Create a game loop that continues until the user quits
12. Write a program that validates and processes multiple data types

---

## 🚀 Tips for Success

### Do's ✓
- ✓ Always use proper indentation (4 spaces)
- ✓ Always use colon (:) after IF, ELIF, ELSE, FOR, WHILE
- ✓ Use meaningful variable names (not `x`, use `age`)
- ✓ Test your code with different inputs
- ✓ Comment your code to explain what it does
- ✓ Start simple, then make it more complex

### Don'ts ✗
- ✗ Don't use `=` for comparison (use `==`)
- ✗ Don't forget to change the condition in WHILE loops
- ✗ Don't use spaces instead of colons at the end of statements
- ✗ Don't forget indentation
- ✗ Don't mix up BREAK and CONTINUE
- ✗ Don't use `for` when you should use `while`

---

## 📚 How to Use These Files

1. **Start with CONTROL_FLOW_MASTER_GUIDE.py**
   - Run this file first to understand the overview
   - Read all the decision trees and summaries

2. **Deep dive into Each Topic**
   - Read if_elif_else_statements.py completely
   - Run it and see all the examples
   - Try modifying examples to understand better

3. **Learn Loops**
   - Read for_while_loops.py thoroughly
   - Understand the difference between FOR and WHILE
   - Try creating your own examples

4. **Master Loop Control**
   - Read break_continue_pass.py
   - Understand when to use each
   - Practice with real-world examples

5. **Practice Projects**
   - Create a grading system
   - Build a simple game
   - Write a data processor
   - Create a menu-driven program

---

## 🎯 Next Steps After Mastering Control Flow

Once you're comfortable with control flow, you can learn:
- Functions (reusable code blocks)
- Lists and Dictionaries (data structures)
- File handling (reading/writing files)
- Object-Oriented Programming (classes and objects)
- Error handling (try-except blocks)

---

## 📞 Quick Reference Card

```
IF-ELIF-ELSE for decisions:
  - One YES/NO → IF-ELSE
  - Multiple options → IF-ELIF-ELSE

FOR LOOP for known iterations:
  for i in range(10):        # 0 to 9
  for item in list:          # Each item
  for key, val in dict.items():  # Key and value

WHILE LOOP for unknown iterations:
  while condition:
      # Change condition to eventually exit!

BREAK to exit loop
CONTINUE to skip iteration
PASS as placeholder

Remember: Indentation and colons are CRITICAL!
```

---

## ✅ Checklist Before Starting Real Projects

- [ ] I understand IF, ELIF, ELSE
- [ ] I can use comparisons operators (==, !=, >, <, >=, <=)
- [ ] I can combine conditions with AND, OR, NOT
- [ ] I understand FOR loops with range()
- [ ] I can loop through lists and dictionaries
- [ ] I understand WHILE loops
- [ ] I can use BREAK to exit loops
- [ ] I can use CONTINUE to skip iterations
- [ ] I understand nested loops
- [ ] I can write real-world programs

Once you check all of these, you're ready to build projects! 🚀

---

**Good Luck with your Python Learning Journey!** 🎉
