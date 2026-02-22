class Person:
    def __init__(self, name: str, city: str):
        self.name = name
        self.city = city

    def get_details(self) -> str:
        return f"Name: {self.name}, City: {self.city}"