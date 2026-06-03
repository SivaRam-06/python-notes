# ═════════════════════════════════════════════════════════════════════════════
# 10. COMMON MISTAKES
# ═════════════════════════════════════════════════════════════════════════════

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                        COMMON MISTAKES                                ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

print("""
MISTAKE 1: Not understanding range() end value
❌ WRONG: range(5) gives [0, 1, 2, 3, 4] - but student thought it would be [0, 1, 2, 3, 4, 5]

✓ CORRECT: range(5) = 0 to 4 (NOT including 5)
          range(1, 6) = 1 to 5

---

MISTAKE 2: Infinite loop in WHILE
❌ WRONG:
number = 1
while number < 10:
    print(number)
    # Forgot to increase number!

✓ CORRECT:
number = 1
while number < 10:
    print(number)
    number = number + 1

---

MISTAKE 3: Not indenting loop code
❌ WRONG:
for i in range(3):
print(i)  ← Not indented (ERROR!)

✓ CORRECT:
for i in range(3):
    print(i)  ← Indented

---

MISTAKE 4: Forgetting colon after for/while
❌ WRONG:
for i in range(5)
    print(i)

✓ CORRECT:
for i in range(5):
    print(i)

---

MISTAKE 5: Modifying loop variable for wrong reason
❌ WRONG:
for number in [1, 2, 3]:
    number = 0  ← This doesn't affect the list!

---

MISTAKE 6: Off-by-one error
❌ WRONG:
for i in range(5):  ← Runs 0, 1, 2, 3, 4 (5 times)
    print(i)
Wanted 1 to 5, but got 0 to 4

✓ CORRECT:
for i in range(1, 6):  ← Runs 1, 2, 3, 4, 5
    print(i)
""")