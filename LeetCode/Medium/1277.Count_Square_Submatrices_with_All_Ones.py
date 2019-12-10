class Solution:
    def countSquares(self, matrix) -> int:

        dir = [(-1, 0), (-1, -1), (0, -1)]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j]:
                    matrix[i][j] = min(matrix[i + incX][j + incY] for incX, incY in dir) + 1

        return sum(map(sum, matrix))
