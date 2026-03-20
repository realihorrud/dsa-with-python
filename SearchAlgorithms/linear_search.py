from random import randint


def linear_search(lst, target):
    for index, value in enumerate(lst):
        if target == value:
            return index
    return None


data_lst = [randint(1, 100) for i in range(100)]
print(linear_search(data_lst, randint(1, 100)))

print()

print("Best Case Time Complexity:", "O(1)")
print("Average Case Time Complexity:", "O(n)")
print("Worst Case Time Complexity:", "O(n)")
