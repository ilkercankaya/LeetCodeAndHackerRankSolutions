class Solution:
    # generalized for K separable dominos
    def minDominoRotations(self, *args) -> int:
        input = [arg for arg in args]

        if not input[0]:
            return 0

        colSet = {}

        transpose = list(zip(*input))
        for i, col in enumerate(transpose):
            colSet[i] = set(col)

        candidates = list(set(transpose[0]))
        results = [[0] * len(candidates) for _ in range(len(input))]

        for j in range(len(input[0])):
            for i in range(len(input)):
                colSet[j].remove(input[i][j])
                for k, candidate in enumerate(candidates):
                    if candidate != input[i][j] and candidate in colSet[j]:
                        results[i][k] += 1
                    elif candidate != input[i][j] and candidate not in colSet[j]:
                        results[i][k] = float("inf")

                colSet[j].add(input[i][j])

        minGlobal = min([min(row) for row in results])
        return -1 if minGlobal == float("inf") else minGlobal