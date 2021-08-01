# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    i = 0

    if l1.val == 0 and l2.next is None and l2.val == 0 and l1.next is None:
        return ListNode(0)

    first = 0
    while l1:
        first += l1.val * (10 ** i)
        l1 = l1.next
        i += 1

    second = 0
    i = 0

    while l2:
        second += l2.val * (10 ** i)
        l2 = l2.next
        i += 1

    res = first + second

    res_l = ListNode()

    res_link = res_l

    while res != 0:
        nume = res % 10
        res = res // 10
        res_link.next = ListNode(nume)
        res_link = res_link.next

    return res_l.next
