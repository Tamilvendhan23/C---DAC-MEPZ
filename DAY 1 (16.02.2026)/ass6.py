from my_utils import reverse_number

def main():
    n = int(input("Enter the number: "))
    res = reverse_number(n)
    
    print(f"The reversed value is: {res[0]}")
    print(f"The middle value is: {res[1]}")

main()
