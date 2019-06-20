# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
T: O(log N * log N) due to leftDepth == rightDepth check will execute after root has been switched to one of the branches
if the height is > 2, in every level since we check the height it is bounded by O(log N)

"""

"""
S: O(log N) due to leftDepth == rightDepth check will execute after the root has been switched to one of the branches
if the height is > 2, stack frames will add up to log N times most
"""

class Solution:
    def _leftMostDepth(self, node):
        if node is None:
            return 0

        return 1 + self._leftMostDepth(node.left)

    def _rightMostDepth(self, node):
        if node is None:
            return 0

        return 1 + self._rightMostDepth(node.right)

    def countNodes(self, root: TreeNode) -> int:

        if root is None:
            return 0

        rightDepth = self._rightMostDepth(root)
        leftDepth = self._leftMostDepth(root)

        if leftDepth == rightDepth:
            return (1 << rightDepth) - 1

        return 1 + self.countNodes(root.right) + self.countNodes(root.left)
