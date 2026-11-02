def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    smaller = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    larger = [x for x in a if x > pivot]
    return quick_sort(smaller) + equal + quick_sort(larger)

if __name__ == "__main__":
    values = list(map(int, input("Enter integers separated by spaces: ").split()))
    print("Sorted list:", quick_sort(values))
