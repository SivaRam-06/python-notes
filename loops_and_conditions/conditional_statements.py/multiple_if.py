# ═════════════════════════════════════════════════════════════════════════════
# 4. MULTIPLE ELIF STATEMENTS (More Complex Examples)
# ═════════════════════════════════════════════════════════════════════════════
# Example 1: Student fee discount based on marks and family income
marks = 78
family_income = 50000
print(f"Marks: {marks}, Family Income: ${family_income}")
if marks >= 90 and family_income < 100000:
    print("Discount: 50% (Excellent marks + Low income)")
elif marks >= 80 and family_income < 100000:
    print("Discount: 30% (Good marks + Low income)")
elif marks >= 90:
    print("Discount: 20% (Excellent marks)")
elif family_income < 50000:
    print("Discount: 15% (Very low income)")
else:
    print("No discount available")

print()

# Example 2: Movie age rating
age = 16
print(f"Your age: {age}")
if age < 13:
    print("Allowed to watch: G (General Audiences)")
elif age < 17:
    print("Allowed to watch: PG-13, PG (Parental Guidance Suggested)")
elif age < 18:
    print("Allowed to watch: PG-13, PG, R (Restricted)")
else:
    print("Allowed to watch: All movies including NC-17")

print()

# Example 3: BMI (Body Mass Index) Category
height = 1.75  # meters
weight = 70    # kilograms
bmi = weight / (height ** 2)
print(f"Height: {height}m, Weight: {weight}kg, BMI: {bmi:.2f}")
if bmi < 18.5:
    print("Category: Underweight (You might need to eat more)")
elif bmi < 25:
    print("Category: Normal weight (You are healthy!)")
elif bmi < 30:
    print("Category: Overweight (Exercise might help)")
else:
    print("Category: Obese (Consult a doctor)")

print("\n")
