

def replace_arr(arr):
    rightMax = -1
    n = len(arr)
    arr[n - 1] = -1
    for i in n - 1, -1, -1:
        rightMax = max(rightMax, arr[i - 1])
        arr[i] = rightMax

        return arr


arr = [33,5656,3434,56565]
result = replace_arr(arr)