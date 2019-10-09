# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root) -> int:
        if not root:
            return 0

        level = 1
        curLevel = 1
        queue = [root]
        maxVal = root.val

        while queue:
            helper = []
            sum = 0
            for num in queue:
                topVal = num.val

                if num.left:
                    helper.append(num.left)

                if num.right:
                    helper.append(num.right)

                sum += topVal

            if sum > maxVal:
                level = curLevel
                maxVal = sum
                
            curLevel += 1
            queue = helper

        return level