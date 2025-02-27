def linear_search(items, value):
    for index, item in enumerate(items):
        if value == item:
            return index
        
    return -1


items = list(map(int, input("Enter items separated by space: ").split()))
item = int(input("Item: "))

result = linear_search(items, item)

if result >= 0:
    print(f"found at: {result}")
else:
    print(f"item not found")
        