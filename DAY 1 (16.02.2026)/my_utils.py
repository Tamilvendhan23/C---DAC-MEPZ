import my_utils
def factorial(num):

    if type(num)!=int:
        raise TypeError("only valid number accepted")
    if num<0:
        raise ValueError("it seems to be eror")
    
    f=1
    while(num>0):
        f*=num
        num-=1
    return f

# Assignment question 1 
def categorize_person(age):
    if type(age)!= int:
        raise TypeError("check the input!!")
    if age<0 or age>120:
        raise ValueError("enter valid age!!")
    if age>0 and age<=12:
        return "child"
    elif age>12 and age<=19:
        return "Teenager"
    elif age>20 and age<=59:
        return "Teenager"
    elif age>=60:
        return "Senior Citizen"
    
# Assignment question 2
def calculate_stipend_bonus(stipend, rating):
    bonus=0
    if stipend>0 and rating>0 and rating<=5:
        if rating==5:
            bonus=0.03*stipend
        elif rating==4:
            bonus=0.02*stipend
        elif rating==3:
            bonus=0.01*stipend
        else:
            bonus=0
    return bonus

# Assignment question 3
def validate_password(pas):
    if len(pas)<8:
        raise ValueError ("Please ensure! The password contains eight characters!!")
        
    count=0
    for i in pas:
        if i.isalpha():
            count+=1
    if not count:
        raise ValueError("Password contains Atleast one digit!!")
    count=0
    for i in pas:
        if i.isupper():
            count+=1
    if not count: 
        raise ValueError("Password must contains one Uppercase:")
    return "Valid password"

# Assignment question 4
def evaluate_marks(marks, attendance):
    if not ((marks>0 and marks<=100) and (attendance>0 and attendance<=100)):
        raise ValueError("Invalid inputs")
    if marks>=90:
        return "A grade"
    elif marks>=75 and marks<90:
        return "B grade"
    elif marks>=50 and marks<75:
        return "C grade"
    elif marks<50:
        return "fail"

# Assignment question 5
def safe_integer_input(promt):

    if not promt.isnumeric():
        raise TypeError("enter the valid promt")
    conver=int(promt)
    return conver


# Assignment question 6
def reverse_number(n):
    if n < 0:
        raise ValueError("Number should be positive!!")
    
    rev = str(n)[::-1]  
    middle_value = rev[len(rev)//2]
    
    return [rev, middle_value]

# Assignment question 7
def sum_of_digits(n):
    if n<0:
        raise ValueError("value must be postive!!")
    while n >= 10:  
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        n = total
    
    return n

# Assignment question 8
def withdraw(balance,amount):
    if  not type(balance)==int:
        raise TypeError("balance should a number")
    if not  type(amount)==int:
        raise TypeError("amount should a number")
    if not (balance>amount):
        raise ValueError("check the balance and enter the amount")
    if amount%100!=0:
        raise ValueError("amount must be multiples of 100")
    return balance-amount

# Assignment question 9
def check_addmission(marks,age,city):

    if not type(marks)==int:
        raise TypeError("Marks should be in number!!")
    if not type(age)==int:
        raise TypeError("age should be in the number!!")
    c=['mumbai','pune','delhi']
    
    if city.lower() not in c:
        raise ValueError("enter valid city!!")
    if marks>=70 and age>=18:
        return "Approved"
    return "Denied"


 # Assignment question 10
def interest_growth(principal, rate):
    if rate <= 0:
        raise ValueError("Rate must be greater than 0!")

    years = 0
    amount = principal
    target = principal * 2

    while amount < target:
        years += 1
        amount += amount * (rate / 100)
        print(f"Year {years}: {amount:.2f}")

    return years
