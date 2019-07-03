class Solution:
    def equationsPossible(self, equations) -> bool:
        parents = [-1] * (ord('z') - ord('a') + 1)

        def find(a):
            if parents[a] < 0:
                return a
            else:
                parents[a] = find(parents[a])
                return parents[a]

        def union(a, b):
            aRoot = find(a)
            bRoot = find(b)

            if aRoot != bRoot:
                parents[aRoot] = bRoot

        stack = []

        for eq in equations:
            lhs = ord(eq[0]) - ord('a')
            rhs = ord(eq[3]) - ord('a')
            if eq[1] == "=":
                union(lhs, rhs)
            else:
                stack.append(eq)

        for eq in stack:
            lhs = ord(eq[0]) - ord('a')
            rhs = ord(eq[3]) - ord('a')
            if find(lhs) == find(rhs):
                return False

        return True

