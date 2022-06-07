# https://practice.geeksforgeeks.org/problems/diagonal-traversal-of-binary-tree/1/?track=amazon-trees&batchId=192#
from collections import deque


def diagonal(root):
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    ; N = number of nodes
    """
    node = root
    out = []
    q = deque([])

    while node:

        out.append(node.data)  # O(1)

        if node.left:  # O(1)
            q.append(node.left)

        if node.right:  # O(1)
            node = node.right
        else:
            if q:
                node = q.popleft()
            else:
                node = None

    return out
