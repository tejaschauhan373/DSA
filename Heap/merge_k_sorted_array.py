# https://leetcode.com/problems/merge-k-sorted-lists

from typing import List, Optional
from queue import PriorityQueue
from heapq import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_l_lists_brute(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Time Complexity = O(NLogN)
    Space Complexity = O(N)
    """
    res = []
    for temp in lists:
        while temp:
            res.append(temp.val)
            temp = temp.next
    res.sort()  # O(NLogN)

    if len(res) == 0:
        return None

    start = ListNode()
    start.val = res[0]
    temp = start

    i = 1
    while i < len(res):  # O(N)
        new_obj = ListNode()
        new_obj.val = res[i]
        temp.next = new_obj
        temp = new_obj
        i += 1

    return start


def merge_k_list_optimal_using_priority_queue(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Time Complexity = O(NLogK)
    Space Complexity = O(N)
    """
    head = point = ListNode(0)
    q = PriorityQueue()
    for l in lists:  # TC = O(K)
        if l:
            q.put((l.val, l))
    while not q.empty():  # TC = O(N)
        val, node = q.get()
        point.next = ListNode(val)
        point = point.next
        node = node.next
        if node:
            q.put((node.val, node))  # TC = (LogK)
    return head.next  # SC = O(N), to create new linked list


def merge_k_list_optimal_using_heap(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Time Complexity = O(NLogK)
    Space Complexity = O(N)
    """
    head = point = ListNode(0)
    q = []
    for l in lists:  # TC = O(K)
        if l:
            heappush(q, (l.val, l))

    while q:  # TC = O(N)
        val, node = heappop(q)
        new_node = ListNode(val)
        point.next = new_node
        point = point.next
        node = node.next
        if node:
            heappush(q, (node.val, node))  # TC = (LogK)
    return head.next  # SC = O(N), to create new linked list
