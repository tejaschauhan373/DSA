# https://leetcode.com/problems/jump-game-ii
from typing import List
from collections import deque


# BFS + Brute
def jump(nums: List[int]) -> int:
    n = len(nums)
    step = 0
    q = deque([(0, 0)])
    while q:
        size = len(q)
        while size:
            curr, step = q.popleft()
            if curr >= n - 1:
                return step
            max_step = nums[curr]
            for i in range(1, max_step + 1):
                temp = (curr + i, step + 1)
                if temp not in q:
                    q.append(temp)
            size -= 1
    return step


# BFS + Optimized Space Complexity
def min_jump_bfs_optimized(nums: List[int]) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(1)
    """
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


# Greedy + Top Down
def min_jump_greedy_reverse(nums: List[int]) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(1)
    """
    n = len(nums)
    position = n - 1
    steps = 0
    while position != 0:
        for i in range(position):
            if nums[i] >= position - i:
                position = i
                steps += 1
                break
    return steps


if __name__ == "__main__":
    a = [2, 3, 1, 1, 4]
    print(min_jump_bfs_optimized(a))
    print(min_jump_greedy(a))
