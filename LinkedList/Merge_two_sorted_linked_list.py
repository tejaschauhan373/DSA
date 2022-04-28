class ListNode:

    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_linked_list(l1: ListNode, l2: ListNode) -> ListNode:
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
