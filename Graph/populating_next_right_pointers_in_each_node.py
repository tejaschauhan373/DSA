# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
from typing import Optional
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# BFS
def connect(root: Optional[Node]) -> Optional[Node]:
    """
    Time complexity = O(V) ; V = no. of vertices of tree
    Space complexity = O(V) ; V = no. of vertices of tree
    """
    if root is None:
        return None

    q = deque()
    q.append(root)

    while q:

        level = q
        new_level = deque()

        i = len(level) - 1
        last = None
        while i >= 0:
            level[i].next = last
            last = level[i]
            i -= 1

        while level:
            curr = level.popleft()
            if curr.left:
                new_level.append(curr.left)
            if curr.right:
                new_level.append(curr.right)

        q = new_level

    return root
