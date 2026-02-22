from person import Person
from invalid_salary_error import InvalidSalaryError


class Employee(Person):
    company_name = "Vinod Technologies"

    def __init__(self, emp_id: str, name: str, city: str, salary: float):
        super().__init__(name, city)

        if not self.is_valid_salary(salary):
            raise InvalidSalaryError("Salary must be greater than zero")

        self.emp_id = emp_id
        self.__salary = salary

    @staticmethod
    def is_valid_salary(salary: float) -> bool:
        return salary > 0

    def get_salary(self) -> float:
        return self.__salary

    def update_salary(self, new_salary: float) -> None:
        if not self.is_valid_salary(new_salary):
            raise InvalidSalaryError("Invalid salary update")
        self.__salary = new_salary

    def get_details(self) -> str:
        return (
            f"Emp ID: {self.emp_id}, "
            f"Name: {self.name}, "
            f"City: {self.city}, "
            f"Salary: {self.__salary}"
        )

    def __add__(self, other):
        if not isinstance(other, Employee):
            raise TypeError("Can only add Employee objects")
        return self.__salary + other.__salary

    def __str__(self):
        return self.get_details()

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return False
        return self.emp_id == other.emp_id

    @classmethod
    def change_company_name(cls, new_name: str):
        cls.company_name = new_name