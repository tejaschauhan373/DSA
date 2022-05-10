# https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620

import heapq


def join_ropes(ropes: list) -> int:
    """
    Time Complexity = O(NLogN)
    Space Complexity = O(1)
    """
    if len(ropes) == 1:
        return 0
    heapq.heapify(ropes)  # O(N)
    total_cost = 0
    digit = heapq.heappop(ropes)

    # Total TC of while loop : O(NLogN)
    while len(ropes) > 0:  # O(N)
        curr = heapq.heappop(ropes)  # O(LogN)
        total_cost += digit + curr
        heapq.heappush(ropes, digit + curr)  # O(LogN)
        digit = heapq.heappop(ropes)

    return total_cost


r = [4, 2, 3, 6]
print(join_ropes(r))
