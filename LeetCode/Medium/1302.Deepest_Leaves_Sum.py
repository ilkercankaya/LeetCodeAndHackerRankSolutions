# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue

class Solution:
    def deepestLeavesSum(self, root) -> int:
        if not root:
            return 0

        que = queue.Queue()

        que.put(root)
        prev = 0
        while que.qsize() > 0:
            prev = 0
            for i in range(que.qsize()):
                curNode = que.get()
                prev += curNode.val
                for dummy in [node for node in [curNode.left, curNode.right] if node]:
                    que.put(dummy)


        return prev