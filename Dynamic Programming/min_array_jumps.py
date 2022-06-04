# https://leetcode.com/problems/jump-game-ii
from collections import deque
from math import inf


# Recursive + Brute + BFS
def find_min_jumps_top_down_brute(arr: list):
    q = deque([[0, 0]])
    while q:
        size = len(q)
        while size:
            curr_index, step = q.popleft()
            if curr_index >= len(arr) - 1:
                return step
            elif curr_index < len(arr):
                curr_val = arr[curr_index]
                i = 1
                while i <= curr_val:
                    q.append([curr_index + i, step + 1])
                    i += 1
            size -= 1
    return -1


# Top Down + Memoization
def find_min_jumps_bottom_up(arr: list, n: int, dp: list, i: int):
    # base case
    if i == n - 1:
        return 0
    if i >= n:
        return inf

    # recursive case
    if dp[i] != 0:
        return dp[i]

    # Assume
    steps = inf
    max_jump = arr[i]

    for jump in range(1, max_jump + 1):
        next_cell = i + jump
        sub_prob = find_min_jumps_bottom_up(arr, n, dp, next_cell)
        if sub_prob != inf:
            steps = min(steps, sub_prob + 1)
    dp[i] = steps
    return dp[i]


# Greedy + Iterative
def find_min_jump_greedy(nums: list):
    n = len(nums)
    left = 0
    right = 0
    jump = 0
    while right < n - 1:
        farthest = left
        for i in range(left, right + 1):
            farthest = max(farthest, i + nums[i])

        left = right + 1
        right = farthest
        jump += 1

    return jump


if __name__ == "__main__":
    arr = [3, 4, 2, 1, 2, 3, 10, 1, 1, 1, 2, 5]
    print(find_min_jumps_top_down_brute(arr))
    dp = [0] * (len(arr))
    print(find_min_jumps_bottom_up(arr, len(arr), dp, 0))
    print(find_min_jump_greedy(arr))
