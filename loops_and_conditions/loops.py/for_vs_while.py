# ═════════════════════════════════════════════════════════════════════════════
# 7. COMPARING FOR LOOP AND WHILE LOOP
# ═════════════════════════════════════════════════════════════════════════════

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║        SECTION 7: FOR LOOP vs WHILE LOOP - Comparison                 ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

print("FOR LOOP vs WHILE LOOP - When to Use Each?")
print("-" * 60)
print("""
SAME TASK - Two Different Ways:

Task: Count from 1 to 5

FOR LOOP:
    for number in range(1, 6):
        print(number)
    ✓ Use when you KNOW exactly how many times
    ✓ Simpler, cleaner code
    ✓ Less chance of infinite loop

WHILE LOOP:
    number = 1
    while number <= 5:
        print(number)
        number = number + 1
    ✓ Use when you repeat UNTIL condition is met
    ✓ More flexible
    ⚠ Danger of infinite loop if not careful

KEY DIFFERENCES:
┌─────────────────────┬──────────────────┬──────────────────┐
│ Feature             │ FOR LOOP          │ WHILE LOOP       │
├─────────────────────┼──────────────────┼──────────────────┤
│ Known iterations    │ ✓ Better         │ ✗ Less ideal     │
│ Unknown iterations  │ ✗ Not ideal      │ ✓ Better         │
│ Processing lists    │ ✓ Perfect        │ ✗ Awkward        │
│ Conditional repeat  │ ✗ Awkward        │ ✓ Perfect        │
│ Infinite loop risk  │ ✗ Low            │ ✓ High           │
│ Code simplicity     │ ✓ Simple         │ ✗ More complex   │
└─────────────────────┴──────────────────┴──────────────────┘

USE FOR LOOP WHEN:
    • You know how many times to repeat
    • You're processing each item in a list
    • You're counting (1, 2, 3, ...)

USE WHILE LOOP WHEN:
    • You repeat UNTIL a condition is met
    • The number of iterations is unknown
    • You're waiting for user input
    • You're running a game that continues until game over
""")

print("\n")