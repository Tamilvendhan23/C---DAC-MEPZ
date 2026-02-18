import copy

# 3.1 Shallow Copy
def create_shallow_copy(data: list) -> list:
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    return data.copy()   # shallow copy


# 3.2 Deep Copy
def create_deep_copy(data: list) -> list:
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    return copy.deepcopy(data)


# 3.3 Append to Nested List
def append_to_nested_list(data: list, value) -> None:
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    for item in data:
        if isinstance(item, list):
            item.append(value)
            return
