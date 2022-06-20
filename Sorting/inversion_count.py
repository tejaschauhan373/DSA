# https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1/#

def merge(arr: list, l: int, r: int) -> int:
    temp = []

    mid = (r + l) // 2

    i = l
    j = mid + 1
    cnt = 0

    while i <= mid and j <= r:

        if arr[i] > arr[j]:
            cnt += mid - i + 1
            temp.append(arr[j])
            j += 1
        else:
            temp.append(arr[i])
            i += 1

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

    return cnt


def inversion_count(arr, left, right):
    """
    Time Complexity = O(NlogN)
    Space Complexity = O(N)
    """
    if left < right:
        mid = (left + right) // 2
        C1 = inversion_count(arr, left, mid)
        C2 = inversion_count(arr, mid + 1, right)
        C3 = merge(arr, left, right)
        return C1 + C2 + C3
    else:
        return 0


a = [10, 10, 10]
print(inversion_count(a, 0, len(a) - 1))
print(a)
