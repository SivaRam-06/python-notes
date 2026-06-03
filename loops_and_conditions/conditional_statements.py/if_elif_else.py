# ═════════════════════════════════════════════════════════════════════════════
# 3. IF-ELIF-ELSE STATEMENT
# ═════════════════════════════════════════════════════════════════════════════
"""
IF-ELIF-ELSE:
    Syntax:
        if condition1:
            # Code if condition1 is TRUE
        elif condition2:
            # Code if condition1 is FALSE and condition2 is TRUE
        elif condition3:
            # Code if condition1 and condition2 are FALSE and condition3 is TRUE
        else:
            # Code if all above conditions are FALSE
    
    • Use ELIF for multiple conditions
    • Check conditions in ORDER - first TRUE condition runs
    • Conditions after first TRUE one are NOT checked
    • ELSE is optional (for when no conditions match)
"""

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║                 SECTION 3: IF-ELIF-ELSE STATEMENT                     ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

print("3. IF-ELIF-ELSE STATEMENT")
print("-" * 60)

# Example 1: Grade system based on marks
marks = 85
print(f"Marks: {marks}")
if marks >= 90:
    print("Grade: A+ (Excellent!)")
elif marks >= 80:
    print("Grade: A (Very Good!)")
elif marks >= 70:
    print("Grade: B (Good!)")
elif marks >= 60:
    print("Grade: C (Pass)")
else:
    print("Grade: F (Fail - Need to improve)")

print()

# Example 2: Traffic light system
light_color = "yellow"
print(f"Traffic light: {light_color}")
if light_color == "red":
    print("STOP! Wait at the signal.")
elif light_color == "yellow":
    print("PREPARE! Get ready to move.")
elif light_color == "green":
    print("GO! The path is clear.")
else:
    print("Invalid traffic light color")

print()

# Example 3: Age group classification
age = 25
print(f"Age: {age}")
if age < 13:
    print("Category: Child")
elif age < 18:
    print("Category: Teenager")
elif age < 60:
    print("Category: Adult")
else:
    print("Category: Senior")

print()

# Example 4: Size selection (S, M, L, XL)
shirt_size = "M"
print(f"Shirt size: {shirt_size}")
if shirt_size == "S":
    print("Size: Small (fits most 8-10 year old kids)")
elif shirt_size == "M":
    print("Size: Medium (fits most teenagers and adults)")
elif shirt_size == "L":
    print("Size: Large (fits bigger adults)")
elif shirt_size == "XL":
    print("Size: Extra Large (fits very big adults)")
else:
    print("Size not available")

print("\n")