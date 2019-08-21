def partition(a, start, end):
    pivot = a[end]
    i = start

    for j in range(start, end):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1

    a[end] = a[i]
    a[i] = pivot
    return i


def sort(a, start, end):
    if start > end:
        return
    i = partition(a, start, end)
    sort(a, start, i - 1)
    sort(a, i + 1, end)


a = [1, 3, 2, 5, 2, 6, 8, 8]
sort(a, 0, 7)
print(a)
