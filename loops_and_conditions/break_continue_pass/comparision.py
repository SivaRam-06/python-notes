# ═════════════════════════════════════════════════════════════════════════════
# 4. COMPARING BREAK, CONTINUE, PASS
# ═════════════════════════════════════════════════════════════════════════════
print("4. BREAK vs CONTINUE vs PASS - Comparison")
print("-" * 60)

print("\nSAME TASK - Three Different Ways:")
print("Task: Process numbers 1 to 10, skip 5, stop at 8")

print("\nMethod 1: Using BREAK (stop at 8)")
print("-" * 40)
for num in range(1, 11):
    if num == 8:
        break
    print(num, end=" ")
print()  # Prints: 1 2 3 4 5 6 7

print("\nMethod 2: Using CONTINUE (skip 5)")
print("-" * 40)
for num in range(1, 11):
    if num == 5:
        continue
    print(num, end=" ")
print()  # Prints: 1 2 3 4 6 7 8 9 10

print("\nMethod 3: Using PASS (doesn't skip, doesn't stop)")
print("-" * 40)
for num in range(1, 11):
    if num == 5:
        pass  # Does nothing
    print(num, end=" ")
print()  # Prints: 1 2 3 4 5 6 7 8 9 10

print("""
┌──────────┬─────────────────────────┬──────────────────┬──────────────────┐
│ Statement│ What Happens            │ Next Iteration?  │ Exit Loop?       │
├──────────┼─────────────────────────┼──────────────────┼──────────────────┤
│ BREAK    │ Exit loop immediately   │ NO - exits loop  │ YES - immediate  │
│ CONTINUE │ Skip rest of iteration  │ YES - continues  │ NO - continues   │
│ PASS     │ Do nothing (no effect)  │ YES - continues  │ NO - continues   │
└──────────┴─────────────────────────┴──────────────────┴──────────────────┘
""")

print("\n")