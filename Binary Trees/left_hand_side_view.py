from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lefftSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if root is None:
            return res

        level = [root]

        while level:
            next_level = []
            for i in level:
                if i.left:
                    next_level.append(i.left)

                if i.right:
                    next_level.append(i.right)

            res.append(level[0].val)

            level = next_level

        return res
