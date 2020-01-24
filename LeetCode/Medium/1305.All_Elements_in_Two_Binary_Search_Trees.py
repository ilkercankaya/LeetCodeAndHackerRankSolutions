# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1, root2):
        def inorder(root, l):
            if not root:
                return

            inorder(root.left, l)
            l.append(root.val)
            inorder(root.right, l)

        treeOne = []
        inorder(root1, treeOne)

        treeTwo = []
        inorder(root2, treeTwo)

        ptrOne = ptrTwo = 0
        results = []

        while ptrOne < len(treeOne) and ptrTwo < len(treeTwo):
            if treeOne[ptrOne] < treeTwo[ptrTwo]:
                results.append(treeOne[ptrOne])
                ptrOne += 1
            else:
                results.append(treeTwo[ptrTwo])
                ptrTwo += 1

        while ptrOne < len(treeOne):
            results.append(treeOne[ptrOne])
            ptrOne += 1

        while ptrTwo < len(treeTwo):
            results.append(treeTwo[ptrTwo])
            ptrTwo += 1

        return results