# Dict Assignment 1

def add_employee(directory: dict, emp_id: str, data: dict) -> None:
    if emp_id in directory:
        print("Employee already exists")
        return
    directory[emp_id] = data


def get_employee(directory: dict, emp_id: str) -> dict:
    return directory.get(emp_id, {})


def delete_employee(directory: dict, emp_id: str) -> None:
    directory.pop(emp_id, None)


# Dict Assignment 2

def get_top_city(sales: dict) -> str:
    return max(sales, key=sales.get)


def get_low_sales_cities(sales: dict, threshold: int) -> dict:
    return {city: amt for city, amt in sales.items() if amt < threshold}


def increase_sales(sales: dict, percentage: float) -> dict:
    return {
        city: int(value + (value * percentage / 100))
        for city, value in sales.items()
    }
