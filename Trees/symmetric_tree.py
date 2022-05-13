# https://leetcode.com/explore/interview/card/top-interview-questions-easy
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_same(left, right):
    if left is None and right is None:
        return True
    elif left and right:
        if left.val == right.val:
            if find_same(left.left, right.right):
                return find_same(left.right, right.left)
            else:
                return False
        else:
            return False
    else:
        return False


def is_symmetric(root: Optional[TreeNode]) ->    bool:
    return find_same(root.left, root.right)
