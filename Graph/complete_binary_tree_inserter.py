# https://leetcode.com/problems/complete-binary-tree-inserter/
# Definition for a binary tree node.
from typing import Optional
from collections import deque


# Here is the trick to find leaf nodes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.deque = deque()
        self.root = root
        q = deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val: int) -> int:
        node = self.deque[0]
        self.deque.append(TreeNode(val))
        if not node.left:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.popleft()
        return node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
