from my_utils import withdraw
def main():
    print("enter the amount and balance :  ")
    m,n=list(map(int,(input().split())))
    res=withdraw(m,n)
    print(f"the value of the result is : {res}")
main()
   