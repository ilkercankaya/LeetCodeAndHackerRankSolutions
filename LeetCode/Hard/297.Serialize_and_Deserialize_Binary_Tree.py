# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ["X"]


        left = self.serialize(root.left)
        right = self.serialize(root.right)

        return [root.val] + left + right

    def deserialize(self, data):

        node = data.pop(0)

        if node == "X":
            return None
        root = TreeNode(node)
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))