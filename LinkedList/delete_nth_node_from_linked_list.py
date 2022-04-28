# Time complexity = O(n)
# Space Complexity = O(1)
# https://leetcode.com/problems/remove-nth-node-from-end-of-list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    start = ListNode()
    start.next = head

    fast = start
    slow = start

    for i in range(n):
        fast = fast.next

    while fast.next != None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return start.next
