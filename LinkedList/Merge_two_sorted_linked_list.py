# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/
class ListNode:

    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_linked_list_optimal_one(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Time Complexity = O(N + M)
    Space Complexity = O(N + M) # to store recursive call stack
    """

    # base case
    if l1 is None:
        return l2

    if l2 is None:
        return l1

    # recursive case
    c = None

    if l1.val > l2.val:
        c = l1
        c.next = merge_two_linked_list_optimal_one(l1.next, l2)
    else:
        c = l2
        c.next = merge_two_linked_list_optimal_one(l1, l2.next)
    return c


def merge_two_linked_list_optimal_two(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Time Complexity = O(N + M)
    Space Complexity = O(1)
    """

    if l1 is None:
        return l2

    if l2 is None:
        return l1

    c = ListNode()
    temp = c
    while l1 and l2:

        if l1.val < l2.val:
            c.next = l1
            l1 = l1.next
        else:
            c.next = l2
            l2 = l2.next
        c = c.next

    if l1 is None:
        c.next = l2
    else:
        c.next = l1

    return temp.next


def merge_two_linked_list_optimal_three(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Time Complexity = O(N+M)
    Space Complexity = O(1)
    """
    if l1 is None:
        return l2

    if l2 is None:
        return l1

    if l1.val > l2.val:
        temp = l1
        l1 = l2
        l2 = temp

    res = l1
    while l1 and l2:
        temp = ListNode()
        while l1 is not None and l1.val < l2.val:
            temp = l1
            l1 = l1.next

        temp.next = l2
        temp = l1
        l1 = l2
        l2 = temp

    return res
