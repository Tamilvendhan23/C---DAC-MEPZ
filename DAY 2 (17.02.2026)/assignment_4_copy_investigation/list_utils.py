def filter_sales_above(sales: list, threshold: int) -> list:
    if not isinstance(sales, list):
        raise TypeError("sales must be a list")
    if not isinstance(threshold, int):
        raise TypeError("threshold must be integer")
    for s in sales:
        if not isinstance(s, int):
            raise TypeError("sales values must be integers")

    return [s for s in sales if s > threshold]


def get_sales_summary(sales: list, first_n: int, last_n: int) -> tuple:
    if not isinstance(sales, list):
        raise TypeError("sales must be a list")
    if not isinstance(first_n, int) or not isinstance(last_n, int):
        raise TypeError("first_n and last_n must be integers")
    if first_n < 0 or last_n < 0:
        raise ValueError("first_n and last_n must be non-negative")

    first_part = sales[:first_n]
    last_part = sales[-last_n:] if last_n != 0 else []

    return (first_part, last_part)


def get_reversed_sales(sales: list) -> list:
    if not isinstance(sales, list):
        raise TypeError("sales must be a list")

    return sales[::-1]


def get_sorted_sales(sales: list, descending: bool = False) -> list:
    if not isinstance(sales, list):
        raise TypeError("sales must be a list")
    if not isinstance(descending, bool):
        raise TypeError("descending must be boolean")

    return sorted(sales, reverse=descending)
