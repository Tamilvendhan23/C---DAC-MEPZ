def load_employees(file_path: str) -> list:
    employees = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                emp_id, name, city, salary = line.strip().split(",")
                employees.append({
                    "id": emp_id,
                    "name": name,
                    "city": city,
                    "salary": float(salary)
                })
    except FileNotFoundError:
        pass
    return employees


def save_employees(file_path: str, emp_list: list) -> None:
    with open(file_path, "w") as file:
        for emp in emp_list:
            file.write(f"{emp['id']},{emp['name']},{emp['city']},{emp['salary']}\n")