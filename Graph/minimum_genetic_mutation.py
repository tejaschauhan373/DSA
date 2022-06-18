# https://leetcode.com/problems/minimum-genetic-mutation/
from typing import List


def min_mutation(start: str, end: str, bank: List[str]) -> int:
    """
    Time Complexity = O(len(start)*step*4)
    Space Complexity = O(len(start)*4)
    """
    queue = [(start, 0)]
    bank_set = set(bank)

    while queue:
        curr, step = queue.pop(0)
        if curr == end:
            return step
        for i in range(len(curr)):
            for c in "AGCT":
                mutation = curr[:i] + c + curr[i + 1:]
                if mutation in bank_set:
                    bank_set.remove(mutation)
                    queue.append((mutation, step + 1))

    return -1
