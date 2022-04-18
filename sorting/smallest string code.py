def merge(arr: list, l: int, r: int):
    temp = []

    mid = (r + l) // 2

    i = l
    j = mid + 1
    k = 0

    while i <= mid and j <= r:

        if arr[i] + arr[j] > arr[j] + arr[i]:
            temp.append(arr[j])
            j += 1
        else:
            temp.append(arr[i])
            i += 1
        k += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= r:
        temp.append(arr[j])
        j += 1

    k = 0
    for i in range(l, r + 1):
        arr[i] = temp[k]
        k += 1


def merge_sort(arr, left, right):
    """
    Time Complexity = O(NlogN)
    Space Complexity = O(N)
    """
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, right)


a = ["a", "ab", "aba"]
merge(a, 0, len(a) - 1)
print("".join(a))
