class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def swapl(self, root):
        if not root:
            return

        self.swapl(root.left)
        self.swapl(root.right)

        temp = TreeNode()

        temp = root.left
        root.left = root.right
        root.right = temp

    def invertTree(self, root: TreeNode) -> TreeNode:
        self.swapl(root)
        return root
