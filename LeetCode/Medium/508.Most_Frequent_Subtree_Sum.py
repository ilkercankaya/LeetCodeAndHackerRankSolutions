# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution:
    def findFrequentTreeSum(self, root):
        freq = collections.defaultdict(int)
        maxFreq = 0

        def subtreeParser(node):
            nonlocal maxFreq
            if not node:
                return 0

            left = subtreeParser(node.left)
            right = subtreeParser(node.right)

            key = node.val + left + right
            freq[key] += 1
            maxFreq = max(maxFreq, freq[key])
            return node.val + left + right

        subtreeParser(root)
        return [val for val,number in freq.items() if number == maxFreq]
