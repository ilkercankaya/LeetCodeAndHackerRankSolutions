# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root, to_delete):
        setToDelete = set(to_delete)
        results = []

        def traverser(root, setToDelete, deletedRecently=True):
            if not root:
                return None

            if root.val not in setToDelete and deletedRecently:
                nonlocal results
                results.append(root)

            flag = root.val in setToDelete
            root.left = traverser(root.left, setToDelete, flag)
            root.right = traverser(root.right, setToDelete, flag)

            return None if flag else root

        traverser(root, setToDelete)
        return results
