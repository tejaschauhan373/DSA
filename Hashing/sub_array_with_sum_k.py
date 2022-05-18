# https://leetcode.com/problems/subarray-sum-equals-k

def sub_array_sum_brute(nums: list, k: int):
    """
    Time Complexity = O(N*N)
    Space Complexity = O(1)
    """
    sub_array_count = 0
    for i in range(len(nums)):
        total_sum = 0
        for j in range(i, len(nums)):
            total_sum += nums[j]
            if total_sum == k:
                sub_array_count += 1
    return sub_array_count


def sub_array_sum_optimal(nums: list, k: int):
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    """
    sum_dict = {0: 1}
    co = 0
    curr = 0
    for n in nums:
        curr += n
        diff = curr - k
        co += sum_dict.get(diff, 0)
        sum_dict[curr] = 1 + sum_dict.get(curr, 0)
    return co
