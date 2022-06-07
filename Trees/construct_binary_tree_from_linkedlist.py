# https://practice.geeksforgeeks.org/problems/make-binary-tree/1/?track=amazon-trees&batchId=192#
# https://www.techiedelight.com/construct-complete-binary-tree-from-linked-list/
from collections import deque


class Tree:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to make binary tree from linked list.
def convert(head):
    # base case
    if head is None:
        return None

    # create the root using the first node of linked list
    root = Tree(head.data)

    # move the head pointer to the next node
    head = head.next

    # create a queue to store tree pointers and enqueue the root node
    q = deque([])
    q.append(root)

    # loop till the end of the linked list is reached
    while head:
        # deque front node
        front = q.popleft()

        # create a left child from the next node in the linked list and enqueue it
        front.left = Tree(head.data)
        q.append(front.left)

        # move the head pointer to the next node
        head = head.next

        # if the linked list did not reach its end
        if head:
            # create the right child from the next node in the linked list
            # enqueue it
            front.right = Tree(head.data)
            q.append(front.right)

            # move the head pointer to next node
            head = head.next

        # return root of the constructed binary tree
    return root
