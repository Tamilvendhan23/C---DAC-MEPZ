def get_unique_cities(cities: list) -> list:
    if not isinstance(cities, list):
        raise TypeError("cities must be a list")

    unique = []
    for city in cities:
        if not isinstance(city, str):
            raise TypeError("city must be string")
        if city not in unique:
            unique.append(city)

    return unique


def get_sorted_cities(cities: list, descending: bool = False) -> list:
    if not isinstance(cities, list):
        raise TypeError("cities must be a list")
    if not isinstance(descending, bool):
        raise TypeError("descending must be boolean")

    return sorted(cities, reverse=descending)


def convert_cities_to_upper(cities: list) -> list:
    if not isinstance(cities, list):
        raise TypeError("cities must be a list")

    return [city.upper() for city in cities]
