# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1, root2, target: int) -> bool:
        def traverseFill(root, hashSet):
            if not root:
                return

            traverseFill(root.left, hashSet)
            hashSet.add(root.val)
            traverseFill(root.right, hashSet)

        if not root1 or not root2:
            return False

        secondTreeSet = set()

        traverseFill(root2, secondTreeSet)

        def contains(root, setToSearch):
            if not root:
                return False

            if target - root.val in setToSearch:
                return True

            return contains(root.left, setToSearch) or contains(root.right, setToSearch)

        return contains(root1, secondTreeSet)
