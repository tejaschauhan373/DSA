# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getDiameter(self, root):
        if root is None:
            return 0

        l = self.getDiameter(root.left)
        r = self.getDiameter(root.right)
        self.ans = max(self.ans, (l + r + 1))
        return max(l, r) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        self.getDiameter(root)
        if self.ans > 0:
            return self.ans - 1
        else:
            return 0
