import collections


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild, rightChild) -> bool:
        nodeSet = set()

        # find all nodes that are pointed by another node
        for i in range(n):
            if leftChild[i] != -1:
                nodeSet.add(leftChild[i])

            if rightChild[i] != -1:
                nodeSet.add(rightChild[i])

        # if there are more than one candidate nodes, the answer is false
        if len(nodeSet) != n - 1:
            return False

        # find the candidate root
        root = -1
        for i in range(n):
            if i not in nodeSet:
                root = i

        visited = set()
        q = collections.deque()

        q.append(root)
        visited.add(root)

        # simple bfs from root to detect cycle
        # since we have the root node we can just do one BFS to determine if there are any cycles
        while len(q) > 0:
            node = q.pop()
            for children in [leftChild[node], rightChild[node]]:
                if children in visited:
                    return False
                if children != -1:
                    q.append(children)
                    visited.add(children)

        # if we havent visited every node during bfs, the answer is false
        return len(visited) == n