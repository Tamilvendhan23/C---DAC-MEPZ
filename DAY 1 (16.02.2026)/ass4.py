from my_utils import evaluate_marks

def main():
    m=int(input("enter marks: "))
    at=int(input("enter attendance: "))
    print("result is ", evaluate_marks(m,at))
main()