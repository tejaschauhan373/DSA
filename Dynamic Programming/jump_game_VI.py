# https://leetcode.com/problems/jump-game-vi
from math import inf
from typing import List
from collections import deque


def max_result_brute(nums: List[int], k: int) -> int:
    """
    Time Complexity = O(k*N)
    Space Complexity = O(N)
    ; N = len(nums)
    """
    n = len(nums)
    dp = [-inf] * n

    def jump(i, curr_sum):
        nonlocal k, dp
        if dp[i] < curr_sum:
            dp[i] = curr_sum
            for j in range(i + 1, min(n, i + k + 1)):
                jump(j, curr_sum + nums[j])

    jump(0, nums[0])

    return dp[-1]


def max_result_most_optimized(nums: List[int], k: int) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    ; N = len(nums)
    """
    n = len(nums)
    dp = [-inf] * n
    dp[0] = nums[0]
    q = deque([0])  # Will be the monotonic queue

    for i in range(1, n):
        if q[0] < i - k:
            q.popleft()

        dp[i] = nums[i] + dp[q[0]]

        while q and dp[q[-1]] <= dp[i]:
            q.pop()

        q.append(i)

    return dp[-1]
