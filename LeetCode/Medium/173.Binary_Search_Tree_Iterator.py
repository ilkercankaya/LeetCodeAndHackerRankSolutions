# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.crawl = None

        if not root:
            return

        dummy = root
        while dummy:
            self.stack.append(dummy)
            dummy = dummy.left

    def next(self) -> int:
        self.crawl = self.stack.pop()
        if self.crawl.right:
            dummy = self.crawl.right
            while dummy:
                self.stack.append(dummy)
                dummy = dummy.left
        return self.crawl.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
