arr = list(map(int, input().split(' ')))
k = int(input())


def getMinDiff(arr, n, k):
    arr.sort()
    mns = []
    maxs = []

    for i in arr:
        mns.append(i - k)
        maxs.append(i + k)

    ans = arr[-1] - arr[0]
    for i in range(n):
        if mns[i] >= 0:
            ans = min(ans, (max(arr[n - 1], maxs[i - 1]) - min(mns[i], maxs[0])))

    return ans


print(getMinDiff(arr, len(arr), k))
