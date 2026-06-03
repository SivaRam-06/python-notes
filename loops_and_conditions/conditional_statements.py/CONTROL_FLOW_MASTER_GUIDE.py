"""
╔════════════════════════════════════════════════════════════════════════════╗
║            CONTROL FLOW STATEMENTS - MASTER GUIDE                         ║
║              Complete Understanding with Examples & Tips                  ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

# ═════════════════════════════════════════════════════════════════════════════
# TABLE OF CONTENTS
# ═════════════════════════════════════════════════════════════════════════════

print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                           TABLE OF CONTENTS                               ║
╚════════════════════════════════════════════════════════════════════════════╝

📚 COMPLETE CONTROL FLOW GUIDE

This guide covers 3 files:

1. if_elif_else_statements.py
   ├─ Simple IF statements
   ├─ IF-ELSE statements (two options)
   ├─ IF-ELIF-ELSE statements (multiple options)
   ├─ Combining conditions with AND, OR, NOT
   ├─ Real-world examples (grades, ATM, admission)
   └─ Common mistakes & tips

2. for_while_loops.py
   ├─ FOR loops with range() function
   ├─ FOR loops with lists and dictionaries
   ├─ WHILE loops (repeat until condition is FALSE)
   ├─ Using enumerate() to get index and item
   ├─ Nested loops (loop inside loop)
   ├─ FOR loop vs WHILE loop comparison
   └─ Real-world examples

3. break_continue_pass.py
   ├─ BREAK: Exit loop immediately
   ├─ CONTINUE: Skip current iteration
   ├─ PASS: Placeholder that does nothing
   ├─ Using these in nested loops
   ├─ Real-world examples (search, authentication, filtering)
   └─ Common mistakes

═══════════════════════════════════════════════════════════════════════════════

📋 QUICK REFERENCE - WHAT TO USE WHEN

SITUATION                          USE THIS              EXAMPLE
────────────────────────────────────────────────────────────────────────────
User is 18 or older?              IF-ELSE               if age >= 18:
                                                            print("Adult")

Mark Grade (A/B/C/F)               IF-ELIF-ELSE          if marks >= 90:
                                                            grade = "A"

Repeat 10 times                    FOR with range()      for i in range(10):
                                                            print(i)

Process each item in list          FOR in list           for item in items:
                                                            print(item)

Repeat while condition is TRUE     WHILE                 while count < 10:
                                                            count += 1

Stop when found                    BREAK                 if item == search:
                                                            break

Skip invalid items                 CONTINUE              if value < 0:
                                                            continue

Placeholder for later code         PASS                  if error:
                                                            pass

═══════════════════════════════════════════════════════════════════════════════
""")

# ═════════════════════════════════════════════════════════════════════════════
# DECISION TREE - WHICH STATEMENT TO USE
# ═════════════════════════════════════════════════════════════════════════════

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                  DECISION TREE - WHICH TO USE?                        ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

print("""
DO YOU NEED TO REPEAT CODE?
│
├─ YES: Need to repeat code
│  │
│  ├─ Know exactly HOW MANY times?
│  │  │
│  │  ├─ YES: Use FOR LOOP
│  │  │       Examples:
│  │  │       • Print 1 to 10
│  │  │       • Process each student in a list
│  │  │       • Create 5 boxes
│  │  │       Code: for i in range(10):
│  │  │
│  │  └─ NO: Repeat UNTIL condition is met?
│  │        │
│  │        └─ YES: Use WHILE LOOP
│  │                Examples:
│  │                • Keep asking for password until correct
│  │                • Play game while lives > 0
│  │                • Download while internet is fast
│  │                Code: while condition:
│  │
│  └─ Need to CONTROL loop flow?
│     │
│     ├─ Stop early when found?  → Use BREAK
│     ├─ Skip this iteration?    → Use CONTINUE
│     └─ Placeholder code?       → Use PASS
│
└─ NO: Just make ONE decision
   │
   ├─ One condition (Yes/No)?   → Use IF or IF-ELSE
   │                               Code: if condition:
   │
   └─ Multiple options?         → Use IF-ELIF-ELSE
                                  Code: if cond1:
                                            elif cond2:
                                            else:

═══════════════════════════════════════════════════════════════════════════════
""")

# ═════════════════════════════════════════════════════════════════════════════
# SYNTAX SUMMARY
# ═════════════════════════════════════════════════════════════════════════════

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                       SYNTAX SUMMARY                                  ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

print("""
1. IF STATEMENT
   ┌─────────────────────────────────────────────────────────────┐
   │ if condition:                                               │
   │     # Code runs only if condition is TRUE                  │
   │     print("This runs if condition is TRUE")                │
   └─────────────────────────────────────────────────────────────┘

2. IF-ELSE STATEMENT
   ┌─────────────────────────────────────────────────────────────┐
   │ if condition:                                               │
   │     # Code if TRUE                                          │
   │ else:                                                       │
   │     # Code if FALSE                                         │
   └─────────────────────────────────────────────────────────────┘

3. IF-ELIF-ELSE STATEMENT
   ┌─────────────────────────────────────────────────────────────┐
   │ if condition1:                                              │
   │     # Code if condition1 is TRUE                            │
   │ elif condition2:                                            │
   │     # Code if condition1 is FALSE and condition2 is TRUE   │
   │ elif condition3:                                            │
   │     # Code if condition1 and condition2 are FALSE          │
   │ else:                                                       │
   │     # Code if all above conditions are FALSE               │
   └─────────────────────────────────────────────────────────────┘

4. FOR LOOP (Repeat Fixed Times)
   ┌─────────────────────────────────────────────────────────────┐
   │ for variable in range(start, end, step):                   │
   │     # Code repeats for each value                          │
   │                                                             │
   │ Examples:                                                   │
   │ for i in range(10):          # 0 to 9 (10 times)          │
   │ for i in range(1, 11):       # 1 to 10                    │
   │ for i in range(0, 10, 2):    # 0, 2, 4, 6, 8             │
   │ for i in range(5, 0, -1):    # 5, 4, 3, 2, 1 (backward) │
   │ for item in list:            # Each item in list          │
   │ for item in dictionary:      # Each key in dictionary     │
   └─────────────────────────────────────────────────────────────┘

5. WHILE LOOP (Repeat Until Condition is False)
   ┌─────────────────────────────────────────────────────────────┐
   │ while condition:                                            │
   │     # Code repeats while condition is TRUE                │
   │     # IMPORTANT: Change condition to eventually make FALSE │
   │                                                             │
   │ Example:                                                    │
   │ count = 0                                                  │
   │ while count < 10:                                          │
   │     print(count)                                           │
   │     count = count + 1  # Must change count!               │
   └─────────────────────────────────────────────────────────────┘

6. BREAK (Exit Loop Immediately)
   ┌─────────────────────────────────────────────────────────────┐
   │ for item in list:                                           │
   │     if item == target:                                     │
   │         break  # Stop loop, jump out                      │
   └─────────────────────────────────────────────────────────────┘

7. CONTINUE (Skip Current Iteration)
   ┌─────────────────────────────────────────────────────────────┐
   │ for number in list:                                         │
   │     if number < 0:                                         │
   │         continue  # Skip rest, go to next iteration       │
   │     print(number)  # Skipped if number < 0                │
   └─────────────────────────────────────────────────────────────┘

8. PASS (Do Nothing - Placeholder)
   ┌─────────────────────────────────────────────────────────────┐
   │ if error_occurred:                                          │
   │     pass  # Do nothing for now (will add code later)      │
   └─────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════
""")

# ═════════════════════════════════════════════════════════════════════════════
# OPERATORS - WHAT CAN YOU USE IN CONDITIONS
# ═════════════════════════════════════════════════════════════════════════════

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║            OPERATORS - COMPARISONS & LOGICAL CONDITIONS               ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

print("""
COMPARISON OPERATORS - Testing values:
┌─────────────┬──────────────┬──────────────────────────────────────┐
│ Operator    │ Meaning      │ Example                              │
├─────────────┼──────────────┼──────────────────────────────────────┤
│ ==          │ Equal to     │ if age == 18:                        │
│ !=          │ Not equal    │ if name != "Ali":                    │
│ >           │ Greater than │ if score > 50:                       │
│ <           │ Less than    │ if age < 18:                         │
│ >=          │ >= to        │ if height >= 160:                    │
│ <=          │ <= to        │ if weight <= 70:                     │
└─────────────┴──────────────┴──────────────────────────────────────┘

LOGICAL OPERATORS - Combining conditions:
┌──────────────┬────────────────────────────┬──────────────────────────────┐
│ Operator     │ Meaning                    │ Example                      │
├──────────────┼────────────────────────────┼──────────────────────────────┤
│ and          │ Both must be TRUE          │ if age >= 18 and has_license │
│ or           │ At least one is TRUE       │ if has_money or friend_pays  │
│ not          │ Reverse (TRUE→FALSE)       │ if not is_raining:           │
└──────────────┴────────────────────────────┴──────────────────────────────┘

MEMBERSHIP OPERATORS - Checking in collections:
┌──────────────┬────────────────────────────┬──────────────────────────────┐
│ Operator     │ Meaning                    │ Example                      │
├──────────────┼────────────────────────────┼──────────────────────────────┤
│ in           │ Element is in list/dict    │ if "apple" in fruits:        │
│ not in       │ Element is NOT in list     │ if student not in passed:    │
└──────────────┴────────────────────────────┴──────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════
""")

# ═════════════════════════════════════════════════════════════════════════════
# COMPLETE EXAMPLE - STUDENT MANAGEMENT SYSTEM
# ═════════════════════════════════════════════════════════════════════════════

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║           COMPLETE EXAMPLE - STUDENT MANAGEMENT SYSTEM                ║")
print("║  Using all control flow concepts in one realistic program             ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

# Student data
students_db = {
    "Ali": {"marks": 85, "attendance": 90, "active": True},
    "Bhavna": {"marks": 92, "attendance": 100, "active": True},
    "Chirag": {"marks": 78, "attendance": 75, "active": False},
    "Deepa": {"marks": 88, "attendance": 95, "active": True}
}

print("EXAMPLE: Student Performance Analysis System\n")

print("1. USING IF-ELIF-ELSE (Determine grade based on marks)")
print("-" * 60)
for student_name, student_info in students_db.items():
    marks = student_info["marks"]
    
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    else:
        grade = "C"
    
    print(f"{student_name}: {marks} marks → Grade: {grade}")

print()

print("2. USING FOR LOOP (Calculate statistics)")
print("-" * 60)
total_marks = 0
total_students = 0

for name, info in students_db.items():
    total_marks = total_marks + info["marks"]
    total_students = total_students + 1

average_marks = total_marks / total_students
print(f"Total students: {total_students}")
print(f"Total marks: {total_marks}")
print(f"Average marks: {average_marks:.2f}")

print()

print("3. USING FOR + IF + CONTINUE (Skip inactive students)")
print("-" * 60)
print("Active students report:")
for name, info in students_db.items():
    if not info["active"]:
        continue  # Skip inactive students
    
    print(f"  {name}: Marks={info['marks']}, Attendance={info['attendance']}%")

print()

print("4. USING FOR + IF + BREAK (Find first topper)")
print("-" * 60)
print("Searching for first student with marks >= 90...")
for name, info in students_db.items():
    if info["marks"] >= 90:
        print(f"  Found! {name} scored {info['marks']} marks")
        break

print()

print("5. USING WHILE LOOP (Interactive menu)")
print("-" * 60)
print("Student database interactive menu:")
menu_choice = ""

while menu_choice != "4":
    print("""
    1. Show all students
    2. Show top performers
    3. Show average marks
    4. Exit
    """)
    
    menu_choice = input("Enter choice (1-4): ")
    
    if menu_choice == "1":
        print("All students:")
        for name, info in students_db.items():
            print(f"  {name}: {info['marks']} marks")
    
    elif menu_choice == "2":
        print("Top performers (marks >= 85):")
        found = False
        for name, info in students_db.items():
            if info["marks"] >= 85:
                print(f"  {name}: {info['marks']} marks")
                found = True
        if not found:
            print("  No students found")
    
    elif menu_choice == "3":
        avg = sum(info["marks"] for info in students_db.values()) / len(students_db)
        print(f"Average marks: {avg:.2f}")
    
    elif menu_choice == "4":
        print("Exiting...")
        pass
    
    else:
        print("Invalid choice!")

print("\n")

# ═════════════════════════════════════════════════════════════════════════════
# COMPARISON TABLE - WHAT TO USE
# ═════════════════════════════════════════════════════════════════════════════
"""
┌────────────────────────┬──────────┬──────────┬────────────┬─────────────┐
│ Task                   │ IF       │ FOR      │ WHILE      │ BREAK/CONT. │
├────────────────────────┼──────────┼──────────┼────────────┼─────────────┤
│ Make one decision      │ ✓✓✓      │          │            │             │
│ Multiple options       │ ✓✓       │          │            │             │
│ Repeat 10 times        │          │ ✓✓✓      │ ✓          │             │
│ Process each item      │          │ ✓✓✓      │ ✓          │             │
│ Repeat until done      │          │ ✓        │ ✓✓✓        │             │
│ Stop early             │          │ ✓        │ ✓          │ ✓✓✓         │
│ Skip this item         │ ✓        │ ✓        │ ✓          │ ✓✓✓         │
│ Placeholder code       │          │          │            │ ✓✓✓         │
│ Countdown              │          │ ✓✓✓      │ ✓          │             │
│ Validate input         │ ✓✓       │          │ ✓✓✓        │             │
│ Find in list           │          │ ✓        │            │ ✓✓✓         │
│ Calculate total        │          │ ✓✓✓      │ ✓          │             │
└────────────────────────┴──────────┴──────────┴────────────┴─────────────┘

✓✓✓ = Best choice
✓✓  = Good choice
✓   = Can work but not ideal

═══════════════════════════════════════════════════════════════════════════════
"""

# ═════════════════════════════════════════════════════════════════════════════
# FLOW DIAGRAMS
# ═════════════════════════════════════════════════════════════════════════════
"""
IF-ELIF-ELSE FLOW:
                    ┌─────────────────────────┐
                    │   Check condition 1?    │
                    └────────┬────────────────┘
                             │
                    ┌────────┴─────────┐
                    │ TRUE            │ FALSE
                    │                 │
                  [Run Block 1]   ┌───┴──────────────┐
                    │            │ Check condition 2?│
                    │            └────┬─────────┬────┘
                    │                 │ TRUE   │ FALSE
                    │               [Run B2]  ┌┴─────────────┐
                    │                 │       │ Check cond 3?│
                    │                 │       └────┬────┬────┘
                    │                 │            │ TRUE
                    │                 │          [Run B3]
                    │                 │            │
                    │                 │        [ELSE Block]
                    │                 │            │
                    └─────────┬───────┴────────────┘
                              │
                         ┌────▼─────┐
                         │ Continue  │
                         └──────────┘

FOR LOOP FLOW (Repeat fixed times):
                    ┌──────────────────────┐
                    │ Set i = start        │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼────────────┐
                    │ Is i < end?          │
                    └──────┬────────┬──────┘
                           │ YES    │ NO
                        [Run       [Exit]
                         Block]     │
                           │        │
                    ┌──────▼──┐     │
                    │ i = i+1 │     │
                    └──────┬──┘     │
                           │        │
                    ┌──────┴────────┘
                    │
                    └──► Check again

WHILE LOOP FLOW (Repeat until condition is false):
                    ┌──────────────────────┐
                    │ Is condition TRUE?   │
                    └──────┬────────┬──────┘
                           │ YES    │ NO
                        [Run Block][Exit]
                           │        │
                        [Change    │
                        condition] │
                           │        │
                    ┌──────┴────────┘
                    │
                    └──► Check again

═══════════════════════════════════════════════════════════════════════════════
"""

# ═════════════════════════════════════════════════════════════════════════════
# FINAL CHECKLIST
# ═════════════════════════════════════════════════════════════════════════════
"""
BEFORE WRITING IF/ELIF/ELSE:
✓ Do I need to make a decision? (not repeat)
✓ Is it a YES/NO decision? (use IF-ELSE)
✓ Are there multiple options? (use IF-ELIF-ELSE)
✓ Did I use == for comparison, not = for assignment?
✓ Did I include a colon (:) after the condition?
✓ Are all the conditional blocks properly indented?

BEFORE WRITING FOR LOOP:
✓ Do I know how many times to repeat?
✓ Am I using range() correctly? (range(10) = 0 to 9)
✓ Did I include a colon (:) after the for statement?
✓ Is the loop body indented?
✓ If processing a list, am I using the right variable?

BEFORE WRITING WHILE LOOP:
✓ Is the number of repetitions unknown?
✓ Do I understand the condition?
✓ Will the condition eventually become FALSE?
✓ Did I include code to change the condition?
✓ Is there a risk of infinite loop?
✓ Did I include a colon (:)?

BEFORE USING BREAK:
✓ Am I inside a loop?
✓ Do I want to exit completely?
✓ Is this the right place to break?

BEFORE USING CONTINUE:
✓ Am I inside a loop?
✓ Do I want to skip this iteration only?
✓ Will the loop continue normally after?

═══════════════════════════════════════════════════════════════════════════════

PRACTICE EXERCISES:

1. Create a program that asks user's age and tells them what movie rating they
   can watch (G, PG, PG-13, R, NC-17)

2. Print the first 10 even numbers

3. Create a program that finds a specific word in a list of words

4. Ask user for a password 3 times. If correct, print "Access Granted"
   If all 3 attempts fail, print "Access Denied"

5. Process a list of marks and skip marks below 40 (invalid marks)

6. Create a simple calculator that keeps running until user enters "exit"

═══════════════════════════════════════════════════════════════════════════════
"""