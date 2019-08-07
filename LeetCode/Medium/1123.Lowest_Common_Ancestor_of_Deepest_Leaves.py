# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root):
        leaveNodes = []

        def getLeaves(node):
            if not node:
                return []

            if not node.right and not node.left:
                leaveNodes.append(node.val)

            getLeaves(node.left)
            getLeaves(node.right)

        def searchAncestor(node):
            if not node:
                return []

            left = searchAncestor(node.left)
            right = searchAncestor(node.right)

            if left in leaveNodes:
                return left

            if right in leaveNodes:
                return right

            key = [node] + left + right

            return key


        getLeaves(root)
        print(leaveNodes)
        return searchAncestor(root)