# https://leetcode.com/problems/find-the-town-judge/
from typing import List


def find_judge(n: int, trust: List[List[int]]) -> int:
    """
    Time Complexity = O(n)
    Time Complexity = O(n)
    """
    count = [0] * (n + 1)

    for source, destination in trust:
        count[source] -= 1  # Out Degree
        count[destination] += 1  # In Degree

    for i in range(1, n + 1):
        if count[i] == n - 1:
            return i
    return -1
