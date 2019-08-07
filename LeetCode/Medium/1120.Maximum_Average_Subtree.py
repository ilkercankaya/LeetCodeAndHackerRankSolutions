# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxAvg = 0.0
    def maximumAverageSubtree(self, root) -> float:
        def _bottomUp(node):
            if not node:
                return (0,0)

            leftSum, leftNum = _bottomUp(node.left)
            rightSum, rightNum = _bottomUp(node.right)

            leftTotal = leftNum * leftSum
            rightTotal = rightNum * rightSum

            total = leftTotal + rightTotal + node.val

            numNode = (leftNum + rightNum + 1)
            avg = total / numNode

            self.maxAvg = max(self.maxAvg, avg)

            return (avg, numNode)

        if not root:
            return 0.0


        _bottomUp(root)
        return self.maxAvg
