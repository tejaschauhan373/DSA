# https://bohenan.gitbooks.io/leetcode/content/linkedlist/linked-list-cycle-ii.html
# https://leetcode.com/problems/linked-list-cycle-ii/
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    fast = head
    slow = head

    while fast and slow:
        if fast.next is None:
            return None
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            entry = head
            while entry != slow:
                entry = entry.next
                slow = slow.next
            return entry
    return None
