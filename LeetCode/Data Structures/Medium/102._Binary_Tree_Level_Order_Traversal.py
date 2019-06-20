# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return []
        node = root

        queue = [node]

        levelTraversel = []

        while len(queue) > 0:

            queueHelper = []
            newQueue = []

            while len(queue) != 0:
                node = queue.pop(0)
                if node:
                    queueHelper.append(node.val)

                if node.left:
                    newQueue.append(node.left)

                if node.right:
                    newQueue.append(node.right)

            levelTraversel.append(queueHelper)

            queue = newQueue

        return levelTraversel