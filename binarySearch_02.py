# Task-03: Binary Search Algorithm

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    step = 1

    print("Step\tLow\tHigh\tMid\tValue\tAction")

    while low <= high:
        mid = (low + high) // 2
        value = arr[mid]

        if value == target:
            print(step, "\t", low, "\t", high, "\t", mid, "\t", value, "\tFound")
            return mid

        elif value < target:
            print(step, "\t", low, "\t", high, "\t", mid, "\t", value,
                  "\tTarget is greater, so low = mid + 1")
            low = mid + 1

        else:
            print(step, "\t", low, "\t", high, "\t", mid, "\t", value,
                  "\tTarget is smaller, so high = mid - 1")
            high = mid - 1

        step += 1

    return -1


numbers = [6, 12, 17, 23, 38, 45, 77, 84, 90]
target = 38

print("Array:", numbers)
print("Searching for:", target)
print()

result = binary_search(numbers, target)

if result != -1:
    print()
    print("Element found at index", result)
else:
    print()
    print("Element not found.")

