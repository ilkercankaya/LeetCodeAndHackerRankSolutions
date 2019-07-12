import copy

class Solution:
    def minPathSum(self, grid) -> int:
        dp = copy.deepcopy(grid)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] += dp[i][j - 1]
                elif j == 0:
                    dp[i][j] += dp[i - 1][j]
                else:
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
