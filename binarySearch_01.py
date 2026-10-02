# Binary Search Algorithm

numbers = list(map(int, input("Enter sorted elements separated by spaces: ").split()))

target = int(input("Enter the value to search: "))

low = 0
high = len(numbers) - 1

found = False

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == target:
        print("Element found at index", mid)
        found = True
        break

    elif numbers[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

if not found:
    print("Element not found.")