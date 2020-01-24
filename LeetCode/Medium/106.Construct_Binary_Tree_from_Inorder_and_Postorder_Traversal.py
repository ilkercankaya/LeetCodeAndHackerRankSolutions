# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        inoderMap = {id: i for i, id in enumerate(inorder)}

        def helper(in_left, in_right):
            if in_left > in_right:
                return None

            val = postorder.pop()
            root = TreeNode(val)

            index = inoderMap[val]

            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            return root

        return helper(0, len(inorder) - 1)