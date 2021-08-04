# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorder_traversal_recursive(self, root: TreeNode) -> List[int]:
        self.res = []

        self.preorder(root)

        return self.res

    def preorder(self, root):
        if root is None:
            return

        self.preorder(root.left)
        self.preorder(root.right)
        self.res.append(root.val)

    def postorder_taversal_iterative(self, root: TreeNode) -> List[int]:

        if root is None:
            return []

        level = [root]

        res = deque([])
        while level:

            ele = level.pop()

            if ele.left:
                level.append(ele.left)

            if ele.right:
                level.append(ele.right)

            res.appendleft(ele.val)

        return res
