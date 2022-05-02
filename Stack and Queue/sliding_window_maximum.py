# https://leetcode.com/problems/sliding-window-maximum
from collections import deque
from typing import List


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    my_q = deque()

    for i in range(k):
        while my_q and nums[my_q[-1]] < nums[i]:
            my_q.pop()  # O(1)

        my_q.append(i)  # O(1)

    max_r = [nums[my_q[0]]]

    for i in range(k, len(nums)):

        while my_q and my_q[0] <= i - k:
            my_q.popleft()  # O(1)

        while my_q and nums[my_q[-1]] < nums[i]:
            my_q.pop()  # O(1)

        my_q.append(i)  # O(1)

        max_r.append(nums[my_q[0]])  # O(1)

    return max_r


arr = [1, 3, -1, -3, 5, 3, 6, 7]
slide_len = 3
print(max_sliding_window(arr, slide_len))
