# https://leetcode.com/problems/flip-equivalent-binary-trees
from typing import Optional
from TreeNode import TreeNode


class Solution:
    def flip_equiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True

        if (root1 is None and root2) or (root2 is None and root1):
            return False

        return (self.flip_equiv(root1.left, root2.left) and
                self.flip_equiv(root1.right, root2.right) or
                self.flip_equiv(root1.left, root2.right) and
                self.flip_equiv(root1.right, root2.left))
