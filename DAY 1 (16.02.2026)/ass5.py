from my_utils import safe_integer_input

def main():
    n=input("enter promt : ").strip()
    res=safe_integer_input(n)
    print(res)
    print(type(res))

main()