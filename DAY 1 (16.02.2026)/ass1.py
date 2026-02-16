from my_utils import categorize_person

age= int(input(" enter the age: "))
print("the given age is belongs to",categorize_person(age))
print("the id value of age is ",id(age))
print(" the type of return value is ",type(age))