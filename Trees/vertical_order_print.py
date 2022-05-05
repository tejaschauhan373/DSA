# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from TreeNode import TreeNode
from typing import List


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = {}
        self.go_and_feel(root, answer, 0, 0)
        final_ans = []

        for i in sorted(answer.keys()):
            level = []
            for j in sorted(answer[i].keys()):
                level.extend(sorted(answer[i][j]))
            final_ans.append(level)
        return final_ans

    def go_and_feel(self, root, answer, vertical, horizontal):
        if root is None:
            return

        if vertical in answer:
            if horizontal in answer[vertical]:
                answer[vertical][horizontal].append(root.val)
            else:
                answer[vertical][horizontal] = [root.val]
        else:
            answer[vertical] = {}
            answer[vertical] = {horizontal: [root.val]}

        self.go_and_feel(root.right, answer, vertical + 1, horizontal + 1)
        self.go_and_feel(root.left, answer, vertical - 1, horizontal + 1)
