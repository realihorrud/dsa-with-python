from random import randint


def quick_sort(lst):
    length = len(lst)

    if length <= 1:
        return lst
    else:
        pivot = lst.pop()

    left = []
    right = []
    for elem in lst:
        if elem < pivot:
            left.append(elem)
        else:
            right.append(elem)

    return quick_sort(left) + [pivot] + quick_sort(right)


data_list = [randint(1, 10_000) for i in range(1, 10)]
print(f"Unsorted List: {data_list}")

result = quick_sort(data_list)

print(result)

print()

print("Best Case Time Complexity:", "O(n * log(n))")
