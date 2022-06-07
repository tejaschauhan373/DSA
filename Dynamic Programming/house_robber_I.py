# https://leetcode.com/problems/house-robber
from typing import List


# Recursive
def rob_recursive(nums: List[int]) -> int:
    """
    Time Complexity = O(2^N)
    Space Complexity = O(N) ; To store a recursive call on the stack
    """
    if len(nums) == 0:
        return 0
    elif len(nums) <= 2:
        return max(nums)

    length = len(nums)

    def recursive(i):
        if i >= length:
            return 0

        include = nums[i] + recursive(i + 2)
        exclude = recursive(i + 1)

        return max(include, exclude)

    return recursive(0)


# Top Down
def rob_top_down(nums: List[int]) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(N) ; At a time to store a recursive call stack
    """
    if len(nums) == 0:
        return 0
    elif len(nums) <= 2:
        return max(nums)

    length = len(nums)
    dp = [-1] * len(nums)

    def top_down_dp(i, dp):
        if i >= length:
            return 0

        if dp[i] != -1:
            return dp[i]

        include = nums[i] + top_down_dp(i + 2, dp)
        exclude = top_down_dp(i + 1, dp)

        dp[i] = max(include, exclude)
        return dp[i]

    return top_down_dp(0, dp)


# Bottom UP
def rob_bottom_up(nums: List[int]) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    """
    n = len(nums)

    if n == 1:
        return max(0, nums[0])

    if n == 2:
        return max(0, max(nums[0], nums[1]))

    dp = [0] * n
    # Bottom Up Logic
    dp[0] = max(0, nums[0])
    dp[1] = max(dp[0], nums[1])

    for i in range(2, n):
        include = dp[i - 2] + nums[i]
        exclude = dp[i - 1]
        dp[i] = max(include, exclude)

    return dp[n - 1]
