# Time complexity = O(n)
# Space Complexity = O(1)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    d = None

    while head:
        my_next = head.next
        head.next = d
        d = head
        head = my_next

    return d
