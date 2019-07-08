# Tabulation solution
import copy


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        dp = copy.deepcopy(obstacleGrid)

        row = len(dp)
        column = len(dp[0])

        for i in range(len(dp)):
            for j in range(len(dp[i])):
                dp[i][j] = (dp[i][j] + 1) % 2

        for i in range(row - 1, -1, -1):
            for j in range(column - 1, -1, -1):
                if dp[i][j] != 0 and not (i == row - 1 and j == column - 1):

                    right = 0
                    down = 0
                    if j + 1 < column:
                        down = dp[i][j + 1]

                    if i + 1 < row:
                        right = dp[i + 1][j]
                    print(i, j, right, down)

                    dp[i][j] = down + right

        return dp[0][0]
