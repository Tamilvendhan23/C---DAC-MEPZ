
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

# Assignment question 7

# Assignment question 8