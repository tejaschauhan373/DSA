# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(inorder, postorder):
    """
    Time Complexity = O(N)
    Space Complexity = O(H); H = Height of Tree [Stack to store recursive function call]
    """

    if not inorder or not postorder:
        return None

    root = TreeNode(postorder[-1])
    i = 0

    while inorder[i] != postorder[-1]:
        i += 1

    root.left = build_tree(inorder[:i], postorder[:i])
    root.right = build_tree(inorder[i + 1:], postorder[i:len(postorder) - 1])
    return root
