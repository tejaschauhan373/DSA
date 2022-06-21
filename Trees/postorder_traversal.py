# Definition for a binary tree node.
from typing import List
from collections import deque


# https://www.techiedelight.com/postorder-tree-traversal-iterative-recursive/
# Left -> Right -> Root
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder_traversal_iterative(root: TreeNode) -> List[int]:

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


class Solution:
    def __init__(self):
        self.res = []

    def postorder_traversal_recursive(self, root: TreeNode) -> List[int]:

        self.post_order(root)

        return self.res

    def post_order(self, root):
        if root is None:
            return

        self.post_order(root.left)
        self.post_order(root.right)
        self.res.append(root.val)
