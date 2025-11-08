# Value return functions for payroll
FICA_RATE = 0.0765
FEDERAL_TAX_RATE = 0.08

def get_gross_pay(hours, rate):
    """Calculate gross pay, including overtime (over 40 hours at 1.5x rate)."""
    if hours <= 40:
        return hours * rate
    else:
        overtime = hours - 40
        return (40 * rate) + (overtime * rate * 1.5)

def get_fica_tax(gross_pay):
    """Calculate FICA tax from gross pay."""
    return gross_pay * FICA_RATE

def get_federal_tax(gross_pay):
    """Calculate federal tax from gross pay."""
    return gross_pay * FEDERAL_TAX_RATE
