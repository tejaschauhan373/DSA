# https://leetcode.com/problems/minimum-jumps-to-reach-home/
from typing import List
from collections import deque


def minimum_jumps(forbidden: List[int], a: int, b: int, x: int) -> int:
    """
    Time Complexity =  O(max(x, max(forbidden)) + a + b)
    Space Complexity = O(max(x, max(forbidden)) + a + b)
    """
    dq = deque([(True, 0)])
    seen = {(True, 0)}
    steps = 0
    furthest = max(x, max(forbidden)) + a + b

    for pos in forbidden:
        seen.add((True, pos))
        seen.add((False, pos))

    while dq:
        size = len(dq)
        while size:
            dir, pos = dq.popleft()
            if pos == x:
                return steps
            forward, backward = (True, pos + a), (False, pos - b)
            if pos + a <= furthest and forward not in seen:
                seen.add(forward)
                dq.append(forward)
            if dir and pos - b > 0 and backward not in seen:
                seen.add(backward)
                dq.append(backward)
            size -= 1
        steps += 1
    return -1
