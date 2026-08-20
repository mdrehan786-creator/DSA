def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
num=int(input("enter number of elements:"))
arr=[]
for i in range(num):
    temp=int(input("enter number:"))
    arr.append(temp)
selection_sort(arr)
print(arr)
