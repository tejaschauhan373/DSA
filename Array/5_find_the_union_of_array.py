arr1 = list(map(int, input().split(' ')))
arr2 = list(map(int, input().split(' ')))


def total_distinct(arr1, n, arr2, m):
    if n < m:
        n = len(set(arr1))
        for i in arr2:
            if i not in arr1:
                n += 1
    else:
        m = len(set(arr2))
        for i in arr1:
            if i not in arr2:
                m += 1
        return m


print(total_distinct(arr1, len(arr1), arr2, len(arr2)))
