class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix:
            return 0

        dp = list(map(lambda x: list(map(int, x)), matrix))

        dir = [(-1, 0), (-1, -1), (0, -1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if dp[i][j] != 0:
                    dp[i][j] = min(dp[i + incX][j + incY] for incX, incY in dir) + 1

        return max(max(row) for row in dp) ** 2
