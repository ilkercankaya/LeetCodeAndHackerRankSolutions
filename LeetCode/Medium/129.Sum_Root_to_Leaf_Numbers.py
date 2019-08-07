# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root) -> int:
        results = []
        path = []

        def dfs(node):
            if not node:
                return

            path.append(str(node.val))

            if not node.left and not node.right:
                results.append(path[:])

            dfs(node.left)
            dfs(node.right)
            path.pop()

        dfs(root)

        return sum([int(''.join(num)) for num in results])
