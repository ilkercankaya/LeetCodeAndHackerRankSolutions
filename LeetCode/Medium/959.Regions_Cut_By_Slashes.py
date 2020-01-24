class Solution:
    def regionsBySlashes(self, grid) -> int:
        N = len(grid)
        parents = [-1] * (4 * N * N)

        def find(a):
            if parents[a] < 0:
                return a
            else:
                parents[a] = find(parents[a])
                return parents[a]

        def unionBySize(a, b):
            aRoot = find(a)
            bRoot = find(b)

            if aRoot == bRoot:
                return

            # make the smaller tree point to larger, no abs is used parent[x] is negative, be careful
            if parents[aRoot] < parents[bRoot]:
                parents[aRoot] += parents[bRoot]
                parents[bRoot] = aRoot
            else:
                parents[bRoot] += parents[aRoot]
                parents[aRoot] = bRoot

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r * N + c)
                if val in '/ ':
                    unionBySize(root, root + 1)
                    unionBySize(root + 2, root + 3)
                if val in '\ ':
                    unionBySize(root, root + 2)
                    unionBySize(root + 1, root + 3)

                # row unions
                if r - 1 >= 0:
                    unionBySize(root, (root - 4 * N) + 3)
                if r + 1 < N:
                    unionBySize(root + 3, (root + 4 * N))

                # column unions
                if c - 1 >= 0:
                    unionBySize(root + 1, (root - 4) + 2)
                if c + 1 < N:
                    unionBySize(root + 2, (root + 4) + 1)

        return sum([parents[i] < 0 for i in range(4 * N * N)])


s = Solution()
print(s.regionsBySlashes([
    "\\/",
    "/\\"
]))
