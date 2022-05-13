# https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809

def len_of_long_sub_arr(nums, target):
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    """
    all_sum = {}
    temp = 0
    max_length = float("-inf")
    for i in range(len(nums)):
        temp += nums[i]
        if temp == target:
            max_length = max(max_length, i + 1)
        else:
            M = temp - target
            if M in all_sum:
                idx = all_sum[M]
                max_length = max(max_length, i - idx)

        if temp not in all_sum:
            all_sum[temp] = i

    if max_length == float("-inf"):
        return 0
    return max_length
