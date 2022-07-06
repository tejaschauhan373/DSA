arr = list(map(int, input().split(' ')))


def maxSubArraySum(a, size):
    curr_sum = a[0]
    max_sum = a[0]
    for i in range(1, size):
        curr_sum = max(a[i], curr_sum + a[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum


print(maxSubArraySum(arr, len(arr)))
