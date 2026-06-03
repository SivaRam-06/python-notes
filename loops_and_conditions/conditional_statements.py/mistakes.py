# ═════════════════════════════════════════════════════════════════════════════
# 8. COMMON MISTAKES
# ═════════════════════════════════════════════════════════════════════════════
"""
MISTAKE 1: Forgetting indentation
❌ WRONG:
if age >= 18:
print("Adult")

✓ CORRECT:
if age >= 18:
    print("Adult")

---

MISTAKE 2: Using = instead of ==
❌ WRONG:
if name = "Ali":
    print("Welcome")

✓ CORRECT:
if name == "Ali":
    print("Welcome")

---

MISTAKE 3: Forgetting colon
❌ WRONG:
if age >= 18
    print("Adult")

✓ CORRECT:
if age >= 18:
    print("Adult")

---

MISTAKE 4: Wrong order in IF-ELIF
❌ WRONG:
if marks >= 60:
    print("Pass")
elif marks >= 90:
    print("Excellent")  # This will never run if marks=95!

✓ CORRECT:
if marks >= 90:
    print("Excellent")
elif marks >= 60:
    print("Pass")

---

MISTAKE 5: Forgetting the condition is checked from top to bottom
❌ Code:
if marks >= 70:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")

If marks = 75:
    Only "A" will print, not "B" or "C"
"""