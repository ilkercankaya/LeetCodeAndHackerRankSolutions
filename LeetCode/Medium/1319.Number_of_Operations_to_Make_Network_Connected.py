class Solution:
    def makeConnected(self, n: int, connections) -> int:

        parents = [-1] * n

        def find(a):
            if parents[a] == -1:
                return a
            else:
                parents[a] = find(parents[a])
                return parents[a]

        def union(a, b):
            parentA = find(a)
            parentB = find(b)

            if parentA != parentB:
                parents[parentA] = parentB
                return 1
            else:
                return 0

        spareConnections = 0
        for computerOne, computerTwo in connections:
            if not union(computerOne, computerTwo):
                spareConnections += 1

        groupCount = parents.count(-1)

        return groupCount - 1 if groupCount - 1 <= spareConnections else -1
