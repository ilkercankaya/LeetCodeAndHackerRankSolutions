# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        if not root:
            return 0

        totalSum = 0
        answer = 0

        def maxMultip(root):
            if not root:
                return 0

            rightSum = maxMultip(root.right)
            leftSum = maxMultip(root.left)

            nonlocal answer
            answer = max(answer, (totalSum - rightSum) * rightSum, (totalSum - leftSum) * leftSum)

            return root.val + rightSum + leftSum

        totalSum = maxMultip(root)
        maxMultip(root)

        return answer % (10 ** 9 + 7)



# This solution is easier to understand, it is not concise tho
# class Solution:
#     def maxProduct(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#
#         totalSum = 0
#
#         def totalSumUpdater(root):
#             if not root:
#                 return
#             nonlocal totalSum
#             totalSum += root.val
#             totalSumUpdater(root.left)
#             totalSumUpdater(root.right)
#
#         totalSumUpdater(root)
#
#         answer = 0
#
#         def maxMultip(root):
#             if not root:
#                 return 0
#
#             rightSum = maxMultip(root.right)
#             leftSum = maxMultip(root.left)
#
#             nonlocal answer
#             answer = max(answer, (totalSum - rightSum) * rightSum, (totalSum - leftSum) * leftSum)
#
#             return root.val + rightSum + leftSum
#
#         maxMultip(root)
#
#         return answer % (10 ** 9 + 7)

