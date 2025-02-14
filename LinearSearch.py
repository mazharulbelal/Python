arr = [24,5,6,7,8,3,6]

def linear_search(arr, target):
    for index, value in enumerate(arr):
     if value == target:
        return index
    return -1


result = linear_search(arr, 7)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")