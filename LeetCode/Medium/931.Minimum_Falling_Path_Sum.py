class Solution:
    def minFallingPathSum(self, A) -> int:
        dp = [[0] * len(A[0]) for i in range(len(A))]

        for i in range(len(A) -1 , -1, -1):
            for j in range(len(A[0])):
                if i == len(A) - 1:
                    dp[i][j] = A[i][j]
                elif j == 0:
                    dp[i][j] = min(dp[i + 1][j + 1], dp[i + 1][j]) + A[i][j]
                elif j == len(A[0]) - 1:
                    dp[i][j] = min(dp[i + 1][j - 1], dp[i + 1][j]) + A[i][j]
                else:
                    dp[i][j] = min(dp[i + 1][j - 1], dp[i + 1][j + 1], dp[i + 1][j]) + A[i][j]



        return min(dp[0])
    
s = Solution()
print(s.minFallingPathSum([[-84,-36,2],[87,-79,10],[42,10,63]]))