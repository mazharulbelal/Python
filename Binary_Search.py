def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


arr = [1, 3, 5, 7, 9, 11]
target = 11
result = binary_search(arr, target)
print(result)