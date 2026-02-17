
from my_utils import interest_growth

def main():
    p = float(input("Enter principal amount: "))
    r = float(input("Enter yearly interest rate (%): "))

    years_needed = interest_growth(p, r)
    print(f"\nAmount doubled in {years_needed} years.")


main()
