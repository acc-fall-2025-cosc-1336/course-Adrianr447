import sys
import os

try:
    from .output import get_sales_tax_amount, get_tip_amount, TAX_RATE
except Exception:
    # Allow running this file directly (as a script) by adding the current package folder
    # to sys.path and importing the sibling module.
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from output import get_sales_tax_amount, get_tip_amount, TAX_RATE

def main():
    try:
        meal_amount = float(input("Enter the meal amount: "))
        tip_rate = float(input("Enter the tip rate (as a decimal, e.g., 0.15 for 15%): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    sales_tax = get_sales_tax_amount(meal_amount)
    tip_amount = get_tip_amount(meal_amount, tip_rate)
    total = meal_amount + sales_tax + tip_amount

    print("\nReceipt")
    print(f"Meal Amount:   {meal_amount:.2f}")
    print(f"Sales Tax:     {sales_tax:.2f}")
    print(f"Tip Amount:    {tip_amount:.2f}")
    print(f"Total:         {total:.2f}")

if __name__ == "__main__":
    main()
