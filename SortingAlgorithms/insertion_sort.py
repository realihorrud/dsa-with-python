from random import randint


def insertion_sort(lst):
    for i in range(len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key > lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


data_list = [randint(1, 10_000) for i in range(1, 10)]
print(f"Unsorted List: {data_list}")

result = insertion_sort(data_list)

print(result)

print()

print("Best Case Time Complexity:", "O(n)")
print("Worst Case Time Complexity:", "O(n ^ 2)")
