# find the total count of given number in sorted array

def lower_bound(arr: list, k: int) -> int:
    """
    Time Complexity = O(log(N)) ; N = no. of elements in array
    Space Complexity = O(1)
    """
    s = 0
    e = len(arr) - 1
    ans = -1
    while s <= e:
        mid = (s + e) // 2

        if arr[mid] == k:
            ans = mid
            e = mid - 1
        elif arr[mid] > k:
            e = mid - 1
        else:
            s = mid + 1

    return ans


def upper_bound(arr: list, k: int) -> int:
    """
    Time Complexity = O(log(N)) ; N = no. of elements in array
    Space Complexity = O(1)
    """
    s = 0
    e = len(arr) - 1
    ans = -1

    while s <= e:
        mid = (s + e) // 2

        if arr[mid] == k:
            ans = mid
            s = mid + 1
        elif arr[mid] > k:
            e = mid - 1
        else:
            s = mid + 1

    return ans


a = [1, 2, 4, 5, 6, 6, 6, 6, 7, 8, 8, 9, 10]
h = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(upper_bound(a, 6) - lower_bound(a, 6) + 1)
