# https://practice.geeksforgeeks.org/problems/sort-a-linked-list/0/?track=amazon-linkedlists&batchId=192#

def get_middle(head):
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def sorted_merge(left, right):
    if left is None:
        return right

    if right is None:
        return left

    if left.data >= right.data:
        result = right
        result.next = sorted_merge(left, right.next)
    else:
        result = left
        result.next = sorted_merge(left.next, right)

    return result


def merge_sort(head):
    """
    Time Complexity = O(NlogN)
    Space Complexity = O(N)
    ; N = number of nodes in linked list
    """
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None
    left = merge_sort(head)
    right = merge_sort(next_to_middle)
    sortedlist = sorted_merge(left, right)
    return sortedlist
