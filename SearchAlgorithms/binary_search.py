def binary_search(lst, target, low, high):
    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid
        elif target > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return None


lst = [3, 4, 5, 6, 7, 8, 9, 10]

# target value to be searched for
target = 10

result = binary_search(lst, target, 0, len(lst) - 1)

if result:
    print(f"Element {target} is found at index {result}")
else:
    print(f"{target} is not found in the list")

print()

print("Best Case Time Complexity:", "O(1)")
print("Average Case Time Complexity:", "O(log(n))")
print("Worst Case Time Complexity:", "O(log(n))")
