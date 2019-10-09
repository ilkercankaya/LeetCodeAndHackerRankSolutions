# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode):
        if not root:
            return 0

        maxSum = float('-inf')

        def pathSum(root):
            if not root:
                return 0

            nonlocal maxSum
            left = pathSum(root.left)
            right = pathSum(root.right)

            maxSum = max(root.val + left + right, maxSum, root.val, root.val + left, root.val + right)

            return max(root.val + right, root.val + left, root.val)

        pathSum(root)
        return maxSum
