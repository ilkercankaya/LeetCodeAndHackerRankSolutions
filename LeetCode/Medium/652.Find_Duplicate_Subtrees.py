# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution:
    def findDuplicateSubtrees(self, root):
        freqDic = collections.defaultdict(int)
        results = []
        def allSubTreesSerialized(node):
            if not node:
                return "#"

            left = allSubTreesSerialized(node.left)
            right = allSubTreesSerialized(node.right)

            key = str(node.val) + left + right
            freqDic[key] += 1
            if freqDic[key] == 2:
                results.append(node)
            return key

        allSubTreesSerialized(root)

        return results
