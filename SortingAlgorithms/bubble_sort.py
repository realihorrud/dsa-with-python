from random import randint


def bubble_sort(lst):
    """
    Use bubble sort for:
        - small datasets
        - when simplicity is more important than effiency
        - when the data is already partially sorted
    """

    size = len(lst)
    for i in range(size):
        swapped = False

        for j in range(size - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        if not swapped:
            # List has already been sorted
            break

    return lst


data_list = [randint(1, 1_000) for i in range(10)]
print(f"Unsorted List: {data_list}")

sorted_list = bubble_sort(data_list)
print(f"Sorted List: {sorted_list}")

print()

print("Best Case Time Complexity:", "O(n)")
print("Worst Case Time Complexity:", "O(n ^ 2)")
print("Average Case Time Complexity:", "O(n ^ 2)")
