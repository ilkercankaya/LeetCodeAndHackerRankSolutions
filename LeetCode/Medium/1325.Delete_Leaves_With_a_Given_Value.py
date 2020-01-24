
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root, target):
        if not root:
            return None

        root.right = self.removeLeafNodes(root.right, target)
        root.left = self.removeLeafNodes(root.left, target)


        if not root.right and not root.left and root.val == target:
            return None

        return root


