# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root) -> int:
        sum = 0
        def traverser(node, parent, grandparent):
            if not node:
                return


            if grandparent and grandparent % 2 == 0:
                nonlocal sum
                sum += node.val

            traverser(node.left, node.val, parent)
            traverser(node.right, node.val, parent)

        traverser(root, None, None)

        return sum