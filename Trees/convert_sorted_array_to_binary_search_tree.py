# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper(self, num, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    node = TreeNode(num[mid])
    node.left = self.helper(num, low, mid - 1)
    node.right = self.helper(num, mid + 1, high)
    return node


def sorted_array_to_bst(self, nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0:
        return None
    head = self.helper(nums, 0, len(nums) - 1)
    return head
