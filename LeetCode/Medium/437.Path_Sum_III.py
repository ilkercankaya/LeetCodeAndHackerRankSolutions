# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    def pathSum(self, root, sum: int) -> int:
        if not root:
            return 0

        result = 0
        cache = defaultdict(int)
        cache[0] = 1

        def dfs(root, parentVal):
            if not root:
                return

            curSum = parentVal + root.val

            nonlocal result
            result += cache[curSum - sum]

            cache[curSum] += 1

            dfs(root.left, curSum)
            dfs(root.right, curSum)

            cache[curSum] -= 1

        dfs(root, 0)
        return result