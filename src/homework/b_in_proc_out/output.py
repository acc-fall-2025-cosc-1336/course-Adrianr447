TAX_RATE = 0.0675

def multiply_numbers(a, b):
    """Returns the product of a and b."""
    return a * b

def get_sales_tax_amount(meal_amount):
    """Returns the sales tax for the given meal amount using the TAX_RATE constant."""
    return meal_amount * TAX_RATE

def get_tip_amount(meal_amount, tip_rate):
    """Returns the tip amount for the given meal amount and tip rate."""
    return meal_amount * tip_rate