# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque, defaultdict


class Solution:
    def verticalOrder(self, root):
        if not root:
            return []

        minVal, maxVal = float("inf"), float("-inf")

        verticOrderMap = defaultdict(list)
        que = deque([(root, 0)])

        while len(que) > 0:

            for i in range(len(que)):
                curNode, val = que.popleft()

                minVal = min(minVal, val)
                maxVal = max(maxVal, val)
                verticOrderMap[val].append(curNode.val)

                if curNode.left:
                    que.append((curNode.left, val - 1))

                if curNode.right:
                    que.append((curNode.right, val + 1))

        res = []
        for i in range(minVal, maxVal + 1):
            res.append(verticOrderMap[i])

        return res