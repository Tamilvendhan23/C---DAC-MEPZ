# list_utils.py
# 1.1 assignment 
def validator(marks, n):
    if not isinstance(marks, list):
        raise TypeError("marks must be a list")

    for i in marks:
        if not isinstance(i, int):
            raise TypeError("all marks must be integers")

    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n <= 0:
        raise ValueError("n must be positive")


def get_top_n_marks(marks, n):
    validator(marks, n)
 
    marks_copy = marks.copy()
    marks_copy.sort(reverse=True)

    return marks_copy[:n]

# 1.2  assignment
def count_mark_occurrence(marks: list, value: int) -> int:
    if not isinstance(marks, list):
        raise TypeError("marks must be a list")

    for m in marks:
        if not isinstance(m, int):
            raise TypeError("all marks must be integers")

    if not isinstance(value, int):
        raise TypeError("value must be an integer")

    return marks.count(value)

# 1.3  assignment
def get_high_scorers(marks: list, threshold: int) -> list:
    if not isinstance(marks, list):
        raise TypeError("marks must be a list")

    for m in marks:
        if not isinstance(m, int):
            raise TypeError("all marks must be integers")

    if not isinstance(threshold, int):
        raise TypeError("threshold must be an integer")

    return [m for m in marks if m >= threshold]


