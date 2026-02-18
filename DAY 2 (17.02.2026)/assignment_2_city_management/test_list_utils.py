from list_utils import (
    get_unique_cities,
    get_sorted_cities,
    convert_cities_to_upper
)

def main():
    cities = ["Chennai", "Delhi", "Mumbai", "Chennai", "Delhi"]

    print("Original cities:", cities)
    print("Unique cities:", get_unique_cities(cities))
    print("Sorted A-Z:", get_sorted_cities(cities))
    print("Sorted Z-A:", get_sorted_cities(cities, descending=True))
    print("Uppercase:", convert_cities_to_upper(cities))
    print("Cities unchanged:", cities)

if __name__ == "__main__":
    main()
