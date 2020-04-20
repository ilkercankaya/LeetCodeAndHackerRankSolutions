# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestZigZag(self, root) -> int:
        result = 0

        if not root:
            return result

        # dir = True -> right, False -> left
        def preOrderDFS(root, res, dir=None):
            nonlocal result
            if not root:
                return
            result = max(result, res)

            lRes = res + 1 if dir else 1
            rRes = res + 1 if not dir else 1

            preOrderDFS(root.left, lRes, False)
            preOrderDFS(root.right, rRes, True)

        preOrderDFS(root.left, 1, False)
        preOrderDFS(root.right, 1, True)
        return result
