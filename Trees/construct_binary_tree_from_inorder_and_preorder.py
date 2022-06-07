# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversa
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(inorder, preorder):
    """
    Time Complexity = O(N)
    Space Complexity = O(H); H = Height of Tree [Stack to store recursive function call]
    """
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = build_tree(preorder[1:mid + 1], inorder[: mid])
    root.right = build_tree(preorder[mid + 1:], inorder[mid + 1:])
    return root
