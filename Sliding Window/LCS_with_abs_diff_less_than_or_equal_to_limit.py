# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

from collections import deque
from typing import List
from heapq import *


# Using monotonic queue
def longest_sub_array_deque(nums: List[int], limit: int) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    ; N = len(nums)
    """
    max_d = deque()
    min_d = deque()
    j = 0
    for a in nums:
        while max_d and max_d[-1] < a: max_d.pop()
        while min_d and min_d[-1] > a: min_d.pop()
        max_d.append(a)
        min_d.append(a)
        if max_d[0] - min_d[0] > limit:
            if nums[j] == max_d[0]: max_d.popleft()
            if nums[j] == min_d[0]: min_d.popleft()
            j += 1
    return len(nums) - j


# Using max heap and min heap
def longest_sub_array_heap(nums: List[int], limit: int) -> int:
    """
    Time Complexity = O(NlogN)
    Space Complexity = O(N)
    ; N = len(nums)
    """
    max_q = []
    min_q = []
    res = 0
    i = 0
    for j, a in enumerate(nums):
        heappush(max_q, [-a, j])
        heappush(min_q, [a, j])
        while -max_q[0][0] - min_q[0][0] > limit:
            i = min(max_q[0][1], min_q[0][1]) + 1
            while max_q[0][1] < i: heappop(max_q)
            while min_q[0][1] < i: heappop(min_q)
        res = max(res, j - i + 1)
    return res
