# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root):
        elements = []

        def inorder(root):
            if not root:
                return None

            inorder(root.left)
            nonlocal elements
            elements.append(root.val)
            inorder(root.right)

        inorder(root)

        def buildTree(leftPtr, rightPtr):

            if leftPtr > rightPtr:
                return None

            mid = (leftPtr + rightPtr) // 2
            root = TreeNode(elements[mid])
            
            root.left = buildTree(leftPtr, mid - 1)
            root.right = buildTree(mid + 1, rightPtr)

            return root


        return buildTree(0, len(elements) - 1)
