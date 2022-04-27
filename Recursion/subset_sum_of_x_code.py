# Count total subsets which sums to given number

def count_subsets(arr: list, n: int, i: int, x: int) -> int:
    if i == n:
        if x == 0:
            return 1
        else:
            return 0

    inc = count_subsets(arr, n, i + 1, x - arr[i])
    exc = count_subsets(arr, n, i + 1, x)
    return inc + exc


a = [1, 2, 3, 4, 5]

print(count_subsets(a, len(a), 0, 10))
