# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Codec:
    def serialize(self, root):
        res = collections.deque()

        def _serialize(root):
            if not root:
                res.append(None)
                return

            res.append(root.val)
            _serialize(root.left)
            _serialize(root.right)

        _serialize(root)
        return res

    def deserialize(self, data):
        def _deserialize():
            node = data.popleft()

            if node is None:
                return None
            root = TreeNode(node)
            root.left = _deserialize()
            root.right = _deserialize()

            return root

        return _deserialize()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))