from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    all_list = []

    def inOrder(self, node):
        if node is None:
            return

        self.inOrder(node.left)
        self.all_list.append(node.val)
        self.inOrder(node.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.all_list = []
        self.inOrder(root)
        return self.all_list
