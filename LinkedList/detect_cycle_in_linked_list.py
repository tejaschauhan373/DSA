class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle1(head: ListNode) -> bool:
    """
    :param head:
    :return:

    Brute Force Approach
    """
    all_list = []

    if head is None:
        return False

    while head:
        if head not in all_list:
            all_list.append(head)
        else:
            return True
        head = head.next

    return False


def hasCycle2(head: ListNode) -> bool:
    """
    :param head:
    :return:

    Optimal Approach
    Time Complexity : O(N)
    Space Complexity: O(1)
    """
    if head is None or head.next is None:
        return False

    fast = head
    slow = head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True

    return False
