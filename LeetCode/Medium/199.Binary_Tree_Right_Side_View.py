# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque
class Solution:
    def rightSideView(self, root):
        res = []

        if not root:
            return res


        q = deque()
        q.append(root)
        while len(q) > 0:
            for i in range(len(q)):
                cur = q.popleft()

                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)

            res.append(cur.val)

        return res