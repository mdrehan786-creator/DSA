def binary_search(arr, k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if k == arr[mid]:
            return mid
        elif k < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

n = int(input("enter the no of elements: "))
arr = []
for i in range(n):
    arr.append(int(input("enter the element: ")))

k = int(input("enter the search element: "))
print(binary_search(arr, k))
