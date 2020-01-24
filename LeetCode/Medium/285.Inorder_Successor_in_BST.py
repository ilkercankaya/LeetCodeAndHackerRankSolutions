# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.prev = None
        self.ans = None

    def inorderSuccessor(self, root, p):
        if not root:
            return None

        self.inorderSuccessor(root.left, p)

        if self.prev == p:
            self.prev = root
            self.ans = root
            return root


        self.prev = root

        self.inorderSuccessor(root.right, p)

        return self.ans
