from list_utils import (
    filter_sales_above,
    get_sales_summary,
    get_reversed_sales,
    get_sorted_sales
)

def main():
    sales = [1200, 850, 1600, 900, 2000, 1100]

    print("Original sales:", sales)

    filtered = filter_sales_above(sales, 1000)
    print("Filtered sales (>1000):", filtered)

    first_last = get_sales_summary(sales, 2, 2)
    print("First 2 and Last 2 sales:", first_last)

    reversed_sales = get_reversed_sales(sales)
    print("Reversed sales:", reversed_sales)

    sorted_sales = get_sorted_sales(sales)
    print("Sorted sales:", sorted_sales)

    sorted_desc = get_sorted_sales(sales, descending=True)
    print("Sorted sales (descending):", sorted_desc)

    print("Sales after all operations:", sales)

if __name__ == "__main__":
    main()
