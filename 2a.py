def linear_search(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1

n = int(input("enter the no of elements: "))

arr = []
for i in range(n):
    arr.append(int(input("enter the element: ")))

k = int(input("enter the search element: "))

print(linear_search(arr, k))
