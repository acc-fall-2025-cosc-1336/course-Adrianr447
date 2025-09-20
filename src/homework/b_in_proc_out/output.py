TAX_RATE = 0.0675  # 6.75%

def get_sales_tax_amount(meal_amount: float) -> float:
    """
    Calculate sales tax for the given meal amount.
    """
    return meal_amount * TAX_RATE

def get_tip_amount(meal_amount: float, tip_rate: float) -> float:
    """
    Calculate tip for the given meal amount and tip rate.
    """
    return meal_amount * tip_rate