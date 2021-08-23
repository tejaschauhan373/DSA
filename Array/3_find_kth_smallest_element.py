arr = list(map(int, input().split()))
k = int(input())

def merge(arr, l, mid, r):
    n1 = mid - l + 1
    n2 = r - mid

    a = []
    b = []

    for i in range(n1):
        a.append(arr[l + i])

    for j in range(n2):
        b.append(arr[mid + j + 1])

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:

        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
            k += 1
        else:
            arr[k] = b[j]
            j += 1
            k += 1

    while i < n1:
        arr[k] = a[i]
        k += 1
        i += 1

    while j < n2:
        arr[k] = b[j]
        k += 1
        j += 1


def mergeSort(arr, l, r):
    if l < r:
        mid = (r + l) // 2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid + 1, r)
        merge(arr, l, mid, r)


mergeSort(arr, 0, len(arr) - 1)
print(arr[k - 1])

# Quick Sort
#https://www.youtube.com/watch?v=eA3PMKlRZs8