# Definition for a binary tree node.
from typing import List
from collections import deque


# https://leetcode.com/problems/binary-tree-preorder-traversal/
# https://www.techiedelight.com/preorder-tree-traversal-iterative-recursive/
# Root -> Left -> Right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal_iterative(root: TreeNode) -> List[int]:
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


class Solution:
    def __init__(self):
        self.res = []

    def preorder_traversal_recursive(self, root: TreeNode) -> List[int]:
        self.preorder(root)

        return self.res

    def preorder(self, root):
        if root is None:
            return

        self.res.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
