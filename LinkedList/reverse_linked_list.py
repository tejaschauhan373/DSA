# Time complexity = O(n)
# Space Complexity = O(1)
# https://practice.geeksforgeeks.org/problems/reverse-a-linked-list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list_iterative(head: ListNode) -> ListNode:
    prev = None
    current = head

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev


def reverse_list_recursive(head: ListNode):
    if head is None or head.next is None:
        return head

    s_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return s_head
