class Solution:
    def cloneGraph(self, node):
        if not node:
            return node

        nodeHash = {}
        stack = [node]
        nodeHash[node] = Node(node.val, [])

        while stack:
            currNode = stack.pop()
            for neigNode in currNode.neighbors:
                if not neigNode in nodeHash:
                    stack.append(neigNode)
                    nodeHash[neigNode] = Node(neigNode.val, [])
                nodeHash[currNode].neighbors.append(nodeHash[neigNode])

        return nodeHash[node]
