from datetime import datetime

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday()


subtotal_str = input("Please enter the subtotal: $")
subtotal = float(subtotal_str)

DISCOUNT_THRESHOLD = 50.0
DISCOUNT_RATE = 0.10
SALES_TAX_RATE = 0.06

discount_amount = 0.0

is_tuesday = day_of_week == 1
is_wednesday = day_of_week == 2

if (is_tuesday or is_wednesday) and subtotal >= DISCOUNT_THRESHOLD:
    discount_amount = subtotal * DISCOUNT_RATE

price_before_tax = subtotal - discount_amount

sales_tax_amount = price_before_tax * SALES_TAX_RATE

final_total = price_before_tax + sales_tax_amount

print(f"\n--- Receipt ---")
print(f"Discount amount: ${discount_amount:.2f}")
print(f"Sales tax amount: ${sales_tax_amount:.2f}")
print(f"Total: ${final_total:.2f}")
