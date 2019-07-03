class Solution:
    def calcEquation(self, equations, values, queries):
        tableValue = {}
        varToID = {}
        parents = [-1] * (len(equations) * 2)
        ID = 0

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
                parents[bRoot] = aRoot

        def addToDict(a):
            nonlocal ID
            if a not in varToID:
                varToID[a] = ID
                ID += 1

        mixed = list(zip(equations, values))
        mixed.sort()
        for info in mixed:
            eq = info[1]
            lhs = info[0][0]
            rhs = info[0][1]

            addToDict(lhs)
            addToDict(rhs)

            union(varToID[lhs], varToID[rhs])


            if lhs not in tableValue and rhs not in tableValue:
                tableValue[lhs] = eq
                tableValue[rhs] = tableValue[lhs] / eq
            elif rhs not in tableValue:
                tableValue[rhs] = tableValue[lhs] / eq
            elif lhs not in tableValue:
                tableValue[lhs] = tableValue[rhs] * eq

        result = []
        for lhs, rhs in queries:
            if (lhs not in varToID or rhs not in varToID) or (find(varToID[lhs]) != find(varToID[rhs])):
                result.append(-1.0)
            elif lhs == rhs:
                result.append(1.0)
            else:
                result.append(float(tableValue[lhs] / tableValue[rhs]))

        return result


s = Solution()
# print(s.calcEquation(
#     [["a", "b"], ["c", "d"]],
#     [1.0, 1.0],
#     [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]]
# ))
print(s.calcEquation(
    [["a", "b"], ["b", "e"], ["e", "f"]],
    [3.4, 1.4, 2.3],
    [["b", "a"], ["a", "f"], ["f", "f"], ["e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]]
))

