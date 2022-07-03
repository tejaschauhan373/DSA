from typing import List
from collections import deque


# https://leetcode.com/problems/binary-tree-inorder-traversal/
# https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/
# Left -> Root -> Right
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


# Iterative Methods

def inorderIterative(root):
    # create an empty stack
    stack = deque()

    # start from the root node (set current node to the root node)
    curr = root

    # if the current node is None and the stack is also empty, we are done
    while stack or curr:

        # if the current node exists, push it into the stack (defer it)
        # and move to its left child
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            # otherwise, if the current node is None, pop an element from the stack,
            # print it, and finally set the current node to its right child
            curr = stack.pop()
            print(curr.data, end=' ')

            curr = curr.right
