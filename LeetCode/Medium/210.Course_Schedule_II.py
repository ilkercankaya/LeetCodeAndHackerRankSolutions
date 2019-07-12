class Solution:
    def findOrder(self, numCourses, prerequisites):
        inVertices = [0] * numCourses
        adjList = [[] * numCourses for i in range(numCourses)]

        for child, parent in prerequisites:
            inVertices[child] += 1
            adjList[parent].append(child)

        count = 0
        order = []

        stack = [id for id, num in enumerate(inVertices) if num == 0]

        while stack:
            count += 1
            curr = stack.pop()
            order.append(curr)

            for adj in adjList[curr]:
                inVertices[adj] -= 1
                if inVertices[adj] == 0:
                    stack.append(adj)

        if count != numCourses:
            return []
        else:
            return order