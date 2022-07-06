# https://leetcode.com/problems/invert-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree_brute(root: TreeNode) -> TreeNode:
    """
    Time Complexity = O(N) ; N = number of nodes in tree
    Space Complexity = O(N + H); H = height of tree, to store recursive function call in stack
    """

    def invert(root):
        if root is None:
            return None

        new_root = TreeNode(root.val)
        new_root.left = invert(root.right)
        new_root.right = invert(root.left)

        return new_root

    return invert(root)


def invert_tree_optimized(root: TreeNode) -> TreeNode:
    """
    Time Complexity = O(N); N = number of nodes in tree
    Space Complexity = O(H); H = height of tree, to store recursive function call in stack
    """

    def swap(root):
        if not root:
            return

        swap(root.left)
        swap(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp

    swap(root)
    return root
