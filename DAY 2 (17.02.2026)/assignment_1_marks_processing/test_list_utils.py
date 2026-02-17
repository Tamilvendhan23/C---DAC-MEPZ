from list_utils import get_top_n_marks

def main():
    marks_input=(input("enter marks list : "))
    top=int(input(" how many top marks needed: "))
    marks = []
    for value in marks_input.split():
         marks.append(int(value))
         res=get_top_n_marks(marks,top)
    print(f"Result of the entered marks is {res}")


if __name__ == "__main__":
    main()