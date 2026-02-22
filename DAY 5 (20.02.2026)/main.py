from employee import Employee
from invalid_salary_error import InvalidSalaryError

if __name__ == "__main__":
    try:
        emp1 = Employee("EMP101", "Vinod", "Bangalore", 75000)
        emp2 = Employee("EMP102", "Amit", "Delhi", 60000)

        print(emp1.get_details())
        print(emp2)

        emp1.update_salary(80000)
        print("Updated Salary:", emp1.get_salary())

        total_salary = emp1 + emp2
        print("Total Salary:", total_salary)

        print("Company:", Employee.company_name)

        Employee.change_company_name("Vinod Global Tech")
        print("Updated Company:", Employee.company_name)

        # Trigger custom exception
        emp3 = Employee("EMP103", "Ravi", "Chennai", -5000)

    except InvalidSalaryError as e:
        print("Salary Error:", e)

    except TypeError as e:
        print("Type Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)