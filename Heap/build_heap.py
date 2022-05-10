import heapq
import heapq_max
from queue import PriorityQueue

"""
Key points about heap:

1. Time Complexity of Heap Sort = O(NLogN)
2. Building a heap takes O(N) time
3. Getting minimum element from the min heap takes O(1) time
4. Heap is Complete Binary Tree
"""

min_heap = [10, -3, 1, 2, 3, 4]

heapq.heapify(min_heap)
print(min_heap)
print(min_heap[0], min_heap[-1])
heapq.heappush(min_heap, -4)
print(min_heap[0], min_heap[-1])
heapq.heappush(min_heap, 12)
print(min_heap[0], min_heap[-1])
heapq.heappush(min_heap, -12)
print(min_heap[0], min_heap[-1])
heapq.heappop(min_heap)
heapq.heappop(min_heap)
heapq.heappop(min_heap)
print(min_heap[0], min_heap[-1])
print(heapq.nlargest(len(min_heap), min_heap))
print(min_heap)
max_heap = [0, 10, 3, 6, 8, -1]
heapq_max.heapify_max(max_heap)

print(max_heap)
print(max_heap[0], max_heap[-1])
print(heapq_max.heappush_max(max_heap, 100))
print(heapq_max.heappush_max(max_heap, -100))
print(max_heap[0], max_heap[-1])

pr_queue = PriorityQueue()
for k in [(4, "done"), (5, "remaining"), (0, "done"), (10, "back"), (-1, "light"), (-5, "done")]:
    pr_queue.put(k)

print(pr_queue.get())
while not pr_queue.empty():
    print(pr_queue.get())
    print("Done")
