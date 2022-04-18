# https://leetcode.com/problems/sort-an-array/

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


def quicksort(arr: list, start: int, end: int):
    """
    Time Complexity in Average Case = O(NlogN)
    Time Complexity in Worst Case = O(N*N)
    Space Complexity = O(1)
    """
    if start > end:
        return

    p = partition(arr, start, end)
    quicksort(arr, start, p - 1)
    quicksort(arr, p + 1, end)


a = [1, 2, 4, -1, -3, -2, 10, 9, 8, 7]
print(quicksort(a, 0, len(a) - 1))
print(a)
