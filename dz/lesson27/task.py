def binary_search(arr, target, left, right):
    if left > right:
        return -1  

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)


arr = [1, 3, 5, 7, 9, 11]
target = 7
index = binary_search(arr, target, 0, len(arr)-1)
print("Binary search index:", index)
