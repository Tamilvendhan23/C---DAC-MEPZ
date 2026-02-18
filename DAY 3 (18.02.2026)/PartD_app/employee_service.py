from my_utils import is_positive_number

employees = {}

def add_employee(emp_id, name, city, salary):
    if emp_id in employees:
        print("Employee exists")
        return
    if not is_positive_number(salary):
        print("Invalid salary")
        return

    employees[emp_id] = {"name": name, "city": city, "salary": salary}


def edit_employee(emp_id, name=None, city=None, salary=None):
    emp = employees.get(emp_id)
    if not emp:
        print("Employee not found")
        return

    if name:
        emp["name"] = name
    if city:
        emp["city"] = city
    if salary is not None:
        if not is_positive_number(salary):
            print("Invalid salary")
            return
        emp["salary"] = salary


def delete_employee(emp_id):
    if emp_id in employees:
        employees.pop(emp_id)
    else:
        print("Employee not found")


def list_employees():
    for emp_id, data in employees.items():
        print(emp_id, data["name"], data["city"], data["salary"])
