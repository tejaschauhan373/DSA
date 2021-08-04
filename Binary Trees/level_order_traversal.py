# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return []

        top = [root]

        res = []

        while top:
            level = []
            bottom = []

            for i in top:
                if i.left:
                    bottom.append(i.left)

                if i.right:
                    bottom.append(i.right)

            for i in top:
                level.append(i.val)

            res.append(level)

            top = bottom

        return res
