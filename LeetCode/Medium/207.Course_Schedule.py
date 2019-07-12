class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        if not prerequisites:
            return True

        adjList = [[] for i in range(numCourses)]
        inDegreeList = [0] * numCourses

        for child, parent in prerequisites:
            adjList[parent].append(child)
            inDegreeList[child] += 1

        stack = [id for id, num in enumerate(inDegreeList) if num == 0]
        counter = 0
        while stack:
            current = stack.pop()
            counter += 1
            for adj in adjList[current]:
                inDegreeList[adj] -= 1
                if inDegreeList[adj] == 0:
                    stack.append(adj)

        return counter == numCourses

s = Solution()
print(s.canFinish(2,[[1,0]]))