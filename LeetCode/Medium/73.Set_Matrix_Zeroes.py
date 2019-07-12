class Solution:
    def setZeroes(self, matrix) -> None:
        def directionZeroMaker(i, j, direction):
            if i < 0 or j < 0 or i == len(matrix) or j == len(matrix[0]) or matrix[i][j] is None:
                return
            if matrix[i][j] != 0:
                matrix[i][j] = float("inf")
            rowInc, colInc = direction
            directionZeroMaker(i + rowInc, j + colInc, direction)

        dir = [(0, +1), (-1, 0), (0, -1), (+1, 0)]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    for d in dir:
                        directionZeroMaker(i, j, d)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0

s = Solution()
print(s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))