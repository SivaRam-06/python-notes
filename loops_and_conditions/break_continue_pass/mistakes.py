# ═════════════════════════════════════════════════════════════════════════════
# 8. COMMON MISTAKES
# ═════════════════════════════════════════════════════════════════════════════

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                        COMMON MISTAKES                                ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

print("""
MISTAKE 1: Using BREAK outside a loop
❌ WRONG:
if x > 10:
    break  ← ERROR! Not in a loop

✓ CORRECT:
for i in range(10):
    if x > 10:
        break  ← Inside loop, OK

---

MISTAKE 2: Confusing BREAK and CONTINUE
❌ WRONG - Expecting CONTINUE to exit loop:
for i in range(5):
    if i == 3:
        continue  ← Just skips i=3, loop continues
    print(i)
Output: 0 1 2 4  (loop still runs until end)

✓ CORRECT - Use BREAK to exit:
for i in range(5):
    if i == 3:
        break  ← Exits loop completely
    print(i)
Output: 0 1 2  (loop stops at 3)

---

MISTAKE 3: Code after BREAK that never runs
❌ WRONG:
for i in range(10):
    if i == 5:
        break
        print(i)  ← Never executes (dead code)

✓ CORRECT:
for i in range(10):
    if i == 5:
        print(i)  ← Runs first
        break

---

MISTAKE 4: PASS with conditions that should use CONTINUE
❌ INEFFICIENT:
for num in list:
    if num < 0:
        pass
    else:
        print(num)

✓ BETTER:
for num in list:
    if num < 0:
        continue
    print(num)

---

MISTAKE 5: Forgetting indentation after BREAK/CONTINUE
❌ WRONG:
for i in range(5):
if i == 2:
break  ← Not indented correctly

✓ CORRECT:
for i in range(5):
    if i == 2:
        break  ← Properly indented

---

MISTAKE 6: BREAK in nested loop
❌ WRONG - Expecting both loops to exit:
for i in range(3):
    for j in range(3):
        if condition:
            break  ← Only exits inner loop!
print("Both done")  ← Outer loop continues

✓ CORRECT - Use flag if you need both:
exit_flag = False
for i in range(3):
    for j in range(3):
        if condition:
            exit_flag = True
            break
    if exit_flag:
        break
print("Both done")  ← Both loops exited
""")