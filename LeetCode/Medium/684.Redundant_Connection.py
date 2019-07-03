class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [-1] * len(edges)

        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return
            parent[rootY] = rootX

        for x, y in edges:
            if find(x - 1) == find(y - 1):
                return [x, y]
            else:
                union(x - 1, y - 1)
