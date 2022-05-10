# https://leetcode.com/problems/find-median-from-data-stream
import heapq_max, heapq

arr = [10, 5, 2, 3, 0, 12, 18, 20, 22]


def get_running_median(nums: list):
    """
    Time Complexity = O(NlogN)
    Space Complexity  = O(N)
    """
    if len(nums) == 1:
        return nums[0]
    left_heap = [nums[0]]  # max heap
    right_heap = []  # min heap

    heapq_max.heapify_max(left_heap)
    heapq.heapify(right_heap)

    mid = left_heap[-1]
    ans = [mid]
    for i in range(1, len(nums)):  # O(N-1)
        curr = nums[i]
        if len(left_heap) > len(right_heap):
            if curr < mid:
                heapq.heappush(right_heap, left_heap[0])  # O(LogN)
                heapq_max.heappop_max(left_heap)  # O(LogN)
                heapq_max.heappush_max(left_heap, curr)  # O(LogN)
            else:
                heapq.heappush(right_heap, curr)  # O(LogN)
            mid = (left_heap[0] + right_heap[0]) / 2
        elif len(left_heap) == len(right_heap):
            if curr < mid:
                heapq_max.heappush_max(left_heap, curr)  # O(LogN)
                mid = left_heap[0]
            else:
                heapq.heappush(right_heap, curr)  # O(LogN)
                mid = right_heap[0]
        else:
            if curr < mid:
                heapq_max.heappush_max(left_heap, curr)  # O(LogN)
            else:
                heapq_max.heappush_max(left_heap, right_heap[0])  # O(LogN)
                heapq.heappop(right_heap)  # O(LogN)
                heapq.heappush(right_heap, curr)  # O(LogN)
            mid = (left_heap[0] + right_heap[0]) / 2

        ans.append(mid)
    return ans


print(get_running_median(arr))


class MedianFinder:

    def __init__(self):
        self.left = []  # inverted heap
        self.right = []

    def find_median(self) -> float:
        if len(self.left) == len(self.right):
            return (self.right[0] - self.left[0]) / 2
        else:
            return self.right[0]

    def add_num(self, num: int) -> None:
        if len(self.left) == len(self.right):
            heapq.heappush(self.right, -heapq.heappushpop(self.left, -num))
        else:
            heapq.heappush(self.left, -heapq.heappushpop(self.right, num))
