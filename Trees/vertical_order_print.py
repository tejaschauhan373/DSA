# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# https://practice.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1/?track=amazon-trees&batchId=192#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


def vertical_order(root):
    answer = defaultdict(dict)

    def go_and_feel(root, answer, vertical, horizontal):
        if root is None:
            return

        if horizontal in answer[vertical]:
            answer[vertical][horizontal].append(root.data)
        else:
            answer[vertical][horizontal] = [root.data]

        go_and_feel(root.left, answer, vertical - 1, horizontal + 1)
        go_and_feel(root.right, answer, vertical + 1, horizontal + 1)

    go_and_feel(root, answer, 0, 0)
    final_ans = []
    for i in sorted(answer.keys()):
        column = answer[i]
        for row in sorted(column.keys()):
            final_ans.extend(column[row])
    return final_ans
