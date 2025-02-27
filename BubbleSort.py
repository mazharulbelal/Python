def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]
    return arr

def bubble_sort(arr):
    for index in range(len(arr)):
        for innerIndex in range(len(arr) - index - 1):
            if arr[innerIndex] > arr[innerIndex + 1]:
                swap(arr, innerIndex, innerIndex + 1)

    return arr

result = bubble_sort([100,200,50,888,22])
print(result)