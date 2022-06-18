# https://leetcode.com/problems/fair-distribution-of-cookies
from math import inf
from typing import List


def distribute_cookies(cookies: List[int], k: int) -> int:
    l = [0] * k
    s = inf

    def serve(l, i):
        global s
        if i >= len(cookies):
            s = min(s, max(l))
            return
        if max(l) >= s:
            return
        for j in range(k):
            l[j] += cookies[i]
            serve(l, i + 1)
            l[j] -= cookies[i]

    serve(l, 0)
    return s
