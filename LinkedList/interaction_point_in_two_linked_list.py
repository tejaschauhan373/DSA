# Definition for singly-linked list.
# https://leetcode.com/problems/intersection-of-two-linked-lists/
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def intersection_point_naive(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    Naive Approach Brute Force
    Time Complexity = O(N*M)
    Space Complexity = O(1)
    """

    if headA is None or headB is None:
        return None

    while headA:
        temp = headB
        while temp:
            if headA == temp:
                return temp
            else:
                temp = temp.next

        headA = headA.next
    return None


def intersection_point_better(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    Better Approach
    Time Complexity = O(N+M)
    Space Complexity = O(N)
    """
    if headA is None or headB is None:
        return None
    headb_dict = {}
    while headB:
        headb_dict[headB] = None
        headB = headB.next

    while headA:
        if headA in headb_dict:
            return headA
        else:
            headA = headA.next

    return None


def intersection_point_optimal(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    Optimized approach
    Time Complexity = O(2M)
    Space Complexity = O(1)
    """
    if headA is None or headB is None:
        return None
    temp_a = headA
    temp_b = headB

    while temp_a != temp_b:
        if temp_a:
            temp_a = temp_a.next
        else:
            temp_a = headB

        if temp_b:
            temp_b = temp_b.next
        else:
            temp_b = headA
    return temp_a
