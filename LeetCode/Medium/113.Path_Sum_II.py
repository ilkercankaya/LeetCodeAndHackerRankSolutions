# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):

        results = []

        def dfs(node, prevSum, accumulator):
            if not node:
                return

            prevSum += node.val

            if prevSum == sum and not node.right and not node.left:
                results.append(accumulator + [node.val])
                return

            dfs(node.left, prevSum, accumulator + [node.val])
            dfs(node.right, prevSum, accumulator + [node.val])

        dfs(root, 0, [])
        return results