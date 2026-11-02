def bubble_sort(a):
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

if __name__ == "__main__":
    values = list(map(int, input("Enter integers separated by spaces: ").split()))
    print("Sorted list:", bubble_sort(values))
