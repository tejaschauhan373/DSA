class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head):
        pre = None

        while head:
            next_t = head.next
            head.next = pre
            pre = head
            head = next_t

        return pre

    def isPalindrome(self, head: ListNode) -> bool:

        if head is None:
            return True
        elif head.next is None:
            return True

        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        slow.next = self.reverseList(slow.next)
        slow = slow.next

        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next

        return True
