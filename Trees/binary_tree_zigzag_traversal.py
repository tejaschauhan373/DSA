# Definition for a binary tree node.

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        res = []
        stack = [root]

        nums = 2
        while stack:

            new_stack = []
            for i in stack:
                if i.left:
                    new_stack.append(i.left)

                if i.right:
                    new_stack.append(i.right)

            temp = []
            if nums % 2 == 0:
                for i in stack:
                    temp.append(i.val)
            else:
                for i in stack[::-1]:
                    temp.append(i.val)

            res.append(temp)
            stack = new_stack
            nums += 1

        return res
