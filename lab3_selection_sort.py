def selection_sort(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a

if __name__ == "__main__":
    values = list(map(int, input("Enter integers separated by spaces: ").split()))
    print("Sorted list:", selection_sort(values))
