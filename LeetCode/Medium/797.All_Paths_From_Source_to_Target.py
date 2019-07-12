class Solution:
    def _allPathsSourceTarget(self, graph, list, node, finalList):
        if node == len(graph) - 1:
            finalList.append(list + [node])
            return finalList


        for adj in graph[node]:
            self._allPathsSourceTarget(graph, list + [node], adj, finalList)

        return finalList

    def allPathsSourceTarget(self, graph):
        return self._allPathsSourceTarget(graph, [], 0, [])
