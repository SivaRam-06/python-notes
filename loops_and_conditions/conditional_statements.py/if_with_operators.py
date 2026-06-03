
# ═════════════════════════════════════════════════════════════════════════════
# 5. COMBINING CONDITIONS WITH AND, OR, NOT
# ═════════════════════════════════════════════════════════════════════════════
# Explanation
"""
AND: Both conditions must be TRUE
OR: At least one condition must be TRUE
NOT: Reverses the condition (TRUE becomes FALSE, FALSE becomes TRUE)
"""

print("\nA. USING AND (both conditions must be TRUE):")
print("-" * 60)

# Example: Can you drive? (Age >= 18 AND have license)
age = 20
has_license = True
print(f"Age: {age}, Has License: {has_license}")
if age >= 18 and has_license:
    print("✓ You can drive!")
else:
    print("✗ You cannot drive yet")

print()

# Example 2: Can enter restricted area? (Staff AND Working hours)
is_staff = True
working_hours = False
print(f"Is Staff: {is_staff}, During Working Hours: {working_hours}")
if is_staff and working_hours:
    print("✓ You can enter the restricted area")
else:
    print("✗ You cannot enter the restricted area")

print("\n")

print("B. USING OR (at least one condition must be TRUE):")
print("-" * 60)

# Example: Can watch movie? (Have money OR parents have money)
my_money = 0
parents_money = 500
print(f"My money: ${my_money}, Parents' money: ${parents_money}")
if my_money >= 100 or parents_money >= 100:
    print("✓ You can watch the movie!")
else:
    print("✗ You cannot watch the movie (no money)")

print()

# Example 2: Can use parking? (Member OR Have parking pass)
is_member = False
has_parking_pass = True
print(f"Is Member: {is_member}, Has Parking Pass: {has_parking_pass}")
if is_member or has_parking_pass:
    print("✓ You can use the parking")
else:
    print("✗ You cannot use the parking")

print("\n")

print("C. USING NOT (reverses the condition):")
print("-" * 60)

# Example: Are you underage?
age = 20
print(f"Age: {age}")
if not age < 18:
    print("✓ You are NOT a minor (you are 18+)")
else:
    print("✗ You are a minor")

print()

# Example 2: Is it NOT raining?
is_raining = False
print(f"Is raining: {is_raining}")
if not is_raining:
    print("✓ Great! It's not raining - let's play outside")
else:
    print("✗ Sorry, it's raining - stay inside")

print("\n")