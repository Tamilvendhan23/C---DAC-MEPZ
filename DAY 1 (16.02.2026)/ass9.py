from my_utils import check_addmission
def main():

    print("enter the value of the marks, age, city : ")
    m, n, c = input().split()
    m = int(m)
    n = int(n)
    res=check_addmission(m,n,c)
    print(res)
main()