# https://www.techiedelight.com/binary-search/
# find the specific element from given sorted array

def binary_search_recursive(arr: list, k: int, start: int, end: int) -> int:
    """
    Time Complexity = O(log(N)) ; N = no. of elements in array
    Space Complexity = O(log(N)) ;  To store function call in stack
    """
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        return binary_search_recursive(arr, k, start, mid - 1)
    else:
        return binary_search_recursive(arr, k, mid + 1, end)


def binary_search_iterative(arr: list, k: int) -> int:
    """
    Time Complexity = O(log(N)) ; N = no. of elements in array
    Space Complexity = O(1)
    """
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            end = mid - 1
        else:
            start = mid + 1

    return -1


a = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6, 7, 9]
print(binary_search_recursive(a, 2, 0, len(a) - 1))
print(binary_search_iterative(a, 2))
