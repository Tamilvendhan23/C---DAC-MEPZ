from my_utils import sum_of_digits


def main():
    n=int(input("Enter the number: "))
    sums=sum_of_digits(n)
    print(f"the sum of the given digits is {sums}")
main()