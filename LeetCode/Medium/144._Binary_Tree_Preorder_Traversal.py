# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# root left right
# https://leetcode.com/problems/binary-tree-preorder-traversal/
# beats %99

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []

        if root is None:
            return []

        stack.append(root)

        listNodes = []

        while len(stack) > 0:

            node = stack.pop()

            listNodes.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return listNodes