from random import randint


def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


data_list = [randint(1, 1_000) for i in range(10)]

print(f"Unsorted List: {data_list}")

sorted_list = selection_sort(data_list)
print(sorted_list)

print()

print("Time Complexity:", "O(n ^ 2)")
