from my_utils import validate_password

def main():
    pas=input("enter password: ").strip()
    print(validate_password(pas))
main()
