class Solution:
    # kruskals algorithm
    def minimumCost(self, N, connections) -> int:
        connections.sort(key=lambda x: x[2])

        parents = [-1] * N
        totalCost = 0

        def find(a):
            if parents[a] == -1:
                return a
            else:
                parents[a] = find(parents[a])
                return parents[a]

        def union(a, b, cost):
            parentA = find(a)
            parentB = find(b)
            if parentA != parentB:
                parents[parentB] = parentA
                return cost
            else:
                return 0

        for cityOne, cityTwo, cost in connections:
            cityOne -= 1
            cityTwo -= 1

            totalCost += union(cityOne, cityTwo, cost)

        if parents.count(-1) > 1:
            return -1

        return totalCost
