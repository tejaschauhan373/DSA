# https://leetcode.com/problems/kth-largest-element-in-an-array

def partition(arr: list, start: int, end: int) -> int:
    i = start - 1
    j = start
    pivot = arr[end]
    while j < end:
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quicksort(arr: list, start: int, end: int, kth: int):
    """
    Time Complexity in Average Case = O(NlogN)
    Time Complexity in Worst Case = O(N*N)
    Space Complexity = O(1)
    """
    if start > end:
        return

    p = partition(arr, start, end)
    if p == kth:
        return arr[p]
    elif p < kth:
        return quicksort(arr, p + 1, end, kth)
    else:
        return quicksort(arr, start, p - 1, kth)


a = [1, 2, 3, 4, 5, 6, 8]
print(quicksort(a, 0, len(a) - 1, len(a) - 7))
