from random import randint


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    left_partition = merge_sort(lst[:mid])
    right_partition = merge_sort(lst[mid:])

    return merge(left_partition, right_partition)


def merge(left, right):
    output = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output.extend(left[i:])
    output.extend(right[j:])

    return output


data_list = [randint(1, 1_000) for i in range(10)]

print(f"Unsorted List: {data_list}")

sorted_list = merge_sort(data_list)
print(sorted_list)

print()

print("Time Complexity:", "O(n * log(n))")
