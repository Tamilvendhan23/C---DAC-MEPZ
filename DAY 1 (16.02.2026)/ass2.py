from my_utils import calculate_stipend_bonus

def main():
    stipend=int(input("enter stipend value: "))
    rating=int (input("enter rating value: "))
    print("for stipend of ",stipend,"with rating ",rating, "bonus is ",calculate_stipend_bonus(stipend, rating))
    print(f"id value of stipend {stipend} value is ",id(stipend))
main()