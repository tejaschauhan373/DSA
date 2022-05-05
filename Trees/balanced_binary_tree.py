# https://leetcode.com/problems/balanced-binary-tree

from typing import Optional
from TreeNode import TreeNode


# Time Complexity = O(N)
class Solution:
    def check_balance(self, root):
        if root is None:
            return 0, True

        left = self.check_balance(root.left)
        right = self.check_balance(root.right)
        height = max(left[0], right[0]) + 1

        if abs(left[0] - right[0]) <= 1 and left[1] and right[1]:
            return height, True

        return height, False

    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        res = self.check_balance(root)
        return res[1]
