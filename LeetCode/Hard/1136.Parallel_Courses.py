import collections

class Solution:
    def minimumSemesters(self, N: int, relations) -> int:
        inDegree = [0] * N
        adjList = collections.defaultdict(set)
        for parent, child in relations:
            parent -= 1
            child -= 1
            inDegree[child] += 1
            adjList[parent].add(child)

        queue = [i for i in range(len(inDegree)) if inDegree[i] == 0]

        semesterNum = 0
        while queue:
            nextQueue = []
            for parent in queue:
                for child in adjList[parent]:
                    inDegree[child] -= 1
                    if inDegree[child] == 0:
                        nextQueue.append(child)

            semesterNum += 1
            queue = nextQueue


        for degree in inDegree:
            if degree > 0:
                return -1

        return semesterNum
