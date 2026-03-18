from random import randint


def counting_sort(lst):
    if len(lst) <= 1:
        return lst
    max_elem = max(lst)
    new_lst = [0] * (max_elem + 1)
    for elem in lst:
        new_lst[elem] += 1

    sorted_output = []
    for index in range(len(new_lst) - 1, -1, -1):
        value = new_lst[index]
        if value != 0:
            sorted_output.extend([index] * value)
    return sorted_output


# Since counting sort uses the indexes of a list for sorting, it cannot be used for floating-point numbers.

data_list = [randint(1, 10_000) for i in range(1, 10)]
print(f"Unsorted List: {data_list}")

# Sort the list in descending direction
result = counting_sort(data_list)

print(result)

print()

print("Time Complexity:", "O(n + k)")
