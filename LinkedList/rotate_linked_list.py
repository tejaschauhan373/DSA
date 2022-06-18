# https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/0/?track=amazon-linkedlists&batchId=192#
# https://leetcode.com/problems/rotate-list/

# Function to rotate a linked list.
def rotate(head, k):
    """
    Time Complexity = O(N) ; N = number of nodes
    Space Complexity = O(1)
    """

    if head is None:
        return None

    length = 0

    temp_head = head
    while temp_head:
        temp_head = temp_head.next
        length += 1

    k = k % length

    if k == 0:
        return head

    previous = None
    first = head

    while k > 0:
        previous = first
        first = first.next
        k -= 1

    last = first

    while last.next is not None:
        last = last.next

    previous.next = None
    last.next = head
    return first
