# https://leetcode.com/problems/swapping-nodes-in-a-linked-list

from typing import Optional


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_nodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    start = ListNode()
    start.next = head

    cnt = 1

    while start and cnt <= k:
        start = start.next
        cnt += 1

    temp_1 = start

    temp_2 = head

    while start.next is not None:
        start = start.next
        temp_2 = temp_2.next

    temp_1.val, temp_2.val = temp_2.val, temp_1.val

    return head
