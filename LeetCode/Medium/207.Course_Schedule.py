import collections

class Solution:

    # DFS Cycle Find With Stack
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        adjList = collections.defaultdict(list)

        for fromNode, toNode in prerequisites:
            adjList[toNode].append(fromNode)

        visited = [False] * numCourses

        circleFound = False

        def dfs(node, traversalSet):
            if visited[node]:
                return

            visited[node] = True

            traversalSet.add(node)
            for neig in adjList[node]:
                nonlocal circleFound

                if neig in traversalSet:
                    circleFound = True

                if circleFound:
                    return

                if not visited[neig] and neig not in traversalSet:
                    dfs(neig, traversalSet)

            traversalSet.remove(node)

        for i in range(0, numCourses):
            dfs(i, set())
            if circleFound:
                return not circleFound

        return not circleFound

    # Topological Sort
    # def canFinish(self, numCourses: int, prerequisites) -> bool:
    #     if not prerequisites:
    #         return True
    #
    #     adjList = [[] for i in range(numCourses)]
    #     inDegreeList = [0] * numCourses
    #
    #     for child, parent in prerequisites:
    #         adjList[parent].append(child)
    #         inDegreeList[child] += 1
    #
    #     stack = [id for id, num in enumerate(inDegreeList) if num == 0]
    #     counter = 0
    #     while stack:
    #         current = stack.pop()
    #         counter += 1
    #         for adj in adjList[current]:
    #             inDegreeList[adj] -= 1
    #             if inDegreeList[adj] == 0:
    #                 stack.append(adj)
    #
    #     return counter == numCourses


s = Solution()
print(s.canFinish(2, [[1, 0]]))
