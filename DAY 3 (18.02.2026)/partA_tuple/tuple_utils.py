# Tuple Assignment 1

def create_employee(emp_id: str, name: str, city: str, salary: float) -> tuple:
    if not emp_id or not name or not city:
        raise ValueError("emp_id, name, city cannot be empty")
    if not isinstance(salary, (int, float)) or salary <= 0:
        raise ValueError("salary must be positive")

    return (emp_id, name, city, salary)


def update_salary(employee: tuple, new_salary: float) -> tuple:
    if not isinstance(employee, tuple):
        raise TypeError("employee must be tuple")
    if new_salary <= 0:
        raise ValueError("salary must be positive")

    emp_id, name, city, _ = employee
    return (emp_id, name, city, new_salary)


def get_employee_details(employee: tuple) -> str:
    emp_id, name, city, salary = employee
    return f"ID: {emp_id}, Name: {name}, City: {city}, Salary: {salary}"


# Tuple Assignment 2

def get_highest_revenue(revenues: tuple) -> int:
    return max(revenues)


def get_lowest_revenue(revenues: tuple) -> int:
    return min(revenues)


def count_revenue_occurrence(revenues: tuple, value: int) -> int:
    return revenues.count(value)
