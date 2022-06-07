# https://leetcode.com/problems/house-robber-iii/
from typing import Optional
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive + Brute
def rob_recursive(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    include_root = 0
    if root.left:
        inc_r_ll = rob_recursive(root.left.left)
        inc_r_lr = rob_recursive(root.left.right)
        include_root += inc_r_ll + inc_r_lr

    if root.right:
        inc_r_rl = rob_recursive(root.right.left)
        inc_r_rr = rob_recursive(root.right.right)
        include_root += inc_r_rl + inc_r_rr

    include_root = root.val + include_root
    exclude_root = rob_recursive(root.left) + rob_recursive(root.right)
    return max(include_root, exclude_root)


# Recursive + LRU Cache + Top Down
@lru_cache()
def rob_recursive_top_down(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    include_root = 0
    if root.left:
        inc_r_ll = rob_recursive_top_down(root.left.left)
        inc_r_lr = rob_recursive_top_down(root.left.right)
        include_root += inc_r_ll + inc_r_lr

    if root.right:
        inc_r_rl = rob_recursive_top_down(root.right.left)
        inc_r_rr = rob_recursive_top_down(root.right.right)
        include_root += inc_r_rl + inc_r_rr

    include_root = root.val + include_root
    exclude_root = rob_recursive_top_down(root.left) + rob_recursive_top_down(root.right)
    return max(include_root, exclude_root)
