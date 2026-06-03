# ═════════════════════════════════════════════════════════════════════════════
# 5. BREAK AND CONTINUE WITH NESTED LOOPS
# ═════════════════════════════════════════════════════════════════════════════

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║        SECTION 5: BREAK/CONTINUE WITH NESTED LOOPS                    ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

print("5. BREAK/CONTINUE WITH NESTED LOOPS")
print("-" * 60)

# Example 1: Break exits inner loop only
print("Example 1: BREAK exits INNER loop only")
print("-" * 40)
for row in range(1, 4):
    print(f"Row {row}:", end=" ")
    for col in range(1, 6):
        if col == 3:
            break  # Exits inner loop, continues outer loop
        print(f"{col}", end=" ")
    print()

print("""
Output:
Row 1: 1 2 
Row 2: 1 2 
Row 3: 1 2 

Break only exits the inner loop, not the outer loop!
""")

# Example 2: Continue skips rest of inner loop
print("\nExample 2: CONTINUE skips rest of INNER loop")
print("-" * 40)
for row in range(1, 4):
    print(f"Row {row}:", end=" ")
    for col in range(1, 6):
        if col == 2:
            continue  # Skips col=2, goes to next col
        print(f"{col}", end=" ")
    print()

print("""
Output:
Row 1: 1 3 4 5 
Row 2: 1 3 4 5 
Row 3: 1 3 4 5 

Continue skips just this iteration, continues with col=3,4,5
""")

print("\n")