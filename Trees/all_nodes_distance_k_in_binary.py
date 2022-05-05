# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree

import collections
from TreeNode import TreeNode
from typing import List


class Solution:

    def dfs(self, root, par=None):
        if root:
            root.par = par
            self.dfs(root.left, root)
            self.dfs(root.right, root)

    def distance_k(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.dfs(root)
        res = []
        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == k:
                return [node.val for node, d in queue]

            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d + 1))

        return []
