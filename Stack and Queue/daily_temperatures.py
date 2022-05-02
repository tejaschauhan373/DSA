# https://leetcode.com/problems/daily-temperatures/
from typing import List


def daily_temperatures_brute(temperatures: List[int]) -> List[int]:
    """
    Time Complexity = O(N*N)
    Space Complexity = O(1)
    """
    res = []

    for i in range(len(temperatures)):
        c = temperatures[i]
        count = 0
        got = False
        for j in range(i + 1, len(temperatures)):
            count += 1
            if temperatures[j] > c:
                got = True
                break
        if got:
            res.append(count)
        else:
            res.append(0)
    return res


def daily_temperatures_optimal(temperatures: List[int]) -> List[int]:
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    """
    n = len(temperatures)
    my_stack = [0]
    res = [0 for _ in range(n)]

    for i in range(1, n):

        while my_stack and temperatures[i] > temperatures[my_stack[-1]]:
            res[my_stack[-1]] = i - my_stack[-1]
            my_stack.pop()

        my_stack.append(i)

    return res
