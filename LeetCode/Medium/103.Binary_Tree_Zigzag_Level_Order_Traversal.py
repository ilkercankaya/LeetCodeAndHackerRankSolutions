# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        results = []

        queue = [root]
        reverseMode = False
        while queue:
            levelVals = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                levelVals.append(node.val)
                l, r = node.left, node.right
                if l:
                    queue.append(l)
                if r:
                    queue.append(r)

            if reverseMode:
                levelVals = levelVals[::-1]

            reverseMode = not reverseMode
            results.append(levelVals)

        return results

