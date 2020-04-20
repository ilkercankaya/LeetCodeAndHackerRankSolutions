# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return (0, 0)

            right = helper(root.right)
            left = helper(root.left)

            return (root.val + right[1] + left[1], max(right) + max(left))

        return max(helper(root))