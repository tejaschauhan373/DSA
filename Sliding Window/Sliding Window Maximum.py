# https://leetcode.com/problems/sliding-window-maximum/

from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """
    Time Complexity = O(N*k)
    Space Complexity = O(N)
    """
    if k == 1:
        return nums

    max_r = []

    f_m = max(nums[:k])

    max_r.append(f_m)

    for j in range(k, len(nums)):

        if f_m == nums[j - k]:
            f_m = max(nums[j - k + 1:j + 1])
        elif f_m < nums[j]:
            f_m = nums[j]

        max_r.append(f_m)

    return max_r


def optimize_max_sliding_window(nums: list[int], k: int) -> list[int]:
    """
    Time Complexity = O(N)
    Space Complexity = O(k)
    """

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


print(max_sliding_window([1, 3, 1, 2, 0, 5], 3))
