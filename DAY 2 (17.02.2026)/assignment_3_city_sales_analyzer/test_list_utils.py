from list_utils import (
    create_shallow_copy,
    create_deep_copy,
    append_to_nested_list
)

def main():
    student_data = ["Vinod", ["Mumbai", "Delhi"]]

    print("Original data:", student_data)
    print("Original ID:", id(student_data))
    print("Nested list ID:", id(student_data[1]))

    print("\n--- Shallow Copy Test ---")
    shallow = create_shallow_copy(student_data)
    print("Shallow copy:", shallow)
    print("Shallow ID:", id(shallow))
    print("Shallow nested ID:", id(shallow[1]))

    append_to_nested_list(shallow, "Chennai")
    print("After modifying shallow copy:")
    print("Original data:", student_data)
    print("Shallow copy:", shallow)

    print("\n--- Deep Copy Test ---")
    deep = create_deep_copy(student_data)
    print("Deep copy:", deep)
    print("Deep ID:", id(deep))
    print("Deep nested ID:", id(deep[1]))

    append_to_nested_list(deep, "Bangalore")
    print("After modifying deep copy:")
    print("Original data:", student_data)
    print("Deep copy:", deep)

if __name__ == "__main__":
    main()
