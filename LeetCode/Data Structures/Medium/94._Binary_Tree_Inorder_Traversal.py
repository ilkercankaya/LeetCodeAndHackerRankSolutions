# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# left root right
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# beats 99%

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if root is None:
            return []

        stack = []

        listNodes = []

        node = root

        while node or len(stack) != 0:

            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            listNodes.append(node.val)

            node = node.right

        return listNodes
