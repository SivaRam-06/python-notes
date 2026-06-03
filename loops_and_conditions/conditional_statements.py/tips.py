# ═════════════════════════════════════════════════════════════════════════════
# 7. IMPORTANT NOTES
# ═════════════════════════════════════════════════════════════════════════════
"""
KEY POINTS TO REMEMBER:

1. INDENTATION (Spaces are important!)
   ✓ Correct:
       if age >= 18:
           print("Adult")  ← Indented with 4 spaces
   
   ✗ Wrong:
       if age >= 18:
       print("Adult")  ← NOT indented (will cause error)

2. COLON (:) is required
   ✓ if age >= 18:     ← Has colon
   ✗ if age >= 18      ← Missing colon (error)

3. Condition MUST be True or False (boolean)
   ✓ if age > 18:      ← Results in True or False
   ✓ if is_student:    ← Variable containing True or False
   ✗ if age:           ← Not clear (but will work - truthy/falsy)

4. Single = is ASSIGNMENT, == is COMPARISON
   ✓ if name == "Ali":     ← Compares values
   ✗ if name = "Ali":      ← ERROR! Assigns value

5. Comparison Operators
   == Equal to
   != Not equal to
   >  Greater than
   <  Less than
   >= Greater than or equal
   <= Less than or equal

6. Always check ALL conditions even if one is TRUE
   In IF-ELIF-ELSE, only the FIRST TRUE condition runs
   
7. ORDER MATTERS in IF-ELIF
   if marks >= 60:
       print("Pass")
   elif marks >= 70:
       print("Distinction")
   
   Above is WRONG! If marks = 75, only "Pass" will print
   
   CORRECT:
   if marks >= 70:
       print("Distinction")
   elif marks >= 60:
       print("Pass")

8. NESTED CONDITIONS (conditions inside conditions)
   if age >= 18:
       if has_license:
           print("Can drive")
       else:
           print("Need license")
   else:
       print("Too young")
"""
