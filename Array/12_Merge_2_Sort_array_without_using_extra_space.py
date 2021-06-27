arr1 = list(map(int, input().split(' ')))
arr2 = list(map(int, input().split(' ')))


def merge(arr1, arr2, n, m):
    for i in range(n + m):
        min_m = i
        if i >= n:
            min_v = arr2[min_m - n]
        else:
            min_v = arr1[min_m]

        for j in range(i + 1, n + m):
            if j >= n:
                j -= n
                if arr2[j] < min_v:
                    min_m = j + n
                    min_v = arr2[j]
            else:
                if arr1[j] < min_v:
                    min_m = j
                    min_v = arr1[j]

        if i != min_m:
            if min_m >= n and i >= n:
                min_m -= n
                i -= n
                arr2[min_m], arr2[i] = arr2[i], arr2[min_m]
            elif min_m < n - 1 and i < n - 1:
                arr1[min_m], arr1[i] = arr1[i], arr1[min_m]
            elif min_m < n - 1 and i > n - 1:
                i -= n
                arr1[min_m], arr2[i] = arr2[i], arr1[min_m]
            else:
                min_m -= n
                arr2[min_m], arr1[i] = arr1[i], arr2[min_m]

    return arr1 + arr2


print(list(merge(arr1, arr2, len(arr1), len(arr2))))
