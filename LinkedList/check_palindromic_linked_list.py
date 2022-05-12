# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def check_palindrome_naive(head):
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    """
    if head is None:
        return True
    stack = []
    first = head
    while first:
        stack.append(first.val)
        first = first.next

    i = 0
    last = len(stack) - 1

    while i < last:
        if stack[i] != stack[last]:
            return False
        i += 1
        last -= 1
    return True


def check_palindrome_optimal(head):
    """
    Time Complexity = O(N)
    Space Complexity = O(1)
    """

    def revers_list(head):
        pre = None

        while head:
            next_t = head.next
            head.next = pre
            pre = head
            head = next_t

        return pre

    if head is None:
        return True
    elif head.next is None:
        return True

    fast = head
    slow = head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    slow.next = revers_list(slow.next)
    slow = slow.next

    while slow:
        if slow.val != head.val:
            return False
        slow = slow.next
        head = head.next

    return True
