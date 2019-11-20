def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + high
        guess = arr[mid]
        if guess == key:
            return mid
        if guess < key:
            low = mid + 1
        if guess > key:
            high = mid - 1
    return None


numList = [1, 2, 5, 6, 10]
print(binary_search(numList, 5))
print(binary_search(numList, 3))

