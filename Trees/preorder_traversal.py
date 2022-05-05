# Definition for a binary tree node.
from typing import List
from collections import deque


# https://www.techiedelight.com/preorder-tree-traversal-iterative-recursive/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversalIterative(self, root: TreeNode) -> List[int]:

        if root is None:
            return []

        level = deque([root])

        res = []

        while level:

            ele = level.pop()

            res.append(ele.val)

            if ele.right:
                level.append(ele.right)

            if ele.left:
                level.append(ele.left)

        return res

    def preorderTraversalRecusrive(self, root: TreeNode) -> List[int]:

        self.res = []

        self.preorder(root)

        return self.res

    def preorder(self, root):
        if root is None:
            return

        self.res.append(root.val)

        self.preorder(root.left)
        self.preorder(root.right)
