# https://leetcode.com/problems/validate-binary-search-tree/
from Trees import TreeNode


def is_valid_BST(root: TreeNode) -> bool:
    def validate(root, max, min):
        if root is None:
            return True
        elif (max is not None and root.val >= max) or (min is not None and root.val <= min):
            return False
        else:
            return validate(root.left, root.val, min) and validate(root.right, max, root.val)

    return validate(root, None, None)
