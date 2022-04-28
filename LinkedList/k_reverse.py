# https://leetcode.com/problems/reverse-nodes-in-k-group

from typing import Optional


def reverse_k_linked_list_reverse_remaining(head, k):
    if head is None:
        return None

    prev = None
    cnt = 1
    while head and cnt <= k:
        my_next = head.next
        head.next = prev
        prev = head
        head = my_next
        cnt += 1

    if head:
        head.next = reverse_k_linked_list_reverse_remaining(head, k)
    return prev


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_k_group_exclude_remaining(self, head, k):
        prev = None
        current = head
        temp = None

        cnt = 1

        temp_c = current

        while temp_c and cnt <= k:
            temp_c = temp_c.next
            cnt += 1

        if cnt <= k:
            return head
        else:
            cnt = 1
            while current and cnt <= k:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
                cnt += 1

            if temp:
                head.next = self.reverse_k_group_exclude_remaining(temp, k)

            return prev

    def reverse_k_group_main(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        head = self.reverse_k_group_exclude_remaining(head, k)
        return head
