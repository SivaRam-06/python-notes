# ═════════════════════════════════════════════════════════════════════════════
# 6. REAL-WORLD EXAMPLES
# ═════════════════════════════════════════════════════════════════════════════
account_balance = 500
withdrawal_amount = 200
pin_correct = True

if pin_correct:
    if withdrawal_amount <= account_balance:
        new_balance = account_balance - withdrawal_amount
        print(f"✓ Withdrawal successful!")
        print(f"  Amount withdrawn: ${withdrawal_amount}")
        print(f"  New balance: ${new_balance}")
    else:
        print(f"✗ Insufficient balance!")
        print(f"  Your balance: ${account_balance}")
        print(f"  Requested: ${withdrawal_amount}")
else:
    print("✗ PIN is incorrect! Transaction cancelled.")

print("\n")

print("6. REAL-WORLD EXAMPLE 2: E-commerce Discount System")
print("-" * 60)

cart_total = 5000
customer_is_member = True
customer_purchase_history = 50000  # Total spent before

print(f"Cart Total: ${cart_total}")
print(f"Is Member: {customer_is_member}")
print(f"Total Previous Purchases: ${customer_purchase_history}")

discount_percentage = 0
if customer_is_member and customer_purchase_history >= 100000:
    discount_percentage = 20
elif customer_is_member and customer_purchase_history >= 50000:
    discount_percentage = 15
elif customer_is_member and cart_total >= 10000:
    discount_percentage = 10
elif customer_is_member:
    discount_percentage = 5
elif cart_total >= 10000:
    discount_percentage = 5

discount_amount = (cart_total * discount_percentage) / 100
final_amount = cart_total - discount_amount

print(f"\nDiscount: {discount_percentage}%")
print(f"Discount Amount: ${discount_amount:.2f}")
print(f"Final Amount to Pay: ${final_amount:.2f}")

print("\n")

print("6. REAL-WORLD EXAMPLE 3: School Admission System")
print("-" * 60)

entrance_marks = 85
category = "General"
has_sports_quota = False

print(f"Entrance Marks: {entrance_marks}")
print(f"Category: {category}")
print(f"Has Sports Quota: {has_sports_quota}")

if entrance_marks >= 90:
    print("✓ ADMITTED (Merit based - Excellent scores!)")
elif entrance_marks >= 75 and category == "Reserved":
    print("✓ ADMITTED (Reserved category)")
elif has_sports_quota and entrance_marks >= 70:
    print("✓ ADMITTED (Sports quota)")
elif entrance_marks >= 75:
    print("✓ ADMITTED (General merit)")
elif entrance_marks >= 60:
    print("⏳ On waiting list (Try next year)")
else:
    print("✗ NOT ADMITTED (Marks below cutoff)")

print("\n")