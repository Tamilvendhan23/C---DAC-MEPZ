from employee_service import *

def main():
    add_employee("EMP101", "Vinod", "Bangalore", 75000)
    add_employee("EMP102", "Amit", "Delhi", 60000)

    print("\n--- Employees ---")
    list_employees()

    print("\n--- Edit EMP102 ---")
    edit_employee("EMP102", salary=65000)
    list_employees()

    print("\n--- Delete EMP101 ---")
    delete_employee("EMP101")
    list_employees()

if __name__ == "__main__":
    main()
