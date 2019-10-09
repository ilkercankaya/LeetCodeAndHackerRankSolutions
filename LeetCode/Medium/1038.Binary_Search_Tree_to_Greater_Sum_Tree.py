class Solution:
    def __init__(self):
        self.incHelper = 0

    def bstToGst(self, root):
        if not root:
            return TreeNode(0)

        self.bstToGst(root.right)
        root.val += self.incHelper
        self.incHelper = root.val
        self.bstToGst(root.left)

        return root