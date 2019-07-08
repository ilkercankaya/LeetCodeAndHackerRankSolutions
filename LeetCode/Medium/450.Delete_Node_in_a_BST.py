# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deleteNode(self, root: TreeNode, key: int):
        if not root:
            return

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:

            if not root.left and not root.right:
                return None

            if not root.left:
                return root.right
            if not root.right:
                return root.left

            if root.left and root.right:

                dummy = root.right
                while dummy.left:
                    dummy = dummy.left
                root.val = dummy.val
                root.right = self.deleteNode(root.right, root.val)

        return root
