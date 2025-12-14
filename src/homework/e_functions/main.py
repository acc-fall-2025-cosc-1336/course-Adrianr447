from src.homework.e_functions.value_return_functions import get_gross_pay, get_fica_tax, get_federal_tax
from src.homework.e_functions.void_functions import display_payroll_check

def main():
    try:
        hours = float(input("Enter hours worked: "))
        rate = float(input("Enter hourly rate: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    gross = get_gross_pay(hours, rate)
    fica = get_fica_tax(gross)
    federal = get_federal_tax(gross)
    net = gross - fica - federal
    print("\nPayroll Check:")
    display_payroll_check(gross, fica, federal, net)

if __name__ == "__main__":
    main()