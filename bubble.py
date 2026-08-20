def bubble_sort(arr):
    n=len(arr)
    for i in range(1,n):
        for j in range(n-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
num=int(input("enter number of elements:"))
arr=[]
for i in range(num):
    temp=int(input("enter number:"))
    arr.append(temp)
bubble_sort(arr)
print(arr)
