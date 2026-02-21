from services.employee_service import (
    add_employee,
    edit_employee,
    delete_employee,
    list_employees
)
from utils.file_utils import load_employees, save_employees
from tabulate import tabulate

DATA_FILE = "data/employees.txt"


def menu():
    print("""
1. Add Employee
2. Edit Employee
3. Delete Employee
4. List Employees
5. Save to File
6. Exit
""")


if __name__ == "__main__":
    employees = load_employees(DATA_FILE)

    while True:
        try:
            menu()
            choice = input("Enter choice: ")

            if choice == "1":
                add_employee(
                    employees,
                    input("ID: "),
                    input("Name: "),
                    input("City: "),
                    float(input("Salary: "))
                )

            elif choice == "2":
                edit_employee(
                    employees,
                    input("ID: "),
                    name=input("New Name: "),
                    city=input("New City: "),
                    salary=float(input("New Salary: "))
                )

            elif choice == "3":
                delete_employee(employees, input("ID: "))

            elif choice == "4":
                print(tabulate(list_employees(employees), headers="keys"))

            elif choice == "5":
                save_employees(DATA_FILE, employees)
                print("Saved")

            elif choice == "6":
                if input("Save before exit? (y/n): ").lower() == "y":
                    save_employees(DATA_FILE, employees)
                break

            else:
                print("Invalid option")

        except ValueError as e:
            print("Error:", e)
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Unexpected error:", e)