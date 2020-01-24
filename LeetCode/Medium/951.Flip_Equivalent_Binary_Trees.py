# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# O(min(N,M))
class Solution:
    def flipEquiv(self, root1, root2) -> bool:
        if root1 is root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (
                    self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right))

# O(N + M)
# class Solution:
#     def flipEquiv(self, root1, root2) -> bool:
#         def parentFiller(root, parent, parentMap):
#             if not root:
#                 return
#
#             parentMap[root.val] = parent.val
#             parentFiller(root.left, root, parentMap)
#             parentFiller(root.right, root, parentMap)
#
#         parentOne = {}
#         parentFiller(root1, TreeNode(None), parentOne)
#
#         parentTwo = {}
#         parentFiller(root2, TreeNode(None), parentTwo)
#
#         return parentOne == parentTwo
#
#
