arr = list(map(int, input().split(' ')))


def maxSubArraySum(a, size):
    curr_sum = 0
    max_sum = 0
    for i in range(size):
        curr_sum += a[i]

        if curr_sum < a[i]:
            curr_sum = a[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum


print(maxSubArraySum(arr, len(arr)))

# print(arr)
