# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import math


class Solution(object):
    def isCompleteTree(self, root):

        # Just like in the heap left child and right child count should meet wrt to level order travel
        queue = []

        count = 1
        queue.append([count, root])

        while len(queue) != 0:
            count += 1

            popped = queue.pop(0)
            index = popped[0]
            node = popped[1]

            if index != count:
                return False

            if node.left:
                queue.append([2 * index , node.left])
            if node.right:
                queue.append([2 * index + 1, node.right])

        return True

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.__next__()
            root = stringToTreeNode(line)

            ret = Solution().isCompleteTree(root)

            out = (ret)
            print (out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()